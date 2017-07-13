# typo error in import
import subprocess
ip = raw_input("Lutfen ip degerini giriniz:(orn: 192.168.1)")
aralik = raw_input("Lutfen araligi belirleyiniz:(orn:255)")
lstaktif=[]
lstpasif=[]
for ping in range(1,int(aralik)):
    address = ip + "." + str(ping)
    print ip
    res = subprocess.call(['ping', '-w' , '500' , '-c', '2', address])
    clc = subprocess.call(['clear'])
    if res == 0:
        lstaktif.append(address)
    elif res == 2:
        print "no response from", address
    else:
        lstpasif.append(address)

print "*************************************************************************"
for adress in range(len(lstaktif)):
    print lstaktif[adress] , ": is Online"
print "-------------------------------------------------------------------------"
for adress in range(len(lstpasif)):
    print lstpasif[adress] , ": is Offline"







