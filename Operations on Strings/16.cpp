//Find non-repeating characters in a string

#include <iostream>
#include <string>

using namespace std;
int main()
{
    //Initializing variables.
    string str;
    cout<<"Enter a string: ";
    getline(cin, str);
    int i;
    int freq[256] = {0};
    
    //Calculating frequency of each character.
    for(i = 0; str[i] != '\0'; i++) 
    {
        freq[str[i]]++;
    }
    cout<<"The non repeating characters are: ";
    for(i = 0; i < 256; i++)
    {
        if(freq[i] == 1)//Finding non repeating charcters and printing them.
        {
           cout<<char(i)<<"  " ;
        }
    }
    return 0;
}