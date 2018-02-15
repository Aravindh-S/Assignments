"""
this function reads the image containing single text
and contours the individual letters
"""

import cv2
IMAG = [[[]]]


def img_read(file_path):
    """
    Takes in the file path and returns the image
    """
    return cv2.imread(file_path)

    #cv2.imshow("cropped", imge)
    # cv2.waitKey(0)


def img_correction(image):
    """
    The image is modified to ggrayscale then applied threshold
    to the image and dilated. The false positives are removed
    by morphology and returns the corrected image
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=0)
    opening = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel)
    return opening


def img_obtain_contour(opening_local):
    """
    returns contours for the given image
    """
    _, contours, _ = cv2.findContours(opening_local, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours


def print_contours(contours_local):
    """
    This prints the contours of the image
    """
    for contour in contours_local:
        [xcord, ycord, width, height] = cv2.boundingRect(contour)
        cv2.rectangle(IMAG, (xcord, ycord), (xcord + width, ycord + height), (255, 0, 255), 2)
    cv2.imshow("cropped", IMAG)
    cv2.waitKey(0)


if __name__ == '__main__':
    FILEPATH = "imageedit_2_8893669538.jpg"
    IMAG = img_read(FILEPATH)
    CORRECTED_IMAGE = img_correction(IMAG)
    CONTOURS_OBTAINED = img_obtain_contour(CORRECTED_IMAGE)
    print_contours(CONTOURS_OBTAINED)
