# Loops, Conditions and Parsing

## Requirements
* Allowed editors: vi, vim, emacs
* All the files will be interpreted on Ubuntu 14.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* Not allowed to use awk
* Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all the Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing

## Installation
`$ apt-get install shellcheck`

## Compilation
`$ chmod u+x <filename>`

`$ ./<filename>`

## Example
```
$ head -n 2 1-for_holberton_school 
#!/usr/bin/env bash
# This script is displaying "Holberton School" 10 times
$ ./1-for_holberton_school 
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
$ 
```

## Tasks
* Create a SSH RSA key pair
* Write a Bash script that displays Holberton School 10 times using for loop.
* Write a Bash script that displays Holberton School 10 times using while loop.
* Write a Bash script that displays Holberton School 10 times using until loop.
* Write a Bash script that displays HOlberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.
* Write a Bash script that loops from 1 to 10 and:
	- displays bad luck for the 4th loop iteration
	- displays good luck for the 8th loop iteration
	- displays Holberton School for the other iterations
* Write a Bash script that displays numbers from 1 to 20 and:
	- displays 4 and then bad luck from China for the 4th loop iteration
	- displays 9 and then bad luck from Japan for the 9th loop iteration
	- displays 17 and then bad luck from Italy for the 17th loop iteration
* Write a Bash script that displays the time for 12 hours and 59 minutes:
	- display hours from 0 to 12
	- display minutes from 1 to 59
* Write a Bash script that displays:
	- The content of the current directory
	- In a list format
	- Where only the part of the name after the first dash is displayed (refer to the example)
* Write a Bash script that gives you information about the holbertonschool file.
  Requirements:
	- You must use if and, else (case is forbidden)
	- Your Bash script should check if the file exists and print:
		* if the file exists: holbertonschool file exists
		* if the file does not exist: holbertonschool file does not exist
	- If the file exists, print:
   		* if the file is empty: holbertonschool file is empty
		* if the file is not empty: holbertonschool file is not empty
		* if the file is a regular file: holbertonschool is a regular file
		* if the file is not a regular file: (nothing)
