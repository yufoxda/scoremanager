import cv2  # type: ignore
import requests# type: ignore
from bs4 import BeautifulSoup# type: ignore
import re
import winsound
import time




camera_id = 0
delay = 1
window_name = 'OpenCV Barcode'
filename = "./database/bercode/barReadList.txt"
f = open(filename, 'a')

bd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(camera_id)

count = 0

def aa(codes):
    url = "https://www.ymm.co.jp/p/result_d/pisbn/"+codes
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        bb = soup.find('tr',class_="last",recursive= True).find('td').get_text()
        f.write(bb)
        f.write("\n")
        winsound.Beep(2000,200)
    except:
        print("err")
    return

    


while True:
    ret, frame = cap.read()

    if ret:
        decoded_info,  points ,decoded_type= bd.detectAndDecode(frame)
        if(decoded_info):
            frame = cv2.polylines(frame, points.astype(int), True, (0, 255, 0), 3)
            
            for s, p in zip(decoded_info, points):
                frame = cv2.putText(frame, decoded_info, p[1].astype(int),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            if(count == 0):
                tmpcode = decoded_info
                count = 1
            else:
                if(decoded_info == decoded_info):
                    count +=1
                else:
                    count = 0
            if(count>20):
                
                time.sleep(0.5)
                aa(decoded_info)
                time.sleep(0.5)
        #cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        f.close()
        break

cv2.destroyWindow(window_name)