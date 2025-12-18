---
tags:
- math-199DR/15
- math-199DR/27
- cx-geo
---

Let $X$ be a compact, connected Riemann surface.

In complex analysis [[Complex analysis --- math-135/notes/Meromorphic functions and singularities#_theorem _ the residue formula|the residue formula]] says that the integral of a meromorphic function (times $dz$, and thus the integral of a form) around a bunch of poles is just the sum of the residues at those contained poles. For Riemann surfaces this holds too. In fact the residue theorem is the stronger fact that since the integral of a [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphic and smooth forms|meromorphic form]] on $X$ is zero, the sum of its residues is zero.

##### _theorem:_ the residue theorem

Given a meromorphic form $\omega$ on $X$, the sum of all its [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphic and smooth forms|residues]] vanishes —
$$
\sum_{p \in X} \operatorname{Res}_{p} \omega = 0.
$$

### The analytic proof

### An algebraic proof

Using the trace of a form, we can prove the residue theorem algebraically. Essentially, we prove the residue theorem for the Riemann sphere and it follows that it is true for all Riemann surfaces.

##### _lemma:_ the residue of the trace is the residue of the form at pre-images

Let $\pi : X \to Y$ be a holomorphism and $\omega$ a meromorphic $1$-form on $X$. Then for any $q \in Y$, we have
$$
\operatorname{res}_{q} (\operatorname{tr}_{\pi} \omega) = \sum_{p \in \pi^\text{pre}(\{ q \})} \operatorname{res}_{p} \omega.
$$

###### _proof sketch:_

Compare the $-1$th coefficients of [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Abel's theorem#_proposition _ the trace of a meromorphic $1$-form is meromorphic|their Laurent series]].

I suspect this follows from the proof for the [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Abel's theorem#_lemma _ integral of the trace is the integral of the form on pullback chain|integral of the trace]] if you can do the covering map stuff right.

##### _theorem:_ the residue theorem for algebraic curves

Given a meromorphic form $\omega$ on an [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Algebraic curves#_definition _ algebraic curve|algebraic curve]] $X$, the sum of all its [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Holomorphic and smooth forms|residues]] vanishes —
$$
\sum_{p \in X} \operatorname{Res}_{p} \omega = 0.
$$

###### _proof:_

Let $\pi : X \to \mathbb{C}_{\infty}$ be a non-constant holomorphism (one exists by the definition of an algebraic curve). Then, we have globally that
$$
\operatorname{tr}_{\pi} \omega = r(z) \, dz
$$
where $r(z)$ is a meromorphic function on $\mathbb{C}_{\infty}$, and [[Algebraic curves and Riemann surfaces --- math-199DR/notes/Functions on Riemann surfaces#_example _ meromorphic functions on the Riemann sphere and projective line|thus, rational]]. We expand $r(z)$ into a partial fraction — a sum of terms $c (z - a)^n$ where $c, a \in \mathbb{C}$. It then suffices to show the theorem for meromorphic $1$-forms $c (z - a)^n \, dz$.

If $n \geq -2$, then it has a pole only at $a$ with residue $0$. If $n = -1$ this has a pole with residue $c$ at $a$ and $-c$ at $\infty$. Finally, if $n$ is non-negative it has a pole of residue $0$ at $\infty$. In all cases the residue is $0$.

Now we can just lift the residue theorem from $\operatorname{tr}_{\pi} \omega$ using our lemma comparing the residue of the trace and the form —
$$
\sum_{p \in X} \operatorname{res}_{p} \omega = \sum_{q \in \mathbb{C}_{\infty}} \sum_{p \in \pi^\text{pre}(\{ q \})} \operatorname{res}_{p} \omega = \sum_{q \in \mathbb{C}_{\infty}} \operatorname{res}_{q} (\operatorname{tr}_{\pi}\omega).
$$
