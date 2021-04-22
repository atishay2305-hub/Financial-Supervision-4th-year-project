from tkinter import *
import webbrowser
root = Tk()
def send():
    send ="You =>" +e.get()
    txt.insert(END,"\n" + send)
    if (e.get()=="hello" or "hey" or "hi"):
        txt.insert(END,'\n' + "SAM => Hi")

    elif (e.get()=="how are you?"):
        txt.insert(END,'\n' + "SAM => I am fine and you?")
    elif (e.get()=="fine"):
        txt.insert(END,'\n' + "SAM => nice, How can I assist you?")
    elif (e.get()=="Do tell me about your work "):
        txt.insert(END,'\n' + "SAM => Get all information at: https://www.nseindia.com/")
    elif (e.get()=="Tell me about how to buy your stocks"):
        txt.insert(END,'\n' + "SAM => Please go through the following blog:",  webbrowser.open("https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI"))
    elif (e.get()=="Exit"):
        txt.insert(END,'\n' + "SAM => Thank you for joining us, Good Bye")
    else:
          txt.insert(END,'\n' + "SAM => Sorry, I didn't get you")
    e.delete(0,END)
txt = Text(root)
txt.grid(row = 0, column=0,columnspan=2)
e = Entry(root,width=100)
send=Button(root,text="Send",command = send).grid(row=1,column=1)
e.grid(row =1, column=0)
root.title("CHATBOT")
root.mainloop()

