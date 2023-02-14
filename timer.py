# used section.io for some of this
import time
from threading import Timer

import main


def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))


##Basic timer
def run_once(word_is_guessed):
    display('run_once:')
    t = Timer(10, main.main(), ['you were to slow'])
    t.start()  # Here run is called
    if word_is_guessed:
        t.cancel()
    else:
        pass

run_once()

##Runs immediately and once
print('Waiting.....')