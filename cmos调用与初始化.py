import sensor
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(n=10)
sensor.set_auto_gain(True)
sensor.set_auto_whitebal(True)
sensor.set_hmirror(True)

while(True):
    img = sensor.snapshot()
