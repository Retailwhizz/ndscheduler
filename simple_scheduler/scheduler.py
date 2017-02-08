"""Run the scheduler process."""
from mdmscheduler.server import server


class SimpleServer(server.SchedulerServer):

    def post_scheduler_start(self):
        # New user experience! Make sure we have at least 1 job to demo!
        pass

if __name__ == "__main__":
    SimpleServer.run()
