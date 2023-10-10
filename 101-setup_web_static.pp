# Puppet manifest for setting up web servers for web_static deployment

# Ensure Nginx is installed and running
class { 'nginx':
  ensure  => 'installed',
  enable  => true,
  service => 'running',
}

# Create necessary directories
file { ['/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create the HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Let us deploy web_static',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Configure Nginx for /hbnb_static
file_line { 'nginx_hbnb_static_location':
  line    => '    location /hbnb_static {',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  require => Class['nginx'],
}

file_line { 'nginx_hbnb_static_alias':
  line    => '        alias /data/web_static/current/;',
  path    => '/etc/nginx/sites-available/default',
  after   => '    location /hbnb_static {',
  require => Class['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/data/web_static/current'],
}
