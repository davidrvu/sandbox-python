"""
Example script for Calculator on Windows 10
Requirements:
  - Windows 10
  - pywinauto 0.6.1+
Win10 version of Calculator is very specific. Few different processes (!)
own different windows and controls, so the full hierarchy can be accessed
through Desktop object only.
Minimized Calculator is a process in a "Suspended" state.
But it can be restored with some trick for invisible main window.
"""

import pywinauto

app = pywinauto.Application(backend="uia").start('calc.exe')

dlg = pywinauto.Desktop(backend="uia").Calculator
dlg.type_keys('2*3=')
print(">>> dlg.print_control_identifiers()")
dlg.print_control_identifiers()

print(">>> dlg.minimize()")
dlg.minimize()
print(">>> pywinauto.Desktop(backend='uia').window(title='Calculator', visible_only=False).restore()")
pywinauto.Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()