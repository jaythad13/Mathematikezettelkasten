---
tags:
- prob
- math-157/1
---

In probability we want to assign a number $p \in [0, 1]$ that represents the proportion of some desired event (encoded by a subset) in a space of all possibilities $\Omega$. This is easiest when $\Omega$ is a finite set — the case of discrete probability.

##### _definition:_ discrete measure space, discrete probability space, event, probability

A **(discrete) measure space** $\mu, \Omega$ is a pair of a set $\Omega$ and a measure — a function $\mu : 2^\Omega \to \mathbb{R}_{\geq 0}$ such that $\mu(U) = \sum_{\omega \in U} \mu(\{ \omega \})$. We often abbreviate $\mu(\{ \omega \})$ to $\mu(\omega)$.

A **(discrete) probability space** is a discrete measure space $\mathbb{P}, \Omega$ such that $\mathbb{P}(\Omega) = 1$. Note that we usually write $\mathbb{P}$ for the measure on the probability space.

An **event** $E$ in a probability space $\mathbb{P}, \Omega$ is a subset. The **probability** of the event is $\mathbb{P}(E)$.

---

From here on, let $\mathbb{P}, \Omega$ be a discrete probability space.

##### _example:_ a (possibly unfair) coin

The set $\{ H, T \}$ with $\mathbb{P}(H) = p$ and $\mathbb{P}(T) = 1 - p$ models a coin that comes up heads about $pn$ times out of $n$ tosses. 

---

What if we want to model multiple of the same probability space, acting "independently" at the same time, or two different probability spaces both at the same time? For example, what if we want to model two of the weighted coin above with a die? This is modelled by the product of probability spaces.

##### _definition:_ products of probability spaces

The **product of two probability spaces** $\mathbb{P}_{1}, \Omega_{1}$ and $\mathbb{P}_{2}, \Omega_{2}$ is $\mathbb{P}, \Omega$ with $\Omega = \Omega_{1} \times \Omega_{2}$ and $\mathbb{P}$ given by $\mathbb{P}(\omega_{1}, \omega_{2}) = \mathbb{P}_{1}(\omega_{1}) \mathbb{P}_{2}(\omega_{2})$. 

The **product of $n$ probability spaces** $\mathbb{P}_{i}, \Omega_{i}$ is defined recursively
$$
\prod_{i = 1}^n (\mathbb{P}_{i}, \Omega_{i}) = (\mathbb{P}_{n}, \Omega_{n}) \times \prod_{i = 1}^{n - 1} (\mathbb{P}_{i}, \Omega_{i}).
$$

---

Note that
$$
\mathbb{P}(E_{1}) \mathbb{P}(E_{2}) = \mathbb{P}(E_{1} \times E_{2}) = \mathbb{P}((E_{1} \times \Omega_{2}) \cap (\Omega_{1} \times E_{2}))
$$
Since we *define* this to model the idea that any two product events $E_{1} \times \Omega_{2}$ and $\Omega_{1} \times E_{2}$ are independent, this also motivates our definition for independence within a probability space.

##### _definition:_ independence, dependence

Two events $E_{1}, E_{2} \subseteq \Omega$ are **independent** if $\mathbb{P}(E_{1} \cap E_{2}) = \mathbb{P}(E_{1}) \mathbb{P}(E_{2})$. Otherwise they are **dependent**.

---

### Random variables

Sometimes a real value we want to deal with depends on our probability space. For example, a coin toss bet depends on the probability space of the coin toss. My bank balance is $X = \$100$ if the coin comes up heads and $X = -\$100$ otherwise. A random variable is a useful gadget we can attach to an outcome that depends on a probability space.

##### _definition:_ discrete random variable

A **(discrete) random variable** $X$ on (discrete) $\mathbb{P}, \Omega$ is a function $X : \Omega \to \mathbb{R}$.

Note that the set of random variables naturally has the structure of the vector space $\mathbb{R}^\Omega$. We will use this vector space structure to define the sum $X + Y$ and scaling $\lambda X$ of random variables.

---

Note that for any random variable $X$ and any $f : \mathbb{R} \to \mathbb{R}$, we can create a new random variable $f \circ X : \Omega \to \mathbb{R}$.

We can very naturally define the probability that a random variable takes on a certain value, or even values in a certain range.

##### _definition:_ probability of a random variable

Let $X$ be a random variable on $\mathbb{P}, \Omega$. Let $U \subseteq \mathbb{R}$. The **probability** that $X \in U$ is $\mathbb{P}(X \in U) = \mathbb{P}(X^\text{pre}(U))$.

We sometimes write $\mathbb{P}(X = \alpha)$, $\mathbb{P}(X < \beta)$, et c. for the obvious corresponding $U \subseteq \mathbb{R}$.

---