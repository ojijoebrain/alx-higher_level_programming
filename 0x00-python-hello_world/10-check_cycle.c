#include "lists.h"

/**
 * check_cycle - function to check if list has a cycle
 * @list: linked list
 * Return: 1 if there is a cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
    listint_t *fast, *slow;

    if (!list || !list->next)
        return (0);

    slow = list;
    fast = list;

    while (slow != NULL && fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next;

        if (slow == fast)
        {
            return (1); 
        }
    }

    return (0); 
}
