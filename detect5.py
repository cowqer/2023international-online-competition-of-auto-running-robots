def detect(readimg):
    gray = cv.cvtColor(readimg, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=28)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        max_circle = circles[0][np.argmax(circles[0][:, 2])]
        return max_circle[2], max_circle[0], max_circle[1]
    else:
        return 0, 0, 0
    


