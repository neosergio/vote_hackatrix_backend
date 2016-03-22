# Project: vote_hackatrix_backend
Vote system for Hackatrix (Belatrix Hackathon)

Notes
-----
This project is using different settings and requirements, make sure configure your virtualenv properly.

This is an example of setting environment variables for a django project to your virtual env
*cat >> ~/.virtualenvs/gandalf_project/bin/postactivate export DJANGO_SETTINGS_MODULE=vote_hackatrix.settings.local*

An this is on Heroku:
*heroku config:set DJANGO_SETTINGS_MODULE=vote_hackatrix.settings.production*
