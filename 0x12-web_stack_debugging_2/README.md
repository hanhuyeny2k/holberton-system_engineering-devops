# Web Stack Debugging #2

## Requirements
* All the files will be interpreted on Ubuntu 14.04 LTS
* All the files should end with a new line
* A README.md file at the root of the folder of the project is mandatory
* All the Bash script files must be executable
* The Bash scripts must pass Shellcheck without any error
* The Bash scripts must run without error
* The first line of all Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all Bash scripts should be a comment explaining what is the script doing

## Execution
`$ chmod u+x <filename>`
`$ ./<filename>`

## Example
```
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeonelese www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```
## Tasks
0) Run software as another user
1) Run Nginx as Nginx
