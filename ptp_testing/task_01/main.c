#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

void my_clock(int N, time_t seconds, long milisecs)
{
    double total, average;
    clock_t t_beg, t_end;

    struct timespec tw = {seconds, 1000000*milisecs};
    struct timespec tr;


    for (int i = 0; i < N; i++)
    {
        t_beg = clock();
        nanosleep(&tw, &tr);
        t_end = clock();

        average += (double) (t_end - t_beg) / CLOCKS_PER_SEC;
    }

    total = average / N;

    printf("clock %ld.%ld secs - %f secs\n",seconds, milisecs, total);
}

unsigned long long milisecs_now(void)
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
        return (unsigned long long) -1;
    
    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL; 
}

void my_gettimeofday(int N, time_t seconds, long milisecs)
{
    long long unsigned begin, end;
    struct timespec tw = {seconds, 1000000*milisecs};
    struct timespec tr;
    double average, total;

    for (int i = 0; i < N; i++)
    {
        begin = milisecs_now();
        nanosleep(&tw, &tr);
        end = milisecs_now();

        average += end - begin;
    }

    total = average / N; 

    printf("gettimeofday %ld.%ld secs - %f milisecs\n",seconds, milisecs, total);
}

void my_clock_gettime(int N, time_t seconds, long milisecs)
{
    struct timespec mt1, mt2; 
    long int tt;      
    double average, total;

    struct timespec tw = {seconds, 1000000*milisecs};
    struct timespec tr;

    for (int i = 0; i < N; i++)
    {    
        clock_gettime(CLOCK_REALTIME, &mt1);
        nanosleep(&tw, &tr);
        clock_gettime(CLOCK_REALTIME, &mt2);

        tt = 1000000000*(mt2.tv_sec - mt1.tv_sec) + (mt2.tv_nsec - mt1.tv_nsec);

        average += tt;
    }

    total = average / N / 1000000;

    printf("clock_gettime %ld.%ld secs - %f milisecs\n",seconds, milisecs, total);
}


void show(int N, time_t seconds, long milisecs)
{
    my_clock(N, seconds, milisecs);
    my_clock_gettime(N, seconds, milisecs);
    my_gettimeofday(N, seconds, milisecs);
    puts("");
}

int main(void)
{
    int N;

    printf("Input N: ");
    if (scanf("%d", &N) != 1)
        return EXIT_FAILURE;

    printf("\n");
    show(N, 1, 0);
    show(N, 0, 100);
    show(N, 0, 50);
    show(N, 0, 10);

    return EXIT_SUCCESS;
}