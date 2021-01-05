import os
import glob
import shutil
import unittest

import cli.pbwt_cli as pbwt
import cli.cpbwt.pbwt_cli_cython as cpbwt

from zipfile import ZipFile
from cli.version import ROOT_DIR

TEST_CASES_FOLDER = os.path.join(ROOT_DIR, 'tests', 'examples')
ZIPS = glob.glob(os.path.join(TEST_CASES_FOLDER, '*.zip'))


class TestPBWT(unittest.TestCase):

    def setUp(self):
        self.folders = []

    def tearDown(self):
        for folder in self.folders:
            shutil.rmtree(folder)

    def test_run_test_cython(self):
        for index in [0, 1]:        # run both parallel and sequential
            self.run_test(os.path.join(TEST_CASES_FOLDER, 'easy'), index, cpbwt)
        if os.path.exists(os.path.join(TEST_CASES_FOLDER, 'easy', '.pbwt')):
            os.remove(os.path.join(TEST_CASES_FOLDER, 'easy', '.pbwt'))
        if os.path.exists(os.path.join(TEST_CASES_FOLDER, 'easy', '.unpbwt')):
            os.remove(os.path.join(TEST_CASES_FOLDER, 'easy', '.unpbwt'))

    def test_run_tests(self):
        # from zips in examples
        for index, zip_ in enumerate(ZIPS):
            self.folders.append(self.open_zip(zip_))
            files = os.path.join(self.folders[index], '*')
            for index_file, file in enumerate(glob.glob(files)):
                self.run_test(file, index_file, pbwt)

        # from urls provided

    def run_and_wait_for_exit(self, func, *args):
        try:
            func(*args)
        except SystemExit as e:
            self.assertEqual(e.code, 0)

    def run_test(self, testfile, index, pbwt):
        mode = 'p' if index % 2 == 0 else 's'
        print(f'PBWTTEST - Starting test of {testfile} with mode {mode}')
        outfile = testfile.split('.')[0] + '.pbwt'
        tmpfile = testfile.split('.')[0] + '.unpbwt'
        self.run_and_wait_for_exit(pbwt.zip_, [testfile, outfile, "--chunk_size", 1, "--mode", mode])
        self.run_and_wait_for_exit(pbwt.unzip, [outfile, tmpfile])
        self.run_and_wait_for_exit(pbwt.compare, [testfile, tmpfile])
        print(f'PBWTTEST - Finished test of {testfile}')

    def open_zip(self, zip_):
        zip_dir = zip_.split('.')[0]
        self.__mkdir(zip_dir)
        with ZipFile(zip_, 'r') as zipper:
            zipper.extractall(zip_dir)
        return zip_dir

    def __mkdir(self, dir_):
        if not os.path.exists(dir_):
            os.mkdir(dir_)
