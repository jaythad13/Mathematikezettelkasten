---
tags:
- pep
---


> When introduced to a new idea, always ask why you should care. Do not expect an answer right away, but demand one eventually.

\- Ravi Vakil (a mathematician)

For most people, the first time you see fractions is unsatisfying. I remember not understanding why I would care about fractions, and much less why I would add them so weirdly.

In this handout, you'll invent fractions yourself, just as the first person to invent fractions might have. I hope this will make you more comfortable with fractions, not just teaching you how to work with fractions, but why you should work with them in certain ways. 

There's only one rule. When you see a question in italics _like this_, stop and answer the question for yourself on a piece of paper before you read my answer. It's okay if your answer is incomplete or vague. The important thing is to think hard about the question.

### Inventing numbers

Imagine you've never heard of numbers before. _What might lead you to invent them? What else would you invent to go with numbers?_

It turns out that numbers and all the operations that we can do with them are really natural things to think about. 

If you want to buy matching caps for your best friends Alisha, Bob, and Charlie, how would you tell the salesperson how many caps you wanted? _How could you do it without numbers? How might numbers make it easier?_

Without numbers you'd have no way to express the **sameness** between Alisha, Bob, and Charlie and cap, cap, and cap. You'd just have to keep saying 'cap' for each friend you have.

Instead of saying 'cap' over and over, you could use numbers. With numbers, you just count your best friends and then tell the salesperson you want three caps. That's all that numbers do! They're an easy way to say 'cap' over and over again. This means that when we decide what numbers mean, we should choose them so that three really does mean the same as saying 'cap, cap, cap'.

If you made two new best friends, Darren and Emma, how would you know if you just had numbers, you'd have to count them up all over again: Alisha, Bob, Charlie, Darren and Emma. _What could you invent that would make knowing how many caps you need to buy easier?_

But if you know that just counting an extra two for Darren and Emma from the three for Alisha, Bob, and Charlie counts the same five friends, then you can count the number of caps you need easily. Addition is just this: an easy way to count the combination of two groups! This means that when we decide how to do addition, we have to choose so that adding things numbers of things is the same as the number of things after combining them.

In this worksheet, we will create fractions, and addition, just like we created them for numbers. Hopefully, by the end of this, you will feel comfortable enough to invent multiplication by yourself!

### Why think about fractions?

Now, imagine no one had ever told you about fractions. _Why might you think about them anyway? Why are fractions a natural idea just like whole numbers?_

One natural place for fractions to crop up is sharing. Say you wanted to share a pie with your friends, so you cut the pie into five pieces of the same size. Alisha and Bob finish their pie all at once, but Charlie cuts his piece into two equal pieces, eating one and saving one for later. Finally, Darren cuts his piece into three equal pieces and gives one to Emma. _In what sense are Charlie's two pie pieces the same as Alisha or Bob's one piece?_ _In what sense are Darren's two remaining pieces different from Charlie's and Emma's?_

It makes sense to think of Charlie's two pieces as the same as Alisha's one piece, because when we combine the two pieces, they have the same size as Alisha's piece. In fact, before Darren gives one of his pieces away, Darren's three pieces are together the same as Charlie's two pieces in the same sense. What this tells us is **if we want to keep the same overall size, we can have more small pieces, or fewer big pieces.** Specifically, if we want $2$ times more small pieces with the same total size, we need to cut the pie into $2$ times more pieces. That's why Charlie's pieces look exactly like if the pie was cut into ten pieces and he took two!

We want fractions to represent this idea but for any numbers! Maybe Charlie has a whole pie at home as well. _How many pieces of pie (of the same size as Alisha's) does he have then? How many pieces of pie (of the same size as Darren's) does he have?_

If you tried to answer these questions without fractions, it seems really hard. Fractions make thinking about these questions easy.

##### _(temporary) definition:_ equals (for fractions)

We say the fraction $\dfrac{a}{b}$ equals the fraction $\dfrac{c}{d}$ if there is some number $k$ so that $a = c \times k$ (the first fraction has $k$ times more slices) and $d \times k = b$ (and therefore, the whole pie(s) have to be cut into $k$ times more pieces).

Since this just tells us that
$$
a \times d \times k = b \times c \times k
$$
we can say
$$
a \times d = b \times c
$$
which is the familiar "cross multiplication" rule that you might remember from school! 

_But why would we use this weird cross multiplication thing when the other definition seems so much easier?_ (hint: think about two fractions from the pie example that should be equal, but according to this definition, are not)

