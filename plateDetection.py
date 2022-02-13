import cv2
import imutils
import pytesseract
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
index = ["color", "color_name", "hex", "R", "G", "B"]
plateStored = []
data = pd.read_csv("Resource\\colors.csv", names=index, header=None)
carColor = ""


def recognize_color(R, G, B):
    minimum = 10000
    color_name = ""
    for i in range(len(data)):
        d = abs(R - int(data.loc[i, "R"])) + abs(G -
                                                 int(data.loc[i, "G"])) + abs(B - int(data.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            color_name = data.loc[i, "hex"]
    return color_name


def Detection(PATH):
    global carColor
    image = cv2.imread(PATH)
    image = imutils.resize(image, width=900)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 170, 200)
    cnt, new = cv2.findContours(
        edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    img1 = image.copy()
    cv2.drawContours(img1, cnt, -1, (0, 255, 0), 3)
    cnt = sorted(cnt, key=cv2.contourArea, reverse=True)[:30]
    NumberPlateCnt = None
    img2 = image.copy()
    cv2.drawContours(img2, cnt, -1, (0, 255, 0), 3)
    for c in cnt:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            NumberPlateCnt = approx
            x, y, w, h = cv2.boundingRect(c)
            new_img = gray[y:y + h, x:x + w]
            b, g, r = img2[y+2, x]
            b = int(b)
            g = int(g)
            r = int(r)
            cv2.imwrite('Cropped Images-Text/Croped.png', new_img)
            carColor = recognize_color(r, g, b)
            break

    Img_path = 'Cropped Images-Text/Croped.png'
    cv2.drawContours(image, [NumberPlateCnt], -1, (0, 255, 0), 3)
    Cropped_img_loc = Img_path
    Plate_num = pytesseract.image_to_string(Cropped_img_loc, lang='eng')
    if len(Plate_num) > 6:
        Plate_num = ''.join(e for e in Plate_num if e.isalnum())
    plateStored = []
    plateStored.append(Plate_num)
    plateStored.append(carColor)
    print("detec: ", plateStored)
    return plateStored
