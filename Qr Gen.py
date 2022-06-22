import pyqrcode 
from pyqrcode import QRCode   
from tkinter import *

main_window=Tk()
main_window.title('Qr Code Generator By Krerkkiat')
main_window.resizable(0, 0)

def get_input():
   input=text_box.get("1.0","end-1c")
   print(input)
   url = pyqrcode.create(input) 
   url.svg("QRCode.svg", scale = 10)
text_box=Text(main_window, height=5, width=40)
text_box.pack()

gen= Button(main_window, height=5, width=10, text = 'Generate', fg='#39dbd9', command=lambda: get_input())
gen.pack()

main_window.mainloop()