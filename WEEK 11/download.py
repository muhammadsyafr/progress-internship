import json
import urllib.request

with open("sample.json") as stories_json:
    data = stories_json.read()
    files = json.loads(data)
    check_video_exist =  "vid_url" in data

    for i, val in enumerate(files):
        if(check_video_exist == True):
            urllib.request.urlretrieve(val['url'], str(i) + '.png')
            try:
                urllib.request.urlretrieve(val['vid_url'], str(i) + 'vid.mp4')
            except:
                pass
        else:
            urllib.request.urlretrieve(val['url'], str(i) + '.png')
           




        




