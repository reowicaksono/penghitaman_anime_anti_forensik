import cv2
import numpy as np

def hitamkan_kulit(image_path, output_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([200, 100, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    result = image.copy()
    result[mask > 0] = [0, 0, 0]
    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(output_path, result)