# Tutorial
- https://www.youtube.com/watch?v=XSeox_9pRVA
## The most basic usage of APScheduler: **"Start the job after a few seconds."**

##  basic timing scheduling
- APScheduler is a timed task scheduling framework for Python.
- It provides similar task scheduling based on fixed time intervals, dates, and crontab configurations, and can persist tasks or run tasks in daemon mode.

- Here is a basic example of use:
- It can run job() every 3s, so the program outputs 'job 3s' every 3s. By modifying the parameter seconds of add_job(), you can change the interval of task scheduling.

```py
from apscheduler.schedulers.blocking import BlockingScheduler
 
def job():
    print('job 3s')
 
if __name__=='__main__':
    sched = BlockingScheduler(timezone='MST')
    sched.add_job(job, 'interval', id='3_second_job', seconds=3)
    sched.start()

```

## 2, the difference between BlockingScheduler and BackgroundScheduler

- the main difference is that BlockingScheduler will block the running of the main thread, and BackgroundScheduler will not block. 
- BlockingScheduler: Blocks the current thread after calling the start function. Use when the scheduler is the only thing in your application that you want to run (as in the example above).
- BackgroundScheduler: The main thread does not block after calling start. Use it when you are not running any other frameworks and want the scheduler to execute in the background of your app.

- BlockingScheduler example
- It can be seen that BlockingScheduler will block the current thread after calling the start function, and the while loop in the main program will not be executed.
```py
from apscheduler.schedulers.blocking import BlockingScheduler
import time
 
def job():
    print('job 3s')
 
 
if __name__=='__main__':
 
    sched = BlockingScheduler(timezone='MST')
    sched.add_job(job, 'interval', id='3_second_job', seconds=3)
    sched.start()
 
    While(True): # will not be executed to
        print('main 1s')
        time.sleep(1)

# Output:
job 3s
job 3s
job 3s
job 3s

```

- BackgroundScheduler example
- It can be seen that the BackgroundScheduler does not block the current thread after calling the start function, so it can continue to execute the logic of the while loop in the main program.
- Through this output, we can also find that after calling the start function, job() does not start executing immediately. Instead, it will be scheduled to execute after waiting for 3s.

```py
from apscheduler.schedulers.background import BackgroundScheduler
import time
 
def job():
    print('job 3s')
 
 
if __name__=='__main__':
 
    sched = BackgroundScheduler(timezone='MST')
    sched.add_job(job, 'interval', id='3_second_job', seconds=3)
    sched.start()
 
    while(True):
        print('main 1s')
        time.sleep(1)
# Output:
main 1s
main 1s
main 1s
job 3s
main 1s
main 1s
main 1s
job 3s

```

# More https://www.programmersought.com/article/50481656139/

# Stop job
- https://stackoverflow.com/questions/33036321/python-apscheduler-not-stopping-a-job-even-after-using-remove-job
```py
from apscheduler.schedulers.background import BlockingScheduler

count = 0

def job_function():
    print "job executing"
    global count, scheduler

    # Execute the job till the count of 5 
    count = count + 1
    if count == 5:
        scheduler.remove_job('my_job_id')


scheduler = BlockingScheduler()
scheduler.add_job(job_function, 'interval', seconds=1, id='my_job_id')


scheduler.start()

```




