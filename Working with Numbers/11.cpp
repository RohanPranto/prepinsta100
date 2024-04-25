//cpp code for octal to binary conversion
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(){
    int n;
    cout<<"Enter an octal number: ";
    cin>>n;
    string ans ="";
    int rem;
    while(n>0){
        rem = n%10;
        switch(rem){
            case 0: ans = "000" + ans; break;
            case 1: ans = "001" + ans; break;
            case 2: ans = "010" + ans; break;
            case 3: ans = "011" + ans; break;
            case 4: ans = "100" + ans; break;
            case 5: ans = "101" + ans; break;
            case 6: ans = "110" + ans; break;
            case 7: ans = "111" + ans; break;
        }
        n/=10;
    }
    cout<<"Binary num is "<<ans;
    return 0;
}