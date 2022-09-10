import rotatescreen,time
obj=rotatescreen.get_primary_display()
while True:
    obj.rotate_to(90)
    time.sleep(1)
    obj.rotate_to(180)
    time.sleep(1)
    obj.rotate_to(270)
    time.sleep(1)
    obj.rotate_to(360)
    time.sleep(1)