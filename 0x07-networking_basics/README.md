# Networking Basics #0

## Requirements
* Allowed editors: vi, vim, emacs
* All the Bash script files will be interpreted on Ubuntu 14.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* The Bash script must pass shellcheck without any error
* The first line of all the Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing

## More Info
* For multiple choice question type tasks, just type the number of the correct answer in the answer file.

## Compilation and Execution
`$ chmod u+x <filename>`

`$ ./<filename>`

## Example
```
$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
$
$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
```
## Tasks
0) 	What is the OSI model?
	How is the OSI model organized?
1) 	What type of network are Holberton iMacs connected to?
	What type of network could connect an office in one building to another office in a building a few streets away?
	What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?
2)	What is a MAC address?
	What is an IP address?
3)	Which statement is correct for the TCP box:
	Which statement is correct for the UDP box:
	Which statement is correct for the TCP worker:
4) Write a Bash script that displays listening ports:
	- That only shows listening sockets
	- That shows the PID and name of the program to which each socket belongs
5) Write a Bash script that pings an IP address passed as an argument.
	* Requirements:
		- Accepts a string as an argument
		- Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
		- Ping the IP 5 times
	 
