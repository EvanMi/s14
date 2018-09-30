# -*- coding:utf-8 -*-
# Author: Evan Mi
import hashlib

"""
用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
"""

m = hashlib.md5()
m.update(b"hello")
m.update(b"It's me")
print(m.digest())
m.update(b"It's been a long time since last time we ...")

print(m.digest())  # 2进制格式hash
print(m.hexdigest())  # 16进制格式hash


# ######## md5 ########

hash = hashlib.md5()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha1 ########

hash = hashlib.sha1()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha384 ########

hash = hashlib.sha384()
hash.update(b'admin')
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update(b'admin')
print(hash.hexdigest())
