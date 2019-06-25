import paramiko
{
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='ic-vm-176.cisco.com',username='intucell',password='intucell')

    stdin,stdout,stderr=ssh_client.exec_command("ls")
    print stdout.readlines()
    #[u'remoting\n', u'remoting.jar\n', u'workspace\n']


    stdin,stdout,stderr=ssh_client.exec_command("sudo ls")
    stdin.write('intucell\n')
    print stdout.readlines()
    print stderr.readlines()
    # TODO need to fix
    #[]
    #[u'sudo: no tty present and no askpass program specified\n']

    #Download a file
    ftp_client=ssh_client.open_sftp()
    ftp_client.get('/home/intucell/remoting.jar','/Users/ankuragr/remoting.jar')
    ftp_client.close()

    #upload a file
    ftp_client=ssh_client.open_sftp()
    ftp_client.put('/Users/ankuragr/test.txt', '/home/intucell/test.txt')
    ftp_client.close()
}
{
 # with SSH keys
}
