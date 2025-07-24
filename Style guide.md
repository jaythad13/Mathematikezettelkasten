---
tags:
- logistics
---

Since this is our *mathematikezettelkasten*, we would like to keep it as uniform and organised as possible. To this end we have this style guide.

### Writing style

We write in the first person plural (referring to ourselves as we) and using conversational language when in prose. We use the plural in titles (for example, "Vector spaces", "Number fields", "Euclidean spaces".)

We don't object to informal descriptions of mathematical objects to develop intuition, but they should be supported by exact, rigorous statements. We agree with Evan Chen that natural explanations supersede proofs, but counter that the proofs are important, and for learning math formally, are a large part of the point.

Finally, we use British/Indian spelling, but this may change.

### Note formatting

We use our usual style for handwriting notes adapted to some peculiarities of Obsidian.

##### Page organisation

We write a page for every new big idea. Usually, this is an roughly corresponding to the size of a subsection or a section of [[Linear Algebra Done Right.pdf|Linear Algebra Done Right]] or [[Analysis --- rudin/attachments/texts/Principles of Mathematical Analysis.pdf|Principles of Mathematical Analysis]].

It should contain its own definition and the definitions of a few objects that it is intrinsically linked with. Perhaps there could be 2-3 such ideas in a typical lecture. (There could be more if, for example, a first lecture on algebra defined monoids, semigroups, groups, rings, fields, and algebras)

We organise each idea into sections --- each section heading written as a Heading 3. 

Within (and without of) each section, we include examples, definitions, theorems (or propositions), and strategies, each of which we write as a Heading 5, with "example(s)", "definition", "re-definition", "theorem", "proposition", "strategy" in italics before the name of the thing we are giving examples of, defining, proving, or giving a strategy to do. Note that when handwriting, we would underline, but this is annoying to do in Obsidian.

We write "proof:" as a Heading 6, in italics, before giving the proof below. This allows it to be embedded with the theorem.

Leave a line after every carriage return, regardless of whatever (basically, make every carriage return into two).

##### Multiple instances of the same title

Sometimes, because math, the same title may pop up in different fields, not just as the same name, but the same idea. Often, however, in the different field, the same idea has a radically different interpretation that is important. Basically, we can't just edit the old page. Try to avoid this unless there is very good reason to have two pages talking about the same thing.

### File organisation

##### Directories

We organise all notes in directories corresponding to the "project" that they are part of. For courses this means placing notes corresponding to a particular course in a directory with a course name and course tag. For example, `Calculus --- math-19`. For other projects, we use a unique project tag. For example `Concrete Mathematics --- con-crete`. While the name before a tag may change, **the tag does not change**.

We organise each project directory as follows. We place markdown notes in the `notes` subdirectory of the project directory. We have an `attachments` subdirectory that contains all embeddable content. Articles, references, or books are in the `texts` subdirectory of the `attachments` directory. Attachments for a particular note are in a subdirectory with the same name as the note inside the `for notes` subdirectory of the attachments. If they are images, they are labeled with section number followed by an underscore and a descriptive title with no spaces. Finally, exercises and homeworks are contained in `ex #` or `hw #` subdirectories of `exercises` and `homework` subdirectories of the `attachments` directory. Here `#` is the number of the exercise.

Some examples —
- [[Calculus on Manifolds.pdf|Calculus on Manifolds]] from #spivak is located at `Calculus on manifolds --- spivak/attachments/texts/Calculus on Manifolds.pdf`.
- [[Abstract algebra --- math-171/attachments/for notes/Dihedral groups and an introduction to generators/S2_symmetryExample.jpeg|This picture]] used [[Abstract algebra --- math-171/notes/Dihedral groups and generators#_definition _ symmetry of a regular polygon|in these notes on dihedral groups and generators]] to demonstrate some symmetries of a square is located at `Abstract Algebra I --- math-171/attachments/for notes/Dihedral groups and an introduction to generators/S2_symmetryExample.jpeg`
- [[Differential Geometry --- math-142/attachments/homework/hw 8/hw 8.pdf|Homework assignment #8]] from #math-142 is located at `Differential Geometry --- math-142/attachments/homework/hw 8/hw 8.pdf`.

##### YAML

We tag all files with the following:
1) A unique project tag, for example, `math-19` or `top-geo`. This is the project tag of the largest sub-directory of `~/Desktop/Math/Mathematikezettelkasten` that the file is contained in.
2) Any fields of math that the page relates to. A list of tags is [[Tags|here]].
3) For courses we also add a lecture property to YAML indicating the lecture number. For example, `lecture: math-19-1` refers to the first lecture of `math-19`

### Git

We use Git to keep track of everything that happens in here. 

##### How to commit

Commit with the project name, followed by the section of the project (if relevant) and then a description.

For example, changing the name of `Complex Analysis --- math-135` to `Functions of a Complex Variable --- math-135` would be committed as `math-135, renamed to Functions of a Complex Variable`. Several notes taken during lecture 4 of #math-82 would be committed as `math-82, notes, lecture 4 notes`.

##### Collaboration

To work on $\LaTeX$ documents with collaborators, we add their Overleaf/GitHub as submodules of the repository. The submodule is in the suitable subdirectory of the attachments folder (or is its own subdirectory).

### Mathematical conventions

These describe places where we deviate from the norm, or pick a side between notations.

##### 0 is not a natural number

$\bb{N}$ is the set of positive integers $\{1, 2, 3, \ldots \}$. $0$ is not a member of this set.

Also, it is annoying to write $\{1, \ldots n \}$ every time, so we use $\bb{N}_n = \{1, \ldots n \}$.

##### Set operations

We use $\subseteq$ and $\subsetneq$ whenever we are making new statements (introducing a new theorem, definition, et c.) or it is specifically important. 

We don't object to using $\subset$ for referencing already known statements where it is obvious or doesn't matter whether we have equality. 

For example, $\bb{Q} \subset \bb{R}$ is fine in most contexts because it would be obvious $\bb{Q} \subsetneq \bb{R}$. One context in which this wouldn't be kosher is if we were constructing $\bb{R}$ from $\bb{Q}$.

We use $S \setminus T$ over $S - T$ to denote set minus.

##### Functions

We use the same notation as Napkin for functions because it is unambiguous. For a function $f : X \to Y$, $T \subseteq Y$, and $S \subseteq Y$:

- We denote the pre-image of $T$ by $f^\text{pre}(T)$. Sometimes, we will write $f^\text{pre}(\{ y \})$ as $f^\text{fib}(y)$ for some $y \in Y$.
- We denote the image of $S$ by $f^\text{img}(S)$