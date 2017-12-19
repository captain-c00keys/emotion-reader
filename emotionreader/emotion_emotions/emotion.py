"""."""
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys
import simplejson as json
import os

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': os.environ.get('EMOTION_API_KEY', '')
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'https://scontent-sea1-1.xx.fbcdn.net/v/t1.0-9/16998192_10211730567116496_9207760856371247359_n.jpg?oh=6e0934fb6c28dc40bdaaa52e98cef0c5&oe=5ABDE089' }"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    #   URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    parsed = json.loads(data)

    anger = parsed[0]['scores']['anger']
    contempt = parsed[0]['scores']['contempt']
    disgust = parsed[0]['scores']['disgust']
    fear = parsed[0]['scores']['fear']
    happiness = parsed[0]['scores']['happiness']
    neutral = parsed[0]['scores']['neutral']
    sadness = parsed[0]['scores']['sadness']
    surprise = parsed[0]['scores']['surprise']

    conn.close()
except Exception as e:
    print(e.args)