#!/usr/bin/python2

import cgi,os,commands,time,cgitb
cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()
os_name=data.getvalue('osn')
os_ram=data.getvalue('osr')
os_cpu=data.getvalue('osc')
os_hdd=data.getvalue('osh')
#os_port=data.getvalue('osp')

if os_name == "ubuntu" : 

	os.system('sudo virt-install  --name  '+os_name+'  --ram  '+os_ram+'  --vcpu   '+os_cpu+'  --nodisk   --cdrom  /ubuntu-14.04-desktop-amd64.iso')
	print  "os is about to launch plz wait for 3 minutes !!"

else :
	print  "Bad CHoice !!"

