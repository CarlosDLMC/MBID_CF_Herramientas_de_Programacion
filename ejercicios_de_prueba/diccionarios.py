import pandas as pd
import numpy as np

# gr = ["Hola", "Hello", "Привет"]
# lan = ["Español", "English", "Русский"]
#
# df = pd.DataFrame({"Languages": lan, "Greetings": gr})
#
# print(df)

df = pd.read_csv("heart.csv")
print(df.count())
