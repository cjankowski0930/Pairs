from PTLIB import general_utility as gu
from PTLIB import data as du

#df, instruments = du.get_sp500_df()
# df = du.extend_dataframe(traded=instruments, df=df)

#gu.save_file("./Data/data.obj", (df, instruments))
df, instruments = gu.load_file("./Data/data.obj")
print(df, instruments)