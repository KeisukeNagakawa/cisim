from unittest import TestCase
from cisim.stats import BinomCI, HyperCI


class Testbinom(TestCase):

    def test_validation(self):
        self.assertRaises(ValueError, BinomCI, 100, -10, 0.05)

    def test_ci_sim(self):
        b = BinomCI(n_pop=100, n_obs=10, cl=0.05)
        res = b.ci_sim()
        self.assertEqual(
            [0.049005430267763495, 0.17622473596973592],
            res['interval']
        )


class TestHyperCI(TestCase):
    def test_validation(self):
        self.assertRaises(ValueError, HyperCI, 100, -20, 5)

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
        h = HyperCI(n_pop=10 ** 4, n_draw=10 ** 3, k_s_obs=100)
        res = h.ci_sim()
        self.assertEqual(res['interval'], [830, 1193])
