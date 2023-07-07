# TCP-SYN-PortScanning
This program is a port scanner made using python. It is designed to swiftly analyze a server, whether it be identified by its IP address or host name.  
Its primary function is to meticulously scan the server and provide an extensive report containing a comprehensive list of open ports and their corresponding services whether it's for network analysis or for security assessments.  

To ensure optimal scanning performance, this program intelligently leverages TCP SYN packets while simultaneously disabling **Nagle's algorithm**. By doing so, it significantly enhances the efficiency and accuracy of the port scanning process, guaranteeing faster results and reduced latency.

You can **run the program** with the flags provided as follows (*t flag and lowerrange is optional*) -  
`python filename.py -t timeout_value -u url -p port_range(lowerrange-upperrange)`  
`python filename.py -t timeout_value -h ip_addr -p port_range(lowerrange-upperrange)`
