import re
import requests
import time
file=open('proba.html')
file.write('<!DOCTYPE html><html><head><meta charset=UTF-8"></head><body><ul>')
r=requests.get('https://www.meetup.com/Tomsk-Artificial-Intelligence-Meetup/')
title=re.findall(r'"name":"([\w\ \(\)\:]+)","id":"[\w ]+","time":([\d]+)', r.text)
adress=re.findall(r'"address_1":"([\w\ \.\&]+)"', r.text)
for i in xrange(7):
    file.write('<li><ul>'+str(i)+'-'+str(i+1))
    for j in xrange(len(title)):
    	file.write('<li>' + str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(float(title[j][1])/1000))) + str(title[j][0])+ str(adress[j]) + '</li>')
    file.write('</ul></li>')
file.write('</ul></body></html>')