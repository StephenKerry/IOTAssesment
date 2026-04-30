from gpiozero import Button
from signal import pause

pins = [2,3,4,5,6,17,27,22,10,9,11,13,19,26]

buttons = []

def make_handler(pin):
    def pressed():
        print(f"BUTTON DETECTED on GPIO {pin}")
    return pressed

for p in pins:
    try:
        b = Button(p, pull_up=True, bounce_time=0.2)
        b.when_pressed = make_handler(p)
        buttons.append(b)
    except:
        pass

print("Press your Grove button now...")
pause()
