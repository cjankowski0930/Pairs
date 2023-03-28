#[(46, 162), (118, 273), (96, 116), (92, 200), (102, 231), (153, 226), (173, 248), (237, 285), (48, 276), (25, 291),
# (43, 214), (61, 205), (40, 62), (64, 66), (49, 167), (21, 182), (230, 284), (116, 192), (220, 298), (146, 239),
# (96, 108)]
import json
import PTLIB.indicator_util as indicator
class LBMOM:

    def __init__(self, instruments_config, historical_df, simulation_start, vol_target):
        self.pairs = [(46, 162), (118, 273), (96, 116), (92, 200), (102, 231), (153, 226), (173, 248), (237, 285),
        (48, 276), (25, 291),(43, 214), (61, 205), (40, 62), (64, 66), (49, 167), (21, 182), (230, 284),
        (116, 192), (220, 298), (146, 239),(96, 108)]
        self.historical_df = historical_df
        self.vol_target = vol_target
        self.simulation_start = simulation_start
        with open(instruments_config) as f:
            self.instruments_config =json.load(f)
        self.sysname = "LBMOM"


    def extend_historicals(self, instruments, historical_data):
        for inst in instruments:
            historical_data["{} adx".format(inst)] = indicator.adx_series(
                high = historical_data["{} high".format(inst)],
                low= historical_data["{} low".format(inst)],
                close=historical_data["{} close".format(inst)],
                n=14
            )
            for pair in self.pairs:
                historical_data["{} ema{}".format(inst, str(pair))] = \
                    indicator.ema_series(historical_data["{} close".format(inst)], n=pair[0]) - \
                    indicator.ema_series((historical_data["{} close".format(inst)], n=pair[1])

        return historical_data


    def run_simulation(self, historical_data):
        pass

    def get_subsys_pos(self):
        pass


