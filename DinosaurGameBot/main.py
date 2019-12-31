# Cole Delong
# main function
# 12/26/2019

# imports
import directkeys
import time
import Sensor

# vars for later
UP = 0xC8
DOWN = 0xD0
SHIFT = 0x2a

# Constant variables so Rex knows when to jump
rangeOfSensor = 25
y = 130
dy = 15
x = 140
maxRange = 200
lost = False
sensor = 0

# sleep to give time to switch windows
time.sleep(2)


def millis():
    return int(round(time.time() * 1000))


def setup():

    global lost
    global sensor

    # reset the lost variable
    lost = False

    # create the sensor
    sensor = Sensor.Sensor(rangeOfSensor, x, y, dy, maxRange)


def main():

    # So it does arrow keys, not numbers
    directkeys.PressKey(SHIFT)

    while True:

        # set up the game
        setup()

        # a var so we know how long we've held the up key
        prevJumpTime = 0

        # declare globality of variables
        global lost
        global sensor

        # repeat as long as the game is not yet lost
        while True:

            # update the sensor
            sensor.update()

            # iterate through each frame of a certain area
            for i in range(sensor.rangeOfSensor):

                #    lower sensor                      higher sensor
                if sensor.currentLowPixel(i) != sensor.lowBackground() or sensor.currentHighPixel(i) != sensor.highBackground():
                    prevJumpTime = millis()
                    directkeys.PressKey(UP)
                else:
                    curTime = millis()
                    if curTime - prevJumpTime >= 100:
                        directkeys.ReleaseKey(UP)

        # Restart after losing
        directkeys.PressKey(UP)
        directkeys.ReleaseKey(UP)


if __name__ == "__main__": main()
