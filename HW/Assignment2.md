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
   - $A$: our set of possible actions is dependant on what paths are available from a certain city.
     - If we are in Arad we can move to Zerind, Timisoara, or Sibiu.
     - We should only move to nodes we haven't visited yet.
     - The structure is $(r, d)$ where $r$ is the source city and $d$ is the destination city.
     - Each time we do an action we incur a cost of 1 or increment total steps by 1.
   - $S_0$: Our set of starting states is defined by the starting city of agent $\alpha$, which is Arad.
     - Let $S_0=\{A\}$
   - $G$: our set of goal states is defined by the city in which agent $\beta$ resides, which is vaslui.
     - Let $G=\{V\}$
   - The *forward branching factor* of our problem is defined by the maximum number of adjacent cities we can have at any state.
     - In our case this would be at Bucharest or Sibiu where we have 4 adjacent cities.
     - **Our Forward Branching factor is $4$**

2. Solved Trees
   1. Depth First
      - ![alt text](DepthFirst.svg.png)
   2. Breadth First
      - ![alt text](BreadthFirst.svg.png)
   3. Iterative Deepening
      - As expected we get the same result as Breadth first. The main difference is that we clear our space after we expand each level so the space complexity is less. Time complexity is the same.   
      - ![alt text](IterativeDeepening.svg.png)
   4. A*