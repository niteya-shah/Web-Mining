import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
import math
store_data = pd.read_csv('store_data.csv')
store_data.head()
records = []
for i in range(0, 7500):
    records.append([str(store_data.values[i,j]) for j in range(0, 20) if not pd.isnull(store_data.values[i,j])])
    print(i,end='\r')
association_rules = list(apriori(records, min_support=0.0045, min_confidence=0.3, min_lift=3, min_length=4))
association_rules
