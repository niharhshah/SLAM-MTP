from roboclaw import Roboclaw
import math as m
address = 0x80
debug = 0
d_val=200
rc = Roboclaw("/dev/ttyACM0",115200)
rc.Open()

#------------------Functions----------------------
def delay(val=1000):
    for i in range(0,val):
        pass
	 
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
def encoder_test(speed,d_val):
    print("This will move robot please confirm we are clear to move")
    if(raw_input("[y/n]").lower()=="y"):
        print("encoder_test")
        
    #move motor forward for some time
        SetEncM1(self,address,0):
        SetEncM2(self,address,0):
        rc.ForwardMixed(address,speed)
        delay(d_val)
        rc.stop()
        en1=rc.ReadEncM1(address)
        en2=rc.ReadEncM2(address)
        print("forward: enc1={}; enc2={}".format(en1,en2))
        rc.BackwardMixed(address,speed)
        delay(2*d_val)
        rc.stop()
        en3=rc.ReadEncM1(address)
        en4=rc.ReadEncM2(address)
        print("backward: enc1={}; enc2={}".format(en3,en4))
        if(en1*en3<0 and en2*en4<0 and en3*en4>0 and en2*en1>0)
        print("encoder test done---working fine")
            return True
        else
    	
            print("Error in directions of the motor , please reconnect the wires and tune again!!!")
            raise ValueError
    
  
    	
        #here

def left(speed):
    if(speed > 127 or speed < 0):
        raise ValueError
    rc.TurnLeftMixed(address,speed)
    print("Left")
def right(speed):
    if(speed > 127 or speed < 0):
        raise ValueError
    rc.TurnRightMixed(address,speed)
    print("Right")
def stop():
    rc.ForwardMixed(address,0)
    print("stopped")
speed = 0
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
            encoder_test(speed,d_val)
        if(r_char[0] == "L"):
            speed = int(r_char[1:])
            left(speed);
        if(r_char[0] == "R"):
            speed = int(r_char[1:])
            right(speed)
        if(r_char[0] == "S"):
            stop()
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
