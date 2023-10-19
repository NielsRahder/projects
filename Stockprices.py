import pandas as pd
import quandl as qd
import numpy
import matplotlib.pyplot as plt

qd.ApiConfig.api_key = "eUuL1Pyx1hPeq3-sjXz7"

aapl_data = qd.get('EOD/AAPL', start_date = "2010-01-01", 
end_date = "2011-01-01")
apple = aapl_data.head()

apple
