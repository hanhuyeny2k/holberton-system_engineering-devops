# Processes and Signals

## Requirements
* Allowed editors: vi, vim, emacs
* All the files will be interpreted on Ubuntu 14.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* The Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all the Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing

## Compilation
`$ chmod u+x <filename>`

`$ ./<filename>`

## Example
```$ ./0-what-is-my-pid
4120
```

## Tasks
* Write a Bash script that displays its own PID.
* Write a Bash script that displays a list of currently running processes.
* Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
* Write a Bash script that displays To infinity and beyond indefinitely.
* We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
* Write a Bash script that kills 4-to_infinity_and_beyond process.
* Write a Bash script that displays: "To infinity and beyond" indefinitely, with a "sleep 2" in between each iteration and "I am invincible!!!" when receiving a SIGTERM signal.
* Write a Bash script that kills the process 7-highlander.
