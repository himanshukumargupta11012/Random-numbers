#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "../coeffs.h"
int main(){
    // gaussian("gau2.dat",1000000);
    // gau_gau("gau_gau.dat","../ques_2/gau.dat","gau2.dat",1000000);
    gau_gau("gau_gau3.dat",2,1e6);
    return 0;
}