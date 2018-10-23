from netmiko import ConnectHandler
from paramiko.ssh_exception import SSHException

r1_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.2',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}


def retry(retry):
    ''' Decorator try to reconnect to remote device and print number of total tries an number unsuccessful tries'''
    def real_decorator(func):
        def inner(*args, **kwargs):
            i = 0
            while i in range(0, retry):
                out = func(*args, **kwargs)
                if not out:
                    i += 1
                else:
                    i += 1
                    print('You are trying to connect {} times. {} of them unsuccessful'.format(i, i-1))
                    return out
            out = 'You are trying to connect {} times. All of them unsuccessful'.format(i)
            return out
        return inner
    return real_decorator


@retry(retry=3)
def send_show_command(device, show_command):
    print('Connection to ', device['ip'])
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show_command)
        return result
    except SSHException:
        return False


if __name__ == "__main__":
    output = send_show_command(r1_params, 'sh clock')
    print(output)
