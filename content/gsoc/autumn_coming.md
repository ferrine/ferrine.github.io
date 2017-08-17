title: Autumn is Coming
date: 2017-07-13T08:06:00
status: draft
tags: PyMC3, GSoC

The summer has passed and a lot of things have been done. I still have some work in progress that I did not manage
to finish in time. This work is devoted to Structured Variational Inference that was impossible before. I found
this work very challenging and it took a lot of time to get the right direction and inspiration.

The road was quite long and I was developing new architecture for about 2 weeks. No single line of code was written there.
When I finally got the idea and understanding of what exactly is needed it was hard to stop coding. That's how inspiration
is important, any challenging problem can be solved. I have to thank my mentors who guided me through this journey.
I'm planning to continue further contributions in PyMC3 Variational Inference and improve it even more.

By now I've finished 1 huge [PR](https://github.com/pymc-devs/pymc3/pull/2362) implementing Normalizing Flows. Now
PyMC3 has state-of-the-art VI algorithms for both large and small models. You can see how it works in our
[documentation](http://docs.pymc.io/en/latest/examples.html#variational-inference)

[The second](https://github.com/pymc-devs/pymc3/pull/2416) implements Structured Variational Inference not possible before. It is not ready for merge as it has to be
reviewed a bit more and a lot of examples have to be rerun. That will take some more time for sure. It also allows to create
arbitrary variational distributions in future for individual groups of variables. Gubmel Softmax reparametrization might suit extremely well for
Deep Learning modern approaches. I am sure that PyMC3 will make Bayesian Deep Learining more accessible.
