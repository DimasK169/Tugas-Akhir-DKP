from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from GUImaker import GUI

#Modul yang digunakan :
#Modul 1 Variabel & Array
#Modul 2 Pengkondisian
#Modul 3 Perulangan
#Modul 4 Function & Method
#Modul 5 Class & Constructor
#Modul 8 GUI

#Array
Bilgewater = {
    "Region"       : "Bilgewater",
    "Champion"     : ["Fizz","Miss Fortune", "Tahm Kench","Twisted Fate","Gangplank", "Nautilus"],
    "Mana"         : ["1 ","3 ","4 ", "4 ", "5 ", "7 "]}
PiltoverZaun = {
    "Region"       : "Piltover & Zaun",
    "Champion"     : ["Teemo ", "Ezreal ", "Jinx ", "Viktor ", "Heimerdinger ", "Vi "],
    "Mana"         : ["1","3","4","4","5","5"]}
Lengkap = {
    "Region"        : "Lengkap",
    "Champion"      : ["Fizz", "Teemo", "Ezreal", "Miss Fortune", "Jinx", "Tahm Kench", "Twisted Fate", "Viktor", "Gangplank", "Heimedinger", "Vi", "Nautilus"],
    "Mana"          : ["1","1","3","3","4","4","4","4","5","5","5","7"]}

    
#GUI
window = Tk()
window.geometry("300x300")
window.title('Runeterra Piltover & Zaun/Bilgewater Card List')
window.iconbitmap('d:/Runeterra Icon.ico')
quit_button = Button(window, text= "TUTUP", command= window.destroy)
quit_button.pack()
quit_button.place(x=125 , y=250)
Datang1 = str
Datang2 = str
Region1 = str
Region2 = str
Datang1 = GUI(Datang1, window, "Selamat Datang di Wiki Runeterra", 60 , 50)
Datang1.NewLabel(Datang1, window, "Selamat Datang di Wiki Runeterra", 60, 50)
Datang2 = GUI(Datang2, window, "Pilih Region Untuk Melihat Kartu di Dalamnya", 30 , 70)
Datang2.NewLabel(Datang2, window, "Pilih Region Untuk Melihat Kartu di Dalamnya", 30, 70)
Region1 = GUI(Region1, window, "Region 1", 45 , 110)
Region1.NewLabel(Region1, window, "Region 1", 45, 110)
Region2 = GUI(Region2, window, "Region 2", 45 , 150)
Region2.NewLabel(Region2, window, "Region 2", 45, 150)

strregion1 = StringVar(value='Pilih Region 1') 
region1 = ttk.Combobox(window, width = 17, textvariable = strregion1, state="readonly")
region1.place(x=115, y=110)

region1['values'] = ('Bilgewater',
                 'Piltover & Zaun',
                 'None') 

strregion2 = StringVar(value='Pilih Region 2') 
region2 = ttk.Combobox(window, width = 17, textvariable = strregion2, state="readonly")
region2.place(x=115, y=150)

region2['values'] = ('Bilgewater',
                 'Piltover & Zaun',
                 'None') 



