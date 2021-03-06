#!/usr/bin/python3
### coddy by loadycode
### graphite00020
### gnu general public license v3.0

ftypesImportError=False
pluginsysImportError=False
windllImportError=False
tilebarImportError=False
syntaxImportError=False

## imports
import os
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import ttk
try:
	import coddy_ftypes as ftypes
except ImportError:
	ftypesImportError=True
	print('coddy!error: filetypes array import error')
try:
	from ctypes import windll
except ImportError:
	windllImportError=True
	print('coddy!alert: cant import windll; please install windows')
try:
	import coddy_syntax as syntax
except ImportError:
	syntaxImportError=True
	print('coddy!error: syntax highlighting lib import error')
if windllImportError==False:
	try:
		import coddy_tilebar as tilebar
	except ImportError:
		tilebarImportError=True
		print('coddy!error: custom tilebar lib import error')
else:pass
## filesystem operations

file_extension=None
file_syntax='text'
file_path=None
file_edit=False
file_startpage=True

def file_edit_event(event):
	if file_syntax=='python':
		syntax.python_check(textbox)
	elif file_syntax=='c':
		syntax.c_check(textbox)
	elif file_syntax=='cpp':
		syntax.cpp_check(textbox)
	elif file_syntax=='javascript':
		syntax.js_check(textbox)
	elif file_syntax=='html':
		syntax.html_check(textbox)
	elif file_syntax=='css':
		syntax.css_check(textbox)
	file_edit=True
	try:
			if file_path!=None:
				if tilebarImportError==True:
					window.title(os.path.basename(file_path)+' - coddy')
				else:
					tilebar.rename(os.path.basename(file_path)+' - coddy')
			else:
				if tilebarImportError==True:
					window.title('untitled - coddy')
				else:
					tilebar.rename('untitled - coddy')
	except TypeError:
		window.title('error - coddy')
		print('coddy!error: unknown title error')

def file_new(event):
	global edited, file_path
	def file_new_save(event):
		global file_path, file_edit
		file_edit=False
		if file_path!=None:
			open(file_path,'wt').write(textbox.get('1.0','end'))
		elif file_path=='coddy/config':
			open('coddy/config','wt').write(textbox.get('1.0','end'))
		else:
			file_path=fd.SaveAs(window,filetypes=ftypes.array).show()
			if file_path=='':return
			open(file_path,'wt').write(textbox.get('1.0','end'))
		config_check()
		textbox.delete('1.0','end')
		if tilebarImportError==True:
			window.title('untitled - coddy')
		else:
			tilebar.rename('untitled - coddy')
		dialog.destroy()
		file_path=None
	def file_new_close(event):
		global file_edit
		file_edit=False
		textbox.delete('1.0','end')
		if tilebarImportError==True:
			window.title('untitled - coddy')
		else:
			tilebar.rename('untitled - coddy')
		dialog.destroy()
		file_path=None
	if file_edit==True:
		dialog=tk.Frame(
			window,
			bg='white',
			height=20
			)
		dialog.pack(
			side='bottom',
			fill='x'
			)
		if file_path!=None:
			dialoglabel=tk.Label(
				dialog,
				bg='white',
				text=file_path+' had unsaved changes'
				).pack(side='left')
		else:
			dialoglabel=tk.Label(
				dialog,
				bg='white',
				text='untitled file had unsaved changes'
				).pack(side='left')
		savebtn=tk.Label(
			dialog,
			text='save',
			bg='white'
			)
		dontsavebtn=tk.Label(
			dialog,
			text='dont save',
			bg='white'
			)
		savebtn.bind('<Button-1>',file_new_save)
		dontsavebtn.bind('<Button-1>',file_new_close)
		savebtn.pack(
			side='right',
			padx=10
			)
		dontsavebtn.pack(
			side='right',
			padx=10
			)
	else:
		textbox['state']='normal'
		textbox.delete('1.0','end')
		if tilebarImportError==True:
			window.title('untitled - coddy')
		else:
			tilebar.rename('untitled - coddy')
		file_path=None
	file_startpage=False
	verscroll.pack(
    	fill='y',
    	side='right'
    )
def file_open(event):
	global file_path, file_edit, ftypesImportError, file_extension, file_syntax
	if ftypesImportError==False:	
		file_path=fd.Open(window,filetypes=ftypes.array).show()
	else:
		file_path=fd.Open(window,filetypes=[('all filetypes','*')]).show()
	if file_path=='':return
	textbox['state']='normal'
	textbox.delete('1.0','end')
	textbox.insert('1.0',open(file_path).read())
	file_edit=False
	file_basename=os.path.basename(file_path)
	file_extension=os.path.splitext(file_basename)[1]
	if file_extension=='.py':
		file_syntax='python'
		syntax.python_check(textbox)
		syntaxbtn['text']='python'
	elif file_extension=='.js':
		file_syntax='javascript'
		syntax.js_check(textbox)
		syntaxbtn['text']='javascript'
	elif file_extension=='.c':
		file_syntax='c'
		syntax.c_check(textbox)
		syntaxbtn['text']='c lang'
	elif file_extension=='.cpp':
		file_syntax='cpp'
		syntax.cpp_check(textbox)
		syntaxbtn['text']='c++ lang'
	elif file_extension=='.html':
		file_syntax='html'
		syntax.html_check(textbox)
		syntaxbtn['text']='html'
	elif file_extension=='.css':
		file_syntax='css'
		syntax.css_check(textbox)
		syntaxbtn['text']='css'
	file_startpage=False
	verscroll.pack(
    	fill='y',
    	side='right'
    )
	try:
		if tilebarImportError==True:
			window.title(os.path.basename(file_path)+' - coddy')
		else:
			tilebar.rename(os.path.basename(file_path)+' - coddy')
	except TypeError:
		if tilebarImportError==True:
			window.title('error - coddy')
		else:
			tilebar.rename('error - coddy')
		print('coddy!error: unknown title error')

