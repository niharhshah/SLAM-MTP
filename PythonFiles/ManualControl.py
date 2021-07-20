from roboclaw import Roboclaw
address = 0x80
debug = 0
rc = Roboclaw("/dev/ttyACM0",115200)
rc.Open()

#------------------Functions----------------------
def ForwardFunction(speed):
    if(speed > 127 or speed < 0):
        raise ValueError
    rc.ForwardMixed(address, speed)
    print("forward w speed " + str(speed))
def BackwardFunction(speed):
    if(speed > 127 or speed < 0):
        raise ValueError
    rc.BackwardMixed(address, speed)
    print("Back w speed " + str(speed))
def encoder_test():
    print("This will move robot please confirm we are clear to move")
    if(raw_input("[y/n]").lower()=="y"):
        print("encoder_test")
def left():
    print("Left")
def right():
    print("Right")
def stop():
    print("stopped")
#----------------Main Function -------------------#
print("#########################")
print("Manual Control on jetson nano")
print("please run test to check encoder connection, Case insensitive")
print("Fxxx: Forward w speed xxx ")
print("Bxxx: Backward w speed xxx ")
print("L: Left \t R: Right")
print("E: Encoder test")
while 1:
    try:
        r_char = raw_input("Please Enter your input: ")
        r_char = r_char.upper()
        if (debug == 1):
            print("Raw_input time = " +  str(r_char[0]))
            print("Raw_input variable = " + str(r_char[1:]))
#------------------Main Functions -----------------------------#            
        if(r_char[0] == "F"):
            # try:
            speed = int(r_char[1:])
            ForwardFunction(speed)
            # except:
                # print("Speed Missing or incorrect")
        if(r_char[0] == "B"):
            speed = int(r_char[1:])
            BackwardFunction(speed)
        if(r_char[0] == "E"):
            encoder_test()
        if(r_char[0] == "L"):
            left();
        if(r_char[0] == "R"):
            right()
 
 #-------------Exception Handling-------------------#   
    except KeyboardInterrupt:
        print("\nExiting....")
        break
    except ValueError:
        print("Speed Missing or Incorrect")
    except AttributeError:
        print("Port Not opened")
    except:
        print("Invalid Input")
