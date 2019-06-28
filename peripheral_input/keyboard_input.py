import pynput


class KeyboardInput:

    def __init__(self):
        self.keyboard_control()

    def keyboard_control(self):
        input_keyboard = pynput.keyboard.Controller()
        input_keyboard.press("t")
        input_keyboard.release("t")
        input_keyboard.press("o")
        input_keyboard.release("o")
        input_keyboard.press("u")
        input_keyboard.release("u")
        input_keyboard.press("c")
        input_keyboard.release("c")
        input_keyboard.press("h")
        input_keyboard.release("h")
