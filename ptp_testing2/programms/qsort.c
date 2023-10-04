#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <string.h>

#ifndef NMAX
#error "Init NMAX by flag -DNMAX N"
#endif

int comparator(const void *elem1, const void *elem2)
{
    int num1 = *((int *) elem1);
    int num2 = *((int *) elem2);

    return num1 - num2;
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
    qsort(array, NMAX, sizeof(int), comparator);
    t_end = milisecs_now();

    printf("%lld\n", t_end - t_beg);

    return EXIT_SUCCESS;
}