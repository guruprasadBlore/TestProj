#!/bin/sh

  cd /Users/gvidyash/test_git_proj 
  git pull
  source ./env/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart ecommerce
  exit
