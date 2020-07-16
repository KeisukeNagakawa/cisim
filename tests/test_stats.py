from unittest import TestCase
from cisim.stats import BinomCI, HyperCI


class Testbinom(TestCase):
    b = BinomCI(n_pop=100, n_obs=10, cl=0.05)

    def test_ci_sim(self):
        res = self.b.ci_sim()
        self.assertEqual(
            [0.049005430267763495, 0.17622473596973592],
            res['interval']
        )


class TestHyperCI(TestCase):

    def test_hypergeom_cdf_lower(self):
        from scipy.stats import hypergeom
        h = HyperCI(n_pop=100, n_draw=20, k_s_obs=5)
        k_s = 30
        res = hypergeom.cdf(h.k_s_obs, h.n_pop, k_s, h.n_draw)
        self.assertEqual(res, 0.4009887932548518)

    def test_hypergeom_cdf_upper(self):
        from scipy.stats import hypergeom
        h = HyperCI(n_pop=100, n_draw=20, k_s_obs=5)
        k_s = 30
        res = 1 - hypergeom.cdf(h.k_s_obs - 1, h.n_pop, k_s, h.n_draw)
        self.assertEqual(res, 0.7908367991741947)

    def test_ci_sim(self):
        h = HyperCI(n_pop=10**7, n_draw=10**5, k_s_obs=100)
        res = h.ci_sim()
        print(res['interval'])
        print(res['detail']['upper'])
        self.assertEqual(1, 1)
