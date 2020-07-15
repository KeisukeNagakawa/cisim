from unittest import TestCase
from cisim.stats import BinomCI


class Testbinom(TestCase):
    def test_ci_sim(self):
        b = BinomCI(n_a=100, n_x=10, cl=0.05)
        res = b.ci_sim()
        self.assertEqual([0.04900327615818594, 0.17622100352052053], [res[0].x, res[1].x])
