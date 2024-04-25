//PAIR ELEMENT
// A PAIR Element is an element if there exists at least one element whose difference is less than K where K would be the given integer. This means that an element X is PAIR if there is another element in the range [X-K, X+K] other than X itself.

// Input Format

// The first line of the input will contain two integers: N and K, where N is the size of the array A [] and K is an int number as mentioned above. The second line of input contains N integers separated by space.

// Constraints

// 0 <= A[i] <= 10^9 0 <= K <= 10^5 1 <= N <= 10^5

// Output Format

// Print an integer indicating the number of PAIR elements in total.

// Sample Input 
// 6 3 
// 6 5 7 9 15 2

// Sample Output 
// 5

// Sample Input 
// 3 2 
// 1 3 4
// Sample Output 
// 3