
from thread_file import *

ring_thread = RingThread(1, "Thread of alarm", 1)
update_thread = UpdateThread(1, "Thread of updating", 1)
new_alarm_thread = NewAlarmThread(1, "Thread to add new alarms" ,1)


def start_threads():
    ring_thread.start()
    update_thread.start()
    new_alarm_thread.start()


def stop_threads():
    ring_thread.stop_thread()
    ring_thread.join()
    update_thread.stop_thread()
    update_thread.join()


def main() -> None:
    check_alarm_txt()
    start_threads()
    new_alarm_thread.join()
    stop_threads()
    raise SystemExit()


if __name__ == "__main__":
    main()


