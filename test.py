import keyboard,time
#test keyboard
def simulate1():
    keyboard.press_and_release('f')
    print('f\n')
    time.sleep(0.01)
   
    keyboard.press_and_release('o')
    print('o\n')

    keyboard.press_and_release('f')
    print('f\n')
    time.sleep(0.5)
    print("------------------")
try:
 while True:
     if keyboard.is_pressed("t"):
        simulate1()
       

except:
    KeyboardInterrupt