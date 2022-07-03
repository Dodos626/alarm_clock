from alarm_functions import *
import threading
import time
# globals
ALARM_TIME_ARRAY = []
mutex = threading.Lock()


class RingThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.stop = False

    def run(self):
        while not self.stop:
            mutex.acquire()
            if len(ALARM_TIME_ARRAY) == 0:
                mutex.release()
                continue
            while True:
                if ALARM_TIME_ARRAY[0][1] == 0:
                    ring_alarm(ALARM_TIME_ARRAY[0][0])
                    ALARM_TIME_ARRAY.remove(ALARM_TIME_ARRAY[0])
                    if len(ALARM_TIME_ARRAY) == 0:
                        print("No more alarms left")
                        break
                else:
                    break
            mutex.release()
        return

    def stop_thread(self):
        self.stop = True


class UpdateThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.stop = False

    def run(self):
        while not self.stop:
            mutex.acquire()
            if len(ALARM_TIME_ARRAY) == 0:
                mutex.release()
                continue
            for array in ALARM_TIME_ARRAY:
                array[1] = time_left_till_ring(array[0])
            mutex.release()
            time.sleep(1)

        return

    def stop_thread(self):
        self.stop = True


class NewAlarmThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.stop = False

    def run(self):
        while not self.stop:
            tmp = take_new_alarm_from_input()
            if tmp == "Print":
                print_alarms(ALARM_TIME_ARRAY)
            elif tmp:
                mutex.acquire()
                add_to_alarm(ALARM_TIME_ARRAY, tmp)
                print(ALARM_TIME_ARRAY)
                mutex.release()
            else:
                return

    def stop_thread(self):
        self.stop = True

