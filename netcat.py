import paramiko

#comman credentials 
user = "your_user_name"
password = "your_password"

#configure the diffrent servers
configarutions = {
    "testserver" : {"server":"192.168.0.1","server2":"192.168.63.6","port":"77777"},
    "testserver1" : {"server":"192.168.0.2","server2":"172.19.13.7","port":"77777"},
    "testserver2" : {"server":"192.168.0.3","server2":"172.19.13.8","port":"77777"},
    "testserver3" : {"server":"192.168.0.4","server2":"10.255.255.9","port":"77777"},
    "testserver4" : {"server":"192.168.0.5","server2":"10.255.255.10","port":"77777"}
}

#defining function

def pankaj(server,server2,port):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server,username=user,password=password)

        command = f"nc -zv {server2} {port}"
        stdin, stdout, stderr = ssh.exec_command(command,timeout=10)

        output = stdout.read().decode() #read the raw data & decode convert raw data into readable formate
        error = stderr.read().decode()
        
        if output:
            print(output.strip())
        if error:
            print(error.strip())

    except paramiko.AuthenticationException:
        print("authentication failed")
    except paramiko.SSHException as e:
        print(f"ssh error {e}")
    except Exception as e:
        print (f"error {e}")
    finally:
        if ssh:
            ssh.close()


def main():
    print("Which Market do you want to netcat:")
    select_market=input().strip().lower()

    if select_market in configarutions:
        rawat = configarutions[select_market]
        pankaj(rawat["server"],rawat["server2"],rawat["port"])
    else:
        print("what are you typing buddy")

if __name__ == "__main__":
    main()

