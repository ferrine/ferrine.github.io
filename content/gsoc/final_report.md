title: Final Report
date: 2017-08-24T12:46:01
status: published
tags: PyMC3, GSoC

## Impressions
The summer has passed and a lot of things are done. Some of them were not outlined in the original GSoC proposal. There is still some work in progress that I did not manage
to finish in time. This work is devoted to Structured Variational Inference that was impossible before. I found
this very challenging and it took a lot of time to get the right direction and inspiration.

The road was quite long and I was developing new architecture for about 2 weeks. No single line of code was written there.
When I finally got the idea and understanding of what exactly is needed it was hard to stop coding. That's how inspiration
is important, any challenging problem can be solved. I have to thank my mentors who guided me through this journey.
I'm planning to continue further contributions in PyMC3 Variational Inference and improve it even more.

## Normalising Flows
By now I've finished 2 huge PRs ([pymc3/#2306](https://github.com/pymc-devs/pymc3/pull/2306), [pymc3/#2362](https://github.com/pymc-devs/pymc3/pull/2362)) implementing Normalizing Flows. Now
PyMC3 has state-of-the-art VI algorithms for both large and small models. You can see how it works in our
[documentation](http://docs.pymc.io/en/latest/examples.html#variational-inference). The work that is done here:

-   new `flows.py` module created
-   refactored `pm.variational` to support Normalizing Flows 
-   implemented the following flow families
    
    -   Planar flow
    -   Radial flow
    -   Householder flow
    -   Loc flow
    -   Scale flow

-   created a way to combine flows in formulas

## Structured Variational Inference
The second ([pymc3/#2416](https://github.com/pymc-devs/pymc3/pull/2416)) implements Structured Variational Inference not possible before. It is not ready for merge as it has to be
reviewed a bit more and a lot of examples have to be rerun. That will take some more time for sure. It also allows to create
arbitrary variational distributions in future for individual groups of variables. One of that ideas is Gubmel Softmax reparametrization that
is an approach to relax discreteness and be able to backpropagate the underlying probabilities. It might
suit extremely well for modern deep learning approaches. The scope of this PR is as following

- [x] refactoring `pm.variational`
- [x] rewrite all approximations as groups
- [x] support local approximations everywhere
- [ ] tests/debug
- [ ] rerun notebooks

## Other related work

-   [pymc3/#2312](https://github.com/pymc-devs/pymc3/pull/2312): Add notebook with VI quickstart
-   [pymc3/#2408](https://github.com/pymc-devs/pymc3/pull/2408): Add notebook with flows
-   [pymc3/#2410](https://github.com/pymc-devs/pymc3/pull/2410): Fix some typos in NFVI notebook
-   [pymc3/#2171](https://github.com/pymc-devs/pymc3/pull/2171): Boost minibatches
