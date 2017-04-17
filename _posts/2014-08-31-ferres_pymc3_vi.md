---
title: GSoC Proposal
layout: post
---

## Extend Variational Inference Methods in PyMC3
<!--more-->
### Abstract

Variational inference is a great approach for doing really complex, often intractable Bayesian inference in approximate form. Common methods (e.g. ADVI) lack from complexity so that approximate posterior does not reveal the true nature of underlying problem. In some applications it can yield unreliable decisions.

Recently on NIPS 2017 [OPVI](https://arxiv.org/abs/1610.09033) framework was presented. It generalizes variational inverence so that the problem is build with blocks. The first and essential block is Model itself. Second is Approximation, in some cases $log Q(D)$ is not really needed. Necessity depends on the third and forth part of that black box, Operator and Test Function respectively.

Operator is like an approach we use, it constructs loss from given Model, Approximation and Test Function. The last one is not needed if we minimize KL Divergence from Q to posterior. As a drawback we need to compute $loq Q(D)$. Sometimes approximation family is intractable and $loq Q(D)$ is not available, here comes LS(Langevin Stein) Operator with a set of test functions.

Test Function has more unintuitive meaning. It is usually used with LS operator and represents all we want from our approximate distribution. For any given vector based function of $z$ LS operator yields zero mean function under posterior. $loq Q(D)$ is no more needed. That opens a door to rich approximation families as neural networks.

Not only ADVI and Langevin Stein Operator VI are applicable with OPVI framework. Normalizing, Householder Flows fit well for it.

### Motivation

My recent contributions ([Implementing OPVI](https://github.com/pymc-devs/pymc3/pull/1694)) to PyMC3 created a good basis for extending variational inference in PyMC3 even further. I tried to transfer theoretical framework to python code and it succeed. Now main logic is in base classes and all rotines are abstracted and use public interface that is provided by developer. Implementing state-of-the-art methods is now not a challenge, you should just break the problem into 4 blocks described above and implement abstract methods.

I also have a side project [Gelato](https://github.com/ferrine/gelato) for using PyMC3 in neural networks. So my future plans are the following:

1. Implement Normalizing Flows
2. Implement Householders Flows
3. Implement Langein Stein Operator
4. Integrate OPVI to Gelato

## Literature
- Danilo Jimenez Rezende, Shakir Mohamed ["Variational Inference with Normalizing Flows"](https://arxiv.org/abs/1505.05770) (2015)
- Jakub M. Tomczak, Max Welling ["Improving Variational Auto-Encoders using Householder Flow"](https://arxiv.org/abs/1611.09630) (2016)
- Rajesh Ranganath, Jaan Altosaar, Dustin Tran, David M. Blei ["Operator Variational Inference"](https://arxiv.org/abs/1610.09033) (2016)

## Links
GitHub GSoC [PR#178](https://github.com/numfocus/gsoc/pull/178), [Issue#152](https://github.com/numfocus/gsoc/issues/152)
