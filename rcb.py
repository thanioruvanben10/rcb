import requests,json
video_id = "1000036883"
cdn_url = "http://getcdn.hotstar.com/AVS/besc?action=GetCDN&asJson=Y&channel=TABLET&id=" + video_id + "&type=VOD"
header = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://hotstar.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
response = requests.get(url=cdn_url, headers=header)

json_response = json.loads(response.text.encode('utf-8'))
stream_url = json_response['resultObj']['src'].encode('utf-8')
print(stream_url)
