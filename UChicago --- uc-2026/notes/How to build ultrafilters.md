---
tags:
- uc-2026/ultra/1
- uc-2026/ultra/2
- set
- top
---

Ultrafilters are an abstraction of the idea of a big subset of a set. This can be made precise — an ultrafilter on a set $I$ is the same thing as a finitely additive $0$-$1$ valued measure on $I, 2^I$.

##### _definition:_ filters, ultrafilters

A **filter** on a set $I$ is a subset $D$ of the power set $2^I$ such that
- $I \in D$,
- if $A \in D$ and $A \subseteq B \subseteq I$, then $B \in D$,
- if $A \in D$ and $B \in D$, then $A \cap B \in D$
- $\text{Ø} \in D$.

An **ultrafilter** is a filter such that for each $A \in 2^I$, either $A \in D$ or $I \setminus A \in D$.

---

Note that ultrafilters are maximal filters in a sense — adding any more sets would either break inclusion of finite intersections or the exclusion of the empty set.

##### _example:_ filters that are not ultrafilters

For an example of a filter that is not an ultrafilter, consider $I$ infinite and $D$ the set of cofinite sets. This is a filter, but not an ultrafilter, because we can always break $I$ into two infinite parts. We know how to do this if $I$ is countable. If $I$ is uncountable, then break off a countable subset.

---

How can we build ultrafilters then? The idea is that we can always add one of a new set or its complement to a filter. In fact, we can do this even when $D \subseteq 2^I$ is not a filter.

##### _lemma:_ you can always add a set or its complement

Suppose $D \subseteq 2^I$ has the following property — any finite intersection of elements of $D$ is non-empty. Then, for each $A \subseteq I$, either $D \cup \{ A \}$ or $D \cup \{ I \setminus A \}$ has the same property.

###### _proof:_

Suppose there is some finite collection of $X_{1}, \dots, X_{n} \in D$ such that $A \cap \bigcap X_{i}$ is empty. Then $\bigcap X_{i} \subseteq I \setminus A$. Then, for any finite collection $Y_{1}, \dots, Y_{m} \in D$, we must have $\bigcap Y_{i}$ cannot live in $A$ (else $\bigcap X_{i} \cap \bigcap Y_{i}$ would be empty). That is, $(I \setminus A) \cap \bigcap Y_{i}$ is non-empty.

---

Since you can always take the closure of this set under finite intersections and upward inclusion, we have a way to turn a filter $(I, D)$ into a filter that includes $A$ or $I \setminus A$. Then, by transfinite induction, we can build an ultrafilter from the filter.