# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:43:25 2023

@author: M01
"""

"""
Reference: https://github.com/Johannes4Linux/Simple-ModbusTCP-Server.git
"""
from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
import traceback # 報錯用

def build_server(HOST, PORT):
    # Create an instance of ModbusServer
    server = ModbusServer(HOST, PORT, no_block=True)
    try:
        print("Start server...")
        server.start()
        print("Server is online")
        state = [0]
        while True:
            server.data_bank.set_holding_registers(0, [1314520])
            if state != server.data_bank.get_input_registers(1):
                state = server.data_bank.get_input_registers(1)
                print("Value of Register 1 has changed to " + str(state))
            sleep(0.5)
    
    except:
        print("Shutdown server ...")
        server.stop()
        print("Server is offline")
        note = traceback.format_exc()
        print(note)

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 9527
    build_server(HOST, PORT)