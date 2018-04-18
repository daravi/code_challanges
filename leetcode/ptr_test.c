#include <stdio.h>


int main(int argc, char const *argv[])
{
	int* ptr;
	int a = 5;
	printf("%d\n", a);
	ptr = &a;
	printf("%d\n", *ptr);
	*ptr = 10;
	printf("%d\n", a);
	return 0;
}