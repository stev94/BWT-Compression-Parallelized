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
 * @file 	main.h
 * @author 	Stefano Valladares, ste.valladares@live.com
 * @date	20/12/2018
 * @version 1.1
 *
 * @brief	Main header of the application.
 */

#include "bwtUnzip.h"
#include "parallelBwtZip.h"
#include "sequentialBwtZip.h"

typedef struct timespec ts;

typedef struct Results 
{
    double executionTime;
    long chunkSize;

} Results;

Results _run(void (*runner)(file *in, FILE *out, clong chunkSize),
             cstr inPath, cstr outPath, clong chunkSize, cstr action);

Results zip(str in, str out, cchar mode, clong chunkSize);

Results unzip(cstr in, cstr out);

int compare(cstr in, cstr out);
