from ApiDetails import ApiDetails
from watson_developer_cloud import ToneAnalyzerV3
import json

def blockMessage(message):
	tone_analyzer = ToneAnalyzerV3(username=ApiDetails.username, password=ApiDetails.password, version=ApiDetails.version)
	analysed_json = json.loads(json.dumps(tone_analyzer.tone(text=message), indent=2))

	emotions = {}

	for category in analysed_json["document_tone"]["tone_categories"]:
		if category["category_id"] == "emotion_tone":
			for tone in category["tones"]:
				emotions[tone["tone_id"]] = tone["score"]

	if (emotions["anger"] + emotions["disgust"])/2 > (emotions["joy"] +emotions["fear"])/2:
		return True
	else:
		return False

    
if __name__ == "__main__":
    print(blockMessage("Russian photographer captures stunning images of frozen Lake Baikal, the oldest and deepest lake in the world"))
    print(blockMessage("It's too bad you are really ugly, it ruins the photo!"))
    print(blockMessage("StudentHack V is a good Hackathon"))
    print(blockMessage("Very sad looser!"))
    print(blockMessage("I feel like someone's put a crowbar through my teeth"))
