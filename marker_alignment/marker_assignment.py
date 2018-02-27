import cv2
import numpy as np
from matplotlib import pyplot as plt
MAX_MATCHES = 2000
GOOD_MATCH_PERCENT = 0.1
def alignImages(im1, im2):
    """
    this function aligns the image according
    to the template using ORB

    """
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)


    orb = cv2.ORB_create(MAX_MATCHES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)


    matches.sort(key=lambda x: x.distance, reverse=False)
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    plt.imshow(imMatches), plt.show()

    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :2] = keypoints1[match.queryIdx].pt
        points2[i, :2] = keypoints2[match.trainIdx].pt


    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)


    height, width, channels = im2.shape
    im1Reg = cv2.warpPerspective(im1, h, (width, height))

    return im1Reg, h
if __name__ == '__main__':
    im = cv2.imread("img0005.jpg", cv2.IMREAD_COLOR)
    imReference = cv2.imread("add.jpg", cv2.IMREAD_COLOR)

    imReg, h = alignImages(im, imReference)
    cv2.namedWindow("Source Image", 0)
    cv2.imshow("Source Image", im)
    cv2.namedWindow("Destination Image", 0)
    cv2.imshow("Destination Image", imReference)
    cv2.namedWindow("Warped Source Image", 0)
    cv2.imshow("Warped Source Image", imReg)
    cv2.waitKey(0)