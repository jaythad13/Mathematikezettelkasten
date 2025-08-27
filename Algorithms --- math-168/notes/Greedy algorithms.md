---
tags:
- math-168/1
- math-168/2
- algs
---

If an algorithm is a sequence of steps, then a greedy algorithm makes the optimal decision at each step, in the hopes that this is also globally optimal.

The main idea is that we can prove correctness of algorithms by induction. Suppose the algorithm works for input size $n$ (and possibly all smaller input sizes). Then using that hypothesis, show that some optimal solution to the problem includes the greedy choice at the first step of $n + 1$. Finally check that the optimal solution to the problem can be obtained by the optimal solution for input size $n$.

##### _example:_ the registration problem

Given an input of a set of intervals (say courses with start and end times), we want to find the maximal subset of non-intersecting intervals. Note that we could solve this with some sort of backtracking algorithm. This would not be a greedy algorithm.

We could try to choose the shortest interval greedily, but this wouldn't work — consider the intervals $[-10, 1], [1, 10], [-2, 2]$. If you choose the shortest interval $[-0.2, 0.2]$ then you don't have any more intervals to choose. We could also try to choose the earliest first, but this doesn't work either — consider $[-10, 10], [-7, -5], [5, 7]$. Finally, we could choose the interval with fewest other intersecting intervals. This doesn't work either (see the examples from the slides).

The correct algorithm is to greedily choose the interval ends first. By [[Superdiscrete --- math-55A/notes/Induction and recurrence|induction]] it suffices to show that our first greedy choice is part of some maximal solution. Clearly the greedy solution is maximal when there is just one interval. Suppose greedy solutions are maximal for some $n$, and we are given some maximal subset $S$ of non-intersecting. We claim that $S'$ which is $S$ with its earliest ending time interval replaced with the interval with globally earliest ending time is also maximal.

We don't want just want to show that the greedy algorithm works, we also want to analyse its run time. Once the intervals are sorted by end time, we just need a constant time step at each list element. Thus, the run time is $n + O(n \log n) = O(n \log n)$.

##### _example:_ making change

Given a set of denominations and a target amount that we want to get by adding coins of those denominations, what's the minimum number of coins required to get the target amount?

We could choose the largest denomination greedily, but this isn't always minimal. For example, if we have the pre-decimal British coins with $6, 12, 24, 30$ coins included, then the greedy algorithm requires $3$ coins to get $48$, but that can clearly be achieved.

What sets of denominations does this work for? Note that it works for denominations $\{ 1, b, b^{2}, \dots, b^k \}$ (this is just base $b$ expansion). Similarly, [[Superdiscrete --- math-55A/notes/Induction and recurrence#_theorem _ Zeckendorf's theorem|Zeckendorf's theorem]] guarantees that this works for Fibonacci denominations $\{ F_{n} \}$.

##### _example:_ the corporate party problem

Suppose we have a tree $T$ with root vertex $r$, defining the hierarchy for the company. How can we find a maximal set of vertices with no immediate parent-child pairs (that is, a maximal set of employees without a boss-employee pair). 

Greedily pick leaves (bottom depth vertices)! Again we can prove this by induction on the number of vertices. Clearly it works for a tree (or rather, forest) with just one vertex. Suppose ([[Superdiscrete --- math-55A/notes/Induction and recurrence#Strong induction|strong induction]]) it works on all forests with at most $n$ vertices. Let $T$ be a forest with $n + 1$ vertices. If a leaf is in a given maximal subset, then we are done. If it is not and its parent is, not we can always replace a parent of a leaf in a maximal subset with its child leaf to get a different maximal subset. If it is not and its parent is not, then the subset is not maximal (because we can definitely add the leaf). Thus, we're done.