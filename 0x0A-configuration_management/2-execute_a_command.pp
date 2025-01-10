# kill process
exec { 'kill':
  command => 'pkill killmenow',
}
