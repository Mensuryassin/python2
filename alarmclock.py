import time
import datetime 

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. waiting...")

    while True:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == alarm_time:
            print*"wake up! its time!"
            break

        time.sleep(1)

def alarm_clock():
        print("Welcome to the Alarm Clock!")

        alarm_time = input("Set alarm (HH:MM:SS): ")

        try:
            valid_time = time.strftime(alarm_time, "%H:%M:%S")
            set_alarm(alarm_time)
        except ValueError:
            print("Invalid time format! Please enter the time in HH:MM:SS format.")

alarm_clock()