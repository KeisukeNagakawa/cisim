Confidence Interval of Hypergeometric Distribution Calculating Module
=====================================================================

For a hypergeometric distribution, denoted by :math:`Hyper(n_pop, k_s, n_draw)`, where :math:`n_pop` is the population size, :math:`k_s` is the number of population with 'success', and :math:`n_draw` is the given sample size, this program calculates the confidence interval for :math:`k_s` when :math:`n_pop` is known and number of observed success is given as :math:`k_s_obs`, using simulation scipy optimization tools.


PyPI package link is `here <https://pypi.org/project/cisim/>`_.



First, pip install this package.

shell

.. code-block:: shell

    pip install cisim

Note: if this installing doesn't go well, please try pip install these packages: cerberus, numpy, and scipy.



After the pip-install, you can calculate the interval of a Hypergeometric distribution as follows.

python

.. code-block:: python3

    import cisim
    from cisim.stats import HyperCI
    h = HyperCI(n_pop=10**4, n_draw=10**3, k_s_obs=100)
    res = h.ci_sim()
    print(res[0])
    >>> [830, 1193]



And this program can also calculate confidence interaval for binomial distribution, too.

.. code-block:: python3

    import cisim
    from cisim.stats import BinomCI
    b = BinomCI(n_pop=100, n_obs=10, cl=0.05)
    res = b.ci_sim()
    print(res[0])
    >>> [0.049005430267763495, 0.17622473596973592]




You can check and compare the result with Clopper-Pearson approach on `cluster-text.com <http://www.cluster-text.com/confidence_interval.php>`_


Learn more at `HyperGeometric distribution <https://en.wikipedia.org/wiki/Hypergeometric_distribution>`_, `Binomial Distribution <https://en.wikipedia.org/wiki/Binomial_distribution>`_

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/KeisukeNagakawa/setup.py>`_.
