#include <stdio.h>

int main()
{
    int N, K;
    scanf("%d %d", &N, &K);
    int sub_fac_N = 1, fac_K = 1;
    for (int i = 0; i < K; i++){
        sub_fac_N *= (N - i);
        fac_K *= (K - i);
    }
    printf("%d", sub_fac_N / fac_K);
}
