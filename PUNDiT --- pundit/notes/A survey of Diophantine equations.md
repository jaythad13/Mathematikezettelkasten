---
tags:
- nt
- pundit
---

An obviously natural question to ask is for positive integers that give us $a^2 + b^2 = c^2$? What are all the positive integers?
##### _proposition:_ the ratio of a Pythagorean triple

For any Pythagorean triple $(a, b, c)$, there exist integers $m$ and $n$ such that
$$
a:b:c = 2mn:m^2 - n^2 : m^2 + n^2.
$$
##### _proof:_

Consider $\frac{m}{n} = \frac{a}{c - b}$. Then $a = \frac{m}{n}(c - b)$. Substituting this value for $a$ into $a^2 + b^2 + c^2$, we get $\frac{a}{b} = \frac{2 m n}{m^2 + n^2}$ and $\frac{m^2 - n^2}{m^2 + n^2}$.

But why would you ever bother to write $\frac{m}{n} = \frac{a}{c - b}$? 

Note that if $x = \frac{a}{c}$ and $y = \frac{b}{c}$, then we get $\frac{m}{n} = \frac{y+1}{x}$. This gives us a line $y = \frac{m}{n} x - 1$, a line, and by trigonometry, we get $x^2 + y^2 = 1$, a circle. %% go back to this %%

This generalises!

Consider Pythagorean quadruples! Then, to find them all, we can apply the same technique: look at their ratio, not the numbers themselves.

However, it turns out that you need complex numbers to prove a similar result:

##### _proposition:_ The ratio of Pythagorean quadruples

If $(a, b, c, d)$ is a Pythagorean quadruple, then there exist integers $m$, $n$, and $p$ such that
$$
a:b:c:d = 2mn : 2mp : m^2 - n^2 - p^2: m^2 + n^2 + p^2.
$$

But how do we generate all of the Pythagorean quadruples? It turns out that the ratio works backwards! Any four integers with that ratio are Pythagorean quadruples!

Then we can choose any
$$
	\begin{gathered}
		a = 2 m n q \\
		b = 2 m p q \\
		c = (m^2 - n^2 - q^2) \\
		d = (m^2 + n^2 + q^2)
	\end{gathered}
$$
to get a Pythagorean quadruple. But to get all of the Pythagorean quadruples, we need to let $q$ be a rational sometimes, which isn't pleasant. If we only allow integer $q$, then there are Pythagorean quadruples we can't hit. Worse yet, there's a different integer function that does give the same missed quadruples (see $\alpha, \beta, \gamma, \delta$ equation).

One different approach we can take is to generalise the equation itself. For example, Pythagorean triples correspond to the quadratic in three variables:
$$
a^2 + b^2 - c^2 = 0.
$$
Instead, we can study the whole class of equations
$$
A a^2 + B ab + C b^2 + D ac + E bc + F c^2 = 0
$$
for integer $A, B, C, D, E, F$.