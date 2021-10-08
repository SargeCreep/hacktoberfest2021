import subprocess

class Network:
    def __init__(self,info):
        self.name = info[2].split(':')[1]
        self.password = info[24].split(':')[1]
        self.auth_type = info[22].split(':')[1]
    def show(self):
        print("Name: "+self.name+"\nPassword: "+self.password+"\nAuth-type: "+self.auth_type+"\n----------")

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifi = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]
network_data = []
for w in wifi:
    try:
        network = Network(subprocess.check_output(['netsh','wlan','show','profile',w,'key=clear']).decode('utf-8').split('\n')[8:-1])
        network_data.append(network)
    except:
        continue
f = open('data.txt','w+')
for n in network_data:
    string = "Name: "+n.name + "\nAuth type: " + n.auth_type + "\nPassword: "+n.password+"\n" + 10*"-" +"\n\n"
    f.write(string)
f.close()



