# Function-Approximation
Function Approximation (Tic-tac-toe Game) 

Studying Chapter one of Tom Michaelโs book is highly recommended for understanding the implementation of this mini project. In the first chapter of Tom Mitchelโs book, the learning problem is reduced to a function approximation problem and one specific class of learning Task is chosen to explain in detail. This class is learning from training data with indirect feedback. This class of learning tasks is different from the class of Concept Learning. Concept learning is about learning from direct feedback.

In this project, I have used Mitchelโs described approach to implement an algorithm to learn the tic-tac-toe game. As you know, such tasks abstract as a graph that every board state is a node and every move is an edge. The goal is to find the best move for each state. (You can find details of abstract representation of tic-tac-toe in Russellโs book: artificial intelligent, a modern approach adversarial search Chapter). 
We can define a function ๐: ๐ โ โ that assigns to every state a value and based on ๐ find the best move for each state. If we are able to find ๐, the problem is solved but only a few pairs < ๐ , ๐(๐ ) > are available. There are many states that donโt have the value of ๐. Therefore, we should approximate this function only by these points (training examples). Because of the graph structure of the problem, this is possible to approximate the value of unknown-value states and one can use approximated values to find better approximations. So for unknown-value states, you should use approximated successor stateโs value.

# A) Implementing an algorithm, which learns to play Tic-tac-toe (3ร 3 board) with a function approximation approach.

Steps:

1. Choosing linear representation for ๐ฬ : ๐ฬ(๐ฅโ) = ๐คโ๐๐ฅโ.

2. Finding some good features (๐ฅโ) to describe the states of tic-tac-toe.

3. Initializing all coefficients (๐คโ) in ๐ฬ by zero.

4. Starting with an empty board state and in each non-terminal state (๐ ๐ก) the move has been chosen based on ๐ฬ as follows: Among the moves, someone can do in the current state, choose the one which leads to the highest state value (value of successors of the current state). These chosen successor states are called  ๐ ๐ก+1 and assigned ๐๐ก๐๐๐๐(๐ ๐ก) = ๐ฬ(๐ ๐ก+1). If ๐ t is a terminal state, then we assign ๐๐ก๐๐๐๐(๐ ๐ก) = ๐(๐ ) and set the value of the final state as follows:

    ๐๐ก๐๐๐๐(๐ ๐ก) = 100 If a player wins
    
    ๐๐ก๐๐๐๐(๐ ๐ก) = โ100 If a player loses
    
    ๐๐ก๐๐๐๐(๐ ๐ก) = 0 If a player draws
    
5. Finally, we have new example: < ๐ ๐ก, ๐๐ก๐๐๐๐(๐ ๐ก) >. Based on this example, we update ๐คโ as follows:

    ๐ค๐ = ๐ค๐ + ๐ผ (๐๐ก๐๐๐๐(๐ ๐ก) โ ๐ฬ(๐ ๐ก)) ๐ฅ๐
    
I have assigned a small value for ๐ผ to train the agent and run two agents to play with each other.

# B) Based on the previous part, an agent code has been written that you can play with it.

