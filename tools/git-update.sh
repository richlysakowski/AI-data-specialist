
#!/bin/bash
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
