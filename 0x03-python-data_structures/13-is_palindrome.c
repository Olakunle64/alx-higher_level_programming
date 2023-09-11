#include "lists.h"

/**
 * reverse_listint - reverse a listint_t linked list
 * @head: double pointer to the first node
 *
 * Return: return a pointer to the first node
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prevnode, *current, *nextnode;
	prevnode = NULL;
	current = *head;
	nextnode = *head;
	while (nextnode != NULL)
	{
		nextnode = nextnode->next;
		current->next = prevnode;
		prevnode = current;
		current = nextnode;
	}
	*head = prevnode;
	return (*head);
}	
	
/**
 * is_palindrome - a function that check if a list is
 * a palindrome
 * @head: a pointer to a pointer to a node
 *
 * Return: 1 if is palindrome or 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int arr[3000];
	int i = 0;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	if (current->next == NULL)
		return (1);
	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	i = 0;
	*head = reverse_listint(head);
	current = *head;
	while (current != NULL)
	{
		if (current->n != arr[i])
		{
			return (0);
		}
		current = current->next;
		i++;
	}
	return (1);
}