Think of the pie example again: Charlie has two slices of the same size that cutting the pie into ten slices would give you. Darren has three slices of the same size that cutting the pie into fifteen slices would give you. There isn't any whole number $k$ that will give you $2 \times k = 3$. Still, we feel like the total share of the pie that they have is the same. Why is that true?

If we use the original definition, we have to say that Charlie's two slices are the same as Bob's slice, because $1 \times 2 = 2$ and $5 \times 2 = 10$. Bob's slice is the same as Darren's three slices because $1 \times 3 = 3$ and $5 \times 3 = 15$. 

If Charlie's two slices are the same as Bob's slice, which is the same as Darren's three slices, then it only makes sense that Charlie's two slices are the same as Darren's three slices! If we use the cross multiplication rule we see this really easily! 
$$
2 \times 15 = 10 \times 3.
$$
This means that
$$
\frac{2}{10} = \frac{3}{15}.
$$

This is where the cross multiplication rule comes from! Because this rule captures what we really want when we want two fractions to be equal, this is the proper definition of equal that we choose for fractions.

##### _definition:_ equal (for fractions)

We say the fraction $\dfrac{a}{b}$ equals the fraction $\dfrac{c}{d}$ if $ad = bc$.

Now that we understand what it means for fractions to be equal, we can talk about adding them.

### Adding fractions

Again, we return to the problem of dividing pie among friends. We want to think about how many pieces of pie Emma has after Darren gives her some of his. We know that we can represent the pieces of pie that Emma has with fractions. 

She has one piece of the pie of the original size (that divided the pie into five pieces) and one of Darren's small pieces of pie (fifteen of which can make up the whole pie). From the previous section, we know that we can write these as $\dfrac{1}{5}$ and $\dfrac{1}{15}$ respectively.

Knowing how much pie she has in total then comes from some sense of combining the pieces of pie. We know already we can think of Emma's big piece of pie as the same amount of pie as three of the smaller pieces, and we know from addition on regular numbers that if Emma has three small pieces of pie and one small piece of pie, then in total she has four small pieces of pie. We know how to combine pieces of pie!

But what happens if the pieces of the pie get more complicated? 

Say a fourth friend Frank has pieces that have fractions like $\dfrac{2}{5}$ and $\dfrac{3}{7}$. How much pie does he have then? These are much more complicated pieces, but we can convert them into more of smaller pieces that we can add up easily. That is, we can think of the first two pieces of (five of which would make up a pie) as fourteen pieces such that thirty-five of them make up a whole pie and we can think of the last three pieces (seven of which would make up a pie) as fifteen pieces such that thirty-five of them would make up a whole pie. Frank must have twenty-nine pieces (thirty-five of which would make up a pie).

While it's possible to think about every problem by thinking about the objects directly like this, it's much easier to work with fractions. Just look at how wordy the paragraph above is! Instead, just like with numbers, we want to convert the idea of combining objects into the idea of adding fractions.

Since we want adding fractions to represent combining pieces of pie, the way we add fractions needs to work with what we want. The fraction of the combination of the pieces of pie needs to be equal to the fraction you get by adding fractions of the pieces of pie. Also, we want adding equal fractions to give us the same thing: combining two pieces of pie is the same no matter how small you cut up each piece of pie and addition should work with this too. $\dfrac{1}{3} + \dfrac{2}{4}$ should be the same as $\dfrac{2}{6} + \dfrac{1}{2}$.

The most sensible way to do this is to just replicate what we were doing with the pieces of pie with fractions! Instead of cutting up pieces of pie into pieces all of the same size, we convert fractions into equal fractions but with the same denominator, and then add up the numerators!

That is

##### _definition:_ addition (for fractions)

We say the sum of fractions $\dfrac{a}{b}$ and $\dfrac{c}{d}$ is
$$
\dfrac{a}{b} + \dfrac{c}{d} = \dfrac{a \times d}{b \times d} + \dfrac{b \times c}{b \times d} = \dfrac{a \times d + b \times c}{b \times d}
$$

This works perfectly with all the properties that we wanted! _Check this for yourself: find some examples of problems like the pie problem and show that addition always works the same as combining pieces. Also, check that adding equal fractions really does give equal answers._

### Multiplying fractions

Now that you've understood how to add fractions and you've seen how we come up with ways to think about fractions that make sense, you're ready to try to think about multiplying fractions on your own. This section just has a hint to get you started.

People often say "I'll get two of those bags of chips." or "I couldn't possibly have a third of a pie that big - give me half of that piece". _What is the same about their use of the word "of" in both of these sentences?_