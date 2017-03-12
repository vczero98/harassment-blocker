from flask import Flask, render_template, request, jsonify
import json
from watson_developer_cloud import ToneAnalyzerV3
from ApiDetails import ApiDetails
import shlex
from CounterFile import CounterFile

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

	if (emotions["anger"] + emotions["disgust"])/2 > (emotions["joy"] +emotions["fear"])/2:
		print(message, True)
		CounterFile.increment()
		return True
	else:
		print(message, False)
		return False

@app.route('/')
def index():
	return render_template("index.html", counter=CounterFile.read())
	# return render_template("javascripttest.html")

@app.route('/analyse_text/', methods = ['GET', 'POST'])
def analyse_text():
	message = request.args.get("text")
	message = message.replace("\"", "")
	message = message.replace("[", "")
	message = message.replace("]", "")
	messages = message.split(",")

	replies = []
	for m in messages:
		replies.append(blockMessage(m))

	return jsonify(replies=replies)

if __name__ == "__main__":
	app.run(debug=True)

# print(blockMessage("hello"))
# print(blockMessage("kill yourself"))
# print(blockMessage("i hate you"))
