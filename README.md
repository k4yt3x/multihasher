# Multihasher

## Description

Multihasher is A library that helps hash passwords multiple times, rendering the creation of a rainbow table extremely expensive, thus preventing password from being cracked.

## Usages

```python3
from multihasher import Multihasher
hasher = Multihasher()
hasher.multihash('apassword')
```