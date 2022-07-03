#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "../coeffs.h"


int main(){
    bernoulli("ber.dat",1000000);
    ber_gau("ber_gau.dat","ber.dat","../ques_2/gau.dat",1000000);
    return 0;
}