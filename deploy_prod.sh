#!/bin/sh

  cd /Users/gvidyash/test_git_proj 
  git pull
  source ./env/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart ecommerce
  # collect static files
  #echo "Collecting static files..."
  #python ${MNGR} collectstatic --noinput
 
  # restart apache - deploy Django project
  #echo "Restarting Apache server..."
  #sudo apachectl graceful
  exit
