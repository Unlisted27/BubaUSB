import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

time.sleep(1)

# Dictionary for keyboard commands
duckyCommands = {
    'WINDOWS': Keycode.WINDOWS, 'GUI': Keycode.GUI, 'APP': Keycode.APPLICATION,
    'MENU': Keycode.APPLICATION, 'SHIFT': Keycode.SHIFT, 'ALT': Keycode.ALT,
    'CONTROL': Keycode.CONTROL, 'CTRL': Keycode.CONTROL, 'DOWNARROW': Keycode.DOWN_ARROW,
    'DOWN': Keycode.DOWN_ARROW, 'LEFTARROW': Keycode.LEFT_ARROW, 'LEFT': Keycode.LEFT_ARROW,
    'RIGHTARROW': Keycode.RIGHT_ARROW, 'RIGHT': Keycode.RIGHT_ARROW, 'UPARROW': Keycode.UP_ARROW,
    'UP': Keycode.UP_ARROW, 'BREAK': Keycode.PAUSE, 'PAUSE': Keycode.PAUSE,
    'CAPSLOCK': Keycode.CAPS_LOCK, 'DELETE': Keycode.DELETE, 'END': Keycode.END,
    'ESC': Keycode.ESCAPE, 'ESCAPE': Keycode.ESCAPE, 'HOME': Keycode.HOME,
    'INSERT': Keycode.INSERT, 'NUMLOCK': Keycode.KEYPAD_NUMLOCK, 'PAGEUP': Keycode.PAGE_UP,
    'PAGEDOWN': Keycode.PAGE_DOWN, 'PRINTSCREEN': Keycode.PRINT_SCREEN, 'ENTER': Keycode.ENTER,
    'SCROLLLOCK': Keycode.SCROLL_LOCK, ' ': Keycode.SPACE, 'TAB': Keycode.TAB,
    'BACKSPACE': Keycode.BACKSPACE, '=': Keycode.EQUALS, '/': Keycode.FORWARD_SLASH,
    '?': [Keycode.SHIFT, Keycode.FORWARD_SLASH], ':': [Keycode.SHIFT, Keycode.SEMICOLON],
    '.': Keycode.PERIOD, 'A': Keycode.A, 'B': Keycode.B, 'C': Keycode.C,
    'D': Keycode.D, 'E': Keycode.E, 'F': Keycode.F, 'G': Keycode.G, 'H': Keycode.H,
    'I': Keycode.I, 'J': Keycode.J, 'K': Keycode.K, 'L': Keycode.L, 'M': Keycode.M,
    'N': Keycode.N, 'O': Keycode.O, 'P': Keycode.P, 'Q': Keycode.Q, 'R': Keycode.R,
    'S': Keycode.S, 'T': Keycode.T, 'U': Keycode.U, 'V': Keycode.V, 'W': Keycode.W,
    'X': Keycode.X, 'Y': Keycode.Y, 'Z': Keycode.Z, 'F1': Keycode.F1, 'F2': Keycode.F2,
    'F3': Keycode.F3, 'F4': Keycode.F4, 'F5': Keycode.F5, 'F6': Keycode.F6,
    'F7': Keycode.F7, 'F8': Keycode.F8, 'F9': Keycode.F9, 'F10': Keycode.F10,
    'F11': Keycode.F11, 'F12': Keycode.F12,'0': Keycode.ZERO,'1': Keycode.ONE,'2': Keycode.TWO,
    '3': Keycode.THREE,'4': Keycode.FOUR,'5': Keycode.FIVE,'6': Keycode.SIX,'7': Keycode.SEVEN,
    '8': Keycode.EIGHT,'9': Keycode.NINE
}

keyboard = Keyboard(usb_hid.devices)

def write(string: str):
    for letter in string:
        try:
            if letter.upper() in duckyCommands:
                #Handle special chars
                key = duckyCommands[letter.upper()]
                if isinstance(key, list):
                    print("LIST")
                    for k in key:
                        keyboard.press(k)
                    keyboard.release_all()
                #Handle uppercase and lowercase letters
                elif letter.isupper():
                    print(f"UPPERCASE: {letter}")
                    keyboard.press(Keycode.SHIFT, key)
                    keyboard.release_all()
                else:
                    print(f"LOWERCASE: {letter}")
                    keyboard.press(key)  # Press key without SHIFT
                    keyboard.release_all()
                keyboard.release_all()
            else:
                print(f"Character '{letter}' not found in duckyCommands.")
        except Exception as e:
            print(f"Error with character '{letter}': {e}")

keyboard.press(Keycode.ALT,Keycode.F4)
keyboard.release_all()
keyboard.press(Keycode.WINDOWS, Keycode.R)
#time.sleep(1)
keyboard.release_all()
write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
keyboard.press(Keycode.ENTER)
keyboard.release_all()
