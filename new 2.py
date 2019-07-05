import time
from tkinter import *
from tkinter.filedialog import askopenfilename


def fin():
    mainloop()


class Root(object):
    main = Tk()
    pan = PanedWindow(main, orient=HORIZONTAL)

    def __init__(self):
        self.main.geometry("1500x800+0+0")
        self.main.title('IP Tracer')

        "============================creation de menu =================================================================="

        self.fen1 = Startpage()

        self.fen2 = VueReconstruction()

        self.menu = Menu(self.main)
        self.menuFichier = Menu(self.menu)
        self.menuLoc = Menu(self.menu)
        self.photo = PhotoImage(
            file="C:/Users/Ben MUZINGU/PycharmProjects/TFE/icon/ic_power_settings_new_black_18dp - Copie.jpg")
        self.menu.add_cascade(label="Fichier", menu=self.menuFichier)
        self.menu.add_cascade(label="Localisation", menu=self.menuLoc)
        self.menu.add_command(label="Aide", command=self.aide)
        self.menuFichier.add_command(label="Ouvrir", command=self.ouvrirFic)
        self.menuFichier.add_command(label="Recent", command=self.menRec)
        self.menuFichier.add_command(label="Capture", command=self.menCap)
        self.menuFichier.add_command(label="Reglage", command=self.ouvrirFic)
        self.menuFichier.add_command(image=self.photo, label="Quitter", command=self.quitter)
        self.menuLoc.add_command(label="Mon IP", command=self.chang1)
        self.menuLoc.add_command(label="Autre IP", command=self.chang2)
        self.main.config(menu=self.menu)
        self.pan.pack(expand=Y, fill=BOTH)
        self.pan.add(self.fen1)
        # self.pan.add(self.fen2)
        self.pan.pack()

        "=======================================================different frame====================================================================="

    def ouvrirFic(self):
        fic=askopenfilename(title="Ouvrir une fichier", filetypes=[('pcap', 'cap')])
        print(fic)

    def menRec(self):
        print("rec")


    def menCap(self):
        self.pan.remove(self.fen2)
        self.pan.add(self.fen1)
        self.fen1.capture()

    def menReg(self):
        print("reglege")


    def quitter(self):
        self.main.destroy()

    def aide(self):
        print("aide")

    def chang2(self):
        self.pan.remove(self.fen1)
        self.pan.add(self.fen2)

    def chang1(self):
        self.pan.remove(self.fen2)
        self.pan.add(self.fen1)





