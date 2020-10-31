#include <condition_variable>
#include <iostream>
#include <mutex>
#include <thread>

using namespace std;

mutex mtx;
condition_variable cv;
bool ready = false; // 全局标志位

void printId(int id)
{
    unique_lock<mutex> lck(mtx);
    
    while (!ready) // 如果标志位不为true，则等待
    {
        cv.wait(lck); // 线程被阻塞，直到标志位变为true
    }
    cout << "thread: " << this_thread::get_id() << " id: " << id << "\n";
}

void go()
{
    unique_lock<mutex> lck(mtx);

    ready = true; // 改变全局标志位
    cv.notify_all(); // 唤醒所有线程
}

int main()
{
    thread threads[10];

    for (int i = 0; i < 10; ++i)
    {
        threads[i] = thread(printId, i);
    }
    cout << "create done.\n";

    go();

    for (auto &t : threads)
    {
        t.join();
    }
    cout << "process done.\n";
    return 0;
}