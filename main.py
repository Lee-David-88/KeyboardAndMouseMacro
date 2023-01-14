import keyboard
import mouse


def start_recording(_speed):
    while True:
        if keyboard.is_pressed('enter'):
            record = keyboard.record(until="esc")
            keyboard.wait("shift")
            play_recording(record, _speed)


def play_recording(_record, _speed):
    if _record != "":
        keyboard.play(_record, speed_factor=_speed)
    else:
        print("Empty Record")


if __name__ == '__main__':
    speed = 1
    start_recording(speed)
