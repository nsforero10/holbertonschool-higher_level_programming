#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *current = *head;

	if (!new)
		return (NULL);

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		new->n = number;
		*head = new;
		return (new);
	}

	while (current->next)
	{
		if (current->next->n >= number)
		{
			new->next = current->next;
			current->next = new;
			new->n = number;
			return (new);
		}
		current = current->next;
	}

	current->next = new;
	new->n = number;
	new->next = NULL;
	return (new);
}
