//Binary to Octal Conversion

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(){
    string n;
    cout<<"Enter a binary number: ";
    cin>>n;
    string ans ="";
    int dec = 0;

    //Converting binary to decimal
    for(int i=0; i<n.length(); i++){
        dec += (n[i]-'0')*pow(2,n.length()-1-i);
    }

    //Converting decimal to octal
    while(dec>0){
        ans = to_string(dec%8) + ans;
        dec/=8;
    }

    cout<<"Octal num is "<<ans;
    return 0;
}