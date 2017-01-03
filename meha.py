"""
Project: MEHA

Author K4YT3X, Fa11en

Licensed under GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
(C) K4YT3X (2017)
(C) Fa11en (2017)

Description: Multi Encrypting Hashing Algorithm

"""
import hashlib
import string
import random
import sqlite3

USER_DB = 'd:/meha.db'
DB = sqlite3.connect(USER_DB)


def meha(prehash):

    salts = [''.join([random.choice(string.printable) for _ in range(40)]) for _ in range(int(7))]

    hash1 = hashlib.md5((prehash + salts[0]).encode("UTF-8")).hexdigest()
    hash2 = hashlib.sha256((hash1 + salts[1]).encode("UTF-8")).hexdigest()
    hash3 = hashlib.sha384((hash2 + salts[2]).encode("UTF-8")).hexdigest()
    hash4 = hashlib.sha512((hash3 + salts[3]).encode("UTF-8")).hexdigest()
    hash5 = hashlib.sha384((hash4 + salts[4]).encode("UTF-8")).hexdigest()
    hash6 = hashlib.sha256((hash5 + salts[5]).encode("UTF-8")).hexdigest()
    hash7 = hashlib.md5((hash6 + salts[6]).encode("UTF-8")).hexdigest()
    return hash7, salts


def new_user(username, passwd):

    passwd, salts = meha(passwd)

    cs = DB.cursor()
    tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='pswds'"
    if not DB.execute(tb_exists).fetchone():
        cs.execute('''CREATE TABLE pswds(usnm text, pswd text, salt0 text, salt1 text, salt2 text, salt3 text, salt4 text, salt5 text, salt6 text)''')
    DB.execute("INSERT INTO pswds (usnm, pswd, salt0, salt1, salt2, salt3, salt4, salt5, salt6) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (username, passwd, salts[0], salts[1], salts[2], salts[3], salts[4], salts[5], salts[6]))
    DB.commit()
    cs.close()

    return 0

# Example
print(new_user('fallen',"123456"))
print(new_user('k4t',"testpswd"))
print(new_user('hi',"rainbow"))
print(new_user('user',"table"))