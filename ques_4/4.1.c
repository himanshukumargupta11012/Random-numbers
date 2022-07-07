#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "../coeffs.h"
int main(){
    uniform("uni2.dat",1000000);
    triangular("tri.dat","../ques_1/uni.dat","uni2.dat",1000000);
    
}