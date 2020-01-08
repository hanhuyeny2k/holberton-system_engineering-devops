# HTTPS SSL

## Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* The Bash script must pass Shellcheck (version 0.3.7) without any error
* The first line of all the Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing

## Executable
`chmod u+x <filename>`

## Example
```
$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
$
$
$ ./1-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
$
$ ./1-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
```
## Tasks
0)	* What is HTTPS?
	* Why do you need HTTPS?
	* You want to setup HTTPS on your website, where shall you place the certificate?
1) Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Lets also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.
2) Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.
