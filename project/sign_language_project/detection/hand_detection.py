import cv2

def main():
    # Open webcam (0 = default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Read frame
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame (mirror view)
        frame = cv2.flip(frame, 1)

        # Draw a rectangle (Region of Interest where user will show signs)
        x, y, w, h = 100, 100, 300, 300
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Extract ROI (Region of Interest)
        roi = frame[y:y+h, x:x+w]

        # Convert ROI to grayscale
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply threshold (convert to black & white image)
        _, thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # Show the processed ROI
        cv2.imshow("Thresholded ROI", thresh)

        # Show the main frame
        cv2.imshow("Frame", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
