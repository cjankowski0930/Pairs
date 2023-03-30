from PTLIB import general_utility as gu
from PTLIB import data as du
import random
import json
from dateutil.relativedelta import relativedelta
import subsystems.LBMOM.subsys

df, instruments = du.get_sp500_df()
df = du.extend_dataframe(traded=instruments, df=df)
#
gu.save_file("./Data/data.obj", (df, instruments))
# df, instruments = gu.load_file("./Data/data.obj")
df, instruments = gu.load_file("./Data/data.obj")
print(instruments)

VOL_TARGET = 0.20
print(df.index[-1])
sim_start = df.index[-1] - relativedelta(years=5)
print(sim_start)
strat = subsystems.LBMOM.subsys.LBMOM(instruments_config='./subsystems/LBMOM/config.json',
            historical_df=df, simulation_start=sim_start, vol_target=VOL_TARGET)
strat.get_subsys_pos()

