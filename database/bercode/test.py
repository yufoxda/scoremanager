import cv2
import requests
from bs4 import BeautifulSoup
import re



camera_id = 0
delay = 1
window_name = 'OpenCV Barcode'

bd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(camera_id)

count = 0

def aa(codes):
    url = "https://www.ymm.co.jp/p/result_d/pisbn/"+codes
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    bb = soup.find('tr',class_="last",recursive= True).find('td').get_text()
    print(bb)


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
                aa(decoded_info)
                break
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)