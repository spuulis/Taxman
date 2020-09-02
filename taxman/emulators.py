from taxman.taxman import Taxman

class Greedy():
    def __init__(self):
        self.t = Taxman()
        self.picks = []
        self.res = []
    
    def init(self, n):
        self.t.init(n)
        self.picks = []

    def step(self):
        if self.t.ended() == False:
            pick = self.t.evaluateAll()[-1][1]
            self.picks.append(pick)
            self.t.pick(pick)
            return True
        return False

    def finish(self):
        while self.step() == True:
            pass

    def score(self):
        return self.t.score()

    def finish_range(self, min, max):
        r = []
        for n in range(min, max):
            self.init(n)
            self.finish()
            r.append([n, self.score()])
        self.res = r
        return self.res

    def print_res(self):
        for r in self.res:
            print(f'{r[0]}, {r[1]}')


class Brute():
    def __init__(self):
        self.top_score = 0
        self.picks = []
        self.example = []

    def recursion(self, t):
        if len(t.available()) == 0:
            return {"score": t.score(), "picks": [t.picks]}
        res = []
        for k in t.available():
            t2 = Taxman()
            t2.copy(t)
            t2.pick(k)
            res.append(self.recursion(t2))
        top = []
        top_s = 0
        for i in res:
            if i["score"] > top_s:
                top_s = i["score"]
                top = [i]
            elif i["score"] == top_s:
                top.append(i)
        res_picks = []
        for i in top:
            res_picks += i["picks"]
        return {"score": top_s, "picks": res_picks}

    def brute(self, n):
        t = Taxman()
        t.init(n)
        res = self.recursion(t)
        self.top_score = res["score"]
        self.picks = res["picks"]
        self.example = self.picks[0]
        return self.top_score

    def brute_range(self, min, max):
        for n in range(min, max):
            print(f"{n}, {self.brute(n)}")