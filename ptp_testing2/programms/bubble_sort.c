#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include "string.h"

#ifndef NMAX
#error "Init NMAX by flag -DNMAX N"
#endif

// Функция сортировки пузырьком
int comparator(const void *elem1, const void *elem2)
{
    int num1 = *((int *) elem1);
    int num2 = *((int *) elem2);

    return num1 - num2;
}

void swap(void *left, void *right, size_t size, char *buffer)
{
    memcpy(&buffer, left, size);
    memcpy(left, right, size);
    memcpy(right, &buffer, size);
}

void bubble_sort(void *first, size_t len, size_t size, int (*comparator)(const void *, const void *))
{
    int flag = 1;

    char *left = (char *)first;
    char *right = (char *)first;
    right += size * len - size;
    char buffer[100];

    while ((left < right) && flag)
    {
        flag = 0;

        for (char *i = left; i < right; i += size)
        {
            char *j = i + size;
            if (comparator((const void *)i, (const void *)j) > 0)
            {
                swap(i, j, size, buffer);
                flag = 1;
            }
        }

        right -= size;
        for (char *i = right; i > left; i -= size)
        {
            char *j = i - size;
            if (comparator((const void *)j, (const void *)i) > 0)
            {
                swap(j, i, size, buffer);
                flag = 1;
            }
        }

        left += size;
    }
}

unsigned long long milisecs_now(void)
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
        return (unsigned long long) -1;
    
    return val.tv_sec * 1000000000 + val.tv_usec * 1000; 
}

void init_array(int arr[NMAX], int size)
{
    for (size_t i = 0; i < size; i++)
    {
        arr[i] = i;
    }    
}

int main(void)
{
    int array[NMAX];
    unsigned long long t_beg, t_end;

    init_array(array, NMAX);

    t_beg = milisecs_now();
    bubble_sort(array, NMAX, sizeof(int), comparator);
    t_end = milisecs_now();

    printf("%lld\n", t_end - t_beg);

    return EXIT_SUCCESS;
}