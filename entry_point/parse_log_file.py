import os
from pathmanager import PathManager

from log_parsing.lcs_log_parser import LcsLogParser
from log_reader.log_reader import LogReader
from utils import PATH_MANAGER

assignment_threshold = 0.3


def parse_log_file():
    file_path = os.path.dirname(__file__)
    log_path = os.path.join(file_path, "..", "log_files", "Windows.log")
    reader_path = os.path.join(file_path, "..", "saved_models", "log_reader.dat")
    # PATH_MANAGER.add(name="source_log_file", path=log_path)
    # PATH_MANAGER.add(name="log_reader_object", path=reader_path)

    log_reader = LogReader(log_file_path=log_path)
    log_parser = LcsLogParser(assignment_threshold=0.3)
    # log_reader = LogReader.load(path=reader_path)

    # Read logs
    for log_line in log_reader.get_log():
        print(log_line)
        log_parser.parse(log=log_line)

