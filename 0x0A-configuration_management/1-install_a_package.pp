# using Puppet, install flask


package { 'puppet-lint':
  ensure   => '3.0.0',
  provider => 'gem',
}
