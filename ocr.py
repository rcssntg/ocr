import cv2
import pytesseract

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture the current frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to the image
    thresholded_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)[1]

    # Recognize the text in the image
    text = pytesseract.image_to_string(thresholded_image)

    # Print the text
    print(text)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Check if the user wants to quit
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the resources
video_capture.release()
cv2.destroyAllWindows()