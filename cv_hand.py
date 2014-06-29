#!/usr/bin/python

import cv2
import numpy as np

cap = cv2.VideoCapture(0)


TRACKBAR_RED = [0,33,0,
                17,255,255]
TRACKBAR_BLU = [54,88,145,
                102,255,255]
TRACKBAR_YEL = [80,90,100,
                110,120,130]


class KingfishApp(object):
    def __init__(self):
        self.cv_show_trackbars()
        while True:
            self.h0 = TRACKBAR_RED[0]
            self.s0 = TRACKBAR_RED[1]
            self.v0 = TRACKBAR_RED[2]
            self.h1 = TRACKBAR_RED[3]
            self.s1 = TRACKBAR_RED[4]
            self.v1 = TRACKBAR_RED[5]
            
            self.cv_update_trackbars()
            # Capture frame-by-frame
            ret, frame = cap.read()
            # Our operations on the frame come here

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # define range of blue color in HSV #red
            lower = np.array([self.h0,self.s0,self.v0])
            upper = np.array([self.h1,self.s1,self.v1])
            ## lower = np.array([TRACKBAR_RED[0],TRACKBAR_RED[1],TRACKBAR_RED[2]])
            ## upper = np.array([TRACKBAR_RED[3],TRACKBAR_RED[4],TRACKBAR_RED[5]])
            # Threshold the HSV image to get only red colors
            mask = cv2.inRange(hsv, lower, upper)
            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame,frame,mask=mask)
            
            img_gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            # Display the resulting frame
            cv2.imshow('frame',img_gray)

            edges = cv2.Canny(img_gray,50,150,apertureSize = 3)
            
            #ret, thresh = cv2.threshold(edges, 200, 255,cv2.THRESH_BINARY)
            thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY,11,2)

            contours,hierarchy = cv2.findContours(thresh,2,1)

            try:
                areas = [cv2.contourArea(c) for c in contours]
                max_index = np.argmax(areas)
                cnt = contours[max_index]
                hull = cv2.convexHull(cnt,returnPoints = False)
                defects = cv2.convexityDefects(cnt,hull)

                #cv2.drawContours(frame, [cnt], 0, (0,255,0), 3)
            
                for i in range(defects.shape[0]):
                    s,e,f,d = defects[i,0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])
                    cv2.line(frame,start,end,[0,255,0],2)
                    cv2.circle(frame,far,5,[0,0,255],-1)
            except:
                pass #print "too bad"

            cv2.imshow('frame',thresh)
            cv2.imshow('frame2', edges)
            cv2.imshow('frame3',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    def cv_update_trackbars(self):
        self.h0 = cv2.getTrackbarPos('H0','track_image')
        self.s0 = cv2.getTrackbarPos('S0','track_image')
        self.v0 = cv2.getTrackbarPos('V0','track_image')
        self.h1 = cv2.getTrackbarPos('H1','track_image')
        self.s1 = cv2.getTrackbarPos('S1','track_image')
        self.v1 = cv2.getTrackbarPos('V1','track_image')
                
    def cv_show_trackbars(self):
        def nothing(x):
            pass
        
        cv2.namedWindow('track_image')
        cv2.createTrackbar('H0','track_image',0,180,nothing)
        cv2.createTrackbar('S0','track_image',0,255,nothing)
        cv2.createTrackbar('V0','track_image',0,255,nothing)
        cv2.createTrackbar('H1','track_image',0,180,nothing)
        cv2.createTrackbar('S1','track_image',0,255,nothing)
        cv2.createTrackbar('V1','track_image',0,255,nothing)
        
        cv2.setTrackbarPos('H0','track_image',TRACKBAR_RED[0])
        cv2.setTrackbarPos('S0','track_image',TRACKBAR_RED[1])
        cv2.setTrackbarPos('V0','track_image',TRACKBAR_RED[2])
        cv2.setTrackbarPos('H1','track_image',TRACKBAR_RED[3])
        cv2.setTrackbarPos('S1','track_image',TRACKBAR_RED[4])
        cv2.setTrackbarPos('V1','track_image',TRACKBAR_RED[5])
        
        self.h0 = cv2.getTrackbarPos('H0','track_image')
        self.s0 = cv2.getTrackbarPos('S0','track_image')
        self.v0 = cv2.getTrackbarPos('V0','track_image')
        self.h1 = cv2.getTrackbarPos('H1','track_image')
        self.s1 = cv2.getTrackbarPos('S1','track_image')
        self.v1 = cv2.getTrackbarPos('V1','track_image')
        
if __name__ == '__main__':
    cur_app = KingfishApp()
