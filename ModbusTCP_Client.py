# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:20:58 2023

@author: M01
"""
"""
Reference: https://github.com/Johannes4Linux/Simple-ModbusTCP-Server.git
"""

from pyModbusTCP.client import ModbusClient

class Modbus_Client():
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        
        # TCP auto connect on first modbus request
        self.client = ModbusClient(host=self.HOST, port=self.PORT, auto_open=True, auto_close=True)  
        
    # Read Holding Registers
    def read_holding_registers(self, address):
        # Connect
        self.client.open()
        
        # Address: 0 , bit: 1x16 bit
        serverMessage = self.client.read_holding_registers(address)
        print(serverMessage)
        
        # Close
        self.client.close()
        return True
        

    # Write Single Register
    def write_single_register(self, address, value):
        # Connect
        self.client.open()
        
        # Write Single Register
        self.client.write_single_register(address, value)
        serverMessage = self.client.read_holding_registers(address)
        print(serverMessage)
        
        # Close
        self.client.close()
        return True
    
    # Write Multiple Registers
    def write_multiple_registers(self, address, values:list):
        # Connect
        self.client.open()
        
        # Write Multiple Registers
        self.client.write_multiple_registers(address, values)
        serverMessage = self.client.read_holding_registers(address, len(values))
        print(serverMessage)
            
        # Close
        self.client.close()
        return True

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 9527
    modbus_client = Modbus_Client(HOST, PORT)
    modbus_client.read_holding_registers(0)
    modbus_client.write_single_register(1, 111)
    modbus_client.write_multiple_registers(2, [222, 333, 444])
