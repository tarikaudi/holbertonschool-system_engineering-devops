# web stack debugin3 
exec { 'fixit':
  command  => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  provider => 'shell'
}
