#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// 0 3 4 2 >> YES
// 0 2 5 3 >> NO

vector<string> splitStrings(string);

int checkKangarooMeet(const int &x1, const int &v1, const int &x2, const int &v2) {
    if (x1 == x2) {
        cout << "YES\n";
        return 0;
    } else if (((x1 > x2) and (v1 < v2)) or ((x1 < x2) and (v1 > v2))) {
        if (abs(x1 - x2) % abs(v1 - v2) == 0) {
            cout << "YES\n";
            return abs(x1 - x2) / abs(v1 - v2);
        }
    }
	cout << "NO\n";
	return -1;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string inputString;
	getline(cin, inputString);
	vector<string> inputSplits = splitStrings(inputString);
	if (inputSplits.size() >= 4) {
		int x1 = stoi(inputSplits[0]), v1 = stoi(inputSplits[1]), x2 = stoi(inputSplits[2]), v2 = stoi(inputSplits[3]);
		checkKangarooMeet(x1, v1, x2, v2);
	} else {
        cout << "Incorrect input format.\n";
    }
    return 0;
}

vector<string> splitStrings(string inputString) {
	vector<string> inputSplits;
    string::iterator new_end = unique(inputString.begin(), inputString.end(), 
        [] (const char &x, const char &y) {
            return x == ' ' and y == ' ';
        });
    inputString.erase(new_end, inputString.end());
    if (inputString[inputString.size() - 1] == ' ') inputString.pop_back();
    if (inputString[0] == ' ') inputString = inputString.substr(1, inputString.size() - 1);
    const char delimiter = ' ';
    int pos = 0, next_pos = 0;
    while ((next_pos=inputString.find(delimiter, pos)) != string::npos) {
        inputSplits.push_back(inputString.substr(pos, next_pos - pos));
        pos = next_pos + 1;
    }
    // Add the final element
    inputSplits.push_back(inputString.substr(pos, inputString.size() - pos));
	return inputSplits;
}













