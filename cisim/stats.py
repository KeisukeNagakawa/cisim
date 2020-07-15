import numpy as np
from scipy.stats import binom
from scipy.optimize import minimize_scalar


class BinomCI:
    """
    二項分布に関するクラス
    """

    def __init__(self, n_a, n_x, cl=0.05):
        self.n_a = n_a  # number of all trials
        self.n_x = n_x  # number of observed success
        self.cl = cl  # confidence level

    def diff_of_tail_area_and_cl(self, p, n_t, lf='left'):
        """
        :param n_t: しきい値となる成功数
        :param lf: レフトテイル（left）かライトテイル（right）か
        :param p: 母比率
        :param cl: 信頼水準
        :return:lf='left'の場合は[0:n_x+1]の区間における確率分布の面積を、
        lf='right'の場合は[n_x+1:n_a+1]における確率分布の面積を算出し、
        それらと信頼水準（cl: confidence level）/2の差の絶対値を算出する。
        （最適化関数で最小化するために用いる）
        """
        if abs(p - 0.5) >= 0.5:
            # 最適化関数に食わせるときに[0,1]を超える場合があるので抑えておく。
            return 100000
        if lf == 'left':  # left tailを計算
            return abs(binom.cdf(n_t, self.n_a, p) - self.cl * 0.5)
        elif lf == 'right':  # right tailを計算　
            return abs(1 - binom.cdf(n_t - 1, self.n_a, p) - self.cl * 0.5)
        else:
            return 100000

    def ci_sim(self, debug=False):
        """
        シミュレーションによって信頼区間を算出する。
        :param ul: 上側確率（upper）か、下側確率（lower）か。
        :param debug: True if debug
        :return: sequence of objects like [lower, upper],
        where each objects has x(calculated value) and and other info
        """

        # 信頼上限
        upper = minimize_scalar(
            self.diff_of_tail_area_and_cl, bounds=[0, 1], args=(self.n_x, 'left'), method='Bounded'
        )

        # 信頼下限
        lower = minimize_scalar(
            self.diff_of_tail_area_and_cl, bounds=[0, 1], args=(self.n_x, 'right'), method='Bounded'
        )

        return [lower, upper]


class HyperCI:
    """
    超幾何分布に関するクラス
    """

    def __init__(self, n_pop, k_s, n_draw, k_s_obs, n_s, cl=0.05):
        self.n_pop = n_pop
        self.k_s = k_s
        self.n_draw = n_draw
        self.k_s_obs = k_s_obs
        self.n_s = n_s
