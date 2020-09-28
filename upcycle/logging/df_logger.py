import os
import pickle
import pandas as pd


class DataFrameLogger(object):
    def __init__(self, log_dir):
        self.data = {}
        self.log_dir = os.path.normpath(log_dir)

    def add_table(self, table_name, table_data=None):
        records = [] if table_data is None else table_data
        self.data[table_name] = records

    def log(self, metrics, step, table_name):
        if step is None:
            step = len(self.data[table_name])
        metrics.update({'step': step})
        self.data[table_name].append(metrics)

    def write_csv(self, save_dir=None):
        for table_name, records in self.data.items():
            save_df = pd.DataFrame(records)
            save_dir = self.log_dir if save_dir is None else save_dir
            save_df.to_csv(os.path.join(save_dir, f'{table_name}.csv'), index=False)

    def write_hydra_yaml(self, cfg):
        """Hydra automatically generates a local log of the config"""
        pass

    def save_obj(self, obj, filename):
        save_path = os.path.join(self.log_dir, filename)
        with open(save_path, 'wb') as f:
            pickle.dump(obj, f)
