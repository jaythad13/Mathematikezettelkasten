---
tags:
- self-study
- lin-alg
- ladr/7A
---

[[Linear algebra done right --- ladr/notes/The Riesz representation theorem#_theorem _ Riesz representation theorem|The Riesz representation theorem]] allows us to identify vectors with [[Dual spaces|linear functionals]] through the map $v \mapsto \left< -, v \right>$. However, this is only an isomorphism over real spaces — it fails to be linear because the [[Inner product spaces|inner product]] is only sesquilinear. Note that this notion of flipping the vectors (in matrix form)
$$
\begin{bmatrix}
v_{1} \\
\vdots \\
v_{n}
\end{bmatrix} \mapsto \begin{bmatrix}
v_{1} &  \cdots &  v_{n}
\end{bmatrix}
$$
corresponds to the matrix transpose in some sense. We can combine the intuition of the Riesz representation theorem (flipping vecotrs) with that of the transpose (that the map should go the other way) to get a truly linear map — the adjoint.

##### _definition:_ adjoint, $T^*$

For $T \in \mathcal{L}(V, W)$, the adjoint of $T$ is the function $T^* : W \to V$ such that
$$
\left< Tv, w \right> = \left< v, T^* w \right> 
$$
for every $v \in V$ and $w \in W$.

Note that this definition requires the Riesz representation theorem to make sense. That is, if we fix $w \in W$, then $v \mapsto \left< Tv, w \right>$ is a linear functional on $V$ that we can only represent by the inner product with $T^* w$ because the Riesz representation theorem guarantees that a unique $T^* w$ exists.

##### _example:_ adjoint of a real linear map

Consider $T : \mathbb{C}^3 \to \mathbb{C}^2$ (both with the Hermitian inner product) by
$$
T(v_{1}, v_{2}, v_{3}) = (v_{2} + 3 v_{3}, 2 v_{1}).
$$
The adjoint is a map $T^*$ such that for any $(v_{1}, v_{2}, v_{3}) \in \mathbb C^3$ and $(w_{1}, w_{2}) \in \mathbb{C}^2$, we have
$$
(v_{2} + 3 v_{3}, 2v_{1}) \cdot (w_{1}, w_{2}) = (v_{1}, v_{2}, v_{3}) \cdot T^*(w_{1}, w_{2})
$$
We write left hand side as $2v_{1} \overline{w_{2}} + v_{2} \overline{w_{1}} + 3 v_{3} \overline{w_{1}} = (v_{1}, v_{2}, v_{3}) \cdot (2w_{2}, w_{1}, 3 w_{1})$ which clearly suggests that $T^* : (w_{1}, w_{2}) \mapsto (2w_{2}, w_{1}, 3 w_{1})$.

Notice that here $T^*$ is a linear map, just like we want! Also, notice how keeping the $w$ terms in the second slot everywhere means the conjugates just cancel out!

##### _example:_ adjoint of $T$ for $\dim \operatorname{range} T \le 1$

Fix $v_{0} \in V$ and $w_{0} \in W$ and let $Tv = \left< v, v_{0} \right> w_{0}$. Note that this characterises all linear maps with range of dimension less than $1$. Just choose $w_{0} = Tv_{0}/\lVert v_{0} \rVert^2$. 

Suppose $v \in V$ and $w \in W$. Then
$$
\begin{split}
\left< Tv, w \right> & = \left< \left< v, v_{0} \right> w_{0}, w \right> \\
 & = \left< v, v_{0} \right> \left< w_{0}, w \right> \\
 & = \left< v, \left< w, w_{0} \right> v_{0} \right>. 
\end{split}
$$
Thus, $T^* w = \left< w, w_{0} \right> v_{0}$, a linear map again! Basically, this says that you can do the projection in $V$ first or $W$ first, and in the end you get $\left< v, v_{0} \right> \left< w, w_{0} \right>$. 

Also notice how, again, we find the adjoint from a formula for $Tv$ by algebraic manipulation until $v$ is alone in the first slot of the inner product.

### $T^*$ as a linear map

The adjoint is indeed always linear as we wanted and our examples hinted.

##### _proposition:_ the adjoint of a linear map is linear

If $T \in \mathcal{L}(V, W)$, then $T^* \in \mathcal{L}(W, V)$.

###### _proof:_

Suppose $w_{1}, w_{2} \in W$, $v \in V$ and $\lambda \in \mathbb{F}$. Then
$$
\begin{split}
\left< Tv, \lambda w_{1} + w_{2} \right> & = \overline{\lambda} \left< T v, w_{1} \right> + \left< T v, w_{2} \right> \\
 & = \overline{\lambda} \left< v, T^*w_{1} \right> + \left< v, T^* w_{2} \right> \\
 & = \left< v, \lambda T^* w_{1} + T^* w_{2} \right>.
\end{split}
$$
But we already know $T^*(\lambda w_{1} + w_{2})$ is the unique vector giving $\left< Tv, \lambda w_{1} + w_{2} \right> = \left< v, T^* (\lambda w_{1} + w_{2}) \right>$. Thus, we must have $T^*(\lambda w_{1} + w_{2}) = \lambda T^* w_{1} + T^* w_{2}$. That is, $T^*$ must be linear.

Further, it turns out that the map $T \mapsto T^*$ is almost linear (and actually linear when $\mathbb{F} = \mathbb{R}$) on the respective spaces of linear maps.

##### _proposition:_ the almost linearity of $-^*$

Suppose $S, T \in \mathcal{L}(V, W)$ and $\lambda \in \mathbb{F}$. Then $(S + T)^* = S^* + T^*$ and $(\lambda T)^* = \overline{\lambda} T^*$.

###### _proof:_

Suppose $v \in V, w \in W$. Then
$$
\begin{split}
\left< (S + \lambda T) v, w \right> & = \left< Sv + \lambda T v, w \right> \\
 & = \left< Sv, w \right>  + \lambda \left< Tv, w \right> \\
 & = \left< v, S^* w \right> + \lambda \left< v, T^* w \right>  \\
 & = \left< v, S^* w \right> + \left< v, \overline{\lambda} T^* w \right>  \\
 & = \left< v, S^* w + \overline{\lambda} T^* w \right>.   
\end{split}
$$
The desired result follows pretty easily.

Actually, $-^*$ isn't just almost linear. It's basically as nice as it can be — it's an involution, it distributes over composition anti-symmetrically, it fixes the identity, and it commutes with taking inverses.
##### _proposition:_

Suppose $S \in \mathcal{L}(W, U)$ and $T \in \mathcal{L}(V, W)$. Then
1) $(T^*)^* = T$
2) $(ST)^* = T^* S^*$
3) $I^* = I$ (where $I$ is the identity operator on $V$)
4) if $T$ is invertible, then $T^*$ is invertible and $(T^*)^{-1} = (T^{-1})^*$.

