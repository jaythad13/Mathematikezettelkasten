---
tags:
- spivak
- anal
- calc
- self-study
---

Integrating over closed rectangles is basically just the same as integrating over closed intervals in $\bb R^n$, so this should be pretty simple. 

##### _notation:_ $A$

For this note, $A$ is a closed rectangle in $\bb R^n$ given by
$$
A = \prod_{i = 1}^n [a_i, b_i]
$$

### Partitions

We recall the idea of partitioning an interval of $\bb R$ into lots of subintervals —

##### _definition:_ partition of $[a, b]$, subintervals

A partition, $P$, of the interval $[a, b] \subset \bb R$ is a non-decreasing sequence $t_0, \ldots, t_n$ with $a = t_0$ and $b = t_n$.

Each $[t_{j - 1}, t_j]$ is called a subinterval of $[a, b]$ under $P$. 

Let the set of all subintervals under $P$ be denoted by $\mathcal S(P)$. Note that the union of all of the subintervals under a partition is just the interval

This definition is naturally generalised to a partition of a closed rectangle in $\bb R^n$. That is,

##### _definition:_ partition, subrectangles

A partition $P$ of $A$ is a an $n$-tuple $(P_1, \ldots, P_n)$ where each $P_i$ is a partition of $[a_i, b_i]$.

If each $P_i$ divides $[a_i, b_i]$ into $N_i$ partitions, $P$ divides $A$ into $\prod_{i = 1}^n N_i$ subrectangles, each of the form
$$
\prod_{i = 1}^n s_i
$$
where $s_i \in \mathcal S(P_i)$.

Naturally, we say the set of all subrectangles under $P$ is $\mathcal S(P)$

A natural thing to consider then is a notion of maximum or minimum of a function over each of the subrectangles — can you see where this is going? To be more specific, we speak of the supremum or infimum instead, since we are not guaranteed to have nice continuous functions.

##### _notation:_ $m_s$ and $M_s$

Suppose $f : A \to \bb R$ is a bounded function, and $P$ is a partition of $A$. For each subrectangle $s \in \mathcal S(P)$ let
$$
m_s = \inf \set{f(\bvec x) : \bvec x \in s}
$$
and
$$
M_s = \sup \set{f(\bvec x) : \bvec x \in s}.
$$

We also want to define the volume of a rectangle —

##### _definition:_ volume, $v(A)$

The volume of any (open or closed) rectangle $A$ is
$$
v(A) = \prod_{i = 1}^n (b_i - a_i).
$$

This then allows us to get where it's obvious we were going — defining lower and upper sums for a function on a partition.

##### _definition:_ lower and upper sums

The lower and upper sums of a bounded function $f : A \to \bb R$ for a partition $P$ of $A$ are
$$
L(f, P) = \sum_{s \in \mathcal S(P)} m_s(f) \, v(s)
$$
and
$$
U(f, P) = \sum_{s \in \mathcal S(P)} M_s(f) \, v(s).
$$

Note that we clearly have $L(f, P) \le U(f, P)$ for any partition $P$ since $m_s \le M_s$ for each subrectangle $s$.

Another very natural definition is the notion of a more refined partition — one which contains "smaller" subrectangles. Basically, you take all of the subrectangles of a partition, and either leave them alone, or cut them into even smaller pieces.

##### _definition:_ refined partition

