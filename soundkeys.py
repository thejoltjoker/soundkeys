#!/usr/bin/env python3
import keyboard
from playsound import playsound
from pathlib import Path
import threading

def play_sound(sound_file):
    playsound(sound_file)

def on_key_press(event):
    sound_thread = threading.Thread(target=play_sound, args=(Path("sound.wav"),))
    sound_thread.start()

def main():
    keyboard.on_press(on_key_press)
    keyboard.wait()

if __name__ == '__main__':
    main()
