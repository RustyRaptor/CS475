# Constraint Satisfaction Problem

## Representation A

#### Variables and domains

- Assume $k \geq 0,  k < 5$
- the houses can be defined as
$$house(k) = a_k$$
- such that $a_k$ is the kth house from left to right and the houses start at $0$
- the color of the kth house can be defined as
$$color(k) \in \{R,G,B,Y,I\}$$
- such that $\{R,G,B,Y,I\}$ are Red, Green, Blue, Yellow, Ivory respectively.
- The nationality of the person in the kth house can be defined as
$$nation(k) \in \{E, S, N, U, J\}$$
- such that $\{E, S, N, U, J\}$ are English, Spanish, Norwegian, Ukranian, and Japanese respectively.
- The candy preference of the person in the kth house can be defined as
$$candy(k) \in \{H, M, K, Sm, Sn\}$$
- such that $\{H, M, K, Sm, Sn\}$ are Hershey's, MilyWay, KitKat, Smileys, and Snickers respectively.
- The drink preference of the person in the kth house can be defined as
$$drink(k) \in \{M, C, T, O, W\}$$
- such that $\{M, C, T, O, W\}$ are Milk, Coffee, Tea, Orange Juice, and Water respectively.
- The pet of the person in the kth house can be defined as
$$pet(k) \in \{D, F, S, H, Z\}$$
- such that $\{D, F, S, H, Z\}$ are Dog, Fox, Snail, Horse, and Zebra respectively.

#### Constraints

- The Englishman lives in the red house.
$$\forall k \in \Z: (nation(k) = E) \Leftrightarrow (color(k) = R)$$

- The Spaniard owns the dog.
$$\forall k \in \Z: (nation(k) = S) \Leftrightarrow (pet(k) = D)$$

- The Norwegian lives in the first house on the left.
$$nation(0) = N$$

- The green house is immediately to the right of the ivory house.
$$\forall k \in \Z: (color(k) = I) \Rightarrow (color(k+1) = G)$$

- The man who eats Hershey bars lives in the house next to the man with the fox.
$$\forall k \in \Z: (candy(k) = H) \Rightarrow ((pet(k+1) = F) \lor (pet(k-1) = F)) $$

- Kit Kats are eaten in the yellow house.
$$\forall k \in \Z: (candy(k) = K) \Leftrightarrow (color(k) = Y)$$

- The Norwegian lives next to the blue house.
$$\forall k \in \Z: (nation(k) = N) \Rightarrow ((color(k+1) = B) \lor (color(k-1) = B)) $$

- The Smarties eater owns snails.
$$\forall k \in \Z: (candy(k) = Sm) \Leftrightarrow (pet(k) = S)$$

- The Snickers eater drinks orange juice.
$$\forall k \in \Z: (candy(k) = Sn) \Leftrightarrow (drink(k) = O)$$

- The Ukrainian drinks tea.
$$\forall k \in \Z: (nation(k) = U) \Leftrightarrow (drink(k) = T)$$

- The Japanese eats Milky Ways.
$$\forall k \in \Z: (nation(k) = J) \Leftrightarrow (candy(k) = M)$$

- Kit Kats are eaten in a house next to the house where the horse is kept.
$$\forall k \in \Z: (candy(k) = K) \Rightarrow ((pet(k+1) = H) \lor (pet(k-1) = H)) $$

- Coffee is drunk in the green house.
$$\forall k \in \Z: (drink(k) = C) \Leftrightarrow (color(k) = G)$$

- The Milk is drunk in the middle house
$$drink(2) = M$$ 


#### Possible Solution using Representation A

$$nation(0) = N; color(0) = Y; pet(0)=F; drink(0)=W; candy(0)=K$$
$$nation(1) = U; color(1) = B; pet(1)=H; drink(1)=T; candy(1)=H$$
$$nation(2) = E; color(2) = R; pet(2)=S; drink(2)=M; candy(2)=Sm$$
$$nation(3) = S; color(3) = I; pet(3)=D; drink(3)=O; candy(3)=Sn$$
$$nation(4) = J; color(0) = G; pet(4)=Z; drink(4)=V; candy(4)=M$$


# Representation B

- Given a set of pets we can get any pet as p
$$p \in \{D, F, S, H, Z\}$$

- each $p$ is a tuple describing the pet's owner. 

$$(nation, candy, drink, location)$$

$$nation \in \{E, S, N, U, J\}$$
$$candy \in \{H, M, K, Sm, Sn\}$$
$$drink \in \{M, C, T, O, W\}$$
$$positions = \{1, 2, 3, 4, 5\}$$
$$colors = \{red, green, blue, yellow, ivory\}$$
$$location \in colors \times positions$$
