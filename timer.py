# used section.io for some of this
import time
from threading import Timer


def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))


##Basic timer
def run_once():
    display('run_once:')
    t = Timer(10, display, ['Timeout:'])
    t.start()  # Here run is called


run_once()
if word_is_guessed:
    t.cancel()
else:
    pass
##Runs immediately and once
print('Waiting.....')