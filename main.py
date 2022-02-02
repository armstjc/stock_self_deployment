import time
import threading
import schedule
from datetime import date
from git import Repo
#import queue
from congress import congress
from getInstitutionalHolders import getInstitutionalHolders
from getMajorHolders import getMajorHolders
from getStockFinancials import getStockFinancials
from getStockHistory import getStockHistory
from getStockOptions import getStockOptions
from getStockRecommendations import getStockRecommendations

today = date.today()

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def job1():
    print("Starting job 1")
    congress()
    getInstitutionalHolders()


def job2():
    print("Starting job 2")
    getMajorHolders()

def job3():
    print("Starting job 3")
    getStockFinancials()

def job4():
    print("Starting job 4")
    getStockHistory()

def job5():
    print("Starting job 5")
    getStockOptions()

def job6():
    print("Starting job 6")
    getStockRecommendations()

def git_push():
    PATH_OF_GIT_REPO = '/Users/josepharmstrong/Documents/GitHub/stock_self_deployment/.git'
    today = date.today()
    d_today = today.strftime("%b-%d-%Y")
    d_today = d_today + " update"
    try:
        print('starting commit')
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(d_today)
        origin = repo.remote(name='origin')
        origin.push()
        print('commit finished')
    except:
        print('An error occurred')

# def worker_main():
#     while 1:
#         job_func = jobqueue.get()
#         job_func()
#         jobqueue.task_done()


schedule.every().day.at("19:00").do(run_threaded, job1)
schedule.every().day.at("19:01").do(run_threaded, job2)
schedule.every().day.at("19:02").do(run_threaded, job3)
schedule.every().day.at("19:03").do(run_threaded, job4)
schedule.every().day.at("19:04").do(run_threaded, job5)
schedule.every().day.at("19:05").do(run_threaded, job6)
#schedule.every().day.at("14:23").do(run_threaded, git_push)

while 1:
    schedule.run_pending()
    time.sleep(1)