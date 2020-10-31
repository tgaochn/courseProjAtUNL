//
//  main.cpp
//  LeetCode
//
//  Created by Hao on 2017/3/16.
//  Copyright © 2017年 Hao. All rights reserved.
//
#include <chrono>   // chrono::seconds
#include <iostream> // cout
#include <mutex>    // mutex
#include <thread>   // thread, this_thread::sleep_for

using namespace std;

mutex mtx; // mutex for critical section
int count = 0;
int num_count = 0;

void print_block_0(int n)
{
    // critical section (exclusive access to cout signaled by locking mtx):
    while (true)
    {
        if (count % 3 == 0)
        {
            mtx.lock();

            ++count;

            cout << "A" << endl;

            mtx.unlock();
        }

        if (num_count == 3)
            break;
    }
}

void print_block_1(int n)
{
    // critical section (exclusive access to cout signaled by locking mtx):
    while (true)
    {
        if (count % 3 == 1)
        {
            mtx.lock();

            ++count;

            cout << "B" << endl;

            mtx.unlock();
        }

        if (num_count == 3)
            break;
    }
}

void print_block_2(int n)
{
    // critical section (exclusive access to cout signaled by locking mtx):
    while (true)
    {
        if (count % 3 == 2)
        {
            mtx.lock();

            ++num_count; // must be executed prior to the following statement, or else an extra "A" would be printed

            ++count;

            cout << "C" << endl;

            //            this_thread::sleep_for (chrono::seconds(1)); // sleep in case that an extra "A" is printed

            mtx.unlock();
        }

        if (num_count == 3)
            break;
    }
}

int main()
{
    thread threads[3]; // default-constructed threads

    cout << "Spawning 3 threads...\n";

    threads[0] = thread(print_block_0, 10); // move-assign threads
    threads[1] = thread(print_block_1, 10); // move-assign threads
    threads[2] = thread(print_block_2, 10); // move-assign threads

    cout << "Done spawning threads. Now waiting for them to join:\n";
    for (int i = 0; i < 3; ++i)
        threads[i].join();

    cout << "All threads joined!\n";

    return 0;
}