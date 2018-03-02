"""
This program takes the test image and template image
as params and returns the homography matrix of them
and the aligned image
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


def align_images(test1, temp1):
    """
    this function aligns the image according
    to the template using SIFT Descriptor
    """


    gray_image = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY_INV)
    median = cv2.medianBlur(thresh1, 25)
    gauss = cv2.GaussianBlur(median, (15, 15), 0)
    test = cv2.bitwise_and(test1, test1, mask=gauss)
    temp=temp1
    sift = cv2.xfeatures2d.SIFT_create()
    key_pt_temp, des_temp = sift.detectAndCompute(temp, None)
    key_pt_test, des_test = sift.detectAndCompute(test, None)

    brute_force = cv2.BFMatcher()
    matches = brute_force.knnMatch(des_test, des_temp, k=2)
    good_mat = []
    for match_first, match_second in matches:
        if match_first.distance < 0.85 * match_second.distance:
            good_mat.append(match_first)
    good_mat.sort(key=lambda x: x.distance, reverse=False)

    img3 = cv2.drawMatchesKnn(test, key_pt_test, temp, key_pt_temp, [good_mat], None, flags=2)
    cv2.namedWindow("compare Image", 0)
    cv2.imshow("compare Image", img3)
    cv2.waitKey(0)
    points_test = np.zeros((len(good_mat), 2))
    points_temp = np.zeros((len(good_mat), 2))

    for i, match in enumerate(good_mat):

        points_test[i, :2] = key_pt_test[match.queryIdx].pt
        points_temp[i, :2] = key_pt_temp[match.trainIdx].pt

    print(points_test, '\n', '\n', '\n', points_temp)
    homo, _ = cv2.findHomography(points_test, points_temp, cv2.RANSAC)
    height, width, _ = temp1.shape
    image_aligned = cv2.warpPerspective(test1, homo, (width, height))
    return image_aligned, homo

if __name__ == '__main__':
    TEST_IMAGE = cv2.imread("test_image_pan/pan_test_scan_20.jpeg", cv2.IMREAD_COLOR)
    #TEST_IMAGE = cv2.imread("dhiva_pan.jpg", cv2.IMREAD_COLOR)
    TEMPLATE_IMAGE = cv2.imread("dhiva_pan.jpg", cv2.IMREAD_COLOR)
    IMAGE_ALIGNED, HOMO = align_images(TEST_IMAGE, TEMPLATE_IMAGE)
    cv2.rectangle(IMAGE_ALIGNED, (30, 215), (700, 170), (0, 255, 0), 3)
    cv2.rectangle(IMAGE_ALIGNED, (30, 300), (700, 250), (0, 255, 0), 3)
    cv2.rectangle(IMAGE_ALIGNED, (30, 380), (240, 325), (0, 255, 0), 3)
    cv2.rectangle(IMAGE_ALIGNED, (30, 480), (310, 430), (0, 255, 0), 3)
    cv2.imwrite('result.jpeg', IMAGE_ALIGNED)
    plt.imshow(IMAGE_ALIGNED)
    plt.show()
