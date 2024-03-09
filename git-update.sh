
#!/bin/bash
#
# add manually whatever you want before this automatic step
# gitlab repo -- https://gitlab.com/
# login (lastpass)
#
# create new project (don't mark add README)(one project per folder)
# follow instructions in neew project page
#
# if there is not machine-user SSH key, then
# ssh-keygen -t rsa -C "myemail@myhost.com"  || ssh-keygen
#
# edit .git/hooks/pre-commit
# date > version.txt
# git add version.txt 
#
if [ -z "$1" ]; then
  echo "Usage $0 \"commit text message\""
  exit 1
else
  msg=$1
fi
# manually added
git commit -am "$msg"
git push -u origin main
git log --name-status
