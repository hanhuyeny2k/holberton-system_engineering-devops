# Web Server

## Requirements
* Allowed editors: vi, vim, emacs
* All the files will be interpreted on Ubuntu 16.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* The Bash script must pass Shellcheck (version 0.3.7) without any error
* The first line of all the Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing

## Execution
`$ chmod u+x <filename>`
`$ ./<filename>`

## Example
```
$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
$
$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
$ 
$ touch some_page.html
$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
$
```
Tasks
0) Write a Bash script that transfers a file from our client to a server:
	* Requirements:
		- Accepts 4 parameters
			* The path to the file to be transferred
			* The IP of the server we want to transfer the file to
			* The username scp connects with
			* The path to the SSH private key that scp uses
		- Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
		- scp must transfer the file to the user home directory ~/
		- Strict host key checking must be disabled when using scp
