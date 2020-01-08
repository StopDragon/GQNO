#-*- coding:utf-8 -*-
import serial, sys, time, threading
# 모든 통신은 ASCII만 가능

ser = serial.Serial('/dev/ttyAMA0', baudrate=9600, bits=8, parity=None, stop=1)

def Request_Packet(): # 인버터 상태 요청 패킷 
    ser.write('^P001ST6', encoding="ASCHII")

def Response_Packet(): # 인버터 상태 응답 패킷 
    if ser.readable() == True:
        Rpac = ser.readline()
        # 응답 패킷 예시 ^D612001,0,0,0,10
        
    elif ser.readable() == False:
        print('No response from inverter')
