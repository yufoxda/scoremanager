import cv2
import os

# カレントディレクトリの表示
print(os.getcwd())


img = cv2.imread('image.png')
bd = cv2.barcode.BarcodeDetector()
# bd = cv2.barcode.BarcodeDetector('path/to/sr.prototxt', 'path/to/sr.caffemodel')

decoded_info,  points ,decoded_type= bd.detectAndDecode(img)

print(decoded_info)

img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)

for s, p in zip(decoded_info, points):
    img = cv2.putText(img, decoded_info, p[1].astype(int),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imwrite('barcode_opencv.jpg', img)
# # ('1923055034006', '9784873117980')