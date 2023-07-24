"""
TFTPy - This module implements an interactive and command line TFTP 
client.

This client accepts the following options:
    $ python3 client.py [-p serv_port] server
    $ python3 client.py get [-p serv_port] server remote_file [local_file] 
    $ python3 client.py put [-p serv_port] server local_file [remote_file]

(C) Jaime Ribalonga, Roberlane Oliveira, 2023
"""
import argparse
from tftp import get_file, put_file


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="TFTPy - Cliente de TFTP (em desenvolvimento)")
    parser.add_argument("server", help="TFTP server address")
    parser.add_argument("-p", "--port", type=int, default=69, help="TFTP server port (default: 69)")
    args = parser.parse_args()

    server_addr = args.server
    server_port = args.port

    print("TFTPy - Cliente de TFTP (em desenvolvimento)")
    print("Usage:")
    print("""\
$ python3 client.py [-p serv_port] server
$ python3 client.py get [-p serv_port] server remote_file [local_file] 
$ python3 client.py put [-p serv_port] server local_file [remote_file]
    """)
    # Ask for user command
    user_input = input("Enter command (get/put) or press Enter to exit: ")

    if user_input == "get":
        # Handle get command
        remote_file = input("Enter the remote file to get from the server: ")
        local_file = input("Enter the local file to save the downloaded data: ")

        server_addr = (server_addr, server_port)
        try:
            get_file(server_addr, remote_file)
            print(f"File '{remote_file}' downloaded and saved as '{local_file}'")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif user_input == "put":
        # Handle put command
        local_file = input("Enter the local file to put on the server: ")
        remote_file = input("Enter the remote file name on the server: ")

        server_addr = (server_addr, server_port)
        try:
            put_file(server_addr, local_file)
            print(f"File '{local_file}' uploaded to the server as '{remote_file}'")
        except Exception as e:
            print(f"An error occurred: {e}")


    elif user_input:
        print("Invalid command. Please use 'get' or 'put' or press Enter to exit.")
        return

#:

if __name__ == '__main__':
    main()
#:
