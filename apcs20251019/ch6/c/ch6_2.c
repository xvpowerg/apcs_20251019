/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int input1;
    float input2;
    char input3[10];
    printf("請輸入整數");
    scanf("%d",&input1);
    printf("%d\n",input1);
    printf("請輸入浮點數:");
    scanf("%f",&input2);
    printf("浮點數是:%.2f\n",input2);
    printf("請輸入文字:");
    scanf("%10s",&input3);
    printf("輸入的文字是:%s",input3);
    return 0;
}