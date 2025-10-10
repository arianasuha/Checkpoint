from datetime import datetime

class Commit:
    def __init__(self, message, snapshot = {}):
        self.timestamp = datetime.now()
        self.message = str(message)
        self.snapshot = snapshot

    def __rep__(self):
        print()


class Repository:
    def __init__(self):
        self.commits = []


    def add_commit(self):
        pass


r1 = Repository()

