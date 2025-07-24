---
tags:
- math-145/3
- top
- alg-top
---

Fixed point theorems are really nice! They allow us to say things like "if a map of Claremont is placed in Claremont, there is a point on the map sitting above the point in Claremont". This is a consequence of the relatively easy contraction mapping theorem.

##### _theorem:_ contraction mapping theorem

Let $X$ be a [[Analysis --- math-131/notes/Cauchy sequences#Completeness|complete metric space]] and let $f$ be a contraction (a map such that $d(f(x), f(y)) < c \, d(x, y)$ for some positive $c < 1$). Then $f$ has a unique fixed point.

###### _proof sketch:_

Iteratively apply $f$ to $x$, and see that this forms a [[Analysis --- math-131/notes/Cauchy sequences|Cauchy sequence]] by the contraction condition. Since $X$ is complete, it converges to a point in $X$. This point is the fixed point. There can't be another one since the distance between them would have to contract.

### The Brouwer fixed point theorem in low dimensions

The Brouwer fixed point theorem says that a continuous map on any closed ball has a fixed point. As a result, the same theorem holds for any space homeomorphic to the closed ball.

##### _theorem:_ the Brouwer fixed point theorem

Let $\overline{B^n}$ be the closed unit ball in $\mathbb{R}^n$. If $f : \overline{B^n} \to \overline{B^n}$ is continuous, then there is a fixed point $x \in \overline{B^n}$ such that $f(x) = x$.

The disc must be closed since otherwise you could contract towards a point not included on the boundary, which would. To prove this in general requires a lot of machinery, typically from homology theory, or Sperner's lemma. However, it's actually doable in the case $n \le 2$ (with just the machinery of the [[Simplicial homology and graph theory --- math-145/notes/Continuous and differentiable winding number#_theorem _ the continuous winding number theorem|continuous winding number theorem]]).

##### _theorem:_ the Brouwer fixed point theorem on a point

A continuous map $\overline{B^0} \to \overline{B^0}$ has a fixed point.

###### _proof:_

This is trivially true since $\overline{B^0}$ is just one point.

##### _theorem:_ the Brouwer fixed point theorem on a line

A continuous map $\overline{B^1} \to \overline{B^1}$ has a fixed point.

###### _proof:_

$\overline{B^1}$ is just $[-1, 1]$. Thus, we really want to show that a curve from one side of a the square $[-1, 1]$ to the other must cross the line $y = x$.

By the [[Analysis --- math-131/notes/Continuity#_corollary _ intermediate value theorem|intermediate value theorem]] we can see that $g$ defined by $g(x) = f(x) - x$ has $g(-1) \ge -1 - (-1) = 0$ and $g(1) \le 1 - 1 = 0$, so $g$ must have a zero. That is, there is some $x$ where $f(x) = x$.

##### _theorem:_ the Brouwer fixed point theorem in the plane

A continuous map $\overline{B^2} \to \overline{B^2}$ has a fixed point.

###### _proof:_
is on the [[Simplicial homology and graph theory --- math-145/attachments/homework/hw 3/hw 3.pdf|homework]].