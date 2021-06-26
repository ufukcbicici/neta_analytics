import numpy as np
import pickle


class LogReader(object):
    def __init__(self, log_file_path):
        self.lastIndex = 0
        self.logFilePath = log_file_path

    def get_log(self):
        curr_index = 0
        with open(self.logFilePath) as log_file:
            for line in log_file:
                if curr_index < self.lastIndex:
                    curr_index += 1
                    continue
                else:
                    assert curr_index == self.lastIndex
                yield line
                curr_index += 1
                self.lastIndex = curr_index

    @staticmethod
    def save(path, reader):
        with open(path, "wb") as f:
            pickle.dump(reader, f)

    @staticmethod
    def load(path):
        with open(path, "rb") as f:
            reader = pickle.load(f)
        return reader