def file_save(event):
	global file_path, file_edit, ftypesImportError
	if file_path!=None:
		try:
			open(file_path,'wt').write(textbox.get('1.0','end'))
		except FileNotFoundError:
			file_path=None
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
	if file_syntax=='python':
		syntax.python_check(textbox)
	file_startpage=False
	verscroll.pack(
    	fill='y',
    	side='right'
    )
	try:
		if tilebarImportError==True:
			window.title(os.path.basename(file_path)+' - coddy')
		else:
			tilebar.rename(os.path.basename(file_path)+' - coddy')
	except TypeError:
		if tilebarImportError==True:
			window.title('error - coddy')
		else:
			tilebar.rename('error - coddy')
		print('coddy!error: unknown title error')

def file_saveas(event):
	global file_path, file_edit, ftypesImportError
	if ftypesImportError==False:	
		file_path=fd.SaveAs(window,filetypes=ftypes.array).show()
	else:
		file_path=fd.SaveAs(window,filetypes=[('all filetypes','*')]).show()
	if file_path=='':return
	open(file_path,'wt').write(textbox.get('1.0','end'))
	file_edit=False
	if file_syntax=='python':
		syntax.python_check(textbox)
	file_startpage=False
	verscroll.pack(
    	fill='y',
    	side='right'
    )
	try:
		if tilebarImportError==True:
			window.title(os.path.basename(file_path)+' - coddy')
		else:
			tilebar.rename(os.path.basename(file_path)+' - coddy')
	except TypeError:
		if tilebarImportError==True:
			window.title('error - coddy')
		else:
			tilebar.rename('error - coddy')
		print('coddy!error: unknown title error')

## config edit

def config_open(event):
	file_startpage=False
	verscroll.pack(
    	fill='y',
    	side='right'
    )
	file_path='coddy/config'
	textbox['state']='normal'
	textbox.delete('1.0','end')
	try:
		textbox.insert('1.0',open('coddy/config').read())
	except FileNotFoundError:
		file_path=None
		textbox.delete('1.0','end')
		print('coddy!error: config not found')

def config_check():
	return

def syntax_switch(event):
	global file_syntax
	if file_syntax=='python':
		file_syntax='text'
		syntaxbtn['text']='plain text'
		syntax.delete_tokens(textbox)
	elif file_syntax=='text':
		if file_extension=='.py':
			file_syntax='python'
			syntaxbtn['text']='python'
			syntax.python_check(textbox)

## user interface

window=tk.Tk()
window.title('coddy')
window.minsize(700,400)

# bindings -->
window.bind('<Control-n>',file_new)
window.bind('<Control-o>',file_open)
window.bind('<Control-s>',file_save)
window.bind('<Control-Shift-s>',file_saveas)
window.bind('<Control-p>',config_open)
# <-- bindings

if tilebarImportError==False:
	tilebar.launch(window)

textbox=tk.Text( # textbox
    window,
    relief='flat',
	wrap='none',
    undo=True,
    bg='#222222',
    fg='silver',
	font='Consolas 10',
    insertbackground='orange'
    )
syntax.tokens_init(textbox)
panel=tk.Frame( # bottom panel
	window,
	bg='#222222',
	relief='flat',
	height=20
	)
newbtn=tk.Label( # new file button
	panel,
	bg='#222222',
	fg='white',
	text='new'
	)
openbtn=tk.Label( # open button
	panel,
	bg='#222222',
	fg='white',
	text='open'
	)
savebtn=tk.Label( # save file button
	panel,
	bg='#222222',
	fg='white',
	text='save'
	)
saveasbtn=tk.Label( # save file as button
	panel,
	bg='#222222',
	fg='white',
	text='save as'
	)
confbtn=tk.Label( # config button
	panel,
	bg='#222222',
	fg='white',
	text='config'
	)
syntaxbtn=tk.Label( # syntax button
	panel,
	bg='#222222',
	fg='white',
	text=''
	)
newbtn.bind('<Button-1>',file_new)
newbtn.pack(side='left')
openbtn.bind('<Button-1>',file_open)
openbtn.pack(side='left')
savebtn.bind('<Button-1>',file_save)
savebtn.pack(side='left')
saveasbtn.bind('<Button-1>',file_saveas)
saveasbtn.pack(side='left')
confbtn.bind('<Button-1>',config_open)
confbtn.pack(side='left')
syntaxbtn.bind('<Button-1>',syntax_switch)
syntaxbtn.pack(side='right')
panel.pack(
	side='bottom',
	fill='x'
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
def gui_launch():
	window.geometry('700x400+50+50')
	textbox.insert('1.0',open('coddy/startpage').read())
	textbox['state']='disabled'
	window.bind('<<Modified>>',file_edit_event)
	window.mainloop()

if __name__=='__main__':gui_launch()