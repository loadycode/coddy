#!/usr/bin/python3
### coddy by loadycode
### build310121 01-02-2021 15:44
### gnu general public license v3.0

ftypesImportError=False
pluginsysImportError=False

# cloth dwarf relief east version guide connect device fatigue reward frequent real

import tkinter as tk
import tkinter.filedialog as fd
try:import coddy_ftypes as ftypes
except ImportError:ftypesImportError=True

## filesystem operations

file_path=None
file_edit=False

def file_open(event):
	global file_path, file_edit, ftypesImportError
	if ftypesImportError==False:	
		file_path=fd.Open(window,filetypes=ftypes.array).show()
	else:
		file_path=fd.Open(window,filetypes=[('all filetypes','*')]).show()
	if file_path=='':return
	textbox.delete('1.0','end')
	textbox.insert('1.0',open(file_path).read())
	file_edit=False

def file_save(event):
	global file_path, file_edit, ftypesImportError
	if file_path!=None:
		open(file_path,'wt').write(textbox.get('1.0','end'))
	elif file_path=='coddy/config':
		open('coddy/config','wt').write(textbox.get('1.0','end'))
	else:
		if ftypesImportError==False:
			file_path=fd.SaveAs(window,filetypes=ftypes.array).show()
		else:
			file_path=fd.SaveAs(window,filetypes=[('all filetypes','*')]).show()
		if file_path=='':return
		open(file_path,'wt').write(textbox.get('1.0','end'))
	file_edit=False

def file_saveas(event):
	global file_path, file_edit, ftypesImportError
	if ftypesImportError==False:	
		file_path=fd.SaveAs(window,filetypes=ftypes.array).show()
	else:
		file_path=fd.SaveAs(window,filetypes=[('all filetypes','*')]).show()
	if file_path=='':return
	open(file_path,'wt').write(textbox.get('1.0','end'))
	file_edit=False

## user interface

window=tk.Tk()
window.title("coddy")
window.minsize(700,400)

# bindings -->
window.bind('<Control-o>',file_open)
window.bind('<Control-s>',file_save)
window.bind('<Control-x>',file_saveas)
# <-- bindings

textbox=tk.Text(
        window,
        relief='flat',
		wrap='none',
        undo=True,
        bg='#222222',
        fg='silver',
		font='Consolas 9',
        insertbackground='orange'
        )
textbox.pack(
		side='left',
        fill='both',
        expand=True
        )
verscroll=tk.Scrollbar(
        window,
		relief='flat',
        width=15,
		command=textbox.yview
        )
textbox['yscrollcommand']=verscroll.set
verscroll.pack(
        fill='y',
        side='right'
        )
def gui_launch():
	window.geometry('700x400+50+50')
	textbox.insert('1.0',open('coddy/startpage').read())
	window.mainloop()

if __name__=='__main__':gui_launch()
