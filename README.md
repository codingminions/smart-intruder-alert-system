# smart-intruder-alert-system

I am trying to create an intruder alert system with the help of motion sensor and facial recognition to protect any secure area of the user , which takes help of Amazon Web service (AWS) cloud services to perform facial recognition and alerts the user and the local authorities via an email in case of an intruder tries to break in your secure area. The service here used is AWS Rekognition.


To implement this system you must have an account on AWS and have your location set as one of the following because Amazon Rekognition is currently available in US East (Northern Virginia), US West (Oregon), EU (Ireland) and AWS GovCloud (US) regions only. 

I created two buckets onto the cloud , one Whitelist (containing images of familiar persons) and another BLacklist(containing images of known intruders and other criminals from the police records). The first comparison will be donw with the Whitelist and in case it fails then the Blacklist faces.

**creating_collections.py:**
   This file creates a collection on the cloud and is used to store features of the face extracted from the image present in the S3 bucket. The name of the collection should be unique.

**upload.py:**
  This file uploads the images taken from the camera onto the S3 bucket created on the AWS console.
  
 **extract.py**
  This file extracts facial features from the face detected and stores them in the collection. The different features includes the measure
  of width, height , top , left dimension of the face in the bounding box of the face. It also includes roll , pitch and yaw of the face.At
  the end it gives us an image id which can be used to access any image features from the collection.
  
**delete.py:**
  This file deletes all the images present in the S3 bucket after the extract.py has been executed for the first time. This is because the
  owner and the close associates or family members upload their face and features just once. We don't need to occupy space in the bucket 
  with the known faces who are allowed to enter the area. 
  
I am taking help of a PIR motion sensor and Rpi3 as my peripheral board to detect motion and capture image as soon there is a presence in the  vicinity of the secured area. This captured image is taken and uploaded on the S3 bucket and then its features are compared with the the stored features.

**upload1.py:**
This file uploads the new captured image onto the S3 bucket in the AWS console.

**compare.py:**
This file extracts features from the face detected above and compare with the features of the faces present in the collection.The result is 
stored in a JSON file.

**final.py:**
This file reads the JSON file created above and check two things. a) Is there any face present in the image uploaded by upload1.py 
b)The similarity percentage.

In case (b) , if the similarity percentage is more than 50 then the person is allowed to enter the area , otherwise the system sounds an
alarm and an email is sent to the owner about the possible intruder attack.

Also , In case the similarity percentage is less than 50, the face is compared with the faces present in the Blacklist and if the similarity percentage comes up more then 50 , then an email is sent to the local authorities via any email service provider about the presence of a
criminal in the particular area. Otherwise just the above procedure of informing the owner is executed. 
