from tkinter import *
#import tkinter
def click():
    entered_text=output.get()
    def_value.delete(0.0,END)
    try:
        from_directory=my_directory[entered_text]
    except:
        from_directory="sorry no word definition present"
    def_value.insert(END,from_directory)


window=Tk()
window.title("Online Flash Cards")
photo=PhotoImage(file="images.gif")
window.configure(background="black")

Label(window, image=photo,bg="black",width=1200).grid(row=0,column=0,sticky=W)
Label(window, text="Enter the word you want to search :",bg="black",fg="yellow",font="none 12 bold").grid(row=3,column=0,sticky=W)
output=Entry(window, width=20,bg="white")
output.grid(row=4,column=0,sticky=W)

Button(window, text="SEARCH",width=6,command=click, bg="green",font="none 9 bold").grid(row=5,column=0,sticky=W)

Label(window, text="\nDefinition",bg="black",fg="orange",font="none 12 bold").grid(row=6,column=0,sticky=W)
def_value=Text(window, width=75,height=6,wrap=WORD,bg="grey")
def_value.grid(row=7,column=0,columnspan=2,sticky=W)

my_directory={'java':'james gosling','python':'data analysis','sagar':'citi employee'}
Label(window, text="Click here to close",bg="black",fg="blue",font="none 12 bold").grid(row=8,column=0,sticky=W)
# logoff function
def logoff():
    window.destroy()
    exit()

Button(window, text="LOGOFF",width=14,command=logoff).grid(row=9,column=0,sticky=W)


#Run the main loop to display the window
window.mainloop()