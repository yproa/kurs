# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 04:23:43 2021

@author: hariz
"""

import zmq
from random import randrange, random
import time
from threading import Thread

# 15556

def zmqserver(port):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:"+str(port))
    
    while True:
        z = randrange(100, 1000)
        print(port,"   ",z)
        topic = 0
        socket.send(f"{topic} {z}".encode())
        time.sleep(1)
        
     
startport=15556
# servers=[]


server1=Thread(target=zmqserver, args=(startport+0,))
server2=Thread(target=zmqserver, args=(startport+1,))
server3=Thread(target=zmqserver, args=(startport+2,))
server4=Thread(target=zmqserver, args=(startport+3,))
server5=Thread(target=zmqserver, args=(startport+4,))
server6=Thread(target=zmqserver, args=(startport+5,))
server7=Thread(target=zmqserver, args=(startport+6,))
server8=Thread(target=zmqserver, args=(startport+7,))
server9=Thread(target=zmqserver, args=(startport+8,))
server10=Thread(target=zmqserver, args=(startport+9,))
   
server1.start()
server2.start()
server3.start()
server4.start()
server5.start()
server6.start()
server7.start()
server8.start()
server9.start()
server10.start()


             
      

      
# server1.join()
# server2.join()
# server3.join()
# server4.join()
# server5.join()
# server6.join()
# server7.join()
# server8.join()
# server9.join()
# server10.join()
          

# for i in range(10):
#     zmqserver(startport)
#     servers.append(Thread(target=zmqserver, args=(startport+i,)))
    
    
# for i in range(10):
#     servers[i].start()
    
# time.sleep(120)
# for i in range(10):
#     servers[i].join()