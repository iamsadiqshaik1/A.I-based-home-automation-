import serial,time
ard=serial.Serial('COM3',9600)
time.sleep(2)
def light1():
    ard.write(b'1')
    print("led is on")
def light1off():
    ard.write(b'4')
    print('off1')
def lightson():
    ard.write(b'1')
    ard.write(b'2')
    ard.write(b'3')

def light2():
    ard.write(b'2')
    print("on2")
def light2off():
    ard.write(b'5')
    print("off2")

def light3():
    ard.write(b'3')
    print("on3")
def light3off():
    ard.write(b'6')
    print("off3")

def motor():
    ard.write(b'9')
    print("motor on")
def motoroff():
    ard.write(b'0')
    print("off")
    # elif datauser=='4':
    #     ard.write(b'4')
    #     print("led is off")
    #
    #     print('led off')
    # elif datauser=="5":
    #     ard.write(b'5')
    #     print("off2")
    # elif datauser=="6":
    #     ard.write(b'6')
    #     print("off3")
    # elif datauser=='7':
    #     ard.write(b'7')
    #     print("All")
    #
    # elif datauser=='9':
    #     ard.write(b'9')
    #     print("motor on")
    #
while 1:
    n=input("enter light with no to ON/OFF: ")
    if(n=='light1'):
        light1()
    elif(n=='light2'):
        light2()
    elif(n=='light3'):
        light3()
    if(n=='light1off'):
        light1off()
    elif(n=='light2off'):
        light2off()
    elif(n=='light3off'):
        light3off()
    elif(n=="offall"):
        ard.write(b'0')
        print("all off")
    elif(n=="motoron"):
        motor()
    elif(n=="motoroff"):
        motoroff()

    elif(n=='lightson'):
        lightson()