from taxman.primes import divisors

class Taxman():
    def __init__(self):
        self.n = 1
        self.b = [2, 2]
        self.tScore = 0
        self.pScore = 0
        self.picks = []

    def init(self, n):
        self.picks = []
        self.n = n
        self.b = []
        for i in range(0, n + 1):
            self.b.append(2)
        self.tScore = 0
        self.pScore = 0

    def pick(self, k):
        if self.b[k] == 2:
            self.picks.append(k)
            self.b[k] = 0
            self.pScore += k
            for d in divisors(k):
                if self.b[d] == 2:
                    self.tScore += d
                self.b[d] = 0
            for i in range(0, self.n + 1):
                if self.b[i] == 2 and self.validate(i) == False:
                    self.b[i] = 1
                    self.tScore += i
            return True
        return False

    def pick_mult(self, ks):
        for k in ks:
            self.pick(k)

    
    def evaluate(self, k):
        t = Taxman()
        t.copy(self)
        score = -t.score()
        t.pick(k)
        score += t.score()
        return score

    def available(self):
        availability = []
        for i in range(0, self.n + 1):
            if self.b[i] == 2:
                availability.append(i)
        return availability

    def evaluateAll(self):
        evaluation = []
        for i in self.available():
            evaluation.append([self.evaluate(i), i])
        evaluation.sort()
        return evaluation
            
    def validate(self, k):
        if len(divisors(k)) == 0:
            return False
        for d in divisors(k):
            if self.b[d] != 0:
                return True
        return False

    def ended(self):
        return self.evaluateAll() == []

    def score(self):
        return self.pScore - self.tScore

    def copy(self, t):
        self.n = t.n
        self.b = list(t.b)
        self.tScore = t.tScore
        self.pScore = t.pScore
        self.picks = list(t.picks)
    