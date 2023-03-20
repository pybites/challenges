#!python3
# with_ssh is a script to connect to a server and run a command.

from contextlib import contextmanager
import os

import paramiko

server = os.environ.get('SSH_SERVER')
username = os.environ.get('SSH_USER')
password = os.environ.get('SSH_PASSWORD')


@contextmanager
def check_hostname(host):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)
        yield ssh
    finally:
        ssh.close()


with check_hostname(server) as ssh:
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat /etc/hostname')
    print('%s' % ssh_stdout.readlines())
