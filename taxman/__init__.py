from taxman.taxman import Taxman
from taxman.emulators import Greedy, Brute

t = Taxman()
t.init(10)
g = Greedy()
b = Brute()