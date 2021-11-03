import pandas as pd
import numpy as np

class Valuations():
    def Gordon_growth_model(D0, risk_free, beta, risk_premium, retention_ratio, net_income, average_equity):
        ROE = net_income / average_equity
        growth = retention_ratio * ROE
        r = risk_free + beta * (risk_premium)

        print((D0 * (1 + growth)) / (r - growth))


#Percentage growth rates and ratios need to be written as decimals in the arguements.
Valuations.Gordon_growth_model(30.24, 0.07292, 1.2, 0.05, 0.02, 12595, 45867)

