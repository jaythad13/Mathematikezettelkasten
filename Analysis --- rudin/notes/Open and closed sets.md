---
tags:
- rudin
- anal
- top
- self-study
---

For this section, $X$ denotes a metric space with metric $d$, and any points or subsets we mention are considered to be elements or subsets of $X$.

Recall the definitions of [[Metric spaces#_definition _ open set|open sets]] and [[Metric spaces#_definition _ closed set|closed sets]] in metric spaces. It turns out that open sets and closed sets are interesting in their own right and are incredibly useful. We will spend time learning why.

##### _examples:_ open sets

1) For any any metric space $X$, $X$ and $\emptyset$ are always open.
2) Open intervals $(a, b)$ in the real numbers with the Euclidean metric are always open: they are the prototypical examples of open sets!
3) Any open ball in $\bb{R}^n$, that is $\set{x \in \bb{R}^n: \Vert x - c \Vert < r, c \in \bb{R}^n, r \in \bb{R}^+}$ is open in $\bb{R}^n$.

##### _examples:_ closed sets

1) For any metric space $X$, $X$ and $\emptyset$ are always open.
2) The unit circle is closed in $\bb{R}^2$.
3) The complement of any open ball in $\bb{R}^n$ is closed in $\bb{R}^n$.

##### _examples:_ non-open, non-closed sets

The half-open interval $[0, 1)$ and its complement in $\bb{R}$, $(-\infty, 0) \cup [1, \infty)$ are both neither open nor closed.

These examples suggest a certain correspondence between open and closed sets. Specifically,

##### _theorem:_ Closed sets are complements of open sets

A set $E$ is closed if and only if its complement is open.

###### _proof:_

First, we will prove that if $E$ is closed, its complement is open.

Suppose $E$ is closed. Then, by definition, it contains all of its limit points, and its complement $E^c$ contains none of its limit points.

Thus, every point in $E^c$, $x$ has some neighbourhood containing no distinct points of $E$ (as otherwise it would be a limit point), and thus, no distinct points of $E$ (since $x$ being in $E^c$, cannot be in $E$). Then, that neighbourhood is completely contained in $E^c$.

We have constructed a neighbourhood completely contained in $E^c$ for any arbitrary point in $E^c$, and have thus, shown that $E^c$ is open.

Now we will show that if $E^c$ is open, $E$ is closed.

Suppose $E^c$ is open. Then, by definition, every point in $E^c$ has some neighbourhood completely contained in $E^c$.

Thus, there is no point in $E^c$ such that for every $r > 0$, $N_r(x)\cap E \setminus \set{x}$ is nonempty (otherwise, that point would have no neighbourhood completely contained in $E^c$). That is, there is no limit point of $E$ in $E^c$. Since there are no limit points of $E$ in $E^c$, any limit points of $E$ (in the metric space $X$) must be in $E$, and thus, $E$ is closed.

##### _corollary:_ Open sets are complements of open sets

A set $E$ is open if and only if its complement is open.

This fact becomes even more useful when combined with the extended version of De Morgan's law:

##### _theorem:_ De Morgan's law

Let $\set{E_\alpha}$ be a collection of sets $E_\alpha$ indexed by $\alpha \in A$. Then
$$
(\bigcup_{\alpha \in A} E_\alpha)^c = \bigcap_{\alpha \in A} (E_\alpha^c)
$$

###### _proof:_

Let $U = (\bigcup_{\alpha \in A} E_\alpha)^c$ and $I = \bigcap_{\alpha \in A} (E_\alpha^c)$.

If $x \in U$ then $x \notin E_\alpha$ for all $\alpha \in A$, as if it was in $E_\alpha$ for any $\alpha$, then we would have $x \in U^c = \bigcup_{\alpha \in A} E_\alpha$. Since $x \notin E_\alpha$, $x \in E_\alpha^c$ for all $\alpha \in A$. Thus, $x \in I$. This gives us $U \subseteq I$.

