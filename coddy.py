### coddy by loadycode
### build310121 31-01-2021 17:16
### gnu general public license v3.0

import tkinter as tk
import tkinter.filedialog as fd

## user interface

window=tk.Tk()
window.title("coddy")
window.minsize(600,400)

textbox=tk.Text(
        window,
        relief='flat',
        undo=True,
        bg='#444444',
        fg='silver',
        insertbackground='orange'
        )
textbox.pack(
        fill='both',
        expand=True
        )
verscroll=tk.Scrollbar(
        textbox,
        width=10
        )
verscroll.pack(
        fill='x',
        side='right'
        )
def gui_launch():
    window.geometry('600x400+50+50')
    window.mainloop()

if __name__=='__main__':gui_launch()
