# DAVIDRVU - 2018

#  "win32" backend and call .click(where="check")

# pywinauto requires 2-level hierarchy from Application object to control method. The structure of any call is   app.<DialogName>.<ControlName>.<Method>(<params>)
# EJ: app.Window_(best_match='Dialog', top_level_only=True).ChildWindow(best_match='About').Click()

import pywinauto
import time

app = pywinauto.Application(backend="win32").start('calc.exe')
#dlg = app.window(title_re="Calculator")

time.sleep(3)

app.Window_(best_match='Calculator', top_level_only=True).ChildWindow(best_match='num1Button').Click()



#print(">>> dlg.print_control_identifiers()")
#dlg.print_control_identifiers()

#print("dlg.close()")
#app.close()



#dlg.type_keys('2*3=')
#print(">>> dlg.print_control_identifiers()")
#dlg.print_control_identifiers()
#
#print(">>> dlg.minimize()")
#dlg.minimize()
#print(">>> pywinauto.Desktop(backend='uia').window(title='Calculator', visible_only=False).restore()")
#pywinauto.Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()