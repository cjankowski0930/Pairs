from data import get_sp500_df as du
import general_utility as gu

if __name__ == '__main__':
    df, instruments = du.get_sp500_df()
    df = du.extend_dataframe(traded=instruments, df=df)

    gu.save_file("./Data/data.obj", (df, instruments))