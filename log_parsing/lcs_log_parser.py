import pymongo
import re

from algorithms.longest_common_subsequence import LCS


class LogObject:
    def __init__(self, lcs, id_list):
        self.lcs = lcs
        self.idList = []


class LcsLogParser(object):
    def __init__(self, assignment_threshold):
        # Whitespace, hypen and parenthesis
        # self.tokenRegex = "\s|-|\(|\)|\n|:|,"
        self.assignmentThreshold = assignment_threshold
        self.tokenRegex = "\s"
        self.logMap = []

    def parse(self, log):
        log_tokenized = self.tokenize_log(log=log)
        self.assign_to_log_map(log_tokenized=log_tokenized)
        print("X")

    def tokenize_log(self, log):
        tokenized = re.split(self.tokenRegex, log)
        tokenized = [tkn for tkn in tokenized if tkn != ""]
        return tokenized

    def assign_to_log_map(self, log_tokenized):
        selected_log_id = -1
        selected_lcs = None
        selected_lcs_source = None

        for log_id in range(len(self.logMap)):
            candidate_lcs = LCS.lcs(x=log_tokenized, y=self.logMap[log_id].lcs)
            if selected_lcs is None:
                selected_log_id = log_id
                selected_lcs = candidate_lcs
                selected_lcs_source = self.logMap[log_id].lcs
            elif len(candidate_lcs) > len(selected_lcs):
                selected_log_id = log_id
                selected_lcs = candidate_lcs
                selected_lcs_source = self.logMap[log_id].lcs
            # Compare len(self.logMap[log_id].lcs) with the selected_lcs_source
            elif len(candidate_lcs) == len(selected_lcs) and len(self.logMap[log_id].lcs) < len(selected_lcs_source):
                selected_log_id = log_id
                selected_lcs = candidate_lcs
                selected_lcs_source = self.logMap[log_id].lcs

        if selected_log_id == -1:
            log_object = LogObject(lcs=log_tokenized, id_list=None)
            self.logMap.append(log_object)
        else:
            lcs_ratio = len(selected_lcs) / len(log_tokenized)
            if lcs_ratio >= self.assignmentThreshold:
                self.logMap[selected_log_id].lcs = selected_lcs
            else:
                log_object = LogObject(lcs=log_tokenized, id_list=None)
                self.logMap.append(log_object)




