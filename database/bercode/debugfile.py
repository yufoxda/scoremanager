

filename = "./database/bercode/barReadList.txt"
f = open(filename, 'r')

datalist = f.readlines()

import webbrowser
for i in datalist:
    url = 'https://www.ymm.co.jp/p/detail.php?code='+i
    webbrowser.open(url)
    input()



