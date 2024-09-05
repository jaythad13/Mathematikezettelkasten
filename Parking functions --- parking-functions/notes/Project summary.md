Imagine *n* cars trying to park on a street with *n* parking spots. Each car goes to its preferred parking spot, and tries to park there. If that spot is occupied already, it continues down the road and tries to park in all of the remaining spots. If all cars get to park, the function that assigns each car its preferred spot is called a parking function.

In our research, we defined and enumerated different types of preference restricted parking functions — parking functions where cars' preferences to some subset of the parking spots available. We considered two cases — 
- initial segment restriction — cars preferring only the first few spots (which is equivalent to the case where there aren't enough spots)
- cars having modular preferences — preferring only one of every few spots
both of which we enumerated with novel combinatorial proofs.

The first case of initial segment restrictions, gave us a new enumeration with an involution proof. This enumeration has connections to all kinds of combinatorial objects like Abel's binomial theorem, hyperplane arrangements, and polytopes. It also gave us a new way to sample defective preference lists, building off of Jasper's work from last year. 

In the modular case, our proof vastly simplified the work of Konheim and Weiss who used contour integration and generating functions to get the same result!