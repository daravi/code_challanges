#include <stdio.h>
#include <stdlib.h>
#include <mult_by_five.c>

int main(int argc, char const *argv[])
{
	char *name = (char *) malloc(100);

	int num = mult_by_five(4);

	scanf("%s", name);

	printf("Hello %s%d!\n", name, num);
	return 0;
}