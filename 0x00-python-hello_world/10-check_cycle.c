#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if a singly list has a cycle in it
 * @list: a pointer to listint_t
 *
 * Return: return 0 if there is no cycle, or 1 if there
 * is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *leo;
	listint_t *tort;

	if (list == NULL)
		return (0);
	leo = list;
	tort = list;
	while (leo != NULL && tort != NULL)
	{
		leo = leo->next;
		if (leo != NULL)
			leo = leo->next;
		if (leo == tort)
			return (1);
		tort = tort->next;
	}
	return (0);
}
