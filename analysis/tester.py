import glob
import os
import subprocess

import pandas as pd

from analysis.util import COMPRESSORS, COMPRESSORS_BIN, RES_DIR


class Tester:

    def __init__(self, benchmarks):
        file_list = [file for bench in benchmarks.values() for file in bench]
        self.results = {'deflated': pd.DataFrame(index=file_list, columns=COMPRESSORS),
                        'exec_time': pd.DataFrame(index=file_list, columns=COMPRESSORS)}

    def store_results(self):
        for metric, results in self.results.items():
            results.to_csv(os.path.join(RES_DIR, f'{metric}.csv'))

    def run_compressors(self, file):
        """
        Run all the compressor for a given file and store the results in a
        pandas dataframe.
        """
        file_name = file.split(".")[0]
        for compressor_bin in glob.glob(os.path.join(COMPRESSORS_BIN, '*.sh')):
            compressor_name = compressor_bin.split('/')[-1].split('.sh')[0]
            output_file = f'{file_name}.pbwt'
            process = subprocess.Popen(['bash', compressor_bin, file, output_file],
                                       stdout=subprocess.PIPE)
            self.add_to_results(file, compressor_name, str(process.communicate()[0]))
            os.remove(output_file)

    def add_to_results(self, bench, compressor, stdout):
        results = stdout.split('RESULTS: ')[1]
        input_size, output_size, exec_time = (metric.split('=')[1] for metric
                                              in results.split(','))
        deflated = (1 - (float(output_size) / float(input_size))) * 100
        self.results['deflated'].loc[bench][compressor] = deflated
        self.results['exec_time'].loc[bench][compressor] = exec_time
