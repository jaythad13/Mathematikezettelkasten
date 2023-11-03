---
tags:
- comb
- math-55a
lecture: math-55a-2
---

##### _example:_ triple cups of ice cream

How many triple cups of ice cream are there where we're choosing from $31$ flavours, we can repeat flavours, and order doesn't matter.

We can solve this by dividing into cases for $j$ same flavours.

##### _definition:_ multichoose

$n$ multichoose $k$, denoted $\Big ( \binom{n}{k} \Big )$ is the number of ways to choose $k$ elements from an $n$ element set, with repetitions, but order doesn't matter

Note that for this we can have $n < k$ as long as $n \ge 1$.

##### _theorem:_ the multichoose theorem

$$
\Big ( \binom{n}{k} \Big) = \binom{n + k - 1}{n}
$$

##### _proof:_

We use stars and bars to prove this. Think about choosing the $n$ flavours as dividing your $k$ scoops into $n$ partitions, where some of them can be empty. (Allotting your scoops to flavours).

We can draw this with stars and bars. There are $n - 1$ bars and $k$ stars. How many ways can we draw them? There are $n + k - 1$ total symbols, so just choose the $k$ that are stars. That's just $\binom{n + k - 1}{k}$.

##### _example:_ $n$injas and $k$andies

How many ways are there to divide $k$ (identical) kandies among $n$ ninjas? $\Big ( \binom{n}{k} \Big )$! Stars and bars to prove it! Or the definition!

##### _example:_ more dangerous ninjas

What if we need to give each ninja a kandy? Give each ninja one kandy, and then divide the rest among the ninjas in any way.

Then there are $\Big ( \binom{n}{k - n} \Big )$ ways. But by the [[#_theorem _ the multichoose theorem|the multichoose theorem]] that is just $\binom{k - 1}{n - 1}$.

We can think of this with a different stars and bars analogy! Place $n - 1$ bars in the $k - 1$ spaces between the kandies so that there are no double bars close together.

##### _theorem:_ weirdo multichoose identity

$$
\Big( \binom{n}{k} \Big) = \Big ( \binom{n - 1}{k} \Big)
 + \Big ( \binom{n}{k - 1} \Big )$$
##### _proof:_

How many ways are there to not give ninja $n$ any kandies? How many ways are there to give ninja $n$ at least one kandy?
