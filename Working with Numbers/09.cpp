// cpp code to convert decimal to hexadecimal

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout<<"Enter a decimal number: ";
    cin>>n;
    string ans ="";

    while(n>0){
        int rem = n%16;
        if(rem<10){
            ans = to_string(rem) + ans;
        }else{
            ans = char(rem-10+'A') + ans;
        }
        n/=16;
    }

    cout<<"Hexadecimal num is "<<ans;
    return 0;
}