import subprocess as s
c="aws s3api put-object --bucket facerek1612 --key new_image1.jpeg --body /home/megatron/AWS/111"
s.Popen(c,shell=True,executable='/bin/bash')


c="aws s3api put-object --bucket facerek1612 --key new_image2.jpeg --body /home/megatron/AWS/211"
s.Popen(c,shell=True,executable='/bin/bash')


c="aws s3api put-object --bucket facerek1612 --key new_image3.jpeg --body /home/megatron/AWS/311"
s.Popen(c,shell=True,executable='/bin/bash')


c="aws s3api put-object --bucket facerek1612 --key new_image4.jpeg --body /home/megatron/AWS/411"
s.Popen(c,shell=True,executable='/bin/bash')

