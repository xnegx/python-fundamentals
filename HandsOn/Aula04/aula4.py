from paramiko.client import SSHClient
import paramiko

host = '10.100.0.84'
user = 'root'
password = '4linux'

client = SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname=host, username=user, password=password)
stdin, stdout, stderr = client.exec_command("psql")

print stdout.read()
