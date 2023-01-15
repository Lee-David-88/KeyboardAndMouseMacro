import keyboard
import mouse


def start_keyboard_recording(_speed):
    while True:
        if keyboard.is_pressed('enter'):
            record = keyboard.record(until="esc")

            f = open('test.txt', 'w')
            for i in record:
                f.write(str(i.event_type) + ',' + str(i.scan_code) + ',' + str(i.name) + ',' +
                        str(i.time) + ',' + str(i.is_keypad) + "\n")
            f.close()

            keyboard.wait("shift")

            loaded_record = []
            f = open('test.txt').readlines()
            for line in f:
                row = line.split(',')
                event_type, scan_code, name, time, is_keypad = [i.strip() for i in row]
                keyboard_event = keyboard.KeyboardEvent(event_type, int(scan_code), name, float(time), None, None,
                                                        True if 'True' else False)
                loaded_record.append(keyboard_event)
            play_keyboard_recording(loaded_record, _speed)
            keyboard.send('shift')
            break


def play_keyboard_recording(_record, _speed):
    if _record != "":
        keyboard.play(_record, speed_factor=_speed)
    else:
        print("Empty Record")


def start_mouse_recording(_speed):
    while True:
        if keyboard.is_pressed('enter'):
            record = mouse.record(button="right")
            keyboard.wait("shift")
            play_mouse_recording(record, _speed)
            break


def play_mouse_recording(_record, _speed):
    if _record != "":
        mouse.play(_record, speed_factor=_speed)
    else:
        print("Empty Record")


def start_keyboard_and_mouse_recording():
    return


if __name__ == '__main__':
    speed = 5
    start_keyboard_recording(speed)
