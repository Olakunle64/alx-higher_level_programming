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

	if (head == NULL || *head == NULL)
		return (NULL);
	prevnode = NULL;
	current = *head;
	nextnode = *head;
	if (current->next == NULL)
		return (*head);
	while (nextnode != NULL)
	{
		nextnode = nextnode->next;
		current->next = prevnode;
		prevnode = current;
		current = nextnode;
	}
	nextnode = prevnode;
	return (nextnode);
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
	listint_t *current, *replicate_node;

	if (head == NULL || *head == NULL)
		return (1);
	current = *head;
	if (current->next == NULL)
		return (1);
	replicate_node = reverse_listint(head);
	while (current != NULL)
	{
		if (current->n != replicate_node->n)
			return (0);
		current = current->next;
	}
	return (1);
}

