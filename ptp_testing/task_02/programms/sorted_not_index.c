#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

#ifndef NMAX
#error "Init NMAX by flag -DNMAX N"
#endif

// Функция пузырьковой сортировки
void bubble_sort(int arr[], size_t length)
{
    int temp;
    for (size_t i = 0; i < length; i++)
    {
        for (size_t j = 0; j < length - 1; j++)
        {
            if (*(arr + j) > *(arr + j + 1))
            {
                temp = *(arr + j);
                *(arr + j) = *(arr + j + 1);
                *(arr + j + 1) = temp;
            }
        }
    }
}

unsigned long long milisecs_now(void)
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
        return (unsigned long long) -1;
    
    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL; 
}

void init_sorted_arr(int arr[], int len)
{
    for (size_t i = 0; i < len; i++)
    {
        arr[i] = i;        
    }    
}


int main(void)
{
    int arr[NMAX];
    unsigned long long t_beg, t_end;

    init_sorted_arr(arr, NMAX);

    t_beg = milisecs_now();
    bubble_sort(arr, NMAX);
    t_end = milisecs_now();

    arr[0] = arr[1];
    arr[1] = 1;

    printf("%lld\n", t_end - t_beg);

    return EXIT_SUCCESS;
}