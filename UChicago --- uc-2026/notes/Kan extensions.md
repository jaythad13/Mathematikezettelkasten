---
tags:
- cat-th
- uc-2026
- alicia-lima
---

Kan extensions are extensions of a functor from a subcategory to the whole category. They are special because we have a good understanding of when they exist, and we can use them to subsume all the ideas in category theory.

##### _definition:_ Kan extensions

Let $\mathscr{A}, \mathscr{B}, \mathscr{C}$ be categories. A **left Kan extension** of $F : \mathscr{A} \to \mathscr{C}$ along $G : \mathscr{A} \to \mathscr{B}$ is a functor $\operatorname{Lan}_{G}F : \mathscr{B} \to \mathscr{C}$ and a natural transformation $\eta : F \to \operatorname{Lan}_{G} F \circ G$ satisfying the following universal property — for any $L' : \mathscr{B} \to \mathscr{C}$ with natural transformation $\eta' : F \to L' \circ G$, the natural transformation $\eta'$ factors uniquely through $\eta$.

```tikz
\usepackage{tikz-cd}
\usepackage{amsfonts}
\begin{document}
	\begin{tikzcd}
		\mathcal{A} \ar[rr, "F", ""{name=F}] \ar[rd, "G"]  & & \mathcal{C} \\
		& \mathcal{B} \ar[ru, "L", bend left, ""{name=L}] \ar[ru, "L'"', bend right, ""{name=L'}] \ar[Rightarrow, from=F, "\eta"] \ar[Rightarrow, dashed, from=L, to=L', "\exists !"]
	\end{tikzcd} 
\end{document}
```

A **right Kan extension** of $F$ along $G$ is a functor $\operatorname{Ran}_{G} F : \mathscr{B} \to \mathscr{C}$ and a natural transformation $\varepsilon : \operatorname{Ran}_{G} F \circ G \to F$ satisfying the following universal property — for any $R' : \mathscr{B} \to \mathscr{C}$ with natural transformation $\varepsilon' : R' \circ G \to F$, the natural transformation $\varepsilon'$ factors uniquely through $\varepsilon$.

That is, a right Kan extension is exactly dual to a left Kan extension.

---