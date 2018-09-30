# -*- coding:utf-8 -*-
# Author: Evan Mi
print('from the package package_test')
# import test1 没有生效，待解决
from . import test1  # 因为不在该包下运行脚本，所以要使用.import