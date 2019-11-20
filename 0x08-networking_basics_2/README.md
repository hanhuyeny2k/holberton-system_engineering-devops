# Networking basics #1

## Requirements
* Allowed editors: vi, vim, emacs
* All the files will be interpreted on Ubuntu 14.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* The Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any errors
* The first line of all the Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing

## More info
* For multiple choice question type tasks, just type the number of the correct answer in the answer file.

## Compilation and Execution
`$ chmod u+x <filename>`

`$ ./<filename> | cat -e`

## Example
```
$ ./3-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
```
## Tasks
1) What is localhost?
2) What is 0.0.0.0?
3) Write a Bash script that configures an Ubuntu server with the below requirements.
	* Requirements:
		-localhost resolves to 127.0.0.2
		-facebook.com resolves to 8.8.8.8.
		-The checker is running on Docker, so make sure to read this
4) Write a Bash script that displays all active IPv4 IPs on the machine its executed on.
