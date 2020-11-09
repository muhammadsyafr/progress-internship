import re

regex = r"<!\[CDATA\[(.*?)\]\]>"

test_str = ("<img src=\"https://akcdn.detik.net.id/visual/2020/10/22/aksi-massa-tolak-omnibus-law-di-makassar-berakhir-ricuh_169.png\" align=\"left\" hspace=\"7\" width=\"100\" />\n"
	"<![CDATA[ Kapolda Sulsel Irjen Merdysyam menyebut aksi mahasiswa yang berakhir ricuh di Makassar telah disusupi kelompok Aliansi Makar. ]]>")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print ("{group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))