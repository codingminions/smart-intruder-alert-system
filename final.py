import json 
with open('output1.json' ,'r') as myfile:
	data=myfile.read()

data=json.loads(data)
l=len(data['FaceMatches'])
if l==0:
	import mail
else:
	print("yes")

