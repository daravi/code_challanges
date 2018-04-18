/*
    Author: Pooya Daravi
    Problem 2 of leetcode.com

    Statement:
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
*/
#include <vector>
#include <iostream>
#include <unordered_map>
#include <stdexcept>
#include <string>
#include <algorithm>

using namespace std;

// singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l1_last = l1;
        ListNode* l2_last = l2;
        string num1 = to_string(l1_last->val);
        string num2 = to_string(l2_last->val);
        while (l1_last->next != NULL) {
            l1_last = l1_last->next;
            num1 += to_string(l1_last->val);
        }
        while (l2_last->next != NULL) {
            l2_last = l2_last->next;
            num2 += to_string(l2_last->val);
        }
        reverse(num1.begin(),num1.end());
        reverse(num2.begin(),num2.end());
        string sum_ = to_string(stoi(num1) + stoi(num2));
        reverse(sum_.begin(),sum_.end());
        ListNode* sum = new ListNode((int)sum_[0] - (int)'0');
        ListNode* current = sum;
        for(char& c : sum_.substr(1, sum_.size())) {
            ListNode* next_node = new ListNode((int)c - (int)'0');
            current->next = next_node;
            current = next_node;
        }
        return sum;
    }
};


int main(int argc, char const *argv[])
{
    ListNode* l11 = new ListNode(0);
    // ListNode* l12 = new ListNode(4);
    // ListNode* l13 = new ListNode(3);
    // l11->next = l12;
    // l12->next = l13;
    ListNode* l21 = new ListNode(1);
    // ListNode* l22 = new ListNode(6);
    // ListNode* l23 = new ListNode(4);
    // l21->next = l22;
    // l22->next = l23;
    Solution sol;
    ListNode* sum = sol.addTwoNumbers(l11, l21);
    cout << sum->val << endl;
    if (sum->next == NULL) cout << "finito\n";
    // cout << sum.next->val << endl;
    // cout << sum.next->next->val << endl;
    return 0;
}