#!/bin/bash
if [ $# == 0 ]
then
  echo "You have not provided any arguments. You
  must provide at least 1!"
  echo "filetest.sh"
  echo "Usage: filetest.sh filename1 [filename2,filename\
3,...]"
  echo " "
else
  for file in $*; do
      echo "Testing $file"
      if [ -e $file ]; then
          comment="$file exists!"
          
          permissions=$(ls -l "$file" | awk '{print $1}')
          echo $permissions
          
          if [ -d "$file" ]; then
              comment2="and it is a directory"
          elif [ -f "$file" ]; then
              if [ -s "$file" ]; then
                  comment2="file with content"
              else
                  comment2="it's a blank filr"
              fi
          else
              comment2="nota file or directory"
          fi
          
      else
          comment="$file does not exist"
          comment2=""
          permissions="N/A"
      fi
      
      echo "$comment $comment2"
      echo " "
  done
fi
