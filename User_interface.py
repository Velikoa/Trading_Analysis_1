import tkinter as tk
import tkinter.font as font
from Trading_info import KIO

#Creating the user interface for the Trading Analysis Tool
root = tk.Tk()
frame = tk.Frame(root)

#Stating the size and colour of the window
root.geometry('800x600')
root.config(background='white')

root.title("Trading Analysis Tool")

#Adding image to the first window
topImage = tk.PhotoImage(file='stock_market_1.gif')
stock_img = tk.Label(root, image=topImage, bg="black")
stock_img.grid(row=1, columnspan=3)

#Adding Heading KIO
KIO_Heading = tk.Label(root, text= 'Kumba Iron Ore (Ltd)', wraplength=300, justify="left", bg="white", fg="black", width=50, height=2)
KIO_font = font.Font(family='Calibri', size=20)
KIO_Heading.grid(row=2, column=1, sticky="W", padx=2, pady=2)
KIO_Heading['font'] = KIO_font

def moving_average():
    MVA = KIO.simple_MVA(21, 100, 200)
    print(MVA)

def RSI():
    rsi = KIO.RSI()
    print(rsi)

def MACD():
    macd = KIO.MACD()
    print(macd)

def KIO_vs_Iron():
    iron = KIO.KIO_vs_iron()
    print(iron)

######################################################################################################
def technicals_window():
    #Create an additional window within the main window
    new_window = tk.Toplevel()
    new_window.title("Technical Analysis")
    #Set a fixed size for the window
    new_window.geometry('800x600')
    new_window.config(background='white')

    # The main heading
    title_kio = tk.Label(new_window, text="Kumba Iron Ore", font="Helvetica 20 bold")
    title_kio.grid(row=0, column=0)

    kio_img = tk.PhotoImage(file="kumba_locations.gif")
    kio_top_img = tk.Label(new_window, image=kio_img, bg="black")
    kio_top_img.image = kio_img  # keep a reference of the image or else it will not display.
    kio_top_img.grid(row=1, column=0)

    #Adding the MVA button in the Technicals window
    MVA_button = tk.Button(new_window, text='Simple Moving Average', width=20, bg='black', fg='white', command=moving_average)
    MVA_button.grid(row=2, column=0, sticky='W')

    #Adding the RSI button in the Technicals window
    RSI_button = tk.Button(new_window, text='RSI', width=20, bg='black', fg='white', command=RSI)
    RSI_button.grid(row=2, column=0, sticky='E')

    #Adding the MACD button in the Technicals window
    MACD_button = tk.Button(new_window, text='MACD', width=20, bg='black', fg='white', command=MACD)
    MACD_button.grid(row=3, column=0, sticky='W', pady=5)

    #Adding the KIO vs Iron Ore Spot Price button and graph to the Technicals window
    Spot_Iron_button = tk.Button(new_window, text='KIO vs Iron Spot Price', width=20, bg='black', fg='white', command=KIO_vs_Iron)
    Spot_Iron_button.grid(row=3, column=0, sticky='E', pady=5)

#Add 2 buttons for Technical and Fundemantal analysis
technical_analysis = tk.Button(root, text= 'Technical Analysis', wraplength=200, justify="left", bg="black", fg="white", width=20, height=2, command=technicals_window)
technical_analysis.grid(row=3, column=1, sticky="W", padx=2, pady=2)
fundamental_analysis = tk.Button(root, text= 'Fundamental Analysis', wraplength=200, justify="left", bg="black", fg="white", width=20, height=2)
fundamental_analysis.grid(row=3, column=1, sticky="E", padx=2, pady=2)








#Always need this in order to display window on screen - similiar to Matplotlib where need to type
#the plt.show() command
root.mainloop()