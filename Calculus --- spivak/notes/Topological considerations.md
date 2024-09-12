---
tags:
- spivak/mnfld/1
- top
- anal
- self-study
---

In order to do calculus, having a characterisation of "topologically special" sets in our space is useful — we want a characterisation of [[Analysis --- rudin/notes/Metric spaces#_definition _ open set|open]], [[Analysis --- rudin/notes/Metric spaces#_definition _ closed set|closed]], and [[Compactness|compact]] sets in $\bb{R}^n$. 

### Open and closed sets

Obviously, the prototypical example of a closed set in $\bb R$ is the closed interval $[a, b]$ and for open sets, the open interval $(a, b)$. These have natural generalisations to closed and open sets in $\bb{R}^n$ — the closed rectangle $[a_1, b_1] \times \cdots \times [a_n, b_n]$, and the open rectangle $(a_1, b_1) \times \cdots \times (a_n, b_n)$. Open subsets of $\mathbb{R}^n$ in general should then contain an open rectangle around each point.

##### _definition:_ closed rectangle

The set $[a_1, b_1] \times \cdots \times [a_n, b_n] \subset \bb R^n$, for real numbers $a_i \le b_i$, is called a closed rectangle in $\bb R^n$.

##### _definition:_ open rectangle

The set $(a_1, b_1) \times \cdots \times (a_n, b_n) \subset \bb R^n$, for real numbers $a_i < b_i$, is called a closed rectangle in $\bb R^n$.

##### _definition:_ open set

A set $U \subset \bb R^n$ is an open set if for each $\bvec x \in U$ we have some open rectangle $A$ such that $\bvec x \in A \subset U$.

Note that all though this looks different, it is equivalent to the [[Analysis --- rudin/notes/Open and closed sets|metric space notion of open sets]] with $r$-neighbourhoods. The idea is that since $r$-neighbourhoods are open in this "rectangular topology" and open rectangles are open in the "$r$-neighbourhood topology", if a set is open according to one, it's open in the other. For example, if a set is open in the rectangle topology, then inside every rectangle, we can draw an $r$-neighbourhood around the desired point, and thus, the set is open in the $r$-neighbourhood topology.

##### _definition:_ closed

A set $C \subset \bb R^n$ is a closed set if it is the complement of an open set — that is, if $\bb R^n \setminus C$ is open

A silly verification, but still one we should perform to sanity check our definitions is that a closed rectangle is a closed set.

##### _proposition:_ closed rectangles are closed

Any closed rectangle $[a_1, b_1] \times \cdots \times [a_n, b_n]$ is a closed set.

###### _proof:_

Let $A$ be the closed rectangle. For any point $\bvec x = (x_1, \ldots, x_n) \in \bb R^n \setminus A$, we have at least one $i$ such that $x_i < a_i$ or $x_i > b_i$. Consider the following intervals.

If $x_i \in [a_i, b_i]$ let $I_i = (a_i - 1, b_i + 1)$. If $x_i \notin [a_i, b_i]$, then we must either have $x_i < a_i$ or $x_i > b_i$. If we have the former, then let $I_i = (x_i - 1, a_i)$ and $I_i = (b_i, x_i + 1)$. Then $\prod_{i = 1}^n I_i$ is an open rectangle containing $\bvec x$. Since there is at least one $I_i$ that has no intersection with the corresponding $[a_i, b_i]$ (for which we have $x_i \notin [a_i, b_i]$), this open rectangle also must only contain points not in $A$ — that is, the open rectangle is a subset of $\bb R^n \setminus A$.

We quote that [[Open and closed sets#_proposition _ (Potentially infinite) unions and finite intersections of open sets are open|arbitrary unions and finite intersections of open sets are open]], and [[Open and closed sets#_corollary _ Finite unions and (potentially infinite) intersections of closed sets are closed|finite unions and arbitrary intersections of closed sets are closed]] without proof, but the result is elementary.

If $A \subset \bb R^n$ and $\bvec x \in \bb R^n$, then exactly one of the following must hold
1) There is an open rectangle $B$ such that $\bvec x \in B \subset A$
2) There is an open rectangle $B$ such that $\bvec x \in B \subset \bb R^n \setminus A$
3) Every open rectangle $B$ containing $\bvec x$ contains points of both $A$ and $\bb R^n \setminus A$

This must be true just by exhausting the first two cases, and it allows us to make the following definitions.

##### _definition:_ interior point, interior

For $A \subset \bb R^n$ and $\bvec x \in \bb R^n$, if there is an open rectangle $B$ such that $\bvec x \in B \subset A$, then $\bvec x$ is an interior point of $A$.

The set of all such points $\bvec x$ is the interior of $A$.

##### _definition:_ exterior point, exterior

For $A \subset \bb R^n$ and $\bvec x \in \bb R^n$, if there is an open rectangle $B$ such that $\bvec x \in B \subset \bb R^n \setminus A$, then $\bvec x$ is an exterior point of $A$.

The set of all such points $\bvec x$ is the exterior of $A$.

##### _definition:_ boundary point, boundary

For $A \subset \bb R^n$ and $\bvec x \in \bb R^n$, if every open rectangle $B$ containing $\bvec x$ contains points of both $A$ and $\bb R^n \setminus A$, then $\bvec x$ is a boundary point of $A$

The set of all such points $\bvec x$ is the boundary of $A$.

These definitions make sense intuitively — they match up with our idea of the boundary being "between two sides". Note that a set may or may not contain its boundary, but its interior and exterior of course do not.

Note also that the interior and exterior are obviously open (their definition includes looking at an open rectangle surrounding each point within them). Since the boundary is the complement of their (open) union, the boundary is closed.

### Compactness

One interesting thing that we can do with open sets is to try to "cover" a set with them — to find a collection of open sets whose union covers a particular set we are interested in. This allows us to study the points of $A$ by looking at the "local story" around them in the open set of the cover that contains them.

##### _definition:_ open cover

A collection of open sets, $\mathcal O$ is an open cover of the set $A$ if $A \subset \bigcup_{U \in \mathcal O} U$.

##### _example:_ open cover

The collection $\mathcal O = \set{(\frac{1}{n}, 1 - \frac{1}{n}) : n \in \bb N}$ is a cover of the open interval $(0, 1)$. It would be nice if we could throw away some of these open sets in the cover — particularly, if we only had to look at finitely many sets, that would be nice. However, with finitely many sets, there would be some largest $n$, $N$, leaving out real numbers less than $\frac{1}{N}$.

In fact, the situation where we can always reduce a cover of a set to a "finite sub-cover" is very nice, and non-trivial. It allows us to always reduce an infinite number of "neighbourhoods" to finitely many, and it turns out that it isn't just finite sets for which this is true.

##### _definition:_ compact

A set $A$ is compact if every open cover $\mathcal O$ of $A$ contains a finite subset that also covers $A$.

##### _example:_ finite sets are trivially compact

Any finite set is compact — for $n$ points in the set pick the at-most-$n$ open sets of the open cover necessary to contain the $n$ points.

##### _example:_ the harmonic numbers (with zero) are compact

The set $\set{\frac{1}{n} : n \in \bb N} \cup \set{0}$ is compact. This is because any open interval containing $0$ must contain infinitely many of the harmonic numbers, leaving only finitely many to be covered with at most that many open sets. So with any open cover, we pick the open set that covers $0$ and the finitely many open sets that contain each of the rest of the points giving us a finite sub-cover.

While the fact that compactness is useful will have to wait, we can show that there are non-trivial compact sets right now.

##### _theorem:_ the Heine-Borel theorem

The closed interval $[a, b]$ is compact.

###### _proof:_

We will show that $[a, b]$ is compact by looking at all the sets $[a, x]$ with $x \in [a, b]$ that are almost compact. Specifically, for any open cover of $[a, b]$, $\mathcal O$, consider
$$
A = \set{x \in [a, b] : [a, x] \text{ is covered by a finite subset of } \mathcal O}.
$$
Note that this set is non-empty (since $[a, a]$ is covered by the open set containing $a$) and is bounded above (by $b$). Thus, it has a least upper bound, $\alpha$. We will show that $A$ contains its least upper bound, and that least upper bound is $b$.

First, note that $\alpha \in U$ for some $U \in \mathcal O$ since $\mathcal O$ covers $[a, b]$. Let the interval in $U$ containing $\alpha$ be $I$. Then there must be some $x \in I$ with $x < \alpha$ and $x \in A$ (if there wasn't then the lower bound of $I$ would be a lesser upper bound on $A$). Thus, $[a, x]$ is covered by finitely many sets of $\mathcal O$, and $[a, \alpha]$ can be covered by adding at most one set ($U$, if needed).

If $\alpha < b$, then any $y > \alpha$ with $y \in U$ gives us $[a, y]$ covered by a finite subset of $\mathcal O$ (the finite sub-cover of $[a, \alpha]$, since $\alpha \in A$, plus $U$, if needed). This would make $\alpha$ not an upper bound, and thus, lead to a contradiction. Thus, $\alpha \ge b$, but also since $b$ is an upper bound, $\alpha \le b$, giving us $\alpha = b$.

It is easy to see that for a compact subset $B \subset \bb R^m$ and $\bvec x \in \bb R^n$, $\set{\bvec x} \times B \subset \bb R^{m + n}$ is compact — this just involves moving the open sets around.

##### _proposition:_ moving a subset around in space doesn't change compactness

For a compact subset $B \subset \bb R^m$ and $\bvec x \in \bb R^n$, $\set{\bvec x} \times B \subset \bb R^{m + n}$ is compact.

###### _proof:_

Suppose $\mathcal O$ is an open cover of $\set{\bvec x} \times B$. Then for every $\bvec y \in B$ we have $(\bvec x, \bvec y) \in U \in \mathcal O$. 

Since each $U$ is open, there is an open rectangle, $I \subset U$ such that $(\bvec x, \bvec y) \in I$. If we write $I$ as $(a_1, b_1) \times \cdots \times (a_m, b_m) \times (a_{m + 1}, b_{m + 1}) \times \cdots \times (a_{m + n}, b_{m + n})$, then by definition this means that $\bvec y \in (a_{m + 1}, b_{m + 1}) \times \cdots \times (a_{m + n}, b_{m + n})$. Call this set $\bar I$, and then the set of all such $\bar I$, $\bar{\mathcal O}$, is an open cover of $B$.

Since $\bar{\mathcal O}$ is an open cover, we can reduce it to a finite sub-cover $\set{\bar I_1, \ldots, \bar I_n}$. Thus, the corresponding $\set{I_1, \ldots, I_n}$ is a finite open cover of $\set{\bvec x} \times B$ and finally, the $\set{U_1, \ldots, U_n}$ corresponding to that is the desired finite sub-cover.

This allows us to make an even stronger assertion.

##### _proposition:_ moving a subset around in space allows us to cover an open neighbourhood around it

If $B \subset \bb R^m$ is compact and $\set{\bvec x} \times B$ (with $\bvec x \in \bb R^n$) has an open cover $\mathcal O$, then there is some open set $\bar U \subset \bb R^n$ such that $\bar U \times B$ is covered by a finite subset of $\mathcal O$.

###### _proof:_

Since $B$ is compact, $\set{\bvec x} \times B$ is compact, and thus, instead of looking at $\mathcal O$ we can look at the finite sub-cover $\bar{\mathcal O}$. 

Specifically, for each point $(\bvec x, \bvec y) \in W \in \mathcal O$, look at the open rectangle $U \times V \subset W$ containing it with $U \subset \bb R^n$. Since the sets $V$ form an open cover of $B$, they can be reduced to a finite sub-cover $\set{V_1, \ldots, V_k}$. Also note, that $\bvec x \in U$ for any $U$, and thus, we can also look at only finitely many of the open rectangles $U$ — the corresponding $\set{U_1, \ldots, U_k}$.

Since the finite intersection $\bar U = \bigcap_{i = 1}^k U_i$ is open, and is clearly covered by $\set{U_1, \ldots, U_k}$, we have that $\bar U \times B$ is covered by the finitely many (at most $k$) open sets $W_i \in \mathcal O$ that contain the open rectangles $U_i \times V_i$.

This gives us as a corollary the result that we're obviously working towards: that the product of any two compact sets is compact.

##### _corollary:_ the product of compact sets is compact

If $A \subset \bb R^n$ and $B \subset \bb R^m$ are compact, then $A \times B \subset \bb R^{m + n}$ is compact.

###### _proof:_

Suppose $\mathcal O$ is an open cover of $A \times B$. Then for each $\bvec x \in A$ it is an open cover of $\set{\bvec x} \times B$, and we have an open set $U_{\bvec x}$ such that $\bvec x \in U_{\bvec x}$ and $U_{\bvec x} \times B$ is covered by a finite subset of $\mathcal O$.

However, since the set of all of these open sets $\set{U_{\bvec x}}$ is an open cover of the compact set $A$, a finite subset $\set{U_1, \ldots, U_k}$ covers $A$. Then, since $U_i \times B$ is covered by a finite subset of $\mathcal O$ for each $i \in \bb N_n$, we can take the finite union of those finite subsets, to get an open sub-cover that covers all of $A \times B$.

This then allows us to characterise some compact sets on $\bb R^n$.

##### _corollary:_ closed rectangles are compact

Any closed rectangle $[a_1, b_1] \times \cdots \times [a_n, b_n] \subset \bb R^n$ is compact

###### _proof sketch:_

Do induction on the product of compact sets being compact, starting from the base case that $[a, b]$ is compact by the [[#_theorem _ the Heine-Borel theorem|Heine-Borel theorem]].

The corollary of this and its converse are also sometimes called the Heine-Borel theorem

##### _corollary:_ closed bounded sets are exactly the compact sets

A subset of $\bb R^n$ is compact if and only if it is closed and bounded.

###### _proof:_

First we will show that if a set $K \subset \bb R^n$ is closed and bounded, it is compact.

If $K$ is closed and bounded, then we can bound it within some closed rectangle $C$. If $\mathcal O$ is an open cover of $K$, then together with $\bb R^n \setminus K$ (which is open), we have an open cover of $C$. Since $C$ is compact, we can reduce the open cover to a finite sub-cover $\bar{\mathcal O}$. 

Since $K \subset C$, $K$ too is covered by $\bar{\mathcal O}$, and further, we can get rid of $\bb R^n \setminus K$ and still have it cover $K$. Thus, $\bar{\mathcal O} \setminus \set{\bb R^n \setminus K}$ is an finite subset of $\mathcal O$ that covers $K$.