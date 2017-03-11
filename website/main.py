from flask import Flask, render_template, request, jsonify
import json
from watson_developer_cloud import ToneAnalyzerV3
from ApiDetails import ApiDetails

app = Flask(__name__)
app.secret_key = 'super secret key'

def blockMessage(message):
	tone_analyzer = ToneAnalyzerV3(username=ApiDetails.username, password=ApiDetails.password, version=ApiDetails.version)
	analysed_json = json.loads(json.dumps(tone_analyzer.tone(text=message), indent=2))

	emotions = {}

	for category in analysed_json["document_tone"]["tone_categories"]:
		if category["category_id"] == "emotion_tone":
			for tone in category["tones"]:
				emotions[tone["tone_id"]] = tone["score"]

	if emotions["anger"] > emotions["joy"]:
		return True
	else:
		return False

@app.route('/')
def index():
	return render_template("javascripttest.html", test=55)

@app.route('/analyse_text/')
def analyse_text():
	message = request.args.get("text", 0, type=str)

	return jsonify(block=blockMessage(message))

if __name__ == "__main__":
	app.run(debug=True)

# print(blockMessage("hello"))
# print(blockMessage("kill yourself"))
# print(blockMessage("i hate you"))
