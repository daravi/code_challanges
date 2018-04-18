// #include <bits/stdc++.h>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

vector<string> split_string(string);

int j = 0;

int gcd(const int &a, const int &b) {
    cout << "gcd_" << j << " a >> " << a << "--- b >> " << b << endl;
    if (a == 0)
        return b;
    cout << "gcd_" << j << endl;
    j++;
    return gcd(b % a, a);
}

int lcm(const vector<int> &x) {
    int result = x[0];
    int _gcd = 0;
    for (int i = 1; i < x.size(); ++i) {
        _gcd = gcd(x[i], result);
        result = (_gcd == 0 ? 1 : x[i] * result / _gcd);
    }
    cout << "lcm_" << j << endl;
    j++;
    return result;
}

/*
 * Complete the getTotalX function below.
 */
int getTotalX(vector<int> a, vector<int> b) {
    /*
     * Write your code here.
     */
    int total = 0;
    int a_lcm = lcm(a);
    int b_min = 100;
    for (int i = 0; i < b.size(); ++i) {
        if (b[i] < b_min) b_min = b[i];
    }
    int x = a_lcm, c = 1;
    bool is_factor;
    while (x <= b_min) {
        is_factor = true;
        for (int i = 0; i < b.size(); ++i) {
            cout << "b[" << i << "] = " << b[i] << " and x = " << x << endl;
            if (b[i] % x != 0) {
                is_factor = false;
                break;
            }
        }
        if (is_factor) {
            cout << "here\n";
            total++;
        }
        c++;
        x = c * a_lcm;
    }
    return total;
}

int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));

    string nm_temp;
    getline(cin, nm_temp);

    vector<string> nm = split_string(nm_temp);

    int n = stoi(nm[0]);

    int m = stoi(nm[1]);

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split_string(a_temp_temp);

    vector<int> a(n);

    for (int a_itr = 0; a_itr < n; a_itr++) {
        int a_item = stoi(a_temp[a_itr]);

        a[a_itr] = a_item;
    }

    string b_temp_temp;
    getline(cin, b_temp_temp);

    vector<string> b_temp = split_string(b_temp_temp);

    vector<int> b(m);

    for (int b_itr = 0; b_itr < m; b_itr++) {
        int b_item = stoi(b_temp[b_itr]);

        b[b_itr] = b_item;
    }

    int total = getTotalX(a, b);

    // fout << total << "\n";
    cout << total << "\n";

    // fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}

