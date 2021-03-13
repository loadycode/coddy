### coddy by loadycode
### graphite00070
### gnu general public license v3.0

print ('coddy!alert: module system lib import successful')

## imports

import sys
import os

modules_dir = 'modules/'

sys.path.append (modules_dir)

modules = os.listdir (modules_dir)
modules_num = len (modules)

print ('coddy!modsys: checking modules directory...')
if modules_num == 0:
	print ('coddy!modsys: not modules installed')
else:
	print ('coddy!modsys: found these modules:')
	print (modules)
	print ('coddy!modsys: number of installed modules: ' + str (modules_num))