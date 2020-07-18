Confidence Interval Simulation Module Repository
=================================================

For a hypergeometric distribution, denoted by :math:`Hyper(n_pop, k_s, n_draw)`, where :math:`n_pop` is the population size, :math:`k_s` is the number of population with 'success', and :math:`n_draw` is the given sample size, this program calculates the confidence interval for :math:`k_s` when :math:`n_pop` is known, using simulation scipy optimization tools.


# shell

.. code-block:: shell

    pip install cisim


# python

.. code-block:: python3

    import cisim
    from cisim.stats import HyperCI
    h = HyperCI(n_pop=10**4, n_draw=10**3, k_s_obs=100)
    res = h.ci_sim()
    print(res['interval'])
    >>> [830, 1193]



And this program can also calculate confidence interaval for binomial distribution, too.

.. code-block:: python3

    import cisim
    from cisim.stats import BinomCI
    b = BinomCI(n_pop=100, n_obs=10, cl=0.05)
    res = b.ci_sim()
    print(b.ci_sim()['interval'])
    >>> [0.049005430267763495, 0.17622473596973592]




You can check and compare the result with Clopper-Pearson approach on `cluster-text.com <http://www.cluster-text.com/confidence_interval.php>`_


Learn more at `HyperGeometric distribution <http://www.kennethreitz.org/essays/repository-structure-and-python>`_, `Binomial Distribution <https://ja.wikipedia.org/wiki/%E4%BA%8C%E9%A0%85%E5%88%86%E5%B8%83>`_

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/KeisukeNagakawa/setup.py>`_.
