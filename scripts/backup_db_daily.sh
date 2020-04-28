#!/bin/bash

# **Important** run this command from inside the container, where you have
# Django and dependencies installed. This is typically run automatically 
# (nightly) via a cron job. See the Dockerfile, or shell into the uwsgi container:
# > service cron status
# > crontab -l
# > crontab -e

td=$(date +'%m-%d')
export td
#echo $td

mkdir /code/backup/daily/$td #Creates daily backup folder
for db in "users" "api" "main" "logs" 
  do
    echo "Backing up $db"
    /usr/local/bin/python /code/manage.py dumpdata $db > /code/backup/daily/$td/${db}_${td}.json #Dumps data into weekly backup
done

find /code/backup/daily/ -type d -mtime +7 -exec rm -rf {} \; #Deletes directories older than 30 days
