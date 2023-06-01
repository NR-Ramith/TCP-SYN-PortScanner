import socket
import sys
import random

# python filename.py -t timeout_value -u url -p port_range(upperrange)
# python filename.py -t timeout_value -u url -p port_range(lowerrange-upperrange)
# python filename.py -t timeout_value -h ip_addr -p port_range(upperrange)
# python filename.py -t timeout_value -h ip_addr -p port_range(lowerrange-upperrange)

# This method may not give accurate results if the server blocks the TCP SYN message
def port_scanner(host, port_start, port_end, timeout_time):
    open_ports = []
    print("Started TCP SYN scanning for IP: {}".format(host))

    for port in range(port_start, port_end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout_time)
        source_port = random.randint(1024, 65535)   # To balance connection load by selecting random ports

        try:
            # Send SYN packet
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            # The socket.IPPROTO_TCP constant is a flag that represents the TCP protocol
            # Setting the TCP_NODELAY option to 1 disables the Nagle's algorithm for the socket, allowing each packet to be sent immediately without any delay
            # Nagle's algorithm aims to improve network efficiency by combining small outgoing TCP packets into larger ones
            s.bind((host, source_port))
            s.connect_ex((host, port))
            s.send(b'')

            # Receive the response
            response = s.recv(1024)

            # Analyze the response
            if response:
                open_ports.append(port)
        except socket.timeout:
            pass
        finally:
            s.close()

    return open_ports

# Same function without optimization
# def port_scanner(host, port_start, port_end, timeout_time):
#     open_ports = []
#     # host_name = socket.gethostbyname_ex(host)
#     print("Started portscan for ip: {}".format(host))
    
#     for port in range(port_start, port_end+1):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.settimeout(timeout_time)
#         try:
#             conn = s.connect_ex((host, port))
            
#             if conn == 0:
#                 # Port is open
#                 open_ports.append(port)
#         except socket.timeout:
#             pass
#         finally:
#             s.close()

#     return open_ports

# main
ports_and_services = {
    7: 'echo',
    20: 'ftp',
    21: 'ftp',
    22: 'ssh',
    23: 'telnet',
    25: 'smtp',
    43: 'whois',
    53: 'dns',
    67: 'dhcp',
    68: 'dhcp',
    80: 'http',
    110: 'pop3',
    123: 'ntp',
    137: 'netbios',
    138: 'netbios',
    139: 'netbios',
    143: 'imap4',
    443: 'https',
    513: 'rlogin',
    540: 'uucp',
    554: 'rtsp',
    587: 'smtp',
    873: 'rsync',
    902: 'vmware',
    989: 'ftps',
    990: 'ftps',
    1194: 'openvpn',
    3306: 'mysql',
    5000: 'unpn',
    8080: 'https-proxy',
    8443: 'https-alt'
}


if len(sys.argv) == 1:
    print("Insufficient number of arguements")
    print("Example: portscanner.py -u <url> -p port_range")
    exit(0)


host = "8.8.8.8"
start_port = 1
end_port = 444
timeout_time = 0.25

for arg_index in range(1, len(sys.argv), 2):
    arg = sys.argv[arg_index]
    try:
        value = sys.argv[arg_index+1]
    except IndexError:
        print("Invalid arguements.")
        exit(0)
    if  arg == "-u":
        host = str(socket.gethostbyname(str(value)))
    elif arg == "-h":
        host = value
    elif arg == "-t":
        try:
            timeout_time = float(value)
        except:
            print("The timeout value should be a float value")
    elif arg == "-p":
        port_list = value.split("-")
        if len(port_list) == 1:
            try:
                end_port = int(port_list[0])
            except:
                print("Port value should be an integer")
                exit(0)
        elif len(port_list) == 2:
            try:
                start_port = int(port_list[0])
                end_port = int(port_list[1])
            except:
                print("Port value should be an integer")
                exit(0)
        else:
            print("Invalid value given for port")
            exit(0)
    else:
        print("Invalid arguement provided")
        exit(0)


open_ports = port_scanner(host, start_port, end_port, timeout_time)

if len(open_ports) == 0:
    print("All the ports are closed")
else:
    print("PORT\t STATUS\t SERVICE")
    for port_no in open_ports:
        if port_no in ports_and_services:
            service = ports_and_services[port_no]
        else:
            service = "unknown"
        print("{}\t OPEN\t {}".format(port_no, service))