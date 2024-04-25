// Convert digit/number to words.

#include <iostream>
#include <string>
#include <vector>
using namespace std;

string convertToWords(int n) {
    vector<string> ones = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    vector<string> tens = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    vector<string> teens = {"", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};

    string result = "";
    int num = n;
    if (num >= 100) {
        result += ones[num / 100] + " Hundred ";
        num %= 100;
    }
    if (num >= 20) {
        result += tens[num / 10] + " ";
        num %= 10;
    }
    if (num >= 11) {
        result += teens[num - 10] + " ";
        num = 0;
    }
    if (num >= 1) {
        result += ones[num] + " ";
    }
    return result;
}