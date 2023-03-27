import data as du
import general_utility as gu


df, instruments = du.get_sp500_df()
df = du.extend_dataframe(traded=instruments, df=df)

gu.save_file("./Data/data.obj", (df, instruments))