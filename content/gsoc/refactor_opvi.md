title: OPVI Refactoring
date: 2017-05-05T02:20:00
tags: GSoC, issues

Recently I've started working on [normalizing flows](https://arxiv.org/abs/1505.05770). That is a very powerful and
expressive family of distributions. Utilizing that approach for varialional inference can give very nice results.
Moreover this inference is tractable when dealing with huge datasets as it supports minibatching.

## Problems met
Recently I've started implementing Normalizing Flows but encountered problems in early stage. They did not fit
my proposal timeline so it will be fair to speak about it here.

Architecture I created this winter for variational inference supposed to be modular so implementations of new method is
few lines of code with math for computing samples from initial distribution ($z_0$) and probability ($q(z)$) for
generated posterior ($z$). So not much left for a developer: there is abstract method $f_{\theta} : z_0 \rightarrow z $
that generates $z$ and parametrized with $\theta$. The result is approximate posterior.  

