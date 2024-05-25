---
tags:
- parking-functions
- research
- comb
---

### What a parking function is

Imagine there are $n$ cars trying to park in $n$ spots on a one way street. Each driver has a desired parking spot. They will drive to that spot, and if it's unoccupied, park in it. If the spot is occupied, the driver will park in the next unoccupied spot (in the direction of the one way street), or if there isn't one, not park at all. Parking functions answer the question "what preference lists" allow everyone to park.

##### _definition:_ parking function

A parking function is an $n$-tuple $\pi \in \mathbb{N}_{n}^n$ such that if $n$ cars wanted to park in $n$ spots on a one-way street with the $j$th car wanting to park in the $\pi_{j}$th spot, then all the cars would get to park.

Really, it turns out that we can characterise parking functions completely by the non-decreasing rearrangement of the preference list. That is, we can determine whether a preference list is a parking function just with this idea.

##### _definition:_ non-decreasing rearrangement

Given a list $\pi \in \mathbb{N}_{n}^n$, it's non-decreasing rearrangement is $\pi' \in \mathbb{N}_{n}^n$ such that $\pi'_{i} \le \pi'_{i + 1}$ for all $i \in \mathbb{N}_{n - 1}$ and $\pi'_{i} = \pi_{\sigma(i)}$ for some permutation $\sigma \in S_{n}$.

Specifically, we have the following result.

##### _proposition:_ the $\pi_{i}$ condition for parking functions

A preference list $\pi \in \mathbb{N}_{n}^n$ with non-increasing rearrangement $\pi'$ is a parking function if and only if $\pi_{i}' \le i$ for all $i \in \mathbb{N}_{n}$.

###### _proof:_

Suppose $\pi$ is a parking function. Then there cannot be fewer than $i$ cars that want to park in the first $i$ spots — if there were, then one of the first $i$ spots would be empty, and thus, $\pi$ would not be a parking function. Thus, $\pi_{i}' \le i$.

Suppose $\pi$ is not a parking function. Then there must be some earliest spot unoccupied — say the $j$th spot. If all $i \le j$ gave $\pi_{i}' \le i$, then cars $\sigma ^{-1}(1), \dots, \sigma ^{-1}(j)$ would be parked in spots $1, \dots, j$ and the $j$th spot would not be empty.