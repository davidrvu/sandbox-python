# DAVIDRVU - 2018

# https://github.com/lundbird/AutoGui
# https://docs.microsoft.com/en-us/dotnet/api/system.windows.automation.automationelement?view=netframework-4.7.2
import autogui
import time

# autogui.click(“Editor,class:=EditorClass,id:=EditorID”)

def main():
    print("Opening CALCULATOR ...")
    autogui.open("calc")
    autogui.setWindow("calculadora")
    autogui.click("AutomationId:=num1Button")
    autogui.click("AutomationId:=num7Button")
    autogui.click("AutomationId:=multiplyButton")
    autogui.click("AutomationId:=num2Button")
    autogui.click("AutomationId:=equalButton")
    A = autogui.getProperty("AutomationId:=CalculatorResults","Name")
    print(A)
    print("DONE!")

if __name__ == "__main__":
    main()