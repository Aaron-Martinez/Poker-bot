#include <iostream>
#include <stdlib.h>
#include <string>
#include "src/SevenEval.h"

int main(int argc, char** argv) {

    if(argc != 8) {
	std::cout << "Must have 7 arguments" << std::endl;
	return 1;
    }
    int a[7];
    for(int i = 1; i <= 7; i++) {
	a[i-1] = atoi(argv[i]);
    }
    std::cout << std::to_string( SevenEval::GetRank(a[0], a[1], a[2], a[3], a[4], a[5], a[6]) );
    std::cout.flush();

    //std::cout << "done" << std::endl;
    return 0;

    //return SevenEval::GetRank(a[0], a[1], a[2], a[3], a[4], a[5], a[6]);
}
