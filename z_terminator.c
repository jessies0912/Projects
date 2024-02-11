/******************************************************************************
Jasmeet Salh
190770960
z_terminator.c
*******************************************************************************/
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    //command
	system("./z_creator &"); 
	system("ps -l"); 
	
	sleep(7);
	//command
	system("kill -9 $(ps -l|grep -w Z|tr -s ''|cut -d '' -f 5)"); 
	
	sleep(10); // to kill parent
	
	printf("\nThe updated list of processes and their status is: \n"); 
	//command
	system("ps -l"); 
	return 0;
}