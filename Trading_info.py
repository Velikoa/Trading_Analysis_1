import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker as tick

class KIO:
    def __init__(self, df, df_iron):
        self.df = df
        self.df_iron = df_iron

    def simple_MVA(self, twenty_one_day, hundred_day, two_hundred_day):
        dates = self.df["Date"]
        closing = self.df["Close"]

        ax = plt.subplot()

        #setting titles and axess labels
        ax.set_title("KIO Closing Price", fontsize=20)
        ax.set_xlabel("Date")
        ax.set_ylabel("Closing Prices")

        ax.tick_params(axis='both', which='major', labelsize=10)

        ax.plot(dates, closing)
        rolling_mean_21 = closing.rolling(window=twenty_one_day).mean()
        rolling_mean_100 = closing.rolling(window=hundred_day).mean()
        rolling_mean_200 = closing.rolling(window=two_hundred_day).mean()

        plt.plot(dates, rolling_mean_21, color="black")
        plt.plot(dates, rolling_mean_100, color="magenta")
        plt.plot(dates, rolling_mean_200, color="red")

        ax.legend(["One-Year Movement", "21-Day MVA", "100-Day MVA", "200-Day MVA"])

        plt.show()

    def RSI(self):
        dates = self.df["Date"][1:]

        #Provide the mean closing price over the entire period
        average_year = self.df["Close"].mean(skipna=True)
        #Adding numbers to strings makes no sense so need to first convert number to a string.
        print("Mean for entire period: " + str(average_year))

        #Count the number of entries in the dataframe
        df_size = self.df["Close"].count()
        print("Number of rows in the dataframe: " + str(df_size))

        #Printing the differences between the prior closing price and the next
        daily_differences = self.df["Close"].diff().dropna()

        #Allocating all positive differences to a variable
        #daily_differences is a dataframe - so you need to select only the positives from it using []
        up = daily_differences[daily_differences > 0]
        Upzero = daily_differences.copy()
        Upzero[Upzero < 0] = 0
        avg_up_movements = Upzero.rolling(window=14).mean()

        #Allocating all negative differences to a variable
        down = daily_differences[daily_differences < 0]
        Downzero = daily_differences.copy()
        Downzero[Downzero > 0] = 0
        avg_down_movements = abs(Downzero.rolling(window=14).mean())

        RS = avg_up_movements / avg_down_movements
        RSI = 100.0 - (100.0 / (1.0 + RS))

        ax = plt.subplot()

        ax.set_title("Relative Strength Index", fontsize=20)
        ax.set_xlabel("Date")
        ax.set_ylabel("Closing Prices")

        loc = tick.MultipleLocator(base=30.0)
        ax.xaxis.set_major_locator(loc)
        plt.plot(dates, RSI)
        plt.axhline(y=50, color="black")

        plt.show()

    def MACD(self):
        self.df.dropna()
        dates = self.df["Date"]

        MVA_12 = self.df["Close"].rolling(window=12).mean()
        MVA_26 = self.df["Close"].rolling(window=26).mean()

        #The MACD line - being the difference between the 26 and 12-day EMA
        MACD_line = MVA_26 - MVA_12

        #The signal line - being the 9-day moving average of the MACD line
        signal_line = MACD_line.rolling(window=9).mean()

        ax = plt.subplot()
        ax.set_title("MACD")
        ax.set_xlabel("Date")
        ax.set_ylabel("Closing Prices")

        plt.plot(dates, MACD_line, color="black")
        plt.plot(dates, signal_line, color="red")
        plt.axhline(y=0)

        ax.legend(["MACD line", "Signal line", "Oscillator"])

        plt.show()

    def KIO_vs_iron(self):
        #df = pd.read_csv("C:/Users/Veliko/Documents/Documents/Trading/Source_files/2020/KIO-07Feb.csv", parse_dates=["Date"])
        #df_iron = pd.read_excel("C:/Users/Veliko/Documents/Documents/Trading/Source_files/2020/Iron_ore/Iron_ore-07Feb.xlsx", parse_dates=["DATE"])

        self.df["Date"] = self.df["Date"].astype("datetime64[ns]")
        self.df_iron["DATE"] = self.df_iron["DATE"].astype("datetime64[ns]")
        self.df["Date"] = pd.to_datetime(self.df["Date"], format="%Y-%m-%d", errors="coerce")

        #Change the date format to have - instead of /
        self.df_iron["DATE"] = pd.to_datetime(self.df_iron["DATE"], format="%Y-%m-%d", errors="coerce")
        self.df_iron.replace("/", "-")

        del self.df["Open"]
        del self.df["High"]
        del self.df["Low"]
        del self.df["Adj Close"]
        del self.df_iron["OPEN"]
        del self.df_iron["DAILY HIGH"]
        del self.df_iron["DAILY LOW"]

        sorted_iron = self.df_iron.sort_values(by=["DATE"], ascending=False)

        df_merged = pd.concat([self.df, self.df_iron], sort=True)

        fig, ax1 = plt.subplots()
        plt.plot(df_merged["DATE"], df_merged["CLOSING PRICE"], color="red")
        plt.title("KIO Closing Price versus Iron Ore Spot Price")
        ax1.set_ylabel("Iron Ore Spot Price")
        ax1.legend(['Iron Ore'])

        ax2 = ax1.twinx()
        ax2.set_ylabel("KIO Closing Price")
        plt.plot(df_merged["Date"], df_merged["Close"])


        plt.show()



KIO = KIO(pd.read_csv("C:/Users/Veliko/Documents/Documents/Trading/Source_files/2020/KIO-07Feb.csv", parse_dates=["Date"]),
          pd.read_excel("C:/Users/Veliko/Documents/Documents/Trading/Source_files/2020/Iron_ore/Iron_ore-07Feb.xlsx", parse_dates=["DATE"]))

# KIO.simple_MVA(21, 100, 200)
# KIO.RSI()
# KIO.MACD()
# KIO.KIO_vs_iron()


