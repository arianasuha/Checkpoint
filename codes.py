from datetime import datetime

class Commit:
    def __init__(self,commit_id, message):
        self.commit_id = self.hash_commit_id(commit_id)
        self.timestamp = datetime.now()
        self.message = str(message)

    @staticmethod
    def hash_commit_id(commit_id):
        pass


class Repository:
    def __init__(self, repo_name):
        self.reponame = name
