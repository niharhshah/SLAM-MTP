import cv2
import time
import numpy as np
play = 1
kernal = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
kernel = np.array([[-1,10],[1,-10]])
print(kernal)
tyme = [0,0]
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
fps_array = np.zeros(100)
min_fps = 30
i = 0
while 1:
    if (i < 99):
        i+=1
    else:
        i = 1
    _,img = cap.read()
    tyme[1] = time.time()
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img1 = cv2.filter2D(img, -1, kernal)
    # img2 = cv2.filter2D(img, -1, kernel)
    fps = 1 / (tyme[1]-tyme[0])
    mystr = "Real time FPS: " + str(fps)
    tyme[0] = tyme[1]

    # cv2.imshow('Kernel2',img2)
    # cv2.putText(img1,mystr,(0,0),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow("kernal",img1)
    print(mystr)
    if (fps < min_fps) and fps > 1:
        min_fps = fps
    fps_array[i] = fps
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
ave = (np.average(fps_array))
print("Average FPS: {:.3f} and Minimum FPS is {:.3f}".format(ave,min_fps))
cv2.destroyAllWindows()
