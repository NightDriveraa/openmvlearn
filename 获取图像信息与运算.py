import sensor
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(n=10)
sensor.set_auto_gain(True)
sensor.set_auto_whitebal(True)
sensor.set_hmirror(True)
#cmos reset

def main():
    img = sensor.snapshot()
    img.get_pixel(10,10)
    img.set_pixcel(10,10,(255,0,0))
    test = image.width(img)
    image.height(img)
    image.format(img)
    image.size(img)
    image.invert(img)
