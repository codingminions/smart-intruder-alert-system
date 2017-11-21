import subprocess as s
c="aws rekognition index-faces \
--image '{\"S3Object\":{\"Bucket\":\"facerek1612\",\"Name\":\"new_image1.jpeg\"}}' \
--collection-id \"images\" \
--region us-east-1 \
--profile adminuser"
s.Popen(c,shell=True,executable='/bin/bash')


c="aws rekognition index-faces \
--image '{\"S3Object\":{\"Bucket\":\"facerek1612\",\"Name\":\"new_image2.jpeg\"}}' \
--collection-id \"images\" \
--region us-east-1 \
--profile adminuser"
s.Popen(c,shell=True,executable='/bin/bash')

c="aws rekognition index-faces \
--image '{\"S3Object\":{\"Bucket\":\"facerek1612\",\"Name\":\"new_image3.jpeg\"}}' \
--collection-id \"images\" \
--region us-east-1 \
--profile adminuser"
s.Popen(c,shell=True,executable='/bin/bash')

c="aws rekognition index-faces \
--image '{\"S3Object\":{\"Bucket\":\"facerek1612\",\"Name\":\"new_image4.jpeg\"}}' \
--collection-id \"images\" \
--region us-east-1 \
--profile adminuser"
s.Popen(c,shell=True,executable='/bin/bash')




