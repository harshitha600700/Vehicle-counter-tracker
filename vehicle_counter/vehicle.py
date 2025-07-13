import cv2
import numpy as np

# Load video file
cap = cv2.VideoCapture('video.mp4')
print("Video opened:", cap.isOpened())

min_width_react = 80
min_height_react = 80
count_line_position = 550
offset = 6  # Allowable pixel error
counter = 0

# Initialize background subtractor
algo = cv2.createBackgroundSubtractorMOG2()

# List to store detected center points
detect = []

# Function to find the center of a rectangle
def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

while True:
    ret, frame1 = cap.read()
    if not ret:
        break

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    img_sub = algo.apply(blur)
    dilated = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    # edges of moving objs(contours))
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # draws counting line
    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (255, 127, 0), 3)

    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_react) and (h >= min_height_react)
        if not validate_counter:
            continue
        # draws green box around detected vehicle
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Vehicle " + str(counter), (x, y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # draw red dot at center
        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

    # checks if center crosses line counts it updates line color and removes point
    for (x, y) in detect:
        if (count_line_position - offset) < y < (count_line_position + offset):
            counter += 1
            cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (0, 127, 255), 3)
            detect.remove((x, y))
            print("Vehicle Counter:", counter)

    # Display the vehicle count on the frame
    cv2.putText(frame1, "VEHICLE COUNTER : " + str(counter), (450, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    
    #shows final frame
    cv2.imshow('Video Original', frame1)

    if cv2.waitKey(1) == 13:  # Enter key to exit
        break

cap.release()
cv2.destroyAllWindows()