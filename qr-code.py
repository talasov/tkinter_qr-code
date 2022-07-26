import tkinter as tk
from tkinter import ttk
import sys
import qrcode
from tkinter import *
from PIL import Image, ImageTk
import os


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('900x800')
        self.resizable(False, False)
        self.title('qr-code')
        self.set_ui()
        self['bg'] = '#fff'

    def set_ui(self):

        self.delete()

        '''input для ввода текста'''

        self.label = tk.Label(text="Вставьте ссылку")
        self.data = tk.Entry(width=100)
        self.label.pack()
        self.data.pack()

        calculate = ttk.Button(self, text='Сгенерировать qr-code', command=self.calculate)
        calculate.pack(fill=tk.X)
        self.label2 = tk.Label(text='qr-code')
        self.label2.pack()

        self.canvas = tk.Canvas(width=600, height=600)
        self.canvas.pack()
        self.get_image()

        '''Открыть изображение'''
        open_dir = ttk.Button(self, text='Открыть qr-code', command=self.open_img)
        open_dir.pack(fill=tk.X)

        '''Закрыть'''
        close_button = ttk.Button(self, text="Закрыть", command=self.app_exit, )
        close_button.pack(fill=tk.X)

    def get_image(self):
        '''Вывод qr-code '''
        if os.path.exists('site.png') == True:
            self.image = Image.open('site.png')
        else:
            self.image = Image.open('fon.jpg')
        self.qr_obj = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.qr_obj)

    def app_exit(self):
        '''Функция закрытия'''
        self.destroy()
        sys.exit()

    def calculate(self, filename="site.png"):
        '''Генерирование qr-code '''
        data = self.data.get()
        img = qrcode.make(data)
        img.save(filename)
        self.refresh()

    def refresh(self):
        self.get_image()

    def delete(self):
        if os.path.exists('site.png') == True:
            os.remove('site.png')

    def open_img(self):
        if os.path.exists('site.png') == True:
            img = Image.open('site.png')
            img.show()


root = Application()
root.mainloop()
