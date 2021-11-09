"""EX 2.6 protocol implementation
   Author: IDAN DORON HAI MAMAN 214926941
   Date:10/26/2021

 __o__       o__ __o            o         o        o          o
   |        <|     v\          <|>       <|>      <|\        /|>
  / \       / \     <\         < >       < >      / \\o    o// \
  \o/       \o/       \o        |         |       \o/ v\  /v \o/
   |         |         |>       o__/_ _\__o        |   <\/>   |
  < >       / \       //        |         |       / \        / \
   |        \o/      /         <o>       <o>      \o/        \o/
   o         |      o           |         |        |          |
 __|>_      / \  __/>          / \       / \      / \        / \



"""

LENGTH_FIELD_SIZE = 2
PORT = 8820

import random
import socket
import datetime


def ](data):
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    data = str(data)
    return data in ("RAND", "NAME", "TIME", "EXIT")


def create_msg(data):
    """Create a valid protocol message, with length field"""
    return str(len(data)).zfill(LENGTH_FIELD_SIZE) + data


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """

    size = my_socket.recv(LENGTH_FIELD_SIZE).decode()

    if size.isdigit():
        msg = my_socket.recv(int(size)).decode('ascii')
        return True, msg
    else:
        return False, "Error"


def create_server_rsp(cmd):
    """Based on the command, create a proper response"""
    if cmd == "RAND":
        return str(random.randint(0, 10))
    if cmd == "NAME":
        return socket.gethostbyaddr(socket.gethostname())[0]
    if cmd == "TIME":
        return str(datetime.datetime.now())
    if cmd == "EXIT":
        return "EXIT"
