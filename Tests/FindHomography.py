import cv2
import numpy as np

min_count = 20

img1 = cv2.imread("image/f1.jpg", 0)
img2 = cv2.imread("image/f2.jpg", 0)

finder = cv2.AKAZE_create()

kp1, desc1 = finder.detectAndCompute(img1, None)
kp2, desc2 = finder.detectAndCompute(img2, None)

desc1 = np.float32(desc1)
desc2 = np.float32(desc2)

Flann_Index_Kdtree = 0
index_param = dict(algorithm = Flann_Index_Kdtree, trees = 5)
search_param = dict(checks = 50)

matcher = cv2.BFMatcher()
matches = matcher.knnMatch(desc1, desc2, k = 2)

validmatches = []

for p1, p2 in matches:
    if p1.distance < 0.7 * p2.distance:
        validmatches.append(p1)

if len(validmatches) > min_count:
    src = np.float32([kp1[m.queryIdx].pt for m in validmatches]).reshape(-1, 1, 2)
    dst = np.float32([kp2[m.trainIdx].pt for m in validmatches]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()

    h, w = img1.shape
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    destination = cv2.perspectiveTransform(pts, M)

    img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
else:
    print("Not enough matches are found.")
    matchesMask = None

draw = dict(matchColor = (255, 0, 0), singlePointColor = None, matchesMask = matchesMask, flags = 2)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, validmatches, None, **draw)

cv2.imshow('Cute_SYW', img3)
if cv2.waitKey(0):
    cv2.destroyAllWindows()