If $x \in I$, then $x \in E_\alpha^c$ for all $\alpha \in A$. Thus, $x \notin E_\alpha$ for all $\alpha \in A$. Thus, $x \notin U^c = \bigcup_{\alpha \in A} E_\alpha$ giving us $x \in U$. This gives us $I \subseteq U$.

Together, these give us $U = I$.

##### _proposition:_ (Potentially infinite) unions and finite intersections of open sets are open

For any collection $\set{G_\alpha}$ of open sets $G_\alpha$ indexed by $\alpha \in A$, $\bigcup_{\alpha \in A} G_\alpha$ is open. If $\set{G_\alpha}$ is finite, $\bigcap_{\alpha \in A} G_\alpha$ is open.

###### _proof:_

First we will prove that the union of any collection of open sets is open.

Let $U = \bigcup_{\alpha \in A} G_\alpha$.

Consider any point $p \in U$. We must have $p \in G_\alpha$ for some $\beta \in A$. 

Since $G_\beta$ is open, we also have some neighbourhood of $p$, $N_r(p)$ contained in $G_\beta$. Thus, $N_r(p)$ is also contained in $U$. 

Thus, we've shown that we have a neighbourhood of any arbitrary point in $U$ contained in $U$. That is, $U$ is open.

Now we will show that the intersection of a finite collection of open sets is open.

Let $I = \bigcap_{\alpha \in A}G_\alpha$ where $A$ is a finite set.

Consider any point $p \in I$. We must then have $p \in G_\alpha$ for every $\alpha \in A$. 

Since each $G_\alpha$ is open, we have a neighbourhood $N_{r_\alpha}(p)$ contained in each $G_\alpha$. The intersection of these neighbourhoods must be contained in $I$ and is itself a neighbourhood $N_{r_\beta}(p)$ where $r_\beta = \min_{\alpha \in A}{\set{r_\alpha}}$. 

Note that $r_\beta$'s existence is only guaranteed if $A$ is finite.

With $N_{r_\beta}$ we have shown that we have a neighbourhood of an arbitrary point in $I$ contained in $I$. Thus, $I$ is open.

##### _corollary:_ Finite unions and (potentially infinite) intersections of closed sets are closed

For any collection $\set{F_\alpha}$ of open sets $F_\alpha$ indexed by $\alpha \in A$, $\bigcap_{\alpha \in A} F_\alpha$ is open. If $\set{F_\alpha}$ is finite, $\bigcup_{\alpha \in A} F_\alpha$ is open.

###### _proof:_

First we will show that the intersection of any collection of closed sets is closed.

Let $I = \bigcap_{\alpha \in A} F_\alpha$.

Since each $F_\alpha$ is closed, each $F_\alpha^c$ is open. By [[#_theorem _ De Morgan's law|De Morgan's law]],
$$
I^c = \bigcup_{\alpha \in A} (F_\alpha^c).
$$
By the proposition, $I^c$ is open, and thus, $I$ is closed.

Now we will show that the union of any finite collection of closed sets is closed.

Let $U = \bigcup_{\alpha \in A}F_\alpha$ where $A$ is a finite set.

Since each $F_\alpha$ is closed, each $F_\alpha^c$ is open. Again, by [[#_theorem _ De Morgan's law|De Morgan's law]],
$$
U^c = \bigcap_{\alpha \in A}(F_\alpha^c).
$$
By the proposition, $U^c$ is open, and thus, $U$ is closed.

##### _example:_ a non-open infinite intersection of open sets

Consider the collection of open sets $\set{G_n}$ with $G_n = (-\frac{1}{n}, \frac{1}{n})$ for each $n \in \bb{N}$ in the metric space $\bb{R}$.

By the Archimedean property, for any $x > 0$ we can find $n \in \bb{N}$ with $\frac{1}{n} < x$ and for any $x < 0$ we can find $n \in \bb{N}$ with $-\frac{1}{n} > x$. Thus, for any $x \neq 0$, there is some $G_n$ such that $x \notin G_n$. Note that $0 \in G_n$ for all $n \in \bb{N}$.

Thus, the intersection $\bigcap_{n \in \bb{N}} G_n = \set{0}$, which is obviously not open in $\bb{R}$.
