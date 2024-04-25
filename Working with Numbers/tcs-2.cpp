//CANDIES IN A BOX
// Krishna loves candies a lot, so whenever he gets them, he stores them so that he can eat them later whenever he wants to. He has recently received N boxes of candies each containing Ci candies where Ci represents the total number of candies in the ith box. Krishna wants to store them in a single box. The only constraint is that he can choose any two boxes and store their joint contents in an empty box only. Assume that there are an infinite number of empty boxes available. At a time he can pick up any two boxes for transferring and if both the boxes contain X and Y number of candies respectively, then it takes him exactly X+Y seconds of time. As he is too eager to collect all of them he has approached you to tell him the minimum time in which all the candies can be collected.

// Input Format

// 1) The first line of input is the number of test case T
// 2) Each test case is comprised of two inputs
// 3) The first input of a test case is the number of boxes N
// 4) The second input is N integers delimited by whitespace denoting the number of candies in each box

// Output Format

// Print the minimum time required, in seconds, for each of the test cases. Print each output on a new line.

// Sample Input 
// 1
// 4
// 1 2 3 4
// Sample Output 
// 19

// Give me cpp code


#include <iostream>
#include <queue>
using namespace std;

int main() {
    int T;
    cin >> T; // number of test cases
    
    while (T--) {
        int N;
        cin >> N; // number of boxes

        priority_queue<int, vector<int>, greater<int>> pq; // min heap to store candies
        
        // input candies into priority queue
        for (int i = 0; i < N; ++i) {
            int candies;
            cin >> candies;
            pq.push(candies);
        }
        
        long long total_time = 0;
        
        // merge boxes until only one box remains
        while (pq.size() > 1) {
            int x = pq.top();
            pq.pop();
            int y = pq.top();
            pq.pop();
            
            int sum = x + y;
            total_time += sum;
            pq.push(sum); // store merged candies back into the queue
        }
        
        cout << total_time << endl; // output minimum time required
    }
    
    return 0;
}
