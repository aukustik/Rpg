class Achievment:
    def notify(self):
        raise NotImplementedError

class FirstKill(Achievment):
    def notify(self):
        print('YOU KILLED FIRST ENEMY, CONGRATULATIONS!')