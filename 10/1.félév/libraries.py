import time

class Timer:
    def __init__(self, pStart, pEnd, totalTime):
        self.pStart = pStart
        self.pEnd = pEnd
        self.totalTime = totalTime

    def start(self):
       self.pStart = time.time()

    def stop(self):
        self.pEnd = time.time()
        self.totalTime = self.pStart - self.pEnd
        print("Ennyi idő alatt futott le: ",self.totalTime)

Timer.start()

k = 158 ** 8

Timer.stop()