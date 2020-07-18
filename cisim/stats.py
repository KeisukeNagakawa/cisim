from scipy.stats import binom, hypergeom
from scipy.optimize import minimize, minimize_scalar
from cerberus import Validator
from .schemas import schema_binom, schema_hyper


def format_result(interval, lower_result, upper_result):
    """
    :param interval: sequence of numbers
    :param lower_result: <class 'scipy.optimize.optimize.OptimizeResult'>
    :param upper_result: <class 'scipy.optimize.optimize.OptimizeResult'>
    :return: unpacked value as follows,
        interval, success, detail
    """
    success = upper_result['success'] and lower_result['success']  # True if all calculation terminated safely.
    detail = {'upper': upper_result, 'lower': lower_result}
    return interval, detail, success


class CI:
    def __init__(self):
        pass


class BinomCI(CI):
    """
    Class on Binomial Distribution's Confidence Interval
    """

    def __init__(self, n_pop, n_obs, cl=0.05):
        v = Validator(schema_binom)
        input_arg = {'n_pop': n_pop, 'n_obs': n_obs, 'cl': cl}
        if not v.validate(input_arg):
            raise ValueError(v.errors)
        self.n_pop = n_pop  # number of all trials
        self.n_obs = n_obs  # number of observed success
        self.cl = cl  # confidence level
        self.p_obs = self.n_obs / self.n_pop

    def diff_of_tail_area_and_cl(self, p, lf='left'):
        """
        :param n_t: threshold for number of success
        :param lf: left tail or right tail
        :param p: success probability
        :param cl: confidence interval
        :return:
        when lf='left' it returns sum of density among [0:n_x+1] minus (confidence level) *0.5
        when lf='right' it returns sum of density [n_x:n_pop+1] minus (confidence level) *0.5
        """
        if abs(p - 0.5) >= 0.5:
            # used when p<0 or p>1, which may occur in optimizing
            # do not raise error here. It causes to stop optimizing.
            return 100000

        if lf == 'left':  # calc left tail
            return abs(binom.cdf(self.n_obs, self.n_pop, p) - self.cl * 0.5)
        elif lf == 'right':  # calc right tail
            return abs(1 - binom.cdf(self.n_obs - 1, self.n_pop, p) - self.cl * 0.5)
        else:
            raise TypeError('lf must be "left" or "right"')

    def ci_sim(self, debug=False):
        """
        calculate confidence interval
        :param debug: True if debug
        :return: objects. Important attribute is 'interval', which has sequence of lower and upper confidence level.
        """

        # upper confidence level
        upper = minimize_scalar(
            self.diff_of_tail_area_and_cl, bounds=[self.p_obs, 1], args=('left'), method='Bounded'
        )

        # lower confidence level
        lower = minimize_scalar(
            self.diff_of_tail_area_and_cl, bounds=[0, self.p_obs], args=('right'), method='Bounded'
        )
        interval = [lower.x, upper.x]
        return format_result(interval, upper, lower)


class HyperCI:
    """
    Class on Hypergeometric distribution's Confidence Interval
    """

    def __init__(self, n_pop, n_draw, k_s_obs, cl=0.05):
        input_arg = {'n_pop': n_pop, 'n_draw': n_draw, 'k_s_obs': k_s_obs, 'cl': cl}
        v = Validator(schema_hyper)
        if not v.validate(input_arg):
            raise ValueError(v.errors)
        self.n_pop = n_pop
        self.n_draw = n_draw
        self.k_s_obs = k_s_obs
        self.cl = cl

    def diff_of_tail_area_and_cl(self, k_s_x, lf='left'):
        """
        :param k_s_x: number of success in the population
        :param lf: left tail or right tail
        :return:
        when lf='left' it returns sum of density among [0:k_s_t+1] minus (confidence level) *0.5
        when lf='right' it returns sum of density [k_s_t:n_pop+1] minus (confidence level) *0.5
        """
        if lf == 'left':  # left tailを計算
            return abs(
                hypergeom.cdf(self.k_s_obs, self.n_pop, k_s_x, self.n_draw) - self.cl * 0.5
            )
        elif lf == 'right':  # right tailを計算　
            return abs(
                1 - hypergeom.cdf(self.k_s_obs - 1, self.n_pop, k_s_x, self.n_draw) - self.cl * 0.5
            )
        else:
            raise TypeError('lf must be "left" or "right"')

    def ci_sim(self, debug=False):
        """
        :param debug:
        :return: objects. Important attribute is 'interval', which has sequence of lower and upper confidence level.
        """

        # expected value
        k_s_expected = int(round(self.k_s_obs / self.n_draw * self.n_pop))

        upper = minimize(
            self.diff_of_tail_area_and_cl,
            x0=[k_s_expected],
            args=('left'),
            method='nelder-mead',
            options={'xatol': 1e-8, 'disp': debug}
        )

        lower = minimize(
            self.diff_of_tail_area_and_cl,
            x0=k_s_expected,
            args=('right'),
            method='nelder-mead',
            options={'xatol': 1e-8, 'disp': debug}
        )
        # confidence interval
        interval = [int(round(lower.x[0])), int(round(upper.x[0]))]
        return format_result(interval, upper, lower)
