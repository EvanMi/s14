# -*- coding:utf-8 -*-
# Author: Evan Mi
import hmac

h = hmac.new(b'test', b'12345')
print(h.hexdigest())
