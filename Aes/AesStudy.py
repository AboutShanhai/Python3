#!user/bin/python
# -*- coding: UTF-8 -*-

from AesEverywhere import aes256        # pip install aes-everywhere

key = 'Ua^FkU=+l_TYgODQ'

# 腾讯云COS
print('\n\n\n------------------------------腾讯云COS------------------------------')
accessId = 'U2FsdGVkX1+fLz50PSZK5CAxjlhYYCajrFg29tV+QbIE0NlMSrAUSLnB7jNU+kKEEFCR210vxODzitz1ECgABQ=='
accessKeySecret = 'U2FsdGVkX1+sBi2HcH6WH88iVu+VQMR7MsdY+N1Iv0dqNrXxkjZUcK225A/4iYEIKStI6+xekc95uYWPpiRaqw=='
# decryption
decrypted = aes256.decrypt(accessId, key)
print('解密：', decrypted)
# bytes转str
decrypted = bytes.decode(decrypted)
# encryption
encrypted = aes256.encrypt(decrypted, key)
print('加密：', encrypted)


# decryption
decrypted = aes256.decrypt(accessKeySecret, key)
print('解密：', decrypted)
# bytes转str
decrypted = bytes.decode(decrypted)
# encryption
encrypted = aes256.encrypt(decrypted, key)
print('加密：', encrypted)
print('----------------------------------------------------------------------')


print('\n\n\n------------------------------阿里云OSS------------------------------')
# 阿里云OSS
accessId = 'U2FsdGVkX19XVZGlI5eMpJmzjV8uZzTBke5//9yjNVXhGqy4PE3wRrQy6yPyrpq8'
accessKeySecret = 'U2FsdGVkX18jMZNZKNjoz85ujKVPSUJ0vCdrmSVo55ppQ8cfRNoEli/9l3/EPnZB'
# decryption
decrypted = aes256.decrypt(accessId, key)
print('解密：', decrypted)
# bytes转str
decrypted = bytes.decode(decrypted)
# encryption
encrypted = aes256.encrypt(decrypted, key)
print('加密：', encrypted)


# decryption
decrypted = aes256.decrypt(accessKeySecret, key)
print('解密：', decrypted)
# bytes转str
decrypted = bytes.decode(decrypted)
# encryption
encrypted = aes256.encrypt(decrypted, key)
print('加密：', encrypted)
print('----------------------------------------------------------------------')


print('\n\n\n------------------------------阿里云OSS 战斗牛、战狼------------------------------')
# 阿里云OSS
accessId = 'U2FsdGVkX18F1dVRxNXjoD/PaoeJMh86yyEELCxbLlVknEYFrtwQa2aPzWf1t1B4'
accessKeySecret = 'U2FsdGVkX1/0ggfZk5GbWi4EIcmWOk6FyYB6vXHXRlfoBurnDkHAmPIkxMr/kMZl'
# decryption
decrypted = aes256.decrypt(accessId, key)
print('解密：', decrypted)
# bytes转str
decrypted = bytes.decode(decrypted)
# encryption
encrypted = aes256.encrypt(decrypted, key)
print('加密：', encrypted)


# decryption
decrypted = aes256.decrypt(accessKeySecret, key)
print('解密：', decrypted)
# bytes转str
decrypted = bytes.decode(decrypted)
# encryption
encrypted = aes256.encrypt(decrypted, key)
print('加密：', encrypted)
print('----------------------------------------------------------------------')


print('\n\n\n------------------------------阿里云OSS 天下互娱------------------------------')
# 阿里云OSS
accessId = 'U2FsdGVkX1/xOPWHLTJm73OoDbuQ68KSqwgspdl55D1ETJVnzbjZCW5s+w2ZF+lS'
accessKeySecret = 'U2FsdGVkX18a/gJ5NhKf3WfkztPWVmwowGHlwMkB9BqS5aceFqZbVke6/ipRZxmB'
# decryption
decrypted = aes256.decrypt(accessId, key)
print('解密：', decrypted)
# bytes转str
decrypted = bytes.decode(decrypted)
# encryption
encrypted = aes256.encrypt(decrypted, key)
print('加密：', encrypted)


# decryption
decrypted = aes256.decrypt(accessKeySecret, key)
print('解密：', decrypted)
# bytes转str
decrypted = bytes.decode(decrypted)
# encryption
encrypted = aes256.encrypt(decrypted, key)
print('加密：', encrypted)
print('----------------------------------------------------------------------')


# str转bytes：
bytes('123', encoding='utf8')
str.encode('123')

# bytes转str：
str(b'123', encoding='utf-8')
bytes.decode(b'123')
