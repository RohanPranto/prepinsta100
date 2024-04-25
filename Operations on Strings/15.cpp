#include <iostream>
using namespace std;

int main() {
    // Initializing variables.
    string str;
    char letter;
    int frequency = 0;

    // Taking input sentence and the letter to count its frequency.
    cout << "Enter a string: ";
    getline(cin, str);
    cout << "Enter a letter: ";
    cin >> letter;

    // Calculating frequency of the given letter in the sentence.
    for (char ch : str) {
        if (ch == letter || ch == toupper(letter) || ch == tolower(letter)) {
            frequency++;
        }
    }

    // Printing frequency of the given letter.
    cout << "Frequency of letter '" << letter << "' in the sentence: " << frequency << endl;

    return 0;
}
