# File: Ex2_10
# Author: Niki Leppänen
# Description: Code the alarm clock, use objects.

from datetime import datetime
import time


class AlarmClock:

    def __init__(self):
        self.wake_up_time = ""

    # This method allows user to set alarm
    def set_alarm(self):
        self.wake_up_time = input("Set your alarm (Use hh:mm:ss): ")

    # This method returns value of user input in set_alarm function
    def get_alarm_time(self):
        return self.wake_up_time

    # Alarm method follows current time and updates it to user every second with time function. When current time is
    # equal to users input, alarm goes off
    def alarm(self, set_alarm_timer):
        while True:
            time.sleep(1)
            current_time = datetime.now()
            now = current_time.strftime("%H:%M:%S")
            print(now)

            if now == set_alarm_timer:
                print("WAKE UP!!!")
                break


# The main function
def main():

    # Create an object from the AlarmClock class
    alarm = AlarmClock()

    # Calls set_alarm function from AlarmClock class
    alarm.set_alarm()

    # Gets user input and prints it
    time_set = alarm.get_alarm_time()
    print("Alarm set to ", alarm.get_alarm_time())

    # Uses alarm function and gives it the user input
    alarm.alarm(time_set)


main()




