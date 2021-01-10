import io
import os
import glob
import shutil
import zipfile

from requests import get

from analysis.util import ZIP_DIR, BENCHMARKS, create_dir, RES_DIR


def _download_benchmarks():
    print("Starting download of benchmarks")
    benchmarks = {}
    for bench_name, bench in BENCHMARKS.items():
        bench_dir = os.path.join(ZIP_DIR, bench_name)
        if not os.path.exists(bench_dir):
            zip_bytes = get(bench['url']).content
            if '404 Not Found' in str(zip_bytes):
                raise ValueError(f'URL not found: {bench["url"]}')
            zip_file = zipfile.ZipFile(io.BytesIO(zip_bytes))
            zip_file.extractall(bench_dir)
            zip_file.close()
        benchmarks[bench_name] = [os.path.join(bench_dir, file) for file in
                                  glob.glob(os.path.join(bench_dir, '*'))]
    return benchmarks


class InputProvider:

    def __init__(self):
        create_dir(ZIP_DIR, remove=False)
        create_dir(RES_DIR)
        self.benchmarks = self.init_benchmarks()
        self._benchmarks_list = list(self.benchmarks.keys())
        self.benchmarks_done = []
        self.current_files = list(self.benchmarks.values())[0]
        self.current_bench_index = 0
        self.current_file_index = 0

    @property
    def all_done(self):
        return all(b in self.benchmarks_done for b in self.benchmarks)

    @property
    def next_file(self):
        if self.current_file_index < len(self.current_files):
            self.current_file_index += 1
            return self.current_files[self.current_file_index - 1]
        return self.next_benchmark()

    def next_benchmark(self):
        self.finish_benchmark()
        if self.all_done:
            print('Benchmarks finished.')
            return None

        next_bench = [bench for bench in BENCHMARKS
                      if bench not in self.benchmarks_done][0]
        self.current_file_index = 1
        self.current_files = self.benchmarks[next_bench]
        return self.current_files[self.current_file_index - 1]

    def finish_benchmark(self):
        self.benchmarks_done.append(self._benchmarks_list[self.current_bench_index])
        self.current_bench_index += 1

    def init_benchmarks(self):
        benchmarks = _download_benchmarks()
        return benchmarks

    def clean(self):
        shutil.rmtree(ZIP_DIR)
