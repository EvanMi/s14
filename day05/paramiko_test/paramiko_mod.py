# -*- coding:utf-8 -*-
# Author: Evan Mi
# import paramiko
"""
该模块的主要功能是用于通过SSH来连接远程主机执行命令
也就是python自带的SSH工具（只不过是编程方式的）

"""

# 创建SSH对象
# ssh = paramiko.SSHClient()
# 允许连接不再konw_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
# ssh.connect(hostname='c1.salt.com',port=22,username='wupeiqi',password='123')
# 执行命令
# stdin, stdout, stderr = shh.exec_command('df')
# 获取结果
# result = stdout.read()
# 关闭连接
# ssh.close()

'''上传文件类似与scp'''
# transport = paramiko.Transport(('hostname', 22))
# transport.connect(username='wupeiqi', password='123')
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.put('123.txt','456.txt')
# sftp.get('456.txt','123.txt')
# transport.close()


# import paramiko
# private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
# 创建SSH对象
# ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
# ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', pkey=private_key)
# 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
# result = stdout.read()
# 关闭连接
# ssh.close()


# import paramiko

# private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

# transport = paramiko.Transport(('hostname', 22))
# transport.connect(username='wupeiqi', pkey=private_key)

# sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
# sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')
# transport.close()
