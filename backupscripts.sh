#!/bin/bash

#What to backup
backup_file="/home/gabrielam/scripts"


#Where to create the backup 
destination="/home/gabrielam/backups"

#Create archive filename
day=$(date +%F%T)
username=$(whoami)
archive_filename="$username-$day.tgz"

#Backup of the file
tar czf $destination/$archive_filename $backup_file

# Print end of script and add it in a log file
echo "Backup finished: $archive_filename + date ">>backupslog.log
 
#Check to see the archive created 
ls -lh $destination

