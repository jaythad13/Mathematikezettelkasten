---
tags:
- comb
- math-55a
lecture: math-55a-2
---

##### _example:_ triple cups of ice cream

How many triple cones of ice cream are there, where we're choosing from $31$ flavours, we can repeat flavours, and order (obviously) matters? $31^3$ — just choose one of the $31$ flavours for each of the scoops. 

How many triple cups of ice cream are there where we're choosing from $31$ flavours, we can repeat flavours, and order doesn't matter. We can't just divide the answer for cones by $3!$ (for one, $31^3$ isn't even divisible by it), because not all permutations of all cups are distinct cones (a Neapolitan cup gives you $3!$ cones, but if you replace vanilla with another chocolate, the extra permutations you get by swapping them around don't make any difference).

We can solve this by dividing into cases for $1$, $2$, or $3$ distinct flavours in the cup:
$$
\binom{31}{1} + 2 \binom{31}{2} + \binom{31}{3}.
$$
Unfortunately, if we were really celebrating with lots of scoops, this would get tedious very quickly. The real answer is $31$

##### _definition:_ multichoose

$n$ multichoose $k$, denoted $\Big ( \binom{n}{k} \Big )$ is the number of ways to choose $k$ elements from an $n$ element set, with repetitions, but order doesn't matter. 

Another way to say this is that it's the number of ways to choose $k$ items from $n$ types of items (where you can choose as many of any particular type as you want).

Note that for this we can have $n < k$ as long as $n \ge 1$.

##### _theorem:_ the multichoose theorem

$$
\Big ( \binom{n}{k} \Big) = \binom{n + k - 1}{k}
$$

##### _proof:_

We use stars and bars to prove this. Think about choosing the $n$ flavours as dividing your $k$ scoops into $n$ partitions, where some of them can be empty. (Allotting your scoops to flavours).

We can draw this with stars and bars. There are $n - 1$ bars and $k$ stars. How many ways can we draw them? There are $n + k - 1$ total symbols, so just choose the $k$ that are stars. That's just $\binom{n + k - 1}{k}$.

##### _example:_ $n$injas and $k$andies

How many ways are there to divide $k$ (identical) $k$andies among $n$ $n$injas? $\Big ( \binom{n}{k} \Big )$! Stars and bars to prove it! Or the definition!

Note that this feels different from the idea of choosing items, because we want to think about choosing $k$andies, but here we're choosing ninjas to assign to each $k$andy.

##### _example:_ more dangerous ninjas

What if we need to give each $n$inja a $k$andy? Give each $n$inja one $k$andy, and then divide the rest among the $n$injas in any way.

Then there are $\Big ( \binom{n}{k - n} \Big )$ ways. But by the [[#_theorem _ the multichoose theorem|the multichoose theorem]] that is just $\binom{k - 1}{n - 1}$.

We can think of this with a different stars and bars analogy! Place $n - 1$ bars in the $k - 1$ spaces between the $k$andies so that there are no double bars close together.

##### _theorem:_ (not Pascal's) multichoose identity

$$
\Big( \binom{n}{k} \Big) = \Big ( \binom{n - 1}{k} \Big)
 + \Big ( \binom{n}{k - 1} \Big )$$
##### _proof sketch:_

How many ways are there to not give $n$inja $n$ any $k$andies? How many ways are there to give $n$inja $n$ at least one $k$andy?
