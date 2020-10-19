// https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#include <stdio.h>
#include <stdlib.h>
int main(){
    int n,a,b,c,i;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d %d %d", &a, &b, &c);
        if(abs(a-c)<abs(b-c)){
            printf("Cat A\n");
        } else if(abs(a-c)>abs(b-c)){
            printf("Cat B\n");
        } else{
            printf("Mouse C\n");
        }
    }
}
