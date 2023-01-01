# Function-Approximation
Function Approximation (Tic-tac-toe Game) 

Studying Chapter one of Tom Michael’s book is highly recommended for understanding the implementation of this mini project. In the first chapter of Tom Mitchel’s book, the learning problem is reduced to a function approximation problem and one specific class of learning Task is chosen to explain in detail. This class is learning from training data with indirect feedback. This class of learning tasks is different from the class of Concept Learning. Concept learning is about learning from direct feedback.

In this project, I have used Mitchel’s described approach to implement an algorithm to learn the tic-tac-toe game. As you know, such tasks abstract as a graph that every board state is a node and every move is an edge. The goal is to find the best move for each state. (You can find details of abstract representation of tic-tac-toe in Russell’s book: artificial intelligent, a modern approach adversarial search Chapter). 
We can define a function 𝑉: 𝑆 → ℝ that assigns to every state a value and based on 𝑉 find the best move for each state. If we are able to find 𝑉, the problem is solved but only a few pairs < 𝑠, 𝑉(𝑠) > are available. There are many states that don’t have the value of 𝑉. Therefore, we should approximate this function only by these points (training examples). Because of the graph structure of the problem, this is possible to approximate the value of unknown-value states and one can use approximated values to find better approximations. So for unknown-value states, you should use approximated successor state’s value.

# A) Implementing an algorithm, which learns to play Tic-tac-toe (3× 3 board) with a function approximation approach.

Steps:

1. Choosing linear representation for 𝑉̂ : 𝑉̂(𝑥⃗) = 𝑤⃗𝑇𝑥⃗.

2. Finding some good features (𝑥⃗) to describe the states of tic-tac-toe.

3. Initializing all coefficients (𝑤⃗) in 𝑉̂ by zero.

4. Starting with an empty board state and in each non-terminal state (𝑠𝑡) the move has been chosen based on 𝑉̂ as follows: Among the moves, someone can do in the current state, choose the one which leads to the highest state value (value of successors of the current state). These chosen successor states are called  𝑠𝑡+1 and assigned 𝑉𝑡𝑟𝑎𝑖𝑛(𝑠𝑡) = 𝑉̂(𝑠𝑡+1). If 𝑠t is a terminal state, then we assign 𝑉𝑡𝑟𝑎𝑖𝑛(𝑠𝑡) = 𝑉(𝑠) and set the value of the final state as follows:

    𝑉𝑡𝑟𝑎𝑖𝑛(𝑠𝑡) = 100 If a player wins
    
    𝑉𝑡𝑟𝑎𝑖𝑛(𝑠𝑡) = −100 If a player loses
    
    𝑉𝑡𝑟𝑎𝑖𝑛(𝑠𝑡) = 0 If a player draws
    
5. Finally, we have new example: < 𝑠𝑡, 𝑉𝑡𝑟𝑎𝑖𝑛(𝑠𝑡) >. Based on this example, we update 𝑤⃗ as follows:

    𝑤𝑖 = 𝑤𝑖 + 𝛼 (𝑉𝑡𝑟𝑎𝑖𝑛(𝑠𝑡) − 𝑉̂(𝑠𝑡)) 𝑥𝑖
    
I have assigned a small value for 𝛼 to train the agent and run two agents to play with each other.

# B) Based on the previous part, an agent code has been written that you can play with it.

