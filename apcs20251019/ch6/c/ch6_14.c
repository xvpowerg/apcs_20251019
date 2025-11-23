/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

void test(){
    printf("Hello!\n");
    
}

void test2(int v1,int v2){
    int ans = v1 + v2;
    printf("ans:%d\n",ans);
}

int test3(int v1,int v2){
    int c  = v1 * v2;
    return c;
}

int main()
{  
   test();
   test();
   test2(10,20);
   int result = test3(2,5);
   printf("result:%d",result);
    return 0;
}