#Pengkondisian, Function, Perulangan, dan Class
def submit():
    if strregion1.get() == 'Pilih Region 1':
        messagebox.showerror("Error","BELUM MEMILIH REGION")
        return
    elif strregion2.get() == 'Pilih Region 2':
        messagebox.showerror("Error","BELUM MEMILIH REGION")
        return
    elif strregion1.get() == 'None' and strregion2.get() == 'None':
        messagebox.showerror("Error","BELUM MEMILIH REGION")
        return
    elif strregion1.get() ==  strregion2.get() :
        messagebox.showerror("Error","Pilih Region yang beda \n *Jika ingin memilih 1 region none pada salah satu pilihan")
        return

    if strregion1.get() != 'None' and strregion2.get () != "None" :
            lengkap = Toplevel()
            lengkap.title('Daftar Kartu' + " " + strregion1.get() + " dan " + strregion2.get())
            lengkap.iconbitmap('d:/Runeterra Icon.ico')
            lengkap.geometry("300x350")
            label1= Label(lengkap, text="Daftar Kartu\n" + strregion1.get() + " dan " + strregion2.get())
            label1.pack()
            label1.place(x= 65, y=40)
            lbchamp = str
            lbchamp = GUI (lbchamp, lengkap, "Champion", 143, 80)
            lbchamp.NewLabel(lbchamp, lengkap, "Champion", 143, 80)
            lbmana = str
            lbmana = GUI (lbmana, lengkap, "Mana", 85, 80)
            lbmana.NewLabel(lbmana, lengkap, "Mana", 85, 80)
            quit_button = Button(lengkap, text= "TUTUP", command= lengkap.destroy)
            quit_button.pack()
            quit_button.place(x=120 , y=300)
            LengkapChampArr = []
            LengkapManaArr = []
            for i in range(0, len(Lengkap["Champion"])):
                LengkapChampArr.append((Lengkap["Champion"][i]))
            lbchamplengkap = Label(lengkap, text = "\n".join(LengkapChampArr))
            lbchamplengkap.pack()
            lbchamplengkap.place(x=137, y=100)
            for i in range(0, len(Lengkap["Mana"])):
                LengkapManaArr.append((Lengkap["Mana"][i]))
            lbmanalengkap = Label (lengkap, text = "\n".join(LengkapManaArr))
            lbmanalengkap.pack()
            lbmanalengkap.place(x=98, y= 100)
    elif strregion1.get() == 'None':
            Terbatas2 = Toplevel()
            Terbatas2.title('Kartu' + " " + strregion2.get())
            Terbatas2.iconbitmap('d:/Runeterra Icon.ico')
            Terbatas2.geometry("300x300")
            label1= Label(Terbatas2, text="Daftar Kartu Champion " + "\n""--" +strregion2.get() + "--")
            label1.pack()
            label1.place(x= 80, y=40)
            lbchamp = str
            lbchamp = GUI (lbchamp, Terbatas2, "Champion", 138, 80)
            lbchamp.NewLabel(lbchamp, Terbatas2, "Champion", 138, 80)
            lbmana = str
            lbmana = GUI (lbmana, Terbatas2, "Mana", 85, 80)
            lbmana.NewLabel(lbmana, Terbatas2, "Mana", 85, 80)
            quit_button = Button(Terbatas2, text= "TUTUP", command= Terbatas2.destroy)
            quit_button.pack()
            quit_button.place(x=120 , y=220)
            BilgeChampArr = []
            BilgeManaArr = []
            PnZChampArr = []
            PnZManaArr = []
            if strregion2.get() == 'Bilgewater':
                for i in range(0, len(Bilgewater["Champion"])):
                    BilgeChampArr.append((Bilgewater["Champion"][i]))
                lbbilgechamp = Label(Terbatas2, text = "\n".join(BilgeChampArr))
                lbbilgechamp.pack()
                lbbilgechamp.place(x=130 , y=100)
                for i in range(0, len(Bilgewater["Mana"])):
                    BilgeManaArr.append((Bilgewater["Mana"][i]))
                lbbilgemana = Label(Terbatas2, text = "\n".join(BilgeManaArr) )
                lbbilgemana.pack()
                lbbilgemana.place(x=98 , y=100)
            if strregion2.get() == 'Piltover & Zaun' :
                for i in range (0, len(PiltoverZaun["Champion"])):
                    PnZChampArr.append((PiltoverZaun["Champion"][i]))
                lbpnzchamp = Label(Terbatas2, text = "\n".join(PnZChampArr))
                lbpnzchamp.pack()
                lbpnzchamp.place(x=130 , y=100)
                for i in range(0, len(PiltoverZaun["Mana"])):
                    PnZManaArr.append((PiltoverZaun["Mana"][i]))
                lbPnZmana = Label(Terbatas2, text = "\n".join(PnZManaArr) )
                lbPnZmana.pack()
                lbPnZmana.place(x=98 , y=100)
    elif strregion2.get() == 'None':
            Terbatas2 = Toplevel()
            Terbatas2.title('Kartu' + " " + strregion1.get())
            Terbatas2.iconbitmap('d:/Runeterra Icon.ico')
            Terbatas2.geometry("300x300")
            label1= Label(Terbatas2, text="Daftar Kartu Champion " + "\n""--" +strregion1.get() + "--")
            label1.pack()
            label1.place(x= 80, y=40)
            lbchamp = str
            lbchamp = GUI (lbchamp, Terbatas2, "Champion", 138, 80)
            lbchamp.NewLabel(lbchamp, Terbatas2, "Champion", 138, 80)
            lbmana = str
            lbmana = GUI (lbmana, Terbatas2, "Mana", 85, 80)
            lbmana.NewLabel(lbmana, Terbatas2, "Mana", 85, 80)
            quit_button = Button(Terbatas2, text= "TUTUP", command= Terbatas2.destroy)
            quit_button.pack()
            quit_button.place(x=120 , y=220)
            BilgeChampArr = []
            BilgeManaArr = []
            PnZChampArr = []
            PnZManaArr = []
            if strregion1.get() == 'Bilgewater':
                for i in range(0, len(Bilgewater["Champion"])):
                    BilgeChampArr.append((Bilgewater["Champion"][i]))
                lbbilgechamp = Label(Terbatas2, text = "\n".join(BilgeChampArr) )
                lbbilgechamp.pack()
                lbbilgechamp.place(x=130 , y=100)
                for i in range(0, len(Bilgewater["Mana"])):
                    BilgeManaArr.append((Bilgewater["Mana"][i]))
                lbbilgemana = Label(Terbatas2, text = "\n".join(BilgeManaArr) )
                lbbilgemana.pack()
                lbbilgemana.place(x=98 , y=100)
            if strregion1.get() == 'Piltover & Zaun' :
                for i in range (0, len(PiltoverZaun["Champion"])):
                    PnZChampArr.append((PiltoverZaun["Champion"][i]))
                lbpnzchamp = Label(Terbatas2, text = "\n".join(PnZChampArr))
                lbpnzchamp.pack()
                lbpnzchamp.place(x=130 , y=100)
                for i in range(0, len(PiltoverZaun["Mana"])):
                    PnZManaArr.append((PiltoverZaun["Mana"][i]))
                lbPnZmana = Label(Terbatas2, text = "\n".join(PnZManaArr) )
                lbPnZmana.pack()
                lbPnZmana.place(x=98 , y=100)
                

btn1 = Button(window, command = submit, text="CARI").place(x=130,y=200)

window.mainloop()