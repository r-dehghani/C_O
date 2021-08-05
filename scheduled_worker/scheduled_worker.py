import time
import schedule

def job():
    pass

schedule.every().day.at("15:00").do(job())

while True:
    schedule.run_pending()
    time.sleep()