
# import pandas library
import pandas as pd

# set variable to load csv file
file_to_load = "Resources/purchase_data.csv"
# set variable to read and establish a data frame
purchase_date = pd.read_csv(file_to_load)
purchase_date.head()

# Player Count
players_count = len(purchase_date["SN"].unique())
print("Total number of players is:" ,players_count)
 