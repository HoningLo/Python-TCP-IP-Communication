# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:20:58 2023

@author: M01
"""
"""
Reference: https://github.com/Johannes4Linux/Simple-ModbusTCP-Server.git
"""

from pyModbusTCP.client import ModbusClient

# TCP auto connect on first modbus request
client = ModbusClient(host="localhost", port=9527, auto_open=True, auto_close=True)

# Connect
client.open()

# Address: 0 , bit: 1x16 bit
serverMessage = client.read_holding_registers(0)
print(serverMessage)

# Write Single Register
client.write_single_register(1, 666)
serverMessage = client.read_holding_registers(1)
print(serverMessage)

# Write Multiple Registers
client.write_multiple_registers(2, [777, 888, 999])
serverMessage = client.read_holding_registers(0, 5)
print(serverMessage)

# Close
client.close()
