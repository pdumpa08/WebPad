# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.holdtap import HoldTap

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
holdtap = HoldTap()
keyboard.modules.append(macros)
keyboard.modules.append(holdtap)

# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10, board.D11]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define keymap combos and modtaps
LIVE = simple_key_sequence(
    (KC.LCMD(KC.L), KC.LCMD(KC.O))
)
DUAL_KEY = KC.HT(hold=KC.MACRO(Press(KC.LCMD), Press(KC.LSFT), Tap(KC.M), Release(KC.LCMD), Release(KC.LSFT)), 
                 tap=KC.MACRO(Press(KC.LCMD), Press(KC.LALT), Tap(KC.J), Release(KC.LCMD), Release(KC.LALT)),
                 prefer_hold=True,
                 tap_interrupted=False)

# Define the keymap
# refresh, inspect, clear cache, start live server, switch to console, responsive development mode
keyboard.keymap = [
    [KC.MACRO(Press(KC.LCMD), Tap(KC.R), Release(KC.LCMD)), 
     KC.MACRO(Press(KC.LCMD), Press(KC.LSFT), Tap(KC.DELETE), Release(KC.LCMD), Release(KC.LSFT)), 
     KC.MACRO(Press(KC.LCMD), Press(KC.LALT), Tap(KC.C), Release(KC.LCMD), Release(KC.LALT)), 
     LIVE,
     DUAL_KEY,]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()