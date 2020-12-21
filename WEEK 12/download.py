import json
import urllib.request

def download():
    with open("sample.json") as stories_json:
        data = stories_json.read()
        files = json.loads(data)
        check_video_exist =  "vid_url" in data

        for i, val in enumerate(files):
            if(check_video_exist == True):
                urllib.request.urlretrieve(val['url'], 'poster_' + str(i+1) + '.png')
                try:
                    urllib.request.urlretrieve(val['vid_url'], 'video_' + str(i+1) + '.mp4')
                except:
                    pass
            else:
                urllib.request.urlretrieve(val['url'], 'poster_' + str(i+1) + '.png')

download()

           




        




