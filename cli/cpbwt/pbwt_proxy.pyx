cdef extern from "util.h":
    ctypedef char* str

cdef extern from "main.h":
    ctypedef struct Results:
        double executionTime
        int chunkSize
    Results zip(str infile, str outfile, char mode, long chunk_size)
    Results unzip(str infile, str outfile)
    void compare(bytes f1, bytes f2)

def zip_(str in_path, str out_path, int chunkSize, long mode):
    cdef Results results = zip(in_path, out_path, mode, chunkSize)


def unzip(str in_path, str out_path):
    cdef Results results = unzip(in_path, out_path)


def compare(str f1_path, str f2_path):
    compare(f1_path, f2_path)
