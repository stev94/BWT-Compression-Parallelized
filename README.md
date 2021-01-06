# Parallel Burrows-Wheeler compression 

This is a parallel implementation of the Burrows-Wheeler compression. 
It has been carried out using the C programming language using the PThread library
for the parallelization part.

The library offers both a c interface (with row results and without checks) and
a python cli, where instead input validation is performed and results are formatted.

Below you can find how to install the full program (c and python), and how to use it.

## Installation
1. You need to have already setup python3 and a gcc compiler.

2. Then download the source code from the [repository](https://github.com/stev94/Parallel-BWT-Compression).
    ```
    git clone https://github.com/stev94/Parallel-BWT-Compression.git
   ```

3. Go in the created folder and install pbwt. This will create an executable 
   named pbwt inside the folder.
    ```
   cd Parallel-BWT-Compression
   make install 
   ```

4. Now, if everything should be setup, you can verify it by typing `./pbwt` 
   inside the Parallel-BWT-Compression folder. The command should be equal to the following one:
    ```
    Usage: pbwt [OPTIONS] COMMAND [ARGS]...
    
      A command line interface for PBWT.
    
    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.
    
    Commands:
      compare  Compare two files.
      unzip    Unzip the input file and put the result in the output file.
      zip      Zip the input file and put the result in the output file.
   ```
   
5. [OPTIONAL]. If you want to use pbwt from everywhere inside your computer follow 
   the following commands:
   ```
   cd Parallel-BWT-Compression
   sudo mv pbwt /usr/local/bin/pbwt
   sudo chmod 755 /usr/local/bin/pbwt
   ```
   
6. Verify the installation by typing the following command from everywhere in your computer
   you should see the `help` message as in point 4:
    ```bash
    pwbt 
   ```


## How to use
Three commands are available:
- Zip a file.
    ```bash
    pbwt zip [OPTIONS] INPUT_FILE [OUTPUT_FILE] 
    ```
- Unzip a file.
  ```bash
  pbwt unzip INPUT_FILE [OUTPUT_FILE] 
    ```
- Compare two files
  ```bash
  pbwt compare FILE1 FILE2 
    ```

For more information you can use the `pbwt [COMMAND] --help` option.

## Documentation
The documentation as well as a presentation of the work can be found [in this folder](https://github.com/stev94/Parallel-BWT-Compression/blob/master/doc).

## Tests
There are some tests to validate the algorithm that use some benchmarks files that
can be found [here](https://github.com/stev94/Parallel-BWT-Compression/blob/master/tests/examples).
Each file is zipped, then unzipped, and the original file is compared with the unzipped one. They 
must be equal to pass the test.

The tests can be run by typing inside the `Parallel-BWT-Compression` folder, the following command:
```
make test
```

## References
The algorithm has been taken from the following work:
- J. Gilchrist and A. Cuhadar (2007). 
  Parallel Lossless Data Compression Based on the Burrows-Wheeler Transform.
  21st International Conference on Advanced Information Networking and Applications (AINA '07).