import subprocess as s
c="aws s3api put-object --bucket facerek1612 --key new_image91.jpeg --body /home/megatron/AWS/99"
s.Popen(c,shell=True,executable='/bin/bash')


