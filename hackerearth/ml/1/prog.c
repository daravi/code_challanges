/*
// Sample code to perform I/O:
#include <stdio.h>

int main(){
	int num;
	scanf("%s", &num);              			// Reading input from STDIN
	printf("Input number is %d.\n", num);       // Writing output to STDOUT
}

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here

#include "stdio.h"

int main(int argc, char const *argv[])
{
	float ppb = 0;
	float pab = 0;
	float p1 = 0;
	// printf("Please enter the probability that Puya takes the bus: ");  
	scanf("%f", &ppb);
	// printf("Please enter the probability that Alice takes the bus: "); 
	scanf("%f", &pab);
	// printf("Please enter the probability that it rains: ");            
	scanf("%f", &p1);

	float prs = p1 * (1 - ppb * pab - (1 - ppb) * (1 - pab));

	// printf("The probability of a romantic encounter is: %f\n", prs);
	printf("%f\n", prs);
	return 0;
}