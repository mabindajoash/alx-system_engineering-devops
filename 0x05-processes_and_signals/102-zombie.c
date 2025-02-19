#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>

/**
  * infinite_while - infinite while
  * Return: 0
  */
int infinite_while(void)
{
	while (1)
	{
		sleep (1);
	}
	return (0);
}
/**
  * main - entry point for the programme
  * Return: 0
  */
int main(void)
{
	pid_t pid;
	char count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			count++;
		}
		else
			exit(0);
	}
	infinite_while();

	return (EXIT_SUCCESS);
}
