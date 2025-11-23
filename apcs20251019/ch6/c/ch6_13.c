/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{  
    int number[5] = {10,11,21,31,41};
    printf("%d\n",number[2]);
    int i = 0;
    for (i=0;i<5;i++){
        printf("%d\n",number[i]);
    }   
 
    return 0;
}