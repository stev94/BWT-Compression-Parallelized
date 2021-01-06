import glob
import os
import subprocess

import pandas as pd

from analysis.util import COMPRESSORS, COMPRESSORS_BIN


class Tester:

    def __init__(self):
        self.results = {'deflated': pd.DataFrame(columns=COMPRESSORS),
                        'exec_time': pd.DataFrame(columns=COMPRESSORS)}

    def run_compressors(self, file):
        """
        Run all the compressor for a given file and store the results in a
        pandas dataframe.
        """
        for compressor_bin in glob.glob(os.path.join(COMPRESSORS_BIN, '*.sh')):
            process = subprocess.Popen([compressor_bin, file], stdout=subprocess.PIPE)
            self.add_to_results(str(process.communicate()[0]))

    def add_to_results(self, stdout):
        pass

