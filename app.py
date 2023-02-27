import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.dialogs import MessageDialog
from tkinter.filedialog import askopenfilename
from ttkbootstrap.constants import *
from pypdf import PdfReader, PdfWriter
import os

app = ttk.Window(title="SecurePDF v. 0.5", themename="superhero", iconphoto ='pdf_48.png', size=(1000, 500))
app.place_window_center()

colors = app.style.colors

def zabezpiecz():    # ZABEZPIECZANIE PLIKU
    filename = filepath.get()
    passpdf = newpass.get()

    if filename == "":
        st1.insert(END, '\nPlik PDF nie został wybrany') 
        return

    if len(passpdf) < 8:
        st1.insert(END, '\nHasło nie może być krótsze niż 8 znaków') 
        return
    
    try:
        reader = PdfReader(filename)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(passpdf)

        dirfile = os.path.split(filename)
        sciezka = dirfile[0]
        plik = dirfile[1]
        encfile = os.path.join(sciezka, 'enc_' + plik)

        with open(encfile, 'wb') as ef:
            writer.write(ef)
    except:
        text = '\nBłąd zabezpieczania pliku - ' + plik
    else:    
        text = '\nPlik został zabezpieczony hasłem. Nowa nazwa - ' + 'enc_' + plik
        
    st1.insert(END, text)

def open_file():   # DIALOG WYBORU PLIKU
    path = askopenfilename()
    if path:
        filepath.set(path)
        print(filepath.get())

def about():
    md = MessageDialog(message = 'SecurePDF 0.5\n\n * zabezpieczanie plików PDF hasłem\n\nAutor: Leszek Owczarek\nLicencja: MIT', title = 'Informacja', buttons=["OK:primary"])
    md.show()

# WYBÓR PLIKU PDF

container1 = ttk.Frame()
container1.pack(fill=X, expand=YES, pady=5)

b1 = ttk.Button(master=container1, text="Wybierz plik PDF", bootstyle=SUCCESS, command=open_file)
b1.pack(side=LEFT, padx=5, pady=5)
filepath = ttk.StringVar()
e1 = ttk.Entry(master=container1, textvariable=filepath)
e1.pack(padx=5, pady=5, expand=YES, fill=BOTH,)


# PODANIE HASŁA I WYWOŁANIE FUNKCJI ZABEZPIECZ

container2 = ttk.Frame()
container2.pack(fill=X, expand=YES, pady=5)

lb1 = ttk.Label(master=container2,bootstyle="info", text='Podaj hasło ')
lb1.pack(side=LEFT,padx=5, pady=5)
newpass = ttk.StringVar()
e2 = ttk.Entry(master=container2, textvariable=newpass)
e2.pack(side=LEFT,padx=5, pady=5)
b2 = ttk.Button(master=container2, text="Zabezpiecz plik", bootstyle=(INFO, OUTLINE), command=zabezpiecz)
b2.pack(side=LEFT, padx=5, pady=5)

# INFO
b5 = ttk.Button(master=container2, text="I", bootstyle=(INFO, OUTLINE), command=about)
b5.pack(side=RIGHT, padx=5, pady=5)

# OKNO KOMUNIKATÓW
st1 = ScrolledText(app, padding=5, height=10, autohide=True)
st1.pack(fill=BOTH, expand=YES)


if __name__ == "__main__":
    app.mainloop()
