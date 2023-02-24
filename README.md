# selffish_pony
2 -> 自私的小马爬山算法；
3 -> 自私的小马和无私的小马一起爬山问题

### 2:
Selfish Pony Behaviour
The "s" (selfish) ponies only care about themselves. Each selfish pony travels individually along the path,
completely disregarding other ponies also traveling on the path.
Pony energy follows these rules:
• Ponies use energy when travelling to higher elevations.
• Ponies gain energy when they move to lower elevations.
• Energy usage is the elevation difference between the source location and the destination.
• A pony cannot have negative energy.
For example, when an "s" pony with an energy of 52 moves from elevation 13 to 30, its energy is reduced by 17,
leaving it with energy = 35. Similarly, when an "s" pony with an energy of 54 moves from elevation 30 to 13, its
energy is increased by 17, leaving it with an energy of 71. A selfish pony with 10 energy can not move from
elevation 20 to 31, because that would lead to negative energy - so it is stuck at its current location.

### 3:
Altruistic pony behaviour
At each time step, an altruistic pony can give its energy to other ponies. Altruistic ponies will try to help other
ponies move along the path before moving along the path itself.
At a timestep t, assumes that P1 is an altuistic pony and P2 is a pony of any type, and if all of the following are
true in P1's turn:
• P1 and P2 are in the same location
• P2 has a smaller id than P1
• P2 is stuck at the location
• P1 can give enough energy to P2 so that P2 has enough energy to move to the next location
• After giving P2 the energy it requires, P1 still has non-negative energy then the following two events will
occur in order:
• In this timestep t, P1 gives P2 exactly enough energy to allow P2 to move to the next location
• In this timestep t, P1 moves to the next location if it still has sufficient energy to do so
Note that at a time step, an altruistic pony P1 can give its energy to multiple ponies. If there are multiple ponies
that satisfy the four criteria above, the altruistic pony gives its energy to the pony with the lower id first. Also, if any
of the four criteria for giving energy are not satisfied (that is, no ponies need help or P1 is not able to help), then the
altruistic pony P1 behaves just like a selfish pony.

Your task in this question is to write a function
teamork_climb(elevations, path, ponies) that simulates the
movement of selfish and altruistic ponies and returns a dictionary in the
format described below.
This function should have three arguments - elevations, path, and ponies
as described in the previous question.
Your function should return a dictionary where each key is an integer
timestep (ie. 0, 1, 2...), and the values are a list of pony tuples at that
timestep. Consistent with Q2, each ponies list should be sorted by id. That
is, ponies with lower ids are at the front. Please also refer to 02 for the
definition of the final timestep.
This task is similar to the task in the previous question, with the difference
being that ponies either have the personality "s" or "a". Remember that at
each time step, ponies try to move in order of ascending id (ie Pony 0, then
Pony 1, then Pony 2 ... etc)
