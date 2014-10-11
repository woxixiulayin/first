__author__ = 'liuzhigang'
from ctypes import *
import win32api
import win32con
import time
from pymouse import PyMouse
import os
class POINT(Structure):
     _fields_ = [("x", c_ulong),
     ("y", c_ulong)]
orig = POINT()
orig1 = POINT()
windll.user32.GetCursorPos(byref(orig))
print orig.x
windll.user32.GetCursorPos(byref(orig))
print orig.x

while True:
    windll.user32.SetCursorPos(orig.x+2,orig.y+1)
    time.sleep(0.01)
    """windll.user32.GetCursorPos(byref(orig))
    if orig1.x != orig.x or orig1.y != orig.y:
        orig1.x = orig.x
        orig1.y = orig.y
        print orig1.x,orig1.y"""
