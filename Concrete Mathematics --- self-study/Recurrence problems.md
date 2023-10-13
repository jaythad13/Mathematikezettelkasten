---
tags:
- self-study
- comb
---

### The Tower of Hanoi

One good motivating example for thinking about recurrence is the Tower of Hanoi, invented by French mathematician Edouard Lucas as the problem of Benares temple. The statement of the original problem is roughly

> The Kashi Vishwanath temple in Vanarasi contains a room with high ceilings from up to which three time worn poles stretch, almost kissing them. At the start of time, on the first pole were $64$ annuli of pure, solid gold, stacked from the largest to the smallest from bottom to top. Since then the priests of the Kashi Vishwanath temple have been moving them over to the third pole, one annulus at a time, taking care never to crush a smaller annulus with a larger one above it. What is the least number of times they must move annuli in order to wholly transfer the annuli to the third post?

An actual quote from the original publication is

> According to an old Indian legend, the Brahmins have been following each other for a very long time on the steps of the altar in the Temple of Benares, carrying out the moving of the Sacred Tower of Brahma with sixty-four levels in fine gold, trimmed with diamonds from Golconde. When all is finished, the Tower and the Brahmins will fall, and that will be the end of the world!

The Tower of Hanoi is just the same problem with $8$ disks

We generalise this problem to $n$ annuli and forget pedantry, just calling the annuli disks. Note that this generalisation allows us to look at small cases first, a technique that is almost always useful when solving math problems. It is also useful in the obvious sense: if we solve the problem for all natural numbers $n$ then we have solved the Tower of Hanoi, the problem of Benares temple, the Tower of Brahma, and any other _exotic_ names white mathematicians may assign to problems.

The other strategy we use is formalism: by explicitly naming the things we care about we can manipulate them more easily. In particular using functions (in this case, [[Sequences|sequences]], which are just functions from $\bb{N}$) allows us to very directly manipulate the things we care about. Thus, we let $T_n$ denote the least number of moves for $n$ disks.

We can get some easy small answers. Some trivial cases are
$$
T_0 = 0 \text{ and } T_1 = 1.
$$
These are easy to prove. Vacuously, moving $0$ disks takes $0$ moves. Moving $1$ disk requires at least $1$ move, and we can achieve it in one move.

Thinking about the problem some more can also give us the more difficult case
$$T_2 = 3.$$For $n = 3$  we can then moving the two smallest disks on to the second post, then move the third disk to the third post, and finally, move the two disks to the third post on top of the third disk. This gives us a rough idea of an algorithm and the value of $T_3$.

Again, here generalisation is useful because it allows us to think about the algorithm, for any $n$.

##### _algorithm:_ recursive Tower of Hanoi algorithm

In order to move $n$ disks from post $A$ to post $C$ (when we have three posts: $A$, $B$, and $C$)
1) Move the $n - 1$ smallest disks from post $A$ to post $B$ (using this algorithm).
2) Move the $n$th disk to post $C$.
3) Move the $n-1$ disks from post $B$ to the post $C$ (using this algorithm).

Note that this algorithm references itself. We call this algorithm recursive. It's implied that we know how to move one disk between two empty posts, and that moving no disks involves doing nothing but often, when we define a recursive algorithm, we also have to define some _base case._

Since this algorithm is guaranteed to move the $n$ disks (we can show this by [[Peano axioms|induction]]), we know that the least number of steps to move $n$ disks is not more than the number of steps for this algorithm. That is 
$$
T_n \le 2 T_{n-1} + 1 \text{ for } n \in \bb{N}.
$$

Now that we have a way to do this, we can ask if this is the best we can do. It turns out that it is, and we just have to think up a clever enough argument for it.

Moving $n$ disks from $A$ to $C$ requires moving the $n$th disk from $A$ to $C$. But that requires having no disks on top of the $n$th disk, and no disks on $C$, which means we must first move $n - 1$ disks from post $A$ to $B$. Once we have moved the $n$th disk, we still have to move the $n - 1$ disks from $B$ to $C$ on top of the $n$th disk.

At the very least, we need to perform all of these steps. Even if we use the fewest moves for each step, we have
$$
T_n \ge 2 T_{n - 1} + 1 \text{ for } n \in \bb{N}.
$$
Combining the two inequalities and our value for $T_0$ gives us a way to compute $T_n$ for any $n$ we want:
$$
T_0 = 0
$$
$$
T_n = 2 T_{n - 1} + 1 \text{ for } n \in \bb{N}.
$$

We call this a recurrence relation.

##### _definition:_ recurrence relation

For a function $a : \bb{N} \to S$ where $S$ is some set and $n \mapsto a_n \in S$, we say we have a recurrence relation for $a$ if we can completely define $a$ by some function
$$
\varphi : \bb{N} \times S^k \to S
$$
such that $$a_n = \varphi (n, a_{n - 1}, \ldots a_{n - k})$$and some initial fixed values  $$a_j = \alpha_j \in S \text{ for all } j \in \bb{N}_k.$$
Sometimes we may consider functions $a : \bb{Z} \to S$ satisfying a similar definition to be recurrence relations too, just so that we don't have trivial exceptions.

##### _example:_ computing $T_4$

$$
T_4 = 2 T_3 + 1 = 2 (2 T_2 + 1) + 1 = 2 (2(2 T_1 + 1) + 1) + 1 = 2 (2(2 (2 T_0 + 1) + 1) + 1) + 1
$$

