import pyautogui
import webbrowser as wb
import time
from functools import partial
import tkinter as tk

root = tk.Tk()
root.title("Automate whatsApp Message")
root.geometry('320x150')
def call_result(label_result,n1,label_result1, n2, label_result2, n3):
    if(number1.get().isdigit()):
        wb.open("https://web.whatsapp.com/send?phone=+91"+number1.get())
        time.sleep(30)
        for i in range(number3.get()):
            pyautogui.typewrite(number2.get())
            pyautogui.press("enter")
            time.sleep(2)
        time.sleep(5)
    else:
        label_result.config(font=('arial',12,'bold'),text="must give numbers")
        labelResult.grid(row=4, column=2)
number1 = tk.StringVar()   
number2 = tk.StringVar()
number3 = tk.IntVar()

labelNum1 = tk.Label(root, font=('arial',12,'bold'),text="MobileNumber").grid(row=1, column=0)  
labelResult = tk.Label(root)  
labelResult.grid(row=1, column=3)

labelNum2 = tk.Label(root, font=('arial',12,'bold'),text="Message").grid(row=2, column=0)  
labelResult1 = tk.Label(root)  
labelResult1.grid(row=2, column=3)

labelNum3 = tk.Label(root, font=('arial',12,'bold'),text="Number of time").grid(row=3, column=0)  
labelResult2 = tk.Label(root)  
labelResult2.grid(row=3, column=3)

entryNum1 = tk.Entry(root, font=('arial',14,'bold'), textvariable=number1,width=15,bg="#eee",bd=5).grid(row=1, column=2)  
call_result = partial(call_result, labelResult, number1)

entryNum2 = tk.Entry(root, font=('arial',14,'bold'), textvariable=number2,width=15,bg="#eee",bd=5).grid(row=2, column=2)  
call_result = partial(call_result, labelResult1, number2)

entryNum3 = tk.Entry(root, font=('arial',14,'bold'), textvariable=number3,width=15,bg="#eee",bd=5).grid(row=3, column=2)  
call_result = partial(call_result, labelResult2, number3)


buttonCal = tk.Button(root, text="Result", width=10,command=call_result).grid(row=4, column=0)




