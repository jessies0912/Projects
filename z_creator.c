/******************************************************************************
Jasmeet Salh
190770960
z_creator.c
*******************************************************************************/
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main() 
{
    int cpid = fork();
    
    if (cpid == 0) 
    {
        printf("The child PID: %d\n ",getpid()); 
	    exit(0);
    } 
    
    if (cpid > 0) 
    { 
        //retrieves the parent's PID
        printf("The parent PID: %d\n ",getpid()); 
        sleep(7);
    }
    
    else 
    { 
        exit(1);
    }
    return 0;
}