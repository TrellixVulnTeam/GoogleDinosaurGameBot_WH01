# Cole Delong
# main function
# 12/26/2019

# imports
import directkeys
import time
from PIL import ImageGrab

# vars for later
UP = 0xC8
DOWN = 0xD0
SHIFT = 0x2a
gameCoords = [635, 125, 1300, 300]

def millis():
    return int(round(time.time() * 1000))

def main():

    # Why do i do this to myself
    first = True
    time.sleep(2)

    # Constant variables determining when to jump and shit
    prevJumpTime = millis()
    prevScreen = ImageGrab.grab(bbox=gameCoords)
    startTime = time.time()
    rangeOfSensor = 25

    while True:
        # Yikes
        y = 130
        dy = 15
        x = 140

        if x + rangeOfSensor <= 325:
            rangeOfSensor = int(25 + 1.25 * (time.time() - startTime))

        directkeys.PressKey(SHIFT)
        screen = ImageGrab.grab(bbox=gameCoords)
        print(time.time() - startTime)
        lowBackground = (screen.getpixel((1, y)))
        highBackground = (screen.getpixel((1, y + dy)))

        #  target = ImageGrab.grab(bbox=[885, 240, 1035, 290])
        # iterate through each frame of a certain area... I think...
        for i in range(rangeOfSensor):
            currentLowPixel = (screen.getpixel((x + i, y)))
            currentHighPixel = (screen.getpixel((x + i, y - dy)))

            #    lower sensor                      higher sensor
            if (currentLowPixel != lowBackground or currentHighPixel != highBackground):
            #   directkeys.ReleaseKey(DOWN)

                prevJumpTime = millis()
                directkeys.PressKey(UP)
                #     target.show()
                #    break

            else:
                curTime = millis()
                if (prevJumpTime - curTime >= 100 and time.time() - startTime <= 100) and (time.time() - startTime > 100):
                    directkeys.ReleaseKey(UP)
            #    directkeys.PressKey(DOWN)

    # Restart after losing
    directkeys.PressKey(UP)
    directkeys.ReleaseKey(UP)

if __name__ == "__main__": main()