import sys
from footage_collector import screen_capture
from image_reader import pixel_reader
from peripheral_input import keyboard_input

def main(argv=None):
    if argv is None:
        argv = sys.argv
    screen_capture.ScreenCapture()
    # pixel_reader.PixelReader()
    # keyboard_input.KeyboardInput()

if __name__ == "__main__":
    sys.exit(main())
