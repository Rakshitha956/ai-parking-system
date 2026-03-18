import cv2
import numpy as np

def detect_parking_spaces():
    print("AI Parking System Started...")

    # Create a dummy image (simulation)
    img = np.zeros((400, 600, 3), dtype=np.uint8)

    # Draw parking slots (rectangles)
    for i in range(5):
        x = 50 + i * 100
        cv2.rectangle(img, (x, 150), (x + 80, 300), (0, 255, 0), 2)

    print("Parking slots detected successfully!")

    # Show image (optional)
    # cv2.imshow("Parking System", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_parking_spaces()