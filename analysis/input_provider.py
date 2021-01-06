import os

from requests import get

from analysis.util import BENCHMARKS_URLS, ZIP_DIR


class InputProvider:

    def __init__(self):
        os.mkdir(ZIP_DIR)
        self.benchmarks = self.download_benchmarks()
        self.benchmarks_done = []
        self.current_bench_index = 0
        self.current_file_index = 0
        self.current_files = []

    @property
    def is_finished(self):
        return all(b in self.benchmarks_done for b in self.benchmarks)

    @property
    def next_file(self):
        if self.current_file_index < len(self.current_files):
            self.current_file_index += 1
            return self.current_files[self.current_file_index - 1]

        self.benchmarks_done.append(self.benchmarks[self.current_bench_index])
        self.current_bench_index += 1
        if not self.is_finished:
            self.next_benchmark()
        else:
            print('Benchmarks finished.')
            return None

    def next_benchmark(self):
        self.current_file_index = 0
        self.current_files = []

    def download_benchmarks(self):
        benchmarks = []
        for bench_url in BENCHMARKS_URLS:
            zip = get(bench_url)
        return benchmarks
