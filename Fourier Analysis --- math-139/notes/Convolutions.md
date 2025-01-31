---
tags:
- math-139/4
- anal
---

Convolutions allow one to compute something like a weighted average of a function against another.

##### _definition:_ convolution

Given two $2\pi$ periodic functions $f, g : \mathbb{R} \to \mathbb{C}$, the convolution of $f$ with $g$ is 
$$
f * g(x) = \frac{1}{2 \pi} \int_{- \pi}^\pi f(y) g(y - x)  \, dy 
$$

It's an exercise in change of variables to show that $f * g = g * f$.

##### _example:_ convolving with a characteristic function

Consider $f = \chi_{[-1 / 2, 1/2]}$. Then $f * g$ for any $g$ is
$$
\frac{1}{2\pi} \int_{-\pi}^{\pi} \chi_{[-1 / 2, 1 / 2]} g(y - x) \, dy = \frac{1}{2 \pi} \int_{- 1 / 2}^{1 / 2} g(y - x) \, dy 
$$
Then $(f * g)(x)$ is the average of $g$ on the interval $[x - 1 / 2, x + 1 / 2]$.

##### _example:_ convolving with the [[Fourier Analysis --- math-139/notes/A couple kernels#_definition _ the Dirichlet kernel|Dirichlet kernel]]

Check that
$$
(f * D_{N})(x) = \sum_{n = -N}^N \hat{f}(n) e^{i n x}
$$
the $N$th [[Fourier Analysis --- math-139/notes/Fourier series#_definition _ Fourier series, $N$th partial sum|partial sum]]. Basically, since the Dirichlet kernel looks like the Dirac delta function as $N \to \infty$, the integrals approach the value of the function much like the Fourier series does.