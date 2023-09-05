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

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	current = *head;
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

