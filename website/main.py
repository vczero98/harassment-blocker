# from flask import Flask
import json
from watson_developer_cloud import ToneAnalyzerV3
from ApiDetails import ApiDetails

def blockMessage(message):
	tone_analyzer = ToneAnalyzerV3(username=ApiDetails.username, password=ApiDetails.password, version=ApiDetails.version)
	analysed_json = json.loads(json.dumps(tone_analyzer.tone(text=message), indent=2))

	emotions = {}

	for category in analysed_json["document_tone"]["tone_categories"]:
		if category["category_id"] == "emotion_tone":
			for tone in category["tones"]:
				emotions[tone["tone_id"]] = tone["score"]


	print(emotions["joy"])


	# print(emotions["document_tone"]["tone_categories"]["tones"])

# @app.route('/analyse_text/')
# def analyse_text():
# 	vehicle = request.args.get("text", 0, type=str)
#
# 	# possibleVehicles = []
# 	# for v in vehicles:
# 	# 	possibleVehicles.append(v.name)
#
# 	return jsonify(buildProg=(str(buildProg) + "/" + str(maxBuildSteps)), owned=owned, buildError = buildError)

blockMessage("hello")
