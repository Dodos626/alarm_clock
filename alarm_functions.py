import os
import datetime
import random
import webbrowser


def check_alarm_txt():
    if not os.path.isfile("alarm.txt"):
        print('Creating settings file')
    with open("alarm.txt", "w") as alarm_file:
        alarm_file.write("https://youtu.be/7Q9UqyaRAbQ")


def check_alarm_input(alarm_time):
    match len(alarm_time):
        case 1:
            if 24 > alarm_time[0] >= 0:
                return True
        case 2:
            if 24 > alarm_time[0] >= 0 and 60 > alarm_time[1] >= 0:
                return True
        case 3:
            if 24 > alarm_time[0] >= 0 and 60 > alarm_time[1] >= 0 and 60 > alarm_time[2] >= 0:
                return True
    return False


def take_new_alarm_from_input():
    print("Set a time for the alarm (Ex. 06:30 or 18:30:00) or S/s for stopping the alarm or P/p to print the alarms")
    while True:
        alarm_input = input(">> ")
        try:
            if alarm_input == "S" or alarm_input == "s":
                print("Stopping alarm clock")
                return False
            if alarm_input == "P" or alarm_input == "p":
                return "Print"
            alarm_time = [int(n) for n in alarm_input.split(":")]
            if check_alarm_input(alarm_time):
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")
    for i in range(len(alarm_time), 3):
        alarm_time.append(0)
    return alarm_time


def time_left_till_ring(alarm_time):
    second_hms = [3600, 60, 1]
    alarm_seconds = sum([a * b for a, b in zip(second_hms[:len(alarm_time)], alarm_time)])
    now = datetime.datetime.now()
    current_time_seconds = sum([a * b for a, b in zip(second_hms, [now.hour, now.minute, now.second])])
    time_diff_seconds = alarm_seconds - current_time_seconds
    if time_diff_seconds < 0:
        time_diff_seconds += 86400
    if time_diff_seconds == 0:
        return time_diff_seconds

    return time_diff_seconds


def sort_alarm_clocks(alarm_array):
    alarm_array.sort(key=lambda x: x[1])


def add_to_alarm(alarm_array=None, alarm_to_add=None):
    if alarm_to_add is None:
        print("something went terribly bad")
        raise SystemExit()
    if alarm_array is None:
        tmp = [alarm_to_add, time_left_till_ring(alarm_to_add)]
        alarm_array = [tmp]
        return
    else:
        time_left = time_left_till_ring(alarm_to_add)
        tmp = [alarm_to_add, time_left]
        alarm_array.append(tmp)
        for alarms in alarm_array:
            alarms[1] = time_left_till_ring(alarms[0])
        sort_alarm_clocks(alarm_array)

    return


def ring_alarm(alarm_time):
    print("Alarm with time --> %d:%d:%d rings" % (alarm_time[0],  alarm_time[1],  alarm_time[2]))
    print(">>")
    with open("alarm.txt", "r") as alarm_file:
        videos = alarm_file.readlines()

    webbrowser.open(random.choice(videos))


def print_alarms(alarm_array):
    for alarm in alarm_array:
        print("%d:%d:%d rings in %d seconds" % (alarm[0][0], alarm[0][1], alarm[0][2], alarm[1]))
