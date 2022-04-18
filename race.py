import pyautogui
from PIL import ImageGrab
import time

START_LIGHT_POS = (1052,511)
START_LIGHT_GREY = (193, 193, 193)
START_LIGHT_RED = (240, 72, 105)

CORNER_1_POWER_TIME = 1.875
CORNER_1_LIFT_TIME = .36

CORNER_2_POWER_TIME = 4.85
CORNER_2_LIFT_TIME = 2.6

CORNER_3_POWER_TIME = 4.4
CORNER_3_LIFT_TIME = .35

CORNER_4_POWER_TIME = 4.1
CORNER_4_LIFT_TIME = .3

CORNER_5_POWER_TIME = 3.75
CORNER_5_LIFT_TIME = .25

CORNER_6_POWER_TIME = 1
CORNER_6_LIFT_TIME = 0

s = time.perf_counter()

def corner(power_time, lift_time, no):
    pyautogui.keyDown('space')
    time.sleep(power_time)
    pyautogui.keyUp('space')
    # print("t", no)
    time.sleep(lift_time)


def start_game():
    # print("game started")

    corner(CORNER_1_POWER_TIME, CORNER_1_LIFT_TIME, 1)
    # pyautogui.press('shift')

    corner(CORNER_2_POWER_TIME, CORNER_2_LIFT_TIME, 2)
    pyautogui.press('shift')
    corner(CORNER_3_POWER_TIME, CORNER_3_LIFT_TIME, 3)
    corner(CORNER_4_POWER_TIME, CORNER_4_LIFT_TIME, 4)
    corner(CORNER_5_POWER_TIME, CORNER_5_LIFT_TIME, 5)
    corner(CORNER_6_POWER_TIME, CORNER_6_LIFT_TIME, 6)
    pyautogui.keyDown('space')
    time.sleep(4)
    pyautogui.keyUp('space')
    # pyautogui.keyDown('space')
    # time.sleep(5)
    # pyautogui.keyUp('space')



def perfect_start_lights():
    lights_done = False
    while not lights_done:
        # print("loop 1")

        image = ImageGrab.grab()
        if image.getpixel(START_LIGHT_POS) == START_LIGHT_GREY:
            print("started")
            while not lights_done:
                # print("loop 2")

                image = ImageGrab.grab()
                if image.getpixel(START_LIGHT_POS) == START_LIGHT_RED:
                    #s = time.perf_counter()

                    print("ready")
                    # start_recording()
                    while not lights_done:
                        # print("loop 3")

                        image = ImageGrab.grab()
                        if image.getpixel(START_LIGHT_POS) == START_LIGHT_GREY:
                            #print(time.perf_counter() - s)
                            #print("go")
                            start_game()
                            lights_done = True


# image = ImageGrab.grab()
# print(image.getpixel((1052,511)))""
# print(time.process_time())
# print(time.perf_counter()-s)
def start_recording():
    pyautogui.keyDown("shift")
    pyautogui.keyDown("2")
    pyautogui.keyUp("shift")
    pyautogui.keyUp("2")


def stop_recording():
    pyautogui.keyDown("shift")
    pyautogui.keyDown("3")
    pyautogui.keyUp("shift")
    pyautogui.keyUp("3")
# time.sleep(3)
# pyautogui.hotkey("shift", "3")


if __name__ == '__main__':
    perfect_start_lights()
    time.sleep(1)
    # stop_recording()
