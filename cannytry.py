import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    imgGrayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgBlurred = cv2.GaussianBlur(imgGrayscale, (5, 5), 0) # blur
    imgCanny = cv2.Canny(imgBlurred, 60, 120)             # get Canny edges
    cv2.namedWindow("imgOriginal", cv2.WINDOW_AUTOSIZE)    # create windows, use WINDOW_AUTOSIZE for a fixed window size
    cv2.namedWindow("imgCanny", cv2.WINDOW_AUTOSIZE)       # or use WINDOW_NORMAL to allow window resizing
    cv2.imshow("imgOriginal", frame)        		   # show windows
    cv2.imshow("imgCanny", imgCanny)
    if cv2.waitKey(1) == 27:				   #27 is the Quit Key
        break
cap.release()
cv2.destroyAllWindows()
