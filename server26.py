"""EX 2.6 server implementation
   Author:
   Date:
"""

import socket
import protocol


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol
        valid_msg, cmd = protocol.get_msg(client_socket)

        if valid_msg:
            print("valid massage: " + str(cmd))
            # 1. Print received message

            if protocol.check_cmd(str(cmd)):

                msg_v = protocol.create_msg(protocol.create_server_rsp(cmd))
                print(msg_v)
                client_socket.send(msg_v.encode())
            # 2. Check if the command is valid
            # 3. If valid command - create response
            else:
                response = "Wrong command"
                client_socket.send(response.encode())
                break
        else:
            response = "Wrong protocol"
            client_socket.send(response.encode())
            client_socket.recv(1024)  # Attempt to empty the socket from possible garbage
        if cmd == "EXIT":
            break

        # Handle EXIT command, no need to respond to the client

        # Send response to the client

    print("Closing\n")
    # Close sockets


if __name__ == "__main__":
    main()
