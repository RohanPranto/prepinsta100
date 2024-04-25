#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(){
    int n;
    cout<<"Enter a decimal number: ";
    cin>>n;
    string ans ="";

    while(n>0){
        ans = to_string(n%8) + ans;
        n/=8;
    }

    cout<<"Octal num is "<<ans;
    return 0;
}