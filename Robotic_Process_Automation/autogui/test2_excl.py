# DAVIDRVU - 2018

# https://github.com/lundbird/AutoGui
# https://docs.microsoft.com/en-us/dotnet/api/system.windows.automation.automationelement?view=netframework-4.7.2
import autogui
import os
import time

# autogui.click(“Editor,class:=EditorClass,id:=EditorID”)

def main():
    print("Opening Excel file ...")
    autogui.open("test.xlsx", setActive=True)
    #autogui.open("test.xlsx")
    #os.startfile("test.xlsx")
    time.sleep(3)
    #autogui.setWindow("Excel")
    #autogui.setWindow("test.xlsx - Excel (Error de activación de productos)")
    #autogui.setWindow("value:=Asistente para la activación de Microsoft Office")
    #autogui.setWindow("Asistente")
    #autogui.setWindow("Update Available")


    #autogui.click("AutomationId:=Close")
    autogui.click("Name:=C3")
    autogui.append("Soy el bot","Name:=C3")
    autogui.click("Name:=C4")
    autogui.append("1313","Name:=C4")
    #autogui.sendkey("{ENTER}")

    #autogui.click("Name:=Cuadrícula,Selection.Selection:=B1")
    #autogui.click("title:=Cuadrícula,text:=Cuadrícula,regexptitle:=Cuadrícula")

    #autogui.sendkey("{CTRL}")
    #autogui.click("Name:=B2")
    #autogui.sendkey("{CONTROL}")
    #autogui.click("Name:=B3")
    #autogui.sendkey("{CONTROL}")
    #autogui.click("Name:=B4")

    autogui.click("Name:=B2")
    autogui.click("Name:=Formato condicional")
    time.sleep(0.5)
    autogui.click("Name:=Escalas de color")
    time.sleep(0.5)
    autogui.click("Name:=Escala de colores verde y amarillo")
    #A1 = autogui.getProperty("Name:=A1","Value") #iaccessiblevalue
    #A2 = autogui.getProperty("Name:=A2","Value")
    #A3 = autogui.getProperty("Name:=A3","Value")
    #A4 = autogui.getProperty("Name:=A3","Value")
    #print("A1 = " + str(A1))
    #print("A2 = " + str(A2))
    #print("A3 = " + str(A3))
    #print("A4 = " + str(A4))
    print("DONE!")

if __name__ == "__main__":
    main()