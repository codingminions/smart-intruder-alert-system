import subprocess as s
c="aws s3 rm s3://facerek1612 --recursive"
s.Popen(c,shell=True,executable='/bin/bash')


