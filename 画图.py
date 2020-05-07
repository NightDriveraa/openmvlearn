import sensor
#reset
sensor.reset()
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.RGB565)
sensor.set_auto_whitebal(False)
sensor.set_auto_gain(True)
sensor.skip_frames(10)
sensor.set_hmirror(True)

def main():
    while(True):
        img = sensor.snapshot()
        img.draw_line((10,10,40,40),color=(255,5,5))
        img.draw_circle((30,30,30),color = (0,255,0))
        img.draw_cross(60,60,size = 10)
        img.draw_rectangle((30,30,20,20),color = (0,0,255))
        img.draw_cross((100,100),size = 100,color = (255,0,0))


main()
