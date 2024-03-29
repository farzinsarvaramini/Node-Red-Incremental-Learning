import json
from creme import preprocessing
import pickle

config = json.loads(input())

savePath = config['savePath']
target = config['target']

scaler = preprocessing.StandardScaler()

while True:

	#wait request
	data = input()
	Xi = json.loads(data)
	y = Xi.pop(target, None)
	Xi = scaler.fit_one(Xi).transform_one(Xi)
	if (y != None):
		Xi[target] = y

	pickle.dump(scaler, open(savePath, 'wb'))

	print(json.dumps(Xi))