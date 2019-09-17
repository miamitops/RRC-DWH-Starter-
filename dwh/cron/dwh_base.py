from django_cron import CronJobBase, Schedule

class DailyDataImport(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'dwh.daily_import'    # a unique code

    def do(self):
        pass    # do your thing here