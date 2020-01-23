# Mysql
## Requirements
* Allowed editors: vi, vim, emacs
* All the files will be interpreted on Ubuntu 16.04 LTS
* All the files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All the Bash script files must be executable
* The Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
* The first line of all the Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all the Bash scripts should be a comment explaining what is the script doing

## Example
```
$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
$
```
```
$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
$
```
## Tasks
0) Install MYSQL in web-01 and web-02 servers
1) Create user and password for both MySQL databases
2) Create at least one table and one row in primary MYSQL server to replicate from
3) Create a new user for the replica server
4) Set up a primary-replica infrastructure using MySQL
5) Write a Bash script that generates a MySQL dump and creates a compressed archive out of it
