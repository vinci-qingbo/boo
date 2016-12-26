from time import sleep


class Ai():
    def __init__(self):
        self.count = 1
        self.ad()

    def ad(self):
        while self.count<600:
            print self.count
            sleep(1)
            self.count += 1


if __name__ == '__main__':
    s = Ai()
