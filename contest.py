# Function to remove background

learningRate = 0

def removeBG(image):
    fgmask = bgModel.apply(image, learningRate=learningRate)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(image, image, mask=fgmask)
    return res

#driver function

#Keyboard Oprations
k = cv2.waitKey(10)
if k == 27:  # press ESC to exit
    camera.release()
    cv2.destroyAllWindows()
    break
elif k == ord('c'):  # press 'c' to capture the empty background
    bgModel = cv2.createBackgroundSubtractorMOG2(0, backgroundSubThreshold) #assign the model when key is pressed
    isBgCaptured = 1
elif k == ord('r'):  # press 'r' to reset the background
    bgModel = None
    isBgCaptured = 0

#starting camera 
    camera = cv2.VideoCapture(0)
    camera.set(10, 250)
    cv2.namedWindow('trackbar')
    cv2.createTrackbar('trh1', 'trackbar', threshold, 100, printThreshold)
	
    while camera.isOpened():
	
        #opens video for user
        ret, frame = camera.read()
		#apply thershold 
        threshold = cv2.getTrackbarPos('trh1', 'trackbar')
		# smoothing filter
        frame = cv2.bilateralFilter(frame, 5, 50, 100)
		# flip the frame horizontally			
        frame = cv2.flip(frame, 1)  
        
		cv2.rectangle(frame, (int(capturingBGregionX * frame.shape[1]), 0), (frame.shape[1], int(capturingBGregionY * frame.shape[0])), (255, 0, 0), 2)
        
		cv2.imshow('background capture', frame)
