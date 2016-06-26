import urllib2
import time
IpList = open("ip_add_all.json","r").read()
Ip = eval(IpList)
flag = 0
file = open('point.json','w')
for i in range(2):
    ip = Ip[i]['ip']
    res = urllib2.urlopen("http://api.map.baidu.com/location/ip?ak=KrmZxHHwvLnl4Xfyt0FMMVzgGLaaxU2j&ip="+ip+"&coor=bd09ll")
    a = res.read()
    zidian = eval(a)
    flag += 1
    if(zidian['status'] == 0):
        print flag,ip
        lng =  zidian['content']['point']['x']
        lat =  zidian['content']['point']['y']
        #print lat,lng
        str_temp = '{"lat": '+lat+', "lng":'+lng+'},\n'
        file.write(str_temp)    
file.close()
