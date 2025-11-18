#Libraries

import logging
from logging.handlers import RotatingFileHandler
import socket

#Constants

logging_format = logging.Formatter('%(message)s')

#Loggers & Logging Files

funnel_logger = logging.getLogger("funnelLogger")
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('audit.log', maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)

creds_logger = logging.getLogger("credsLogger")
creds_logger.setLevel(logging.INFO)
creds_handler = RotatingFileHandler('cmd_audit.log', maxBytes=2000, backupCount=5)
creds_handler.setFormatter(logging_format)
creds_logger.addHandler(creds_handler)

#Emulated Shells

def emulated_shell(channel, client_ip):
    channel.send(b'UNO$')
    command = b""
    while True:
        char = channel.recv(1)
        channel.send(char)
        if not char:
            channel.close()
        
        command += char
        
        if char == b'\r':
            if command.strip() == b'exit':
                response = b'\n BYE \n'
                channel.close()
            if command.strip() == b'pwd':
                response = b'\n\usr\local\\'+b'\r\n'

#SS Servers + Sockets
#Provision SSH-based Honeypot