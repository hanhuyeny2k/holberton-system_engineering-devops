### Configuration Management
## Requirements
* All the files will be interpreted on Ubuntu 14.04 LTS
* All the files should end with a new line
* A README.md file at the root of the folder of the project is mandatory
* The Puppet manifests must pass puppet-lint without any errors
* The Puppet manifests must run without error
* The Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* The Puppet manifests files must end with the extension .pp

## Example
```
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[holberton]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/holberton
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/holberton
root@6712bef7a528:~# cat /tmp/holberton
I love Puppetroot@6712bef7a528:~#
```
## Tasks
0) Using Puppet, create a file in /tmp.
	* Requirements:
		- File path is /tmp/holberton
		- File permission is 0744
		- File owner is www-data
		- File group is www-data
		- File contains I love Puppet
1) Using Puppet, install puppet-lint.
	* Requirements:
		- Install puppet-lint
		- Version must be 2.1.1
2) Using Puppet, create a manifest that kills a process named killmenow.
	* Requirements:
		- Must use the exec Puppet resource
		- Must use pkill
