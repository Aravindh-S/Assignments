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
    test = cv2.GaussianBlur(test1, (9, 9), 0)
    temp = cv2.GaussianBlur(temp1, (9, 9), 0)
    sift = cv2.xfeatures2d.SIFT_create()
    key_pt_temp, des_temp = sift.detectAndCompute(temp, None)
    key_pt_test, des_test = sift.detectAndCompute(test, None)

    brute_force = cv2.BFMatcher()
    matches = brute_force.knnMatch(des_test, des_temp, k=2)
    good_mat = []
    for match_first, match_second in matches:
        if match_first.distance < 0.7 * match_second.distance:
            good_mat.append(match_first)
    good_mat.sort(key=lambda x: x.distance, reverse=False)
    good_mat = good_mat[:300]
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
    TEST_IMAGE = cv2.imread("test_image_pan/pan_test_scan_46.jpeg", cv2.IMREAD_COLOR)
    TEMPLATE_IMAGE = cv2.imread("dhiva_pan.jpg", cv2.IMREAD_COLOR)
    IMAGE_ALIGNED, HOMO = align_images(TEST_IMAGE, TEMPLATE_IMAGE)
    cv2.rectangle(IMAGE_ALIGNED, (40, 210), (700, 160), (0, 255, 0), 3)
    cv2.rectangle(IMAGE_ALIGNED, (40, 300), (700, 250), (0, 255, 0), 3)
    cv2.rectangle(IMAGE_ALIGNED, (40, 385), (230, 340), (0, 255, 0), 3)
    cv2.rectangle(IMAGE_ALIGNED, (40, 475), (290, 430), (0, 255, 0), 3)
    plt.imshow(IMAGE_ALIGNED)
    plt.show()
