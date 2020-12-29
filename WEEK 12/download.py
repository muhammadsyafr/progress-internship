import json
# import urllib.request
from urllib.request import urlopen
from shutil import copyfileobj

def download():
    with open("sample.json") as stories_json:
        data = stories_json.read()
        files = json.loads(data)
        check_video_exist =  "vid_url" in data

        for i, val in enumerate(files):
            if(check_video_exist == True):
                urllib.request.urlretrieve(val['url'], 'poster_' + str(i+1) + '.png')

                # with urlopen(val['url']) as in_stream, open('poster_' + str(i+1) + '.png', 'wb') as out_file:
                #     copyfileobj(in_stream, out_file)
                try:
                    urllib.request.urlretrieve(val['vid_url'], 'video_' + str(i+1) + '.mp4')

                    # with urlopen(val['vid_url']) as in_stream, open('poster_' + str(i+1) + '.png', 'wb') as out_file:
                    #     copyfileobj(in_stream, out_file)
                except:
                    pass
            else:
                urllib.request.urlretrieve(val['url'], 'poster_' + str(i+1) + '.png')

                # with urlopen(val['url']) as in_stream, open('poster_' + str(i+1) + '.png', 'wb') as out_file:
                #     copyfileobj(in_stream, out_file)

download()

           




        




