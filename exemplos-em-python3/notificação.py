from tkinter import *
master = Tk()
#tirar botões da janela
master.overrideredirect(True)

#aparecer no centro, mas sem definir geometry
#master.eval('tk::PlaceWindow %s center' % master.winfo_pathname(master.winfo_id()))

def xx():
    master.destroy()

notf_text = Label(master, text="Teste de notificação")
notf_text.place(x=20, y=25)

remov_notf = Button(master, text="x", command=xx, bg="#da4453", bd=0)
remov_notf.place(x=467, y=0)

master.geometry("500x70-50-50")
master.mainloop()
