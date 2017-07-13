title: Grouped Variational Inference
date: 2017-07-13T08:06:00
status: published
tags: PyMC3, GSoC, Ideas

## Motivation
One of the core motivations behind non-MeanField variational approximations is creating interactions between
latent variables as fully factorized Gaussian does not capture this important property of posterior distribution.

Common way to relax this condition is to introduce full rank gaussian approximation with dense covariance matrix, parametrized
with Cholesky decomposition. But this parametrization is computationally expensive for large dimensions. So we meet another
limitation in terms of computational tractability. One can decide to use block matrix for covariance to hold interactions between 
selected latent variables. This is for sure great idea and I believe it will remain tractable even for deep neural networks.

## Reformulation
Let's think it over a little more. The latter idea is to use sparse covariance matrix. But what about reformulation of this statement?
We can treat this group of latent variables separately. For simplicity we'll have 2 groups: one stands for interactions, the other
does not have them at all. Using FullRank approximation for the first group and MeanField for the other one we'll get the same
parametrization as we decided to have earlier. 

### Notations
That can be written in the following form:

-   $D$ - latent space dimensionality
-   $p(z|D)$ - true posterior distribution
-   $K$ - number of grouped posterior components
-   $\mathcal{G}_k$ indices of grouped components
-   $z_{[k]}$ slice of $z$ that includes all components from $\mathcal{G}_k$
-   $q_{k}(z_{[k]})$ - distribution for group $k$
-   $q(z) = \prod_{k=1}^K q_{k}(z_{[k]})$ - posterior approximation


Now having the following notation we can formulate our interactions in the structured way. We have exactly 2 groups and distributions:

1. $z_{[1]} \sim \mathcal{N}(\mu_1, diag(\sigma_1))$
2. $z_{[2]} \sim \mathcal{N}(\mu_2, \Sigma_2)$

Having them we can sample variables group wise and construct $q(z)$.

## Extensions

In notations we did not specify the form of group distribution. So we are free to introduce any tractable density there.
This group distribution can be either simple FullRank/MeanField or more complex one such as NormalizingFlow. Usually interactions
require a lot of costly math to compute samples, density and gradients. Proposed approach limits number of interactions and thus
reduces computational overhead. As number of groups can be chosen by hand this core idea opens a way to deal with trade-off between
computational cost and captured interactions. I finally found some studies about current approach:
[Structured Stochastic Variational Inference](https://arxiv.org/abs/1404.4114) and [Copula variational inference](arxiv.org/abs/1506.03159).
So see it soon in [PyMC3](https://github.com/pymc-devs/pymc3).