import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from prac import df

order_details=pd.read_csv("order_details.csv")
# # print(order_details)
products=pd.read_csv("products.csv")
# # print(products)
customers=pd.read_csv("customers.csv")
# # print(customers)
orders=pd.read_csv("orders.csv")
# # print(orders)
#
#
customers=pd.DataFrame(customers)
# # print(customers)
orders=pd.DataFrame(orders)
# # print(orders)
products=pd.DataFrame(products)
# # print(products)
order_details=pd.DataFrame(order_details)
# # print(order_details)



