/******************************************************************************
 * Copyright (C) 2018 by Stefano Valladares                                   *
 *                                                                            *
 * This file is part of ParallelBWTzip.                                       *
 *                                                                            *
 *   ParallelBWTzip is free software: you can redistribute it and/or modify   *
 *   it under the terms of the GNU Lesser General Public License as           *
 *   published by the Free Software Foundation, either version 3 of the       *
 *   License, or (at your option) any later version.                          *
 *                                                                            *
 *   ParallelBWTzip is distributed in the hope that it will be useful,        *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of           *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            *
 *   GNU Lesser General Public License for more details.                      *
 *                                                                            *
 *   You should have received a copy of the GNU Lesser General Public         *
 *   License along with ParallelBWTzip. 									  *
 *   If not, see <http://www.gnu.org/licenses/>.     						  *
 ******************************************************************************/

/**
 * @file 	main.c
 * @author 	Stefano Valladares, ste.valladares@live.com
 * @date	20/12/2018
 * @version 0.1.0
 *
 * @brief	Main of the application.
 */

#include "../headers/main.h"

Results _run(void (*runner)(file *in, FILE *out, clong chunkSize),
             cstr inPath, cstr outPath, clong chunkSize, cstr action)
{
    ts start, end;
	file *in  = openFileRB(inPath);
	FILE *out = openFileWB(outPath);

	printf("PBWT - Starting %s...\n", action);
    clock_gettime(CLOCK_MONOTONIC, &start);
    runner(in, out, chunkSize);
    clock_gettime(CLOCK_MONOTONIC, &end);
	printf("PBWT - Finished %s.\n", action);

	fclose(in);
	fclose(out);

    double time = (end.tv_sec - start.tv_sec) + 
                    (end.tv_nsec - start.tv_nsec) / 1000000000.0;

    return (Results) {time, chunkSize};
}

Results zip(cstr inPath, cstr outPath, cchar  mode, clong chunkSize)
{
	if(mode == 'p') {
	    extern Buffer readin, bwt, arith;
        Results results = _run(compressParallel, inPath, outPath, chunkSize, "zip");
        free(readin.queue);
        free(bwt.queue);
        free(arith.queue);
        return results;
    } else 
        return _run(compressSequential, inPath, outPath, chunkSize, "zip");
}

Results unzip(cstr inPath, cstr outPath)
{
    return _run(decompress, inPath, outPath, NULL, "unzip");
}

int compare(cstr f1Path, cstr f2Path)
{
	file *f1 = openFileRB(f1Path);
	file *f2 = openFileRB(f2Path);

	puts("PBWT - Starting comparison...");
	int result = compareFiles(f1, f2, fileSize(f2), fileSize(f2));
	puts("PBWT - Finished comparison.");

	if(result == 1)
		puts("PBWT - Files are equals.");
	else if(result == 0)
		puts("PBWT - File1 has less bytes than file2.");
	else
		puts("PBWT - File1 has more bytes than file2.");

	fclose(f1);
	fclose(f2);

    return result == 1 ? 0 : 1;
}

int main(int argc, char *argv[], char *env[])
{
    cstr action = argv[1];
    cstr inPath = argv[2];
    cstr outPath = argv[3];

    if (!strcmp(action, "zip"))
    {
        clong chunkSize = atof(argv[4]) * 1024 * 1024;
        cchar mode = argv[5];
        Results results = zip(inPath, outPath, mode, chunkSize);
        printf("Results are: execution_time %ld - chunk_size = %d.\n" ,
                results.executionTime, results.chunkSize);
        return 0;
    } else if (!strcmp(action, "unzip"))
    {
        Results results = unzip(inPath, outPath);
        printf("Results are: execution_time %ld - chunk_size = %d.\n" ,
                results.executionTime, results.chunkSize);
        return 0;
    } else
    {
        int result = compare(inPath, outPath);
        if (result == 0)
            printf("The files are equal.\n");
        else
            printf("The files are not equal.\n");
        return result;
    }
}
