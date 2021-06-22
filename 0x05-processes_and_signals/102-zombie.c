#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void);

int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 1; i <= 5; i++)
    {
        child_pid = fork();
        if (child_pid == -1)
        {
            perror("Fork failed");
            return (0);
        }
        if (child_pid == 0)
        {
            pause();
        }
        else
        {
            printf("Zombie process created, PID: %d\n", child_pid);
        }
    }
    infinite_while();
	return (1);
}

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
