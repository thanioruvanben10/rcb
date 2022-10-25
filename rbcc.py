import requests,json
creds={"ssotoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJ1bmlxdWUiOiI5MzVkMTNiNy1mNzdhLTRmNzktOTYxYS1jMzEwZmFiY2QzZGMiLCJ1c2VyVHlwZSI6IlJJTHBlcnNvbiIsImF1dGhMZXZlbCI6IjIwIiwiZGV2aWNlSWQiOm51bGwsImp0aSI6IjBhNTc1YjNiLTU0OWEtNDI2OC1iNGEzLTgxMjE0NDg1N2ZhZiIsImlhdCI6MTY2NjY4NTkwMn0.CZZuAd71PDCQlQBfPM6I-BK7hIx6TX-HWkIHCwXp6YsW9Z6eg46cEkcJDqjgy9UxJ1d_DpkqWQi14vDGQH2XqA", "uniqueID": "935d13b7-f77a-4f79-961a-c310fabcd3dc"}
ssotoken = creds['ssotoken']
uniqueID = creds['uniqueID']
Request_URL = "https://prod.media.jio.com/apis/common/v3/playbackrights/get/"
Meta_URL = "https://prod.media.jio.com/apis/common/v3/metamore/get/"
def get_manifest(VideoID):
    headers = {
    'ssotoken': ssotoken,
    'bitrates': 'true',
    'os': 'Android',
    'user-agent': 'JioOnDemand/1.5.2.1 (Linux;Android 4.4.2) Jio',
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    }
    response = requests.post(url = Request_URL + VideoID , data = '{"uniqueId":"' + uniqueID + '"}' , headers = headers)
    return json.loads(response.text)

vidid = "003c2a70247511edbfd9c13b366470c9"
manifest = get_manifest(vidid)
print (manifest)
