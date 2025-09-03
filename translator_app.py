from  tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
LANGUAGES = [
    "english", "hindi", "french", "german", "spanish", "italian",
    "chinese", "japanese", "korean", "russian", "arabic"
]

def change(text="type", src="english", dest="hindi"):
    translated = GoogleTranslator(source=src, target=dest).translate(text)
    return translated

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk()
root.title("translator")
root.config(bg='grey')
root.geometry("500x700")

lab_txt=Label(root,text="Translator",font=("Time new roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="source Text",font=("Time new roman",20,"bold"),fg="black",bg="grey")
lab_txt.place(x=100,y=100,height=20,width=300)

sor_txt = Text(frame,font=("Time new roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=100,width=480)

list_text = LANGUAGES

comb_sor =ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")

button_change = Button(frame,text ="Translate",relief=RAISED,command = data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest =ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root,text="Dest Text",font=("Time new roman",20,"bold"),fg="black",bg="grey")
lab_txt.place(x=100,y=360,height=20,width=300)


dest_txt = Text(frame,font=("Time new roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=100,width=480)


root.mainloop()
