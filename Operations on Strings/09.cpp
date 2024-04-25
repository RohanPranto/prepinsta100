// Print the given string in reverse order.

#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    cin>>s;
    for(int i=s.length()-1;i>=0;i--){
        cout<<s[i];
    }
    cout<<endl;
}


//explanation
//in 11th line, we are starting from the end. So, we are using "int i=s.length()-1;i>=0;i--".

//in normal case, we use "int i=0;i<s.length();i++" to start from the beginning.

//here we are starting from the end. So, we are using "int i=s.length()-1;i>=0;i--". and then replacing with s[i] which is he first character.

//so its reversed