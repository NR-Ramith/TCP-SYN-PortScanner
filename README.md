# TCP-SYN-PortScanning
This program is a port scanner made using python. The program scans a server whose IP address or host name is provided to it and lists out all the ports and services which are open on the server. The scanning is done by sending TCP SYN packets to the server by disabling Nagle's algorithm to improve efficiency of port scanning.

You can run the program with the flags provided as follows (t flag is optional) -

python filename.py -t timeout_value -u url -p port_range(upperrange)

python filename.py -t timeout_value -u url -p port_range(lowerrange-upperrange)

python filename.py -t timeout_value -h ip_addr -p port_range(upperrange)

python filename.py -t timeout_value -h ip_addr -p port_range(lowerrange-upperrange)
