//Highest Common Factor(HCF) of two numbers
//also called as GCD
//HCF ( Highest Common Factor ) of two numbers is the 
//largest positive integer that can divide both the numbers

// APPROACH 1
// #include <iostream>
// int hcf(int a, int b) {
//     if (b == 0)
//         return a;
//     return hcf(b, a % b);
// }

// int main() {
//     int num1, num2;
//     std::cout << "Enter first number: ";
//     std::cin >> num1;
//     std::cout << "Enter second number: ";
//     std::cin >> num2;

//     int result = hcf(num1, num2);
//     std::cout << "HCF of " << num1 << " and " << num2 << " is: " << result << std::endl;

//     return 0;
// }


// APPROACH 2 BY COPILOT
#include <iostream>
using namespace std;



int main()
{
    int a,b;
    cout<<"Enter two numbers: ";
    cin>>a>>b;
    while(a!=b)
    {
        if(a>b)
        {
            a=a-b;
        }
        else
        {
            b=b-a;
        }
    }
    cout<<"HCF is: "<<a;


    return 0;
}
