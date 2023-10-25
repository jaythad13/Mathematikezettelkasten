---
tags:
- logistics
---

Since this is our *mathematikezettelkasten*, we would like to keep it as uniform and organised as possible. To this end we have this style guide.

### Writing style

We write in the first person plural (referring to ourselves as we) and using conversational language when in prose. We use the plural in titles (for example, "Vector spaces", "Number fields", "Euclidean spaces")
We don't object to informal descriptions of mathematical objects to develop intuition, but they should be supported by exact, rigorous statements. We agree with Evan Chen that natural explanations supersede proofs, but counter that the proofs are important, and for learning math formally, are a large part of the point.
Finally, we use British/Indian spelling, but this may change.

### Note formatting

We use our usual style for handwriting notes adapted to some peculiarities of Obsidian.
##### Page organisation

We write a page for every new big idea. Usually, this is an roughly corresponding to the size of a subsection or a section of _Linear Algebra Done Right_ or _Principles of Mathematical Analysis_. 
It should contain its own definition and the definitions of a few objects that it is intrinsically linked with. Perhaps there could be 2-3 such ideas in a typical lecture. (There could be more if, for example, a first lecture on algebra defined monoids, semigroups, groups, rings, fields, and algebras)

We organise each idea into sections --- each section heading written as a Heading 3. 

Within (and without of) each section, we include examples, definitions, theorems (or propositions), and strategies, each of which we write as a Heading 5, with "example(s)", "definition", "re-definition", "theorem", "proposition", "strategy" in italics before the name of the thing we are giving examples of, defining, proving, or giving a strategy to do. Note that when handwriting, we would underline, but this is annoying to do in Obsidian.

We write "proof:" again, as a Heading 5, in italics, before giving the proof below. We usually write strategies as a list of steps.

Leave a line after every carriage return, regardless of whatever (basically, make every carriage return into two).

##### Multiple instances of the same title

Sometimes, because math, the same title may pop up in different fields, not just as the same name, but the same idea. Often, however, in the different field, the same idea has a radically different interpretation that is important. Basically, we can't just edit the old page.

As far as possible we try to avoid creating two pages with the same title even when they are in different folders so it is kosher to do so. We prefer to use notation like "re-definition" (see the example of [[Modules|modules]] and [[Vector spaces|vector spaces]]). When it is unavoidable (it shouldn't be), we create a second page with the same title.
### File organisation

##### Folders

We organise all notes in folders corresponding to the "project" that they are part of. For courses this means placing notes corresponding to a particular course in a folder with a course name and course tag. For example, "Calculus --- math-19". For self-study, we use a name and the self-study tag. For example "Concrete Mathematics --- self-study"

##### YAML

We tag all files with the following:
1) The course name, for example, `math-19` or `self-study`
2) Any fields of math that the page relates to. A list of tags is [[Tags|here]].
3) For courses we also add a lecture property to YAML indicating the lecture number. For example, `lecture : 1`

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

- We denote the pre-image of $T$ by $f^{pre}(T)$. Sometimes we may abuse notation to abbreviate $f^{pre}(\{y\})$ to $f^{pre}(y)$ for some $y \in Y$.
- We denote the image of $S$ by $f^{img}(S)$


