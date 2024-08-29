---
tags:
- math-157/2
- prob
---

Conditional probability is a way of calculating the probability of an event happening given another event happening — you're more likely to test positive for flu if you actually have the flu (or so you hope).

##### _definition:_ conditional probability

The probability of $A$ conditioned on $B$, $\mathbb{P}(A \mid B)$ is $\mathbb{P}(A \cap B) / \mathbb{P}(B)$.

The law of total probability follows easily from this definition — it says we can split up the probability of an event into disjoint cases of the event.

##### _theorem:_ law of total probability

For any disjoint events $B_{1}, \dots, B_{n}$ such that $\bigsqcup_{i = 1}^n B_{i}$ is the universe
$$
\mathbb{P}(A) = \mathbb{P}(A \mid B_{1}) \mathbb{P}(B_{1}) + \dots + P(A \mid B_{n}) \mathbb{P}(B_{n}) 
$$

###### _proof:_

Since the events are disjoint and spanning, we can write
$$
A = \bigsqcup_{i = 1}^n A \cap B_{i}
$$
which directly gives us
$$
\begin{split}
\mathbb{P}(A) & = \sum_{i = 1}^n \mathbb{P}(A \cap B_{i}) \\
 & = \sum_{i  =1}^n \mathbb{P}(A \mid B_{i}) \mathbb{P}(B_{i})
\end{split}
$$
##### _example:_ the game of craps

The game of craps works as follows —
- roll two dice to get a total $x$
- if $x = 7$ or $11$, you win immediately
- if $x \in \{ 2, 3, 12 \}$, you lose immediately
- if $x$ is anything else, roll until you get $x$ again (in which case you win) or you get $x = 7$ (in which case you lose)

What's the probability of winning at craps? One easy way to do this is to check the probability for each case of $x$. That is we can use the law of total probability!

We know that $\mathbb{P}(\text{win} \mid x = 7)$ and $\mathbb{P}(\text{win} \mid x = 11)$ are $1$ and $\mathbb{P}(\text{win} \mid x = 2)$, $\mathbb{P}(\text{win} \mid x = 3)$, and $\mathbb{P}(\text{win} \mid x = 12)$ are all $0$. We just need to check the probability that we win after rolling one of the other values of $x$.

The obvious way to this is infinite series — just sum up over all $n$ the probability that the first $n$ throws were neither $a$ nor $7$ and that the $n$th throw is $a$. For example, this gives us $1 / 3$ for $a = 4$.

Another way to do this is to realise that a non-winning throw doesn't change the outcomes of any of the next throws. That is, if $\Pi_{a}$ is the probability of rolling $a$ before $7$, then $\Pi_{a} = \mathbb{P}(x = a) +  \mathbb{P}(x \neq a) \Pi_{a}$. 

Finally, we do this problem by comparing the probability of rolling a $7$ and the probability of rolling an $a$. We have to end in one of them, so we can say that the probability is $\frac{\mathbb{P}(x = a)}{\mathbb{P}(x = a) + \mathbb{P}(x = 7)}$.

Whatever you use, in the end, summing everything up the gives us $0.49\overline{29}$. This is almost fair! So how do casinos win so often?

##### _example:_ the gambler's ruin problem

If I make $\$1$ bets starting from $\$i$ with probability $p$ of winning (and $q = 1 - p$ of losing), what's the probability that I eventually get to $\$n$ or go broke trying? Particularly, we might consider trying to get $\$100$ from $\$60$ while playing craps.

Call the probability I win $a_{i}$. If I win, I have $\$ i + 1$ and need to get to $\$ n$ and otherwise I have $\$ i - 1$ and need to get to $\$ n$. That is, by the law of conditional probability,
$$
a_{i} = pa_{i + 1} + q a_{i - 1}.
$$
Using $1 = p + q$ we can convert this into a much simpler recurrence —
$$
p(a_{i + 1} - a_{i}) = q(a_{i} - a_{i - 1}).
$$
That is,
$$
a_{i + 1} - a_{i} = \frac{q}{p}(a_{i} - a_{i - 1}).
$$
Since $a_{0} = 0$ (you can't win with nothing to bet), we can get
$$
a_{i} - a_{i - 1} = \left( \frac{q}{p} \right)^{i - 1} a_{1}.
$$
Adding these, you get a telescoping sum —
$$
a_{i} - a_{1} = a_{1} \left( \left( \frac{q}{p} \right)^1 + \dots + \left( \frac{q}{p} \right)^{i - 1} \right)  
$$
or, if $\frac{q}{p} \neq 1$, by the finite geometric series formula
$$
a_{i} = a_{1} \left( \frac{1 - (q / p)^i}{1 - q / p} \right).
$$
using the fact that $a_{n} = 1$ (you've already won if you already have the money), you can get the value for $a_{1}$ and thus, all $a_{i}$. If $q/p = 1$, adding up $i$ ones and dividing by $n$ gives you $a_{i} = i / n$.

Even though $\lim_{ p/q \to 1} a_{i}$ is the same as $a_{i}$ for $p/q = 1$ as $p / q$ decreases, $a_{i}$ decreases rapidly. For example, $a_{60}$ is $0.6$ for $p / q = 1$ but $0.28$ for $p/q = 0.493 / 0.507$ (craps). By the time you get to roulette odds ($p \approx 0.47$).

Note that you can improve your odds with a better betting strategy — if you bet $\$40$, you have a $0.493$ chance of winning on just your first try. Even if you fail on your first try, there are other ways to win. Adding all of these up gives you a $0.59$ chance of winning. However, this still isn't fair because you have a higher downside — you stand to lose $\$60$ versus winning $\$40$. Fair odds would be $0.6$ but results from stochastic theory say betting $\$40$ gives you the best odds you can get (from an initial of $\$60$).