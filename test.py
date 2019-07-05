class MainWindow(Tk):
    def __init__(self, width=100,height=100,bg="white"):
        Tk.__init__(self)
        self.title("IP Tracer")
        self.canvas =Canvas(self,width=width-20, height=height-20, bg=bg)
        self.libelle =Label(text ="Serious Game", font="Helvetica 14 bold")
        self.canvas.pack()
        self.libelle.pack()

class MainWindow(Frame):
    def __init__(self, width=200,height=200,bg="white"):
        Frame.__init__(self)
        self.master.title("Editeur Graphique")
        self.pack()
        self.libelle.pack()
        self.canvas.pack()
        
class MenuBar(Frame):
    def __init__(self,boss=None):
        Frame.__init__(self,borderwidth=2)
        mbuttonFile = Menubutton(self,text='Fichier')
        mbuttonFile.pack(side=LEFT)
        menuFile=Menu(mbuttonFile)
        menuFile.add_command(label='Effacer',command=boss.effacer)
        menuFile.add_command(label='Terminer',command=boss.quit)
        mbuttonFile.configure(menu=menuFile)

class ScrolledCanvas(Frame):
    """Zone Client"""
    def __init__(self, boss, width=100,height=100,bg="white",scrollregion =(0,0,300,300)):
        Frame.__init__(self, boss)
        self.canvas=Canvas(self, width=width-20,height=height-20,bg=bg,
        scrollregion=scrollregion)
        setlf.canvas.grid(row=0,column=0)

    scv=Scrollbar(self,orient=VERTICAL,command =self.canvas.yview)
    sch=Scrollbar(self,orient=HORIZONTAL,command=self.canvas.xview)
    self.canvas.configure(xscrollcommand=sch.set, yscrollcommand=scv.set)
    scv.grid(row=0,column=1,sticky=NS)
    sch.grid(row=1,colum=0,sticky=EW)
    self.bind("<Configure>", self.retailler)
    self.started =False

    def retailler(self,event):
        if not self.started:
            self.started=True
        return
    larg=self.winfo_width()-20,
    haut=self.winfo_height()-20
    self.canvas.config(width=larg,height=haut)







