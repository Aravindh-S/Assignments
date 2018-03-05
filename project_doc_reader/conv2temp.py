"""
This program takes the test image and template image
as params and returns the homography matrix of them
and the aligned image
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt



def image_masking(test1):
    """
    Takes in the test image filters out unwanted part of the image
    like white noise and returns an image which is ready for
    computing key points and descriptors

    :param test1: TEST IMAGE
    :return: FILTERED_IMAGE
    """
    gray_image = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY_INV)
    median = cv2.medianBlur(thresh1, 25)
    gauss = cv2.GaussianBlur(median, (15, 15), 0)
    masked_img = cv2.bitwise_and(test1, test1, mask=gauss)
    return masked_img

def reading_image(path_name):
    """
    Takes in the file path and returns the image in
    the file path
    :param path_name: file path name
    :return: image in the file path
    """
    return cv2.imread(path_name, cv2.IMREAD_COLOR)

def compute_kp_des(img):
    """
    Takes in the image and computes key points and
    descriptors using SIFT
    :param img: Image
    :return: KeyPoint , Descriptor
    """
    sift = cv2.xfeatures2d.SIFT_create()
    key_pt, des = sift.detectAndCompute(img, None)
    return (key_pt,des)

def find_good_matches(key_pt_temp,key_pt_test,des_test,des_temp):
    """
    Takes in the keyPoints and descriptor of both test
    and template image and computes  best matches using
    BruteForce matching and Coordinates of Matches
    :param key_pt_temp: KeyPoints of the Template image
    :param key_pt_test: KeyPoints of the Test image
    :param des_test: Descriptors of the Test image
    :param des_temp: Descriptors of the Template image
    :return:
    """
    brute_force = cv2.BFMatcher()
    matches = brute_force.knnMatch(des_test, des_temp, k=2)
    good_mat = []
    for match_first, match_second in matches:
        if match_first.distance < 0.7 * match_second.distance:
            good_mat.append(match_first)
    good_mat.sort(key=lambda x: x.distance, reverse=False)
    '''
    img3 = cv2.drawMatchesKnn(test, key_pt_test, temp, key_pt_temp, [good_mat], None, flags=2)
    cv2.namedWindow("compare Image", 0)
    cv2.imshow("compare Image", img3)
    cv2.waitKey(0)
    '''
    points_test = np.zeros((len(good_mat), 2))
    points_temp = np.zeros((len(good_mat), 2))

    for i, match in enumerate(good_mat):
        points_test[i, :2] = key_pt_test[match.queryIdx].pt
        points_temp[i, :2] = key_pt_temp[match.trainIdx].pt
    return (points_test,points_temp)

def process_image(test_img,temp_img):
    """
    Takes in both template image and test image
    Processes the image and aligns it according to template

    :param test_img: TestImage
    :param temp_img: TemplateImage
    :return: Aligned Image , Homography Matrix
    """
    masked_image=image_masking(test_img)
    key_pt_temp, des_temp = compute_kp_des(temp_img)
    key_pt_test, des_test = compute_kp_des(masked_image)
    points_test,points_temp=find_good_matches(key_pt_temp,key_pt_test,des_test,des_temp)
    homo, _ = cv2.findHomography(points_test, points_temp, cv2.RANSAC)
    height, width, _ = temp_img.shape
    image_aligned = cv2.warpPerspective(test_img, homo, (width, height))
    return image_aligned, homo




if __name__ == '__main__':

    TEST_IMAGE = reading_image("passport_test_image/passport_test_image_1.jpg")
    #TEST_IMAGE = cv2.imread("dhiva_pan.jpg", cv2.IMREAD_COLOR)
    TEMPLATE_IMAGE = reading_image("passport_temp.jpg")
    IMAGE_ALIGNED, HOMO = process_image(TEST_IMAGE, TEMPLATE_IMAGE)
    '''
    #cv2.rectangle(IMAGE_ALIGNED, (30, 215), (700, 170), (0, 255, 0), 3)
    #cv2.rectangle(IMAGE_ALIGNED, (30, 300), (700, 250), (0, 255, 0), 3)
    #cv2.rectangle(IMAGE_ALIGNED, (30, 380), (240, 325), (0, 255, 0), 3)
    #cv2.rectangle(IMAGE_ALIGNED, (30, 480), (310, 430), (0, 255, 0), 3)
    #cv2.imwrite('result.jpeg', IMAGE_ALIGNED)
    '''
    plt.imshow(IMAGE_ALIGNED)
    plt.show()
