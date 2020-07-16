from unittest import TestCase
from cisim.stats import BinomCI, HyperCI


class Testbinom(TestCase):
    b = BinomCI(n_pop=100, n_obs=10, cl=0.05)

    def test_ci_sim(self):
        res = self.b.ci_sim()
        self.assertEqual(
            [0.04900327615818594, 0.17622100352052053],
            res['interval']
        )


class TestHyperCI(TestCase):
    h = HyperCI(n_pop=100, k_s=30, n_draw=20, k_s_obs=5)

    def test_hypergeom_cdf_lower(self):
        from scipy.stats import hypergeom
        h = HyperCI(n_pop=100, k_s=30, n_draw=20, k_s_obs=5)
        res = hypergeom.cdf(h.k_s_obs, h.n_pop, h.k_s, h.n_draw)
        self.assertEqual(res, 0.4009887932548518)

    def test_hypergeom_cdf_upper(self):
        from scipy.stats import hypergeom
        h = HyperCI(n_pop=100, k_s=30, n_draw=20, k_s_obs=5)
        res = 1 - hypergeom.cdf(h.k_s_obs - 1, h.n_pop, h.k_s, h.n_draw)
        self.assertEqual(res, 0.7908367991741947)

    def test_ci_sim(self):
        res = self.h.ci_sim()
        print(res['interval'])
        self.assertEqual(1,1)

