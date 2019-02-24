# calculating time consumed
class Time:
    def __init__(self,start_time, end_time):
        self._start_time = start_time
        self._end_time = end_time

    def display(self):
        print("The starting time is: ",self._start_time[0], ":", self._start_time[1])
        print("The end time of the exam is: ",self._end_time[0], ":", self._end_time[1])



try:
    x = int(input("enter the starting time(hours only from 1 to 24): "))
    y = int(input("Enter the minutes of starting time: "))
    z = int(input("enter the ending time(hours only from 1 to 24): "))
    w = int(input("Enter the minutes of ending time: "))
    if x - z>=0:
        raise ValueError
    else:
        v = Time([x,y],[z,w])
        v.display()
except ValueError:
    print("Starting time should be before the ending time")