###### _proof:_

1) We have $\left< Tv, w \right> = \left< v, T^* w \right>$ by definition. Taking the conjugate of both sides gives us $\left< T^* w, v \right> = \left< w, T v \right>$, and thus, the fact that $T = (T^*)^*$.
2) We can just compute.
$$
\begin{split}
\left< ST v, u \right> = \left< S(Tv), u \right> \\
 & = \left< Tv, S^* u \right>  \\
 & = \left< v, T^* S^* u \right>.
\end{split}
$$
	Which gives us $(ST)^* = T^* S^*$ as desired.
3) Just notice that
$$
\begin{split}
\left< Iv, w \right> & = \left< v, w \right>  \\
 & = \left< v, I w \right>.
\end{split}
$$
4) We can just apply the adjoint on both sides to the equations $T T^{-1} = I$ and $T ^{-1} T = I$ to see that $T^* (T^{-1})^* = (T^{-1})^* T^* = I$.


We can generalise that last result even further to talk about the null space and range of $T^*$ in relation to range and null space of $T$.

##### _proposition:_ the null space and range of $T^*$

Suppose $T \in \mathcal{L}(V, W)$. Then $\operatorname{null} T^* = (\operatorname{range} T)^\perp$ and $\operatorname{range} T^* = (\operatorname{null} T)^\perp$.

### The conjugate transpose matrix