$$
= 2 \times (2 \times (2 \times (2 \times 0 + 1) + 1) + 1) + 1 = 15.
$$

It's clear hear that while computing $T_n$ is certainly possible by just following this chain of functions down till $T_0$ it gets tedious quickly. A closed form for this function would be much nicer.

Looking at the value of $T_n$ for various small $n$ gives us some idea of what a closed form for $T_n$ might be:
$$T_0 = 0$$
$$T_1 = 1$$
$$T_2 = 3$$
$$T_3 = 7$$
$$T_4 = 15$$
$$T_5 = 31.$$

Specifically, these $T_n$ look a lot like $2^n - 1$. While we should be careful about assuming that this trend continues forever, there is no harm in investigating it. The recurrence relation we have also strongly suggests this: our recurrence relation tells us that $T_n$ is always just a little more than double $T_{n-1}$, just as we'd expect if we're right about the closed form we've guessed.

We can check whether $T_n$ really is $2^n$ by [[Peano axioms|induction]] on $\bb{N} \cup \{0\}$:

We know that $T_0 = 1 = 2^0 - 1$. If $T_k = 2^k - 1$, then $T_{k+1} = 2(2^k - 1) + 1 = 2^{k+1} - 1$.

Thus, by induction, $T_n = 2^n - 1$ for all $n \in \bb{N} \cup \{0\}.$

Thus, we've proven

##### _theorem:_ The Tower of Hanoi

The least number of moves to finish the tower of Hanoi is $2^8 - 1$.

### Lines in a plane

We can also use recurrence relations to solve more explicitly geometric problems. For example, a natural question to ask is, "How many pieces can you slice a pizza into by making $n$ straight cuts?" More specifically, we are concerned with the maximum number of pieces. Typically we write this problem as

> What is the maximum number of regions defined by $n$ lines in the plane?

since considering a circle of arbitrary size is the same as considering the whole plane. We let the answer be denoted $L_n$.

Again, looking at small cases can be fruitful. We can see clearly that zero lines leave the plane as one region, one line divides the plane in two, and two lines divide the plane in four regions.

![[Recurrence_problems_S2_no_lines.jpeg]]
$$
L_0 = 1
$$

![[Recurrence_problems_S2_one_line.jpeg]]
$$
L_1 = 2
$$

![[Recurrence_problems_S2_two_lines.jpeg]]
$$
L_2 = 4
$$

This seems to suggest that $L_n = 2^n$. That would imply that each new line we draw splits every previous region into two new regions. However, when we check $L_3$ we find that it seems impossible to do better than $L_3 = 7$. 

![[Recurrence_problems_S2_three_lines.jpeg]]
$$L_3 = \text{?}$$

If this is indeed the best we can do, each new line doesn't split every previous region. Since it seems hard to do any better, it's probably a good idea for us to think about what really happens when we add a new line. How many regions does it split? Does it depend on how we choose the line? If so, does that get affected by larger values of $n$. 

Obviously, the most important of those questions is the first. Note that there are exactly two ways for a new line to split a convex region: 
1) the new line can intersect one of the region's boundary lines at a point that is not their intersection
or
2) or the new line can pass through the vertex of the region such that it is divided into two segments by that point: one that is completely contained by the complement of the region and one that has a non-empty intersection with the region.
These can be proven to be the only two ways to split a convex region by checking all the possibilities that don't meet the conditions. We know that we don't have to consider concave regions because we start with a convex region and lines always divide convex regions into convex regions (then by induction...). 

Note that in the first case, by intersecting the $k$ lines in this way, the new line produces the $k + 1$ new regions, whereas in the second case the new line produces $k - 1$ regions. Thus, in order to produce the maximum number of new regions, the new line should intersect the maximum number of lines in the first way. Since for the $n$th new line, there are $n - 1$ other lines which it can intersect at most once, the new line can intersect, at most, $n - 1$ lines in the first way described, producing, at most, $n$ new regions. This gives us an upper bound on $L_n$, namely
$$
L_n \le L_{n - 1} + n.
$$

It turns out that we can actually achieve the optimal line that intersects each old line at a point that is not the intersection point of any other lines. By geometry, we know that any non-parallel lines must intersect. Since there are only finitely many (specifically, $n - 1$) previous lines, we can just choose the $n$th line to have a different slope from all of them. 

![[Recurrence_problems_S2_rotate_nth_line.jpeg]]

Furthermore, since there are only finitely many intersection points of those lines (each pair of lines can only intersect once so the number of intersection points is less than $\binom{n - 1}{2}$) we can translate the $n$th line until it does not contain any of the previous intersection points.

![[Recurrence_problems_S2_translate_nth_line.jpeg]]

Thus, we can get the recurrence relation
$$
\begin{gathered}
L_0 = 1 \\
L_n = L_{n - 1} + n.
\end{gathered}
$$
We can see by [[Peano axioms|induction]] that $L_n = 1 + \sum_{k = 1}^n n$ which in turn, again by [[Peano axioms|induction]] we can evaluate to give us
$$
L_n = 1 + \frac{n(n + 1)}{2}.
$$
Thus we've proven

##### _theorem:_ the plane division problem

$n$ lines can divide the plane into a maximum of $1 + \frac{n(n + 1)}{2}$ regions.