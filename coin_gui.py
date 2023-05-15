import tkinter as tk
from tkinter import messagebox


window = tk.Tk()

# declare coins variable
hasPound = tk.BooleanVar()
has50p = tk.BooleanVar()
has20p = tk.BooleanVar()
has10p = tk.BooleanVar()
has5p = tk.BooleanVar()
has2p = tk.BooleanVar()


window.title("Change Calculator - 22225745")
# window.iconbitmap("changeicon.png")
window.configure(background='grey')
window.geometry("1000x500")

coins = {100,50,20,10,5,2,1}
rCoins = set()
def exitApp():
    print("Ending App...")
    window.destroy()

def change():
    """
    This function  returns the minimum available coins change
    given to a custoemr.

    It also handles error for wrong user input.
    """
    print("Update... ")
    print(f"{lblCoinEntry.get()}")


    # get the coins available to give and sort them in descendingorder
    available_coins = sorted(coins, reverse=True)

    # coin variable
    p100 = p50 = p20 = p10 = p5 = p2 = 0

    try:
        # get the amount the user entered
        user_input = float(lblCoinEntry.get())
    except ValueError:
        messagebox.showerror('Python Error', 'Error: Please Enter a number!')


    # loop through the set of sorted avaliable coins
    for coin in available_coins:
        while user_input >= coin:
            user_input -= coin
            
            # increament coins
            if coin == 100:
                p100 += 1
            if coin == 50:
                p50 += 1
            if coin == 20:
                p20 += 1
            if coin == 10:
                p10 += 1
            if coin == 5:
                p5 += 1
            if coin == 2:
                p2 += 1
        

    # display the coins with their corresponding quantity(ies)
    lblResult.configure(text= f"""{'£':3} {p100}\n
{'50p':3} {p50} \n
{'20p':3} {p20} \n
{'10p':3} {p10} \n
{'5p':3} {p5} \n
{'2p':3} {p2}\n
""")
    
    

def exclude(n):
    """
    Function to exclude coins from change to be given to customer.
    It also handles error for when user does not select any coin.
    """
    global coins
    global rCoins
    c ={100:hasPound.get(),
         50:has50p.get(),
         20:has20p.get(),
         10:has10p.get(),
         5:has5p.get(),        
          2:has2p.get()
     }.get(n)
     
    print(f"{n}: {c}")
    if  c:
        coins = coins - {n}
    else:
        coins.add(n)
    print(f"Coins available {coins}")


    # Error handling logic for if the user does not select any coin
    if len(coins) == 1:
        # disable exec button
        btnExe.config(state= "disabled")
        # disable the input box
        lblCoinEntry.config(state= "disabled")
        messagebox.showerror('Python Error', 'Error: Choose at least one coin')
        print('ERROR!!!')
    else:
        # else enable both
        btnExe.config(state= "active")
        lblCoinEntry.config(state= "normal")
    
    
# Title
lblTitle =tk.Label(text="Change Machine...", 
                   font=('Time New Roman', 24,'bold'),
                   bg ='black',
                   fg='white') 
lblTitle.grid(row=0,column=0,columnspan=3,pady=(3,10))

#Entry
lblTitle =tk.Label(text="Change Required: ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
lblTitle.grid(row=1,column=0, sticky=tk.E, padx=(5,5))

# input box
lblCoinEntry =tk.Entry(text="Change Machine...", 
                   font=('Time New Roman', 12,'bold') ) 
lblCoinEntry.grid(row=1,column=1, columnspan=6,pady=(5,5) )
# add  a placeholder to the input box
lblCoinEntry.insert(0, "Enter amount")

#Coin Availability
lblCoins =tk.Label(text="Coins NOT Avalabile:", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
lblCoins.grid(row=2,column=0,pady=(5,2) )


cbPound = tk.Checkbutton(window, text="£", variable=hasPound,
                         font=('Time New Roman', 12,'bold'),
                         bg ='white',
                         fg='black',
                         command= lambda: exclude(100))
cbPound.grid(row=3, column=1)


# £50 pound check box
cb50p = tk.Checkbutton(window, text="50p", variable=has50p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='white',
                       fg='black',
                       command= lambda: exclude(50)) 
cb50p.grid(row=3, column=2)


# £20 pound check box
cb20p = tk.Checkbutton(window, text="20p", variable=has20p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='white',
                       fg='black',
                       command= lambda: exclude(20)) 
cb20p.grid(row=3, column=3)

# £10 pound check box
cb10p = tk.Checkbutton(window, text="10p", variable=has10p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='white',
                       fg='black',
                       command= lambda: exclude(10)) 
cb10p.grid(row=3, column=4)

# £5 pound check box
cb5p = tk.Checkbutton(window, text="5p", variable=has5p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='white',
                       fg='black',
                       command= lambda: exclude(5)) 
cb5p.grid(row=3, column=5)

# £2 pound check box
cb2p = tk.Checkbutton(window, text="2p", variable=has2p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='white',
                       fg='black',
                       command= lambda: exclude(2))
cb2p.grid(row=3, column=6)


#Result
lblCoins = tk.Label(text="Coin break down:", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
lblCoins.grid(row=4,column=0, sticky=tk.N)

lblResult = tk.Label(text='', 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
lblResult.grid(row=4,column=1, pady=(10,2))



# Exec button
btnExe = tk.Button(text="Exec", font=('Time New Roman', 12,'bold'), 
                   command=change, width=10,height=2)
btnExe.grid(row=4, sticky=tk.N, column=9)

btnQuit = tk.Button(text="Quit", font=('Time New Roman', 12,'bold'), 
                    command=exitApp, width=10,height=2)
btnQuit.grid(row=4, sticky=tk.N, column=10)


window.mainloop()


