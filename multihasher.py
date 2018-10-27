#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Multihasher
Dev: K4YT3X
Dev: Fa11en

Date Created: January 2, 2017
Last Modified: October 26, 2018

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) K4YT3X (2017-2018)
(C) Fa11en (2017)

Description: A library that helps hash passwords or
anything else multiple times, rendering the creation
of a rainbow table extremely expensive, thus preventing
password from being cracked.

This is a proof of concept

"""
import hashlib
import random
import string


class Multihasher:

    def __init__(self):
        pass

    def multihash(self, plaintext):
        """ Hashes the plain-text string multiple times

        This method hashes the plain-text content multiple
        times and returns the resultant hash.
        """
        salts = [''.join([random.choice(string.printable) for _ in range(40)]) for _ in range(int(7))]

        hash1 = hashlib.md5((plaintext + salts[0]).encode("UTF-8")).hexdigest()
        hash2 = hashlib.sha256((hash1 + salts[1]).encode("UTF-8")).hexdigest()
        hash3 = hashlib.sha384((hash2 + salts[2]).encode("UTF-8")).hexdigest()
        hash4 = hashlib.sha512((hash3 + salts[3]).encode("UTF-8")).hexdigest()
        hash5 = hashlib.sha384((hash4 + salts[4]).encode("UTF-8")).hexdigest()
        hash6 = hashlib.sha256((hash5 + salts[5]).encode("UTF-8")).hexdigest()
        hash7 = hashlib.md5((hash6 + salts[6]).encode("UTF-8")).hexdigest()
        return hash7, salts

    def verify(self, plaintext, hashed):
        """ Verify a password

        Returns True if password is correct.
        """
        if self.multihash(plaintext) == hashed:
            return True
        return False
