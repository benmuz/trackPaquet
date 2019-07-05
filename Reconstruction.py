from tkinter import *
main = Tk()
main.geometry("737x517+350+400")
main.title('IP Tracer')

def ouvrirFic():
    print("ouvrir fichier")
def menRec():
    main.hide()
    
def menCap():
    print("Capture")
def menReg():
    print("reglege")
def quitter():
    main.destroy()
def aide():
    print("aide")
menu=Menu(main)
menuFichier=Menu(menu)
menuLoc = Menu(menu)
photo = PhotoImage(file="ic_power_settings_new_black_18dp - Copie.jpg")
menu.add_cascade(label="Fichier",menu=menuFichier)
menu.add_cascade(label="Localisation",menu=menuLoc)
menu.add_command(label="Aide",command=aide)
menuFichier.add_command(label="Ouvrir",command=ouvrirFic)
menuFichier.add_command(label="Recent",command=menRec)
menuFichier.add_command(label="Capture",command=menCap)
menuFichier.add_command(label="Reglage",command=ouvrirFic)
menuFichier.add_command(image = photo, label="Quitter",command=quitter)
menuLoc.add_command(label="Mon IP",command=quitter)
menuLoc.add_command(label="Autre IP",command=quitter)


main.config(menu=menu)

main.mainloop()
