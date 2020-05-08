# Untitled - By: ws1224285879 - 周五 5月 8 2020

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(10)
black = (2, 13, -7, 127, -6, 127)

def main():
    while(True):
        img = sensor.snapshot()
        blobs = img.find_blobs([black],invert=False)
        for blob in blobs:
            ROI = blob.rect()
        img.draw_rectangle(ROI)


main()
