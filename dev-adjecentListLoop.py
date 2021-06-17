from collections import defaultdict
from typing import List

class Solution:
    global canFinish
    def canFinish(numCourses: int, prerequisities: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for edge in prerequisities:
            graph[edge[0]].append(edge[1])

        visited = set()

        def visit(vertex):
            visited.add(vertex)
            for neighboor in graph[vertex]:
                if(neighboor in visited or visit(neighboor)):
                    return True #visited => cycle
            visited.remove(vertex)  

            return False #doesn't contain a cycle

        for i in range(numCourses):
            if(visit(i)):
                return False
        return True

    def test():
        #change here
        print('can Finish: ', canFinish(2, [[0,1], [1,0]]))
        print('can Finish: ', canFinish(2, [[0,1], [1,2]]))

    test()