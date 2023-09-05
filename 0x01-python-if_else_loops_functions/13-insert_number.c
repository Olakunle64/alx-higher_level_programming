#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a number into a sorted singly
 * linked list.
 * @head: pointer to the first node
 * @number: number to insert
 *
 * Return: return the address of the new node or NULL
 * if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current, *temp;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (head == NULL || *head == NULL)
	{
		*head = newnode;
		return (newnode);
	}
	current = *head;
	if (current->next == NULL)
	{
		if (current->n > number)
		{
			newnode->next = current;
			current = newnode;
			return (newnode);
		}
		current->next = newnode;
		return (newnode);
	}
	while (current != NULL)
	{
		if (current->n > number)
		{
			break;
		}
		temp = current;
		current = current->next;
	}
	newnode->next = current;
	temp->next = newnode;
	return (newnode);
}

