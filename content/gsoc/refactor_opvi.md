title: OPVI Refactoring
date: 2017-05-05T02:20:00
tags: GSoC, issues

Recently I've started working on [normalizing flows](https://arxiv.org/abs/1505.05770). That is a very powerful and
expressive family of distributions. Utilizing that approach for varialional inference can give very nice results.
Moreover this inference is tractable when dealing with huge datasets as it supports minibatching.
