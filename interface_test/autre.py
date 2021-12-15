from tkinter import *
from functools import partial

def validateLogin(nom, prenom,ndp,sp,fp,nm,sm,fm,se,ln,dn,hn):
    print("username entered :", nom.get())
    print("password entered :", prenom.get())
    print("username entered :", ndp.get())
    print("password entered :", sp.get())
    print("password entered :", fp.get())
    print("password entered :", nm.get())
    print("username entered :", sm.get())
    print("password entered :", fm.get())
    print("password entered :", se.get())
    print("password entered :", ln.get())
    print("username entered :", dn.get())
    print("password entered :", hn.get())
    return
    
#tkwindow est une création de l'instance de la classe Tk
tkWindow = Tk()  
# definition de la taill de l'interface
tkWindow.geometry('1000x1500')  
# titre de l'interface
tkWindow.title('INTERFACE FONCTIONNAIRE')

#username label and text entry box
usernameLabel = Label(tkWindow, text="Name").grid(row=1, column=0)
nom = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=nom).grid(row=1, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=2, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Prenom").grid(row=2, column=0)
prenom = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=prenom).grid(row=2, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=3, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Nom du pere").grid(row=3, column=0)
ndp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=ndp).grid(row=3, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=4, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="situation matrimonial pere").grid(row=4, column=0)
sp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=sp).grid(row=4, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=5, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="fonction du pere").grid(row=5, column=0)
fp = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=fp).grid(row=5, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=6, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="Nom de la mere").grid(row=6, column=0)
nm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=nm).grid(row=6, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=7, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="situation matrimonial de la mere").grid(row=7, column=0)
sm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=sm).grid(row=7, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=8, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="fonction de la mere").grid(row=8, column=0)
fm = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=fm).grid(row=8, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=9, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="sexe enfant").grid(row=9, column=0)
se = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=se).grid(row=9, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=10, column=0)

#**********************************************************************#

#username label and text entry box
usernameLabel = Label(tkWindow, text="lieu de naissance").grid(row=10, column=0)
ln = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=ln).grid(row=10, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=11, column=0)

#***********************************************************************#
#username label and text entry box
usernameLabel = Label(tkWindow, text="date de naissance").grid(row=11, column=0)
dn = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=dn).grid(row=11, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=12, column=0)

#***********************************************************************#
#username label and text entry box
usernameLabel = Label(tkWindow, text="heure de naissance").grid(row=12, column=0)
hn = StringVar()

#insertion d'un separateur
usernameEntry = Entry(tkWindow, textvariable=hn).grid(row=12, column=1)  
separateur = Label(tkWindow, text="\n").grid(row=13, column=0)





#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=14, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=14, column=1)  

validateLogin = partial(validateLogin, nom, prenom,ndp,sp,fp,nm,sm,fm,se,ln,dn,hn)

#login button
loginButton = Button(tkWindow, text="Enregistrer l'enfant", command=validateLogin).grid(row=15, column=0)  

tkWindow.mainloop()