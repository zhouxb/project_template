$ ->
  paths = window.location.pathname.split('/')
  $('a[href*=' + paths[2] + ']').parent().addClass('active')
