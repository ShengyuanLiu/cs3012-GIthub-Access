
from Github_API import listData
import json

firebase=firebase.FirebaseApplication("https://software-engineering-5017c.firebaseio.com/",None)
count=0
while count<len(listData):
       data=dict(listData[count])
       firebase.post('/software-engineering-5017c/Contributor', data)
       count+=1