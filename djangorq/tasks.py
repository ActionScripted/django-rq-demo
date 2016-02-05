from django_rq import job, get_scheduler
from django.utils import timezone

# http://stackoverflow.com/questions/17537771/where-do-i-register-an-rq-scheduler-job-in-a-django-app

scheduler = get_scheduler()


@job
def debug_task():
    return 'Debug task'


@job
def debug_scheduled_task():
    raise ValueError('Hey man, shit broke')
    return 'Scheduled task'


# Delete any existing jobs in the scheduler when the app starts up
'''
for job in scheduler.get_jobs():
    job.delete()
'''


debug_task.delay()
scheduler.schedule(timezone.now(), 'debug_scheduled_task', interval=20)
