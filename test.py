import cv2

# Open the webcam (default is device 0, change to 1, 2, etc., for other webcams)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access the webcam.")
    exit()

# Read a frame from the webcam
ret, frame = cap.read()

if ret:
    # Display the frame in a window
    cv2.imshow("Captured Image", frame)

    # Save the image to a file
    cv2.imwrite("captured_image.jpg", frame)
    print("Photo saved as 'captured_image.jpg'.")

    # Wait for a key press and close the window
    cv2.waitKey(0)
else:
    print("Failed to capture an image.")

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
