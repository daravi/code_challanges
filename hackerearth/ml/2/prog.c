#include "stdio.h"
#include <math.h>

float recursive(double p, double old_sum) {
	double new_sum = p * old_sum + 1;
	if (new_sum == old_sum) {
		return new_sum;
	}
	else {
		return recursive(p, new_sum);
	}
}

int main(int argc, char const *argv[])
{
	double p = 0;
	scanf("%lf", &p);

	double p_1 = recursive(p, 1);
	// double p_ = 1 + (1-p)/p;
	// double p_ = 1.0 / p;
	double p_2 =  p /pow((1-p),2.0);

	printf("%.6f\n%.6f\n", p_1, p_2);

	return 0;
}

// This an embarrassingly poor wording for such an elementary problem. I am not sure if I want to spend my time with this website if they don't understand such elementary concepts like random events. What does it mean that"the  probability of Alice dropping the phone is p"??... Are we talking about a single event in her entire life? Or the event happens per a certain time interval (e.g. daily)? In the first case the expected value is obviously 0.5 and the second case it's 0.5 * the number of time intervals. However I think this is what the problem should have said:
// The probability that the 