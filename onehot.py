import io
import json 
from sklearn.preprocessing import LabelEncoder
with io.open('prep_topics.json','r') as f:
        data=json.load(f)
for key in data:
	val=data[key]
	data[key]=([0]*39)
	data[key][val-1]=1
with open('onehot_topics.json','w') as f:
	json.dump(data,f,sort_keys=True,indent=4)
