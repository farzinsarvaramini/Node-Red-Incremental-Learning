from creme import metrics
import pickle
import json

#read configurations
config = json.loads(input())

modelPath = config['modelPath']
target = config['target']
m = config['metric']


if (m == "Accuracy"):
	metric = metrics.Accuracy()
elif (m == "CrossEntropy"):
	metric = metrics.CrossEntropy()
elif (m == "MacroF1"):
	metric = metrics.MacroF1()
elif (m == "MacroPrecision"):
	metric = metrics.MacroPrecision()
elif (m == "MacroRecall"):
	metric = metrics.MacroRecall()
elif (m == "MicroF1"):
	metric = metrics.MicroF1()
elif (m == "MicroPrecision"):
	metric = metrics.MicroPrecision()
elif (m == "MicroRecall"):
	metric = metrics.MicroRecall()


while True:

	#wait request
	data = input()

	Xi = json.loads(data)
	yt = float(Xi.pop(target))

	loaded_model = pickle.load(open(modelPath, 'rb'))

	yp = loaded_model.predict_one(Xi)
	print("GT: ", yt)
	print("P: ", yp)

	print(metric.update(yt, yp))
