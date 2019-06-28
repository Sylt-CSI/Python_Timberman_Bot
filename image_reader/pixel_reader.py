import cv2
import numpy
import time


class PixelReader:

    def __init__(self):
        self._read_image()

    def _read_image(self):
        time_list = []
        block_list = []
        # for i in range(3,101,2):

        img = cv2.imread("/Users/gcc/Desktop/experimental/experiment_open_cv/timber.jpeg")
        # thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        # print(type(thresh1))
        # cv.imwrite("image_folder/timber_wb.png", thresh1)
        start = time.time()
        thresh1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, th3 = cv2.threshold(thresh1, 11, 255, cv2.THRESH_BINARY)
        # th3 = cv2.adaptiveThreshold(thresh1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 47)

            # time_list.append(turt)
            # block_list.append(i)
        # print(block_list, time_list)
        cv2.imwrite("image_folder/timber_gaussian_2.png", th3)


        # image_array = cv2.imread("image_folder/test_1.png")
        # imgray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite("image_folder/test_1.png", imgray)
