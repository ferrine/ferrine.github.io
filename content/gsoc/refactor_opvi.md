title: OPVI Refactoring
date: 2017-06-21T12:51:00
status: published
tags: GSoC, issues

Recently I've started working on [normalizing flows](https://arxiv.org/abs/1505.05770). That is a very powerful and
expressive family of distributions. Utilizing that approach for variational inference can give very nice results.
Moreover this inference is tractable when dealing with huge datasets as it supports minibatching.

## Problems met
Recently I've started implementing Normalizing Flows but encountered problems in early stage. They did not fit
my proposal timeline so it will be fair to speak about it here.

Architecture I created this winter for variational inference supposed to be modular so implementations of new method is
few lines of code with math for computing samples from initial distribution ($z_0$) and probability ($q(z)$) for
generated posterior ($z$). So not much left for a developer: there is abstract method $f_{\theta} : z_0 \rightarrow z $
that generates $z$ and parametrized with $\theta$. The result is approximate posterior. 

Unfortunately this appeared to be not suitable for sequentially constructed posteriors like normalizing flows. Thus I
decided to do refactoring of variational module to handle that case too. See PR [#2306](https://github.com/pymc-devs/pymc3/pull/2306). 
The idea is as following. You have 2 entry points: one for initial distribution and one for symbolic replacements in the model. 
When constructing posterior one can use that symbolic matrix with initial distribution that is memoized and then memoize all intermediate 
results to use them for creating $log(q)$. That's what exactly done in this PR. I'm about to finish that and finally implement proposed methods.