We say that $P'$, refines $P$, both partitions of $A$, if every $s' \in \mathcal{S}(P')$ is the subset of some $s \in \mathcal{S}(P)$.

Note that if we have $P = (P_{1}, \dots P_{n})$, then if $P_{i}'$ refines $P_{i}$ for every $i \in \mathbb{N}_{n}$, then we have that $P' = (P_{1}', \dots, P_{n}')$ refines $P$.

Obviously, something we want to be true is that refining a partition allows us to get closer to some "true" value of the integral. This would mandate that the lower sums keep getting greater, and the upper sums keep getting smaller until they are the same. So if we want this to be true, we at least need the following result.

##### _definition:_ refining brings lower and upper sums closer

Suppose the partition $P'$ refines $P$ (both partitions of $A$), then, for any continuous function $f : A \to \mathbb{R}$ we have $L(f, P) \le L(f, P')$ and $U(f, P') \le U(f, P)$.

###### _proof:_

Let us have $s \in \mathcal{S}(P)$ divided into $s_{1}, \dots ,s_{\nu} \in \mathcal{S}(P')$, with $v(s) = \sum_{i = 1}^\nu v(s_{i})$.

Since $s_{i} \subset s$, we must have $m(s) \le m(s_{i})$ and $M(s_{i}) \le M(s)$. Thus,
$$
m(s) v(s) \le \sum_{i = 1}^\nu m(s_{i}) v(s_{i})
$$
and
$$
\sum_{i = 1}^\nu M(s_{i}) v(s_{i}) \le M(s) v(s).
$$

##### _corollary:_ any upper sum is greater than any lower sum

If $P$ and $P'$ are any two partitions of $A$, then $L(f, P') \le U(f, P)$ (for any continuous function $f : A \to \mathbb{R}$).

###### _proof:_

Let $P''$ be a partition that refines both $P$ and $P'$. Note that this does actually exist — try to refine each of $P$ and $P'$, and then look at the intersection of the intervals. Then
$$
L(f, P') \le L(f, P'') \le U(f, P'') \le U(f, P).
$$

We can get a further corollary from this — we can look at the least upper bounds and greatest lower bounds on the lower and upper sums (we have these since they are obviously bounded by the trivial partition that just has $A$ as a subrectangle).

##### _definition:_ integrable, integral

A function $f : A \to \mathbb{R}$ is integrable if $f$ is bounded and
$$
\inf \{ U(f, P) : P \text{ partitions } A \} = \sup \{ L(f, P) : P \text{ partitions }A \}.
$$

This number is called the integral of $f$ over $A$, denoted by 
$$
\int_{A} f
$$
or sometimes,
$$
\int_{A}  \, dx_{1} \cdots dx_{n} 
$$
(remember that $n$ comes from $A \subset \mathbb{R}^n$).

The following result feels pretty obvious, and is, but is useful to have.

##### _theorem:_ integrable upper and lower sums get arbitrarily close

A bounded function $f : A \to \mathbb{R}$ is integrable on $A$ if and only if for every $\varepsilon > 0$ there is a partition $P$ of $A$ is such that $U(f, P) - L(f, P) < \varepsilon$.

###### _proof:_

If there is such a partition for every $\varepsilon > 0$, then for any number $u > \sup \{ L(f, P) \}$ we have some $U(f, P') < u$. Just choose $P'$ such that $U(f, P') - L(f, P') < u + \sup \{ L(f, P) \} - L(f, P')$. (This exists by our hypothesis). Thus, $\inf \{ U(f, P)\} \le \sup \{ L(f, P) \}$.

We also always have $U(f, P) > L(f, P')$ for any $P$ and $P'$. That is, every, $L(f, P')$ is a lower bound of $\{ U(f, P) \}$. Thus, $\inf \{ U(f, P) \}$ is an upper bound on $\sup \{ L(f, P) \}$ and finally, $\inf \{ U(f, P) \} \ge \sup \{ L(f, P) \}$.

If we have that $f$ is integrable, then there are partitions $P'$ and $P''$ that give us $L(f, P') - U(f, P'') < \varepsilon$ for all $\varepsilon > 0$. Thus, if $P$ refines both of them, then it is the desired partition.

##### _example:_ the famous non-integrable Dirichlet function

Consider $f : [0, 1] \to \mathbb{R}$ defined by
$$
f(x) = \begin{cases}
0 & x \in \mathbb{Q} \\
1 & x \not\in \mathbb{Q}.
\end{cases}
$$

Since [[The reals|the rationals are dense in the reals]], every subrectangle $s$ will contain some points in $\mathbb{Q}$ and thus have $M(s) = 1$ and $m(s) = 0$. Thus, for any partition, $P$
$$
L(f, P) = 0  
$$
and
$$
U(f, P) = v([0, 1]) = 1.
$$

##### _example:_ constant functions are integrable

Any constant function $f = c$ is obviously integrable since any partition gives lower and upper sums $v(A) \, c$, making their lower and upper bounds coincide.