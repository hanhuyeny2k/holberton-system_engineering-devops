# SSH

## Requirements
* Allowed editors: vi, vim, emacs
* All the files will be interpreted on Ubuntu 16.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* The first line of all the Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing

## Executing
`$ chmod u+x <filename>`
## My Servers
| Name         | Username | IP           |
| :------:     | -------- | ----         |
| 862-web-01   | ubuntu   | 35.237.78.35 |

## Example
```
$ ./0-use_a_private_key
Welcome to Ubuntu 16.04.1 LTS (GNU/Linux 4.4.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


*** System restart required ***
Last login: Fri Feb  3 01:12:16 2017 from 104.7.14.91
ubuntu@server01:~$ logout
Connection to 8.8.8.8 closed.
$ 
```
## Tasks
0) Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.
	* Requirements:
		- Only use ssh single-character flags
		- You cannot use -l
		- You do not need to handle the case of a private key protected by a passphrase
1) Write a Bash script that creates an RSA key pair.
	* Requirements:
		- Name of the created private key must be holberton
		- Number of bits in the created key to be created 4096
		- The created key must be protected by the passphrase betty
2) our Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, lets configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
	* Requirements:
		- Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
		- Your SSH client configuration must be configured to refuse to authenticate using a password
3) Now that you have successfully connected to your server, we would also like to join the party.
	* Add the SSH public key below to your server so that we can connect using the ubuntu user.
