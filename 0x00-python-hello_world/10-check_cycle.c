#include "lists.h"

/**
 * check_cycle - search a cicle
 * @list: head of a linked list
 * Return: 1 if a cicle, 0 otherwiese
 */

int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *b = list;

	if (!list || !list->next)
		return (0);

	b = b->next;
	f = f->next->next;

	while (f && b && f->next)
	{
		if (b == f)
			return (1);
		b = b->next;
		f = f->next->next;
	}
	return (0);
}
