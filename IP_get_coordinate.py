import urllib2
import time

#IpList = open("IP.json","r")
IpList = open("ip_add_all.json","r").read()

Ip = eval(IpList)
#print type(IpList)
#print type(Ip)
#print Ip[0]['ip']
flag = 0
file = open('point.json','w')
#file.write('1')
#file.close()

for i in range(90000):
    ip = Ip[i]['ip']
    #print ip
    res = urllib2.urlopen("http://api.map.baidu.com/location/ip?ak=KrmZxHHwvLnl4Xfyt0FMMVzgGLaaxU2j&ip="+ip+"&coor=bd09ll")
    a = res.read()
    #print (a)
    zidian = eval(a)
    flag += 1
    if(zidian['status'] == 0):
        print flag,ip
        print zidian['address']
        print zidian['content']['point']
        file.write(str(zidian['content']['point'])+'\n')    
file.close()
