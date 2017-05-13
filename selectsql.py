import paramiko

def ssh_connect( _host, _username, _password ,_port):
    try:
        _ssh_fd = paramiko.SSHClient()
        _ssh_fd.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        _ssh_fd.connect( _host, username = _username, password = _password ,port=_port)
    except Exception as e:
        print ('ssh %s@%s: %s' % (_username, _host, e))
        exit()
    return _ssh_fd

def ssh_exec_cmd( _ssh_fd, _cmd ):
    return _ssh_fd.exec_command( _cmd )

def ssh_close( _ssh_fd ):
    _ssh_fd.close()

def main():
    hostname = '172.16.100.72'
    port = 22
    username = 'xiaoming.zhou'
    password = 'zxm12123'

    sshd = ssh_connect(hostname, username,  password ,port)
    stdin, stdout, stderr = sshd.exec_command("172.16.103.186")
    # print(stdout.readline())
    stdin, stdout, stderr = sshd.exec_command("2")
    # print(stdout.readline())
    stdin, stdout, stderr = sshd.exec_command("spark")
    stdin, stdout, stderr = sshd.exec_command("AMvyE#Yuf#jPr58R")
    stdin, stdout, stderr = sshd.exec_command("ls")
    print(stdout.readline())


if __name__ == "__main__":
    main()