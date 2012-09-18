from fabric.api import *

def locale():
    local('django-admin.py makemessages -l zh_CN -e haml -s')

def build_locale():
    local('django-admin.py compilemessages')

def server():
    local('./manage.py runserver_plus')

