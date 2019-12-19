'''
Created on Dec 18, 2019

@author: Ben Insler
'''

from tkinter import *
from tkinter import ttk, messagebox, filedialog, simpledialog
import time, datetime, os
import sys
#xxxx


class idol_swap_GUI:
    
    def __init__(self, master):
        
        master.title('Idol Swap')
        master.resizable(False, False)
        master.configure(background = '#e7e7e7')
    
        #Style Config
        self._style = ttk.Style()
        self._style.theme_use('aqua')
        self._style.configure('Notification.TLabel', foreground = '#ff0000')
        self._style.configure('Heading.TLabel', font = ('Arial', 14, 'bold'), foreground = '#999', anchor = CENTER)
        self._style.configure('SectionHead.TLabel', font = ('', 13, 'bold'))
        self._style.configure('PulldownLabel.TLabel', foreground = '#999')
        self._style.configure('Green.TNotebook', background = '#0F0')
        self._style.configure('prefFaded.TLabel', background = '#aaa', foreground ='#666')
        self._style.configure('PrefsHead.TLabel', font = ('', 13, 'bold'), bg = '#aaa')
        self._style.configure('TNotebook.Tab', padding=(8, 8, 8, 0)) #########################################################
        
        self._frameTop = ttk.Frame(master, width = 660, height = 170)
        self._frameTop.pack()
        
        ttk.Label(self._frameTop, text = 'Current settings installed on system'.upper(), style = 'Heading.TLabel').pack(pady = 10)
        
        
        
if __name__ == '__main__':
    
    print('in')
    root = Tk()
    x = idol_swap_GUI(root)
    print("hi")