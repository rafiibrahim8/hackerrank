// https://www.hackerrank.com/challenges/array-left-rotation/problem

#include <stdio.h>

int main(){
    int n,r,i,x,j;
    scanf("%d %d", &n, &r);
    int arr[n];
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for(i = 0; i < r; i++){
        x = arr[0];
        for(j = 1; j < n; j++){
            arr[j-1] = arr[j];
        }
        arr[n-1] = x;
    }

    for(i = 0; i < n-1; i++){
        printf("%d ", arr[i]);
    }
    printf("%d", arr[n-1]);
}
