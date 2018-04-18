/*
    Author: Pooya Daravi
    Problem 1 of leetcode.com

    Statement:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
*/
#include <vector>
#include <iostream>
#include <unordered_map>
#include <stdexcept>

using namespace std;

class Solution {
public:
    // // Brute force:
    // vector<int> twoSum(vector<int>& nums, int target) {
    //     vector<int> indices_vector;
    //     int size = nums.size();
    //     for (int i = 0; i < size; ++i)
    //     {
    //         for (int j = i + 1; j < size; ++j)
    //         {
    //             if (nums[i] + nums[j] == target)
    //             {
    //                 indices_vector.push_back (i);
    //                 indices_vector.push_back (j);
    //                 return indices_vector;
    //             }
    //         }
    //     }
    //     return indices_vector;
    // }
    
    // // Two-pass hash table
    // vector<int> twoSum(vector<int> nums, int target) {
    //     unordered_map<int, int> map;
    //     for (int i = 0; i < nums.size(); i++) {
    //         map.emplace(nums[i], i);
    //     }
    //     for (int i = 0; i < nums.size(); i++) {
    //         int complement = target - nums[i];
    //         if (map.count(complement) > 0 && map[complement] != i) {
    //             return vector<int> { i, map[complement] };
    //         }
    //     }
    //     throw invalid_argument("No two sum solution");
    // }

    // One-pass hash table
    vector<int> twoSum(vector<int> nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.count(complement) > 0) {
                return vector<int> { map[complement], i };
            }
            map.emplace(nums[i], i);
        }
        throw invalid_argument("No two sum solution");
    }

};


int main(int argc, char const *argv[])
{
    vector<int> nums = {1, 7, 11, 8};
    Solution sol;
    vector<int> ivec = sol.twoSum(nums, 9);
    cout << ivec[0] << ivec[1] << endl;
    return 0;
}