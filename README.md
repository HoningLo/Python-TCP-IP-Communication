# Python-TCP-IP-Communication

## Installation

### Git Clone Command

1. Open Git Bash.
2. Clone.

```bash
# 複製 git 到本地
git clone https://github.com/HoningLo/Python-TCP-IP-Communication.git
cd Python-TCP-IP-Communication
```

### Requirements

- Python >= 3.6

Create a virtual environment:

```bash
python -m venv venv

# Windows
.\venv\scripts\activate

# Linux
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Headless Install

Linux:

```bash
./install.sh
```

## Web API

### Build Web API (Http API)

Run the `main.py`:

```bash
python main.py
```

Browse to the sample application at `http://localhost:9527` in a web browser.

![Untitled](figure/Untitled.png)

Edit the file  `main.py` and replace the parameters `HOST` and `PORT` with your specific IP address and port number.

```python
# main.py

...
...
...

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 9527
    uvicorn.run(app, host=HOST, port=PORT)
```

### Requests Web API (Http API)

Edit the file `Requests_WebAPI.py` and replace the text `____Enter_Your_DeviceID____` with your DeviceID.

```python
# main.py

...
data = {"DeviceID": "____Enter_Your_DeviceID____"}
...

```

Run the `Requests_WebAPI.py`:

```bash
python Requests_WebAPI.py
```

Result:

![Untitled](figure/Untitled%201.png)

## Socket

### Build Server

Edit the file  `Socket_Server.py` and replace the parameters `HOST` and `PORT` with your specific IP address and port number.

```python
# Socket_Server.py

...
...
...

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 9527
    build_server(HOST, PORT)
```

Run the `Socket_Server.py`:

```bash
python Socket_Server.py
```

### Client

Edit the file  `Socket_Client.py` and replace the parameters `HOST` and `PORT` with your specific IP address and port number.

```python
# Socket_Client.py

...
...
...

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 9527
    send_message(HOST, PORT)
```

Run the `Socket_Client.py` :

```bash
python Socket_Client.py 
```

Server Result:

![Untitled](figure/Untitled%202.png)

Client Result:

![Untitled](figure/Untitled%203.png)

## ModbusTCP

### Build Server

Edit the file  `ModbusTCP_Server.py` and replace the parameters `HOST` and `PORT` with your specific IP address and port number.

```python
# ModbusTCP_Server.py

...
...
...

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 9527
    build_server(HOST, PORT)
```

Run the `ModbusTCP_Server.py`:

```bash
python ModbusTCP_Server.py
```

### Client

Edit the file  `ModbusTCP_Client.py` and replace the parameters `HOST` and `PORT` with your specific IP address and port number.

```python
# ModbusTCP_Client.py

...
...
...

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 9527
    modbus_client = Modbus_Client(HOST, PORT)
    modbus_client.read_holding_registers(0)
    modbus_client.write_single_register(1, 111)
    modbus_client.write_single_register(2, [222, 333, 444])
```

Run the `ModbusTCP_Client.py` :

```bash
python ModbusTCP_Client.py 
```

Server Result:

![Untitled](figure/Untitled%204.png)

Client Result:

![Untitled](figure/Untitled%205.png)

# Reference

[Johannes4Linux/Simple-ModbusTCP-Server: An example for a Modbus TCP server written in Python with pyModbusTCP (github.com)](https://github.com/Johannes4Linux/Simple-ModbusTCP-Server)

[Python Socket - Python network programming with sockets (zetcode.com)](https://zetcode.com/python/socket/)

[[Python] 使用 socket 模組基本教學 - Clay-Technology World (clay-atlas.com)](https://clay-atlas.com/blog/2019/10/15/python-chinese-tutorial-socket-tcp-ip/)

[tiangolo/fastapi: FastAPI framework, high performance, easy to learn, fast to code, ready for production (github.com)](https://github.com/tiangolo/fastapi)

[FastAPI (tiangolo.com)](https://fastapi.tiangolo.com/)