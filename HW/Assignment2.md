# CS 475 Assignment #2 - Ziad Arafat

1. $<\Sigma, Succ, S_0,G>$
   - Overview
      - While we might at first be tempted to treat this problem such that each agent has to search a path towards the other this will increase our branching factor by an entire degree. Instead of being $N$ where $N$ is the max outgoing paths of any city it will become $N^2$
        - So instead we can just find a route from agent $\alpha$'s starting point to agent $\beta$'s starting point. 
          - If we are worried about finding a solution where the number of steps is distributed equally between the agents we can simply back track $T$ times where T is just the floor of the number of steps taken divided by 2.
      - So our formalization will be defined by finding a path from Arad to Vaslui.
   - $\Sigma$: Our set of possible states is defined by the list of cities in which our agent $\alpha$ could reside
     - let $X$ be a set of all cities in the map.
       - then $\Sigma=\{x \in X\}$
   - $Succ$: Our set of all possible successor transitions is defined by moving accross the paths from one city to the next.
     - Let $Succ=\{x\in \Sigma\times\Sigma\}$
   - 