import io
import json 
with io.open('Topics.json','r') as f:
	data=json.load(f)	
print data
for key in data:
	for i in range(len(data[key])):
		data[key][i]=data[key][i].encode('utf-8')
		try:
			data[key][i]=int(data[key][i])
		except:
			data[key][i]=39
	data[key]=max(data[key],key=data[key].count)	
with open('prep_topics.json','w') as f:
	json.dump(data,f,sort_keys=True,indent=4)	
