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
	listint_t *current;

	if (list == NULL)
		return (0);
	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
