module.exports = function(RED){
	function ClassificationMetricNode(config){
		const path = require('path')
		const utils = require('./utils/utils')

		var node = this;

		//set configurations
		node.file = __dirname + '/ClassificationMetric.py'
		node.config = {
			target: config.target || 'y',
			predict: config.predict || 'Predict',
			metric: config.metric || "Accuracy"
		}
		utils.run(RED, node, config)
	}
	RED.nodes.registerType("ClassificationMetric", ClassificationMetricNode)
}
