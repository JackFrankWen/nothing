from GR86.chassis.taskcenter.tushare_task import TushareTask
import queue
q1 = queue.Queue()


class FinialStatementTask(TushareTask):
    def __init__(self):
        super().__init__()

    def init_queue(self):
        pass
