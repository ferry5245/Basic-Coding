#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,y;
    scanf("%d", &n);
    y=n%10+(n%100/10)+(n%1000/100)+(n%10000/1000)+(n%100000/10000);
    printf("%d",y);
    return 0;
}
