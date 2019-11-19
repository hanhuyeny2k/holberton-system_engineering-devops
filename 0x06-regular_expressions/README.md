# Regular Expression

## Requirements
* Allowed editors: vi, vim, emacs
* All the files will be interpreted on Ubuntu 14.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* The first line of all the Bash scripts should be exactly #!/usr/bin/env ruby
* All the regex must be built for the Oniguruma library

## Compilation and Execution
`$chmod u+x <filename>

`$ ./<filename>`

## Example
```
$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$
```
## Tasks
* 0) - The regular expression must match Holberton.
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
* 1) - Find the regular expression that will match hbttn, hbtttb, hbttttn, hbtttttn.
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
* 2) - Find the regular expression that will match htn, hbtn.
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
* 3) - Find the regular expression that will match hbtn, hbttn, hbtttn, hbttttn.
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
* 4) - Find the regular expression that will match hbn, hbtn, hbttn, hbtttn, hbttttn.
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
* 5) - The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between.
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
* 6) The regular expression must match a 10 digit phone number.
* 7) The regular expression must be only matching: capital letters.
* 8) Solve LinkedIn regex puzzle: https://engineering.linkedin.com/puzzle.
