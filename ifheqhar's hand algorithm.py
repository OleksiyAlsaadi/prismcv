import cv2
import numpy as np

cv2.namedWindow("frame")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, img = vc.read()
else:
    rval = False

#Other Variables
WIDTH=640
HEIGHT=480
ballx=100
bally=HEIGHT/2
balldx=5
balldy=20.0
paddley=HEIGHT/2
paddledy=10
paddlelen=100

'''
def displayBall():
    global ballx, bally, balldx, balldy
    global oldbox
    ballx+=balldx
    bally+=balldy
    if (bally<=balldy+10): balldy=-balldy; bally=balldy+10+1
    if (bally>=HEIGHT-balldy-10): balldy=-balldy; bally=HEIGHT-balldy-20-1
    
    if (ballx>=oldbox[0][0]): None
    cv2.circle(frame,(int(ballx),int(bally)),10,(255,255,255),thickness=-1,lineType=8,shift=0)

def displayPaddle():
    global paddley, paddledy, paddlelen
    if (bally>paddley+paddlelen/2+10): paddley+=paddledy
    if (bally<paddley+paddlelen/2-10): paddley-=paddledy
    if (paddley<0): paddley=0
    if (paddley>HEIGHT-paddlelen): paddley=HEIGHT-paddlelen
    cv2.rectangle(frame,(50,int(paddley)),(50+15,int(paddley+paddlelen)),(255,255,255),-1)
'''


size=0
delay=5
while rval:

    #print res.dtype
    #Take each frame
    _, frame = vc.read()
    #Convert BGR to HSV
    #invert=cv2.bitwise_not(frame,None)
    '''hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)'''
    #Define range of blue color in HSV
    '''lower_blue = np.array([45,80,80])
    upper_blue = np.array([75,255,255])'''
    #Threshold the HSV image to get only blue colors
    '''mask = cv2.inRange(hsv, lower_blue, upper_blue)'''
    #Bitwise-AND mask and original image
    '''res = cv2.bitwise_and(frame, frame, mask=mask)'''
    #Convert to gray
    #gray2 = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
     #gray2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Blur
     #gray=cv2.medianBlur(gray2,5)
    #gray=cv2.GaussianBlur(gray2,(5,5),0)
    #Threshold
     #ret,thresh1=cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #Finding Shapes
    #edges = cv2.Canny(gray,50,150,apertureSize = 3)
    #ret,thresh = cv2.threshold(edges,127,255,0)
    #contours,hierarchy = cv2.findContours(thresh, 1, 2)
    #contours,hierarchy=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #I don't even know anymore
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1=cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #Whatever this does
    contours, hierarchy=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    drawing=np.zeros(frame.shape,np.uint8)
    
    max_area=0
    #if (len(contours)>0):
    if True:
        for n in range(len(contours)):
            cnt=contours[n]
            area=cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=n
        cnt=contours[ci]
        hull=cv2.convexHull(cnt)
        #drawing=np.zeros(frame.shape,np.uint8)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
        cv2.drawContours(drawing,[hull],0,(0,0,255),2)

        #areas = [cv2.contourArea(c) for c in contours]
        #max_index = np.argmax(areas)
        #cnt = contours[max_index]
        #rect = cv2.minAreaRect(cnt)
        #box = cv2.cv.BoxPoints(rect)
        #box = np.int0(box)
        #a=(box[0][0]+box[1][0]+box[2][0]+box[3][0])/4
        #b=(box[0][1]+box[1][1]+box[2][1]+box[3][1])/4

        '''#print(delay)
        if (cv2.contourArea(box)>size-5000 and cv2.contourArea(box)<size+5000):
            size=cv2.contourArea(box); delay=8; oldbox=box
        else: delay-=1
        if (size==0 or delay<=0): size=cv2.contourArea(box); delay=8; oldbox=box
        '''
        
        #cv2.drawContours(frame,[oldbox],0,(0,0,255),2)
        #cv2.circle(gray,(a,b), 5, (0,0,255), -1)

    '''displayBall()
    displayPaddle()'''
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',drawing)

    key = cv2.waitKey(20)
    if key == 27:
        cv2.destroyWindow("frame")
        cv2.destroyWindow("gray")
        vc.release()
        break
