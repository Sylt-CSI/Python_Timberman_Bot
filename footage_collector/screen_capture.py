import time
import mss
import numpy
import cv2


class ScreenCapture:

    def __init__(self, frames_per_second=12, capture_time_in_seconds=1):
        self._start = time.time()
        self.frames_per_second = 1/frames_per_second
        self.capture_time_in_seconds = capture_time_in_seconds
        # total frames = fps*capture time if
        self._total_frames = frames_per_second*capture_time_in_seconds
        # self._capture_screen()
        self._timing()

    # def _capture_screen(self):
    #     with mss.mss() as sct:
    #         monitor = {"top": 0, "left": 0, "width": 200, "height": 200}
    #     frame_number = 0
    #     while frame_number < self._total_frames:
    #         frame_number += 1
    #
    #         # Grab the data
    #         sct_img = sct.grab(monitor)
    #
    #         # Save to the picture file
    #         mss.tools.to_png(sct_img.rgb, sct_img.size, output="image_folder/test_{}.png".format(frame_number))

    def _timing(self):
        upper_left = (50, 50)
        bottom_right = (600, 600)
        frame_number = 0
        start_time = time.time()
        with mss.mss() as sct:
            # Capture the whole display (for some reason width and height are doubled.)
            monitor = {"top": 0, "left": 0, "width": 1280, "height": 800}
            while time.time() < (start_time + float(self.capture_time_in_seconds)):
                frame_number += 1
                sct_img = numpy.array(sct.grab(monitor))  # Capture screen by specified size and convert to numpy array.
                sct_img = cv2.cvtColor(sct_img, cv2.COLOR_BGR2GRAY)  # Gray scale image.
                ret ,sct_img = cv2.threshold(sct_img, 50, 255, cv2.THRESH_BINARY)
                # sct_img = cv2.adaptiveThreshold(sct_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 47)  # Apply filter to make contours.
                # cv2.rectangle(sct_img, upper_left, bottom_right,(255,0,0),2)
                cv2.imwrite("image_folder/test_{}.png".format(frame_number), sct_img)
                print(frame_number)  # Frames produced in set time.

            #     mss.tools.to_png(sct_img, sct_img.size, output="image_folder/test_{}.png".format(frame_number),)
            # print(time.time(), threading.active_count())


        # while True:
        #     time.sleep(1/self.frames_per_second)
        # print(os.getcwd())
        # start = time.time()
        #
        # print(time.time()-start)

