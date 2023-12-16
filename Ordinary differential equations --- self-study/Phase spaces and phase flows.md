---
tags:
- self-study
- diff-eq
---

Ordinary differential equations are a mathematical tool to study particular types of processes. Specifically, ordinary differential equations allow to study some sort of _evolution_ of a system as long as that evolution is deterministic, finite-dimensional, and differentiable, using mathematical objects like phase spaces and phase flows.

### Some unrigorous definitions

Because we're studying exactly those processes, we need to have at least an intuitive idea of what it means for a process to be deterministic, finite-dimensional, and differentiable. These definitions have to be sort of hand-wavy because really, we _hard-code_ in determinism, finite-dimensionality, et c. into the mathematical objects we study, and these are instead properties of less well-defined things like processes.

##### _definition:_ deterministic

A process is deterministic if its entire future course and its entire past are uniquely determined by its state at any "present" point in time.

##### _definition:_ phase space

The set of all possible states of a process is called its phase space.

##### _example:_ deterministic processes and their phase spaces

Classical mechanical models are a good example of deterministic processes. In any classical mechanical system (with no external force acting on it), we can predict the future motion of all its particles just using conservation of momentum and conservation of energy, and we can "wind the clock back" and do the same thing for the past, as long as we have the position and velocity (or more typically, momentum) of each particle. Thus, its phase space is just the set of all possible positions and momentums for each particle — perhaps $(\bb{R}^n \times \bb{R}^n)^m$ for $m$ particles in $n$-dimensional space.