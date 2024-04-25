//cpp code to remove all characters from string except alphabets

#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    cout<<"Enter a string: ";
    cin>>s;
    string ans="";
    for(int i=0;i<s.length();i++){
        if((s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z')){
            ans+=s[i];
        }
    }
    cout<<ans<<endl;
}