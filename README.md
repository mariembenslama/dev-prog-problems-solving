# dev-prog-problems-solving


Search Tree:
  - is Binary search tree algorithm (written in python)
  - Time complexity => O(log(n)) [as it divides search in sub trees - root and it's 2 children]
  - Space complexity => O(n) [as n is number of nodes]
  - The search algorithm depends on the height of the tree, unless in worst case it's only one branch of the tree, it makes 
  the complexity of the algorithm O(n)

| Height  | Nodes | Log calculation |
| ------------- | ------------- | ------------- |
| 0  | 1  | log2(1) = 0  |
| 1  | 3 | log2(3) = 1 |
| 2  | 7  | log2(7) = 2  |
| 3  | 15 | log2(15) = 3   |

Reverse Linked List:
   - Linked list: [{value, next} ...]
   - Reversing [1,2,3] => [3,2,1]
   - Algorithm used: => head.next.next: if head is [1] then next.next => [2,1] and head.next = none
   - The time and space complexity of the algorithm is O(n) since we should pass through the whole linked list and its elements + it stores all the nodes of the        list.
   
