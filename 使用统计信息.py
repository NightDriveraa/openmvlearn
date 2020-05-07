import sensor
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_gain(True)
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)
ROI = (90,30,15,15)

def main():
    while(True):
        img = sensor.snapshot()
        statistics = img.get_statistics(roi = ROI)
        color_1 = statistics.l_mode()
        color_2 = statistics.a_mode()
        color_3 = statistics.b_mode()
        print(color_1,color_2,color_3)
        img.draw_rectangle(ROI)

main()
