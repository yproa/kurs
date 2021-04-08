# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 04:24:13 2021

@author: hariz
"""

import sys
import zmq


#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:15562")


socket.setsockopt(zmq.SUBSCRIBE, b"0")


while True:
    string = socket.recv_string()
    topic, z = string.split()
    print(f"Received {topic} {z}")
    


