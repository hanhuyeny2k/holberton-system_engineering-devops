# Using Puppet to correct the bug so that 2000 requests can go through

exec { '/etc/default/nginx':
  command => "sed -i s/15/2000/g /etc/default/nginx",
  path => ["/bin"]
  }
service { nginx:
  ensure => running,
  subscribe => Exec['/etc/default/nginx']
}
