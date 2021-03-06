### coddy by loadycode
### graphite00020
### gnu general public license v3.0

import tkinter as tk
from ctypes import windll

print('coddy!alert: custom tilebar lib import successful')

isMapped=0
isMaximised=False

def launch(window):
	global tilelabel
	def set_appwindow(window):
		GWL_EXSTYLE=-20
		WS_EX_APPWINDOW=0x00040000
		WS_EX_TOOLWINDOW=0x00000080
		hwnd=windll.user32.GetParent(window.winfo_id())
		stylew=windll.user32.GetWindowLongW(hwnd,GWL_EXSTYLE)
		stylew=stylew&~WS_EX_TOOLWINDOW
		stylew=stylew|WS_EX_APPWINDOW
		res=windll.user32.SetWindowLongW(hwnd,GWL_EXSTYLE,stylew)
		window.wm_withdraw()
		window.after(10,lambda:window.wm_deiconify())
	def mapped(event):
		global isMapped
		window.overrideredirect(True)
		if isMapped==1:
			set_appwindow(window)
		isMapped=0
	window.bind('<Map>',mapped)
	window.overrideredirect(True)
	screenwidth=window.winfo_screenwidth()
	screenheight=window.winfo_screenheight()
	xcoor=(screenwidth/2)-(600/2)
	ycoor=(screenheight/2)-(400/2)
	window.minsize(
		width=600,
		height=450
		)
	def close(event):
		window.destroy()
	def minimise(event):
		global isMapped
		window.state('withdrawn')
		window.overrideredirect(False)
		window.state('iconic')
		isMapped=1
	def maximise(event):
		global isMaximised
		if isMaximised==False:
			window.geometry('{}x{}+{}+{}'.format(
				window.winfo_screenwidth(),
				window.winfo_screenheight(),
				0,
				0
				)
			)
			isMaximised=True
		else:
			window.geometry('{}x{}+{}+{}'.format(
				700,
				400,
				50,
				50
				)
			)
			isMaximised=False	
	def clickpos(event):
		global clickx, clicky
		clickx=event.x
		clicky=event.y
	def moving(event):
		x,y=event.x-clickx+window.winfo_x(),event.y-clicky+window.winfo_y()
		window.geometry('+%s+%s'%(x,y))
	tile=tk.Frame(
		window,
		height=40,
		bg='#222222'
		)
	tile.bind('<B1-Motion>',moving)
	tile.bind('<Button-1>',clickpos)
	tile.pack(
		side='top',
		fill='x'
		)
	tilelabel=tk.Label(
		tile,
		text='coddy',
		justify='center',
		bg='#222222',
		fg='white',
		font='Consolas 10'
		)
	tilelabel.bind('<B1-Motion>',moving)
	tilelabel.bind('<Button-1>',clickpos)
	tilelabel.pack(
		side='left'
		)
	tileclose=tk.Frame(
		tile,
		height=25,
		width=25,
		bg='red'
		)
	tileclose.bind('<Button-1>',close)
	tileclose.pack(
		side='right'
		)
	tilemax=tk.Frame(
		tile,
		height=25,
		width=25,
		bg='green'
		)
	tilemax.bind('<Button-1>',maximise)
	tilemax.pack(
		side='right'
		)
	tilemin=tk.Frame(
		tile,
		height=25,
		width=25,
		bg='blue'
		)
	tilemin.bind('<Button-1>',minimise)
	tilemin.pack(side='right')
	minimise(1)
	set_appwindow(window)
def rename(label):
	global tilelabel
	tilelabel['text']=label