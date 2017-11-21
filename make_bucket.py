import subprocess as s
c="aws s3api create-bucket --bucket facerek1612 --region us-east-1"
s.Popen(c,shell=True, executable='/bin/bash')
