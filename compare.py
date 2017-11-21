import subprocess as s
c="aws rekognition search-faces-by-image \
--image '{\"S3Object\":{\"Bucket\":\"facerek1612\",\"Name\":\"new_image91.jpeg\"}}' \
--collection-id \"images\" \
--region us-east-1 \
--profile adminuser"
s.Popen(c,shell=True,executable='/bin/bash')

