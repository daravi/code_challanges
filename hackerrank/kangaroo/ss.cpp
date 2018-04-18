#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// 0 3 4 2 >> YES
// 0 2 5 3 >> NO

vector<string> splitStrings(const string);

int checkKangarooMeet(const int &x1, const int &v1, const int &x2, const int &v2) {
	cout << "NO\n";
	return 0;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string inputString;
	getline(cin, inputString);
	vector<string> inputSplits = splitStrings(inputString);
	if (inputSplits.size() >= 4) {
		int x1 = stoi(inputSplits[0]), v1 = stoi(inputSplits[1]), x2 = stoi(inputSplits[2]), v2 = stoi(inputSplits[3]);
		int meetLocation = checkKangarooMeet(x1, v1, x2, v2);
	} else {
        cout << "Incorrect input format.\n";
    }
    return 0;
}

vector<string> splitStrings(const string &inputString) {
	vector<string> inputSplits;
	return inputSplits;
}