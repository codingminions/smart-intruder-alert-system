import subprocess as s
c="aws rekognition create-collection \
--collection-id \"images\" \
--region us-east-1 \
--profile adminuser"
s.Popen(c,shell=True,executable='/bin/bash')



