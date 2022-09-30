#!/usr/bin/env python3
import socket as s
import time as t
import datetime as dt

# set variables
i = 1
wait = 5
srv = {'drive.google.com':'8.8.8.8', 'mail.google.com':'8.8.8.8', 'google.com':'8.8.8.8'}
init=0

print(srv)

while 1==1 : #отладочное число проверок
  for host in srv:
    ip = s.gethostbyname(host)
    if ip != srv[host]:
      if i==1 and init !=1:
        print(str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +' [ERROR] ' + str(host) +' IP mistmatch: '+srv[host]+' '+ip)
      srv[host]=ip

  i+=1
  if i >= 50 :
    break
  t.sleep(wait)