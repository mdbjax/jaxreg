#!/bin/bash

# **Important** run this command from inside the container, where you have
# Django and dependencies installed. This is typically run automatically 
# (nightly) via a cron job. See the Dockerfile, or shell into the uwsgi container:
# > service cron status
# > crontab -l
# > crontab -e

td=`date +'%m-%d-%y'`
export td
#echo $td

mkdir /code/backup/weekly/$td #Creates weekly backup folder
for db in "users" "api" "main" "logs" 
  do
    echo "Backing up $db"
    /usr/local/bin/python /code/manage.py dumpdata $db > /code/backup/weekly/${td}/${db}_${td}.json #Dumps data into weekly backup
done

find /code/backup/weekly/ -type d -mtime +30 -exec rm -rf {} \; #Deletes directories older than 30 days
