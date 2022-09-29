exec { 'fix--for-nginx':
  command => "/bin/sed -i /etc/default/nginx -e 's/15/3000/'"
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
