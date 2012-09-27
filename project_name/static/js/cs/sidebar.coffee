$ ->
  paths = window.location.pathname.split('/')
  path = '\\/' + paths[2] + '\\/'
  $('a[href*=' + path + ']').parent().addClass('active')
