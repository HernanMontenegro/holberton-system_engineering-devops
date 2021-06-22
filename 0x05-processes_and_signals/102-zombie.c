#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - create 5 zombie processes
 * ---------------------------------
 * Return: 0 if worked, 1 if not
*/
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 1; i <= 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();

	return (0);
}

/**
 * infinite_while - an infinite loop given by holberton
 * -----------------------------------
 * Return: 0 because yes
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
