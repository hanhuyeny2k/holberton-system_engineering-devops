# Using Puppet to create a manifest that kills a process named killmenow.
exec { 'execute file':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
}
