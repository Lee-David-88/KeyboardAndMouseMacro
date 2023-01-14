import keyboard
import mouse


def start_keyboard_recording(_speed):
    while True:
        if keyboard.is_pressed('enter'):
            record = keyboard.record(until="esc")
            keyboard.wait("shift")
            play_keyboard_recording(record, _speed)


def play_keyboard_recording(_record, _speed):
    if _record != "":
        keyboard.play(_record, speed_factor=_speed)
    else:
        print("Empty Record")


def start_mouse_recording():
    return


if __name__ == '__main__':
    speed = 1
    start_keyboard_recording(speed)
