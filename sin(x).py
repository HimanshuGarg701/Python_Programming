# printing all values of sin(x) from angle 0 to 360 with common diff 15
import math     # importing math module       
for i in range(0,361,15):
    x = math.sin(i*math.pi/180)      # math.pi is basically 22/7
    print("The value of sin(", i, ")is", x)
