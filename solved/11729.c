#include <stdio.h>
#include <math.h>

void hanoi(int n, int from, int to, int temp)
{
	if(n == 1) printf("%d %d\n", from, to);
	else{
		hanoi(n - 1, from, temp, to);
		printf("%d %d\n", from, to);
		hanoi(n - 1, temp, to, from);
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	printf("%d\n", (int)pow(2, n) - 1);
	hanoi(n, 1, 3, 2);
}
