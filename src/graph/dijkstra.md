## Here's a brief explanation of what the code is doing:

- It initializes a dictionary distances to store the shortest distance from the starting node to each node in the graph. The distance to the starting node is set to 0, and all other distances are initialized to infinity.
- It initializes a priority queue pq with a tuple (0, start) representing the distance to the starting node and the starting node itself.
- The algorithm then iterates as long as the priority queue pq is not empty.
In each iteration, it pops the node with the smallest distance from the priority queue.
-  It then checks if the current distance to the node is smaller than the stored distance in the distances dictionary. If it is not, it continues to the next iteration.
- For each neighbor of the current node, it calculates the distance from the starting node via the current node. If this distance is smaller than the previously stored distance for the neighbor, it updates the distance and adds the neighbor to the priority queue.
- Finally, the function returns the distances dictionary containing the shortest distances to all nodes from the starting node.