class VueReconstruction(Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        Frame.__init__(self, bg="powder blue")
        self.bg=PhotoImage(file="C:/Users/Ben MUZINGU/PycharmProjects/TFE/icon/bg.png")
        self.can = Frame(self, width=1500, height=130, bg="blue")
        Label(self, image=self.bg).place(x=30, y=100)
        lblInfo = Label(self.can, font=('arial', 50, 'bold'), text="IP Traceback and tracking", fg="Steel Blue", bd=10,
                        anchor='w')
        lblInfo.grid(row=0, column=0)
        self.can.pack(side=TOP, padx=5, pady=5)
        self.photo2 = PhotoImage(
            file="C:/Users/Ben MUZINGU/PycharmProjects/TFE/icon/fingbox_connect_to_router.jpg")
        self.photo = PhotoImage(
            file="C:/Users/Ben MUZINGU/PycharmProjects/TFE/icon/ic_wifi.png")

        self.chemin(6)

    def chemin(self, nb):
        pos = 1500 // (nb + 1)
        i=pos
        if 1500 % (nb + 1) == 0:
            while pos < 1500:
                Button(self, image=self.photo, relief=RAISED).place(x=pos, y=350)
                Label(self, text="192.168.200.6").place(x=pos - 25, y=380)
                pos = pos+i
                print(pos)
        else:
            pos = pos-100
            while pos < 1500:
                Button(self, image=self.photo, relief=RAISED).place(x=pos, y=350)
                Label(self, text="192.168.200.6").place(x=pos - 25, y=380)
                pos=pos+i
                #print(pos)


class Startpage(Frame):
    text_Input = StringVar()
    valeur=IntVar()

    def __init__(self, **kw):
        super().__init__(**kw)
        Frame.__init__(self, bg="powder blue")
        self.Tops = Frame(self, width=1600, bg="powder blue", relief=SUNKEN)
        self.Tops.pack(side=TOP)
        f1 = Frame(self, width=300, height=600, bg="powder blue", relief=SUNKEN, padx=10, pady=10)
        f1.pack(side=LEFT)
        f2 = Frame(self, width=900, bg="powder blue", relief=SUNKEN, padx=15, pady=10)
        f2.place(x=400, y=230)
        "=====================================recuperation du temps local =========================================================="
        localtime = time.asctime(time.localtime(time.time()))
        "==================================================Info======================================================================"

        lblInfo = Label(self.Tops, font=('arial', 50, 'bold'), text="IP Traceback and tracking", fg="Steel Blue", bd=10,
                        anchor='w')
        lblInfo.grid(row=0, column=0)
        lblInfo1 = Label(self.Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
        lblInfo1.grid(row=1, column=0)
        "==================================================frame 1==================================================================="
        labelPac = Label(f1, font=('arial', 14, 'bold'), text="Paquet", fg='white', bg='blue', width=30)
        labelPac.grid(columnspan=2)
        Button(f1, font=('arial', 14, 'bold'), text="Nouveau", command=self.capture, width=29).grid(row=1,
                                                                                                    columnspan=2)
        self.fgl = LabelFrame(f1, text="Information collecter", width=361, height=300).grid(row=2, columnspan=2)
        Label(f1, font=('arial', 12), text="Analyse en cours...", bg="powder blue").grid(row=3, column=0)
        Button(f1, font=('arial', 12,), text="Reconstruire", padx=55, pady=-10, command=Root.chang2
               ).grid(row=3, column=1)

        "==============================================frame 2 ======================================================================"
        Label(f2, font=('arial', 14, 'bold'), text="Information des paquets", fg='white', bg='blue', width=70).grid(
            columnspan=5)
        "====================================table en tete "
        Label(f2, font=('arial', 12, 'bold'), text="N°", bg="powder blue", width=5, relief=GROOVE).grid(row=1, column=0)
        Label(f2, font=('arial', 12, 'bold'), text="IP Source", bg="powder blue", width=15, relief=GROOVE).grid(row=1,
                                                                                                                column=1)
        Label(f2, font=('arial', 12, 'bold'), text="IP Destination", bg="powder blue", width=15, relief=GROOVE).grid(
            row=1, column=2)
        Label(f2, font=('arial', 12, 'bold'), text="Protocole", bg="powder blue", width=8, padx=2, relief=GROOVE).grid(
            row=1, column=3)
        Label(f2, font=('arial', 12, 'bold'), text="Données", bg="powder blue", width=38, padx=2, relief=GROOVE).grid(
            row=1, column=4)
        ma_liste = [(1, '192.168.43.1  ', '172.16.0.145', 'UDP ', 'Application data'),
                    (2, '192.168.43.145', '172.16.0.145', 'TCP ', 'Application data'),
                    (10, '192.168.4.145', '172.16.0.145', 'TCP ', 'Application data'),
                    (3, '192.168.43.145', '172.16.0.145', 'TCP ', 'Application data'),
                    (4, '192.168.43.145', '172.16.0.145', 'ICMP', 'Application data'),
                    (5, '192.168.4.145 ', '172.16.0.145', 'TCP ', 'Application data'),
                    (6, '192.168.43.5  ', '172.16.0.145', 'TCP ', 'Application data'),
                    (7, '192.168.43.145', '172.16.0.145', 'ICMP', 'Application data'),
                    (8, '192.168.3.145 ', '172.16.0.145', 'TCP ', 'Application data'),
                    (9, '192.168.43.5  ', '172.16.0.145', 'UDP ', 'Application data')
                    ]
        for ligne in range(10):
            for colonne in range(5):
                Label(f2, text=ma_liste[ligne][colonne], bg="powder blue").grid(row=ligne + 3, column=colonne)

        "=====================================================calcul================================================================="

    def capture(self):
        fen = Toplevel(master=self)
        fen.geometry("300x300+100+100")
        fen.title("Capture de trafic")
        Label(fen, font=('arial', 12, "bold"), text="Protocoles", width=200, bg='blue', fg='white').pack()
        listbox = Listbox(fen, width=200)
        listbox.pack(side=TOP)
        #listbox.insert(END, "protocoles")
        for item in ["Ethernet type 0x0806 (ARP)", "Ethernet broadcast", "No ARP", "IPv4 only", "TCP only","UDP only", "ICMP only", "Non-DNS", "HTTP"]:
            listbox.insert(END, item)
        #Entry(fen, font=('arial', 12), textvariable=self.text_Input, width=20, justify='right', bd=2).pack(side=RIGHT)#place(x=100, y=260)
        #Label(fen, font=('arial', 12), text="protocole", width=7).pack(side=LEFT)#place(x=15, y=260)
        Scale(fen,  variable=self.valeur, orient=HORIZONTAL).pack(side=RIGHT)#place( x=100, y=220)

        Label(fen, font=('arial', 12), text="Paquets").pack(side=LEFT)#place(x=15, y=225)
        #Button(fen, text="Annuler", width=15, command=fen.destroy).pack(side=LEFT)
        Button(fen, text="Lancer la capturer", bg='green2', width=200, command=fen.destroy).pack(side=BOTTOM)
        fen.mainloop()


def runCapture(self):
    a=self.valeur.get()

if __name__ == '__main__':
    if __name__ == '__main__':
        app = Root()
        fin()
