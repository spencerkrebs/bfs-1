# Keep track of indegrees using topological sort

# BFS
# O(V+E) time, O(V+E) space
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = {}

        for pr in prerequisites:
            # build the topological sort
            indegrees[pr[0]] += 1
            # build the adjacency list
            if pr[1] not in graph:
                graph[pr[1]] = []
            graph[pr[1]].append(pr[0])

        count = 0
        q = deque()

        for i in range(numCourses):
            # finds the roots - which have 0 prerequisites. Side note - in this problem 1 graph can have many roots
            if indegrees[i] == 0:
                q.append(i)
                count += 1

        # every single course has at least 1 prerequisite (deadlock cycle)
        if not q:
            return False
        # all courses have 0 prereqs. Every course is already ready to take - no need for bfs 
        if count == numCourses:
            return True

        while q:
            curr = q.popleft()
            dependencies = graph.get(curr)
            if dependencies:
                for dep in dependencies:
                    indegrees[dep] -= 1
                    if indegrees[dep] == 0:
                        q.append(dep)
                        count += 1
                        # to finish all courses, count must eventually equal numCourses. 
                        # as soon as you decrement indegree to 0 for a course, you add it to the queue and increment count
                        # if count == numCourses, you already found a valid path for all courses 
                        if count == numCourses:
                            return True

        return False


# DFS O(V+E) time, O(V+E) space
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.map = {}
        self.path = [False] * numCourses
        self.visited = [False] * numCourses

        for pr in prerequisites:
            if pr[1] not in self.map:
                self.map[pr[1]] = []
            self.map[pr[1]].append(pr[0])

        for i in range(numCourses):
            if self.hasCycle(i):
                return False

        return True

    def hasCycle(self, i: int) -> bool:
        if self.visited[i]:
            return False

        if self.path[i]:
            return True

        self.path[i] = True

        neighbours = self.map.get(i)
        if neighbours is not None:
            for ne in neighbours:
                if self.hasCycle(ne):
                    return True

        # you could have A->B->C and A->C. if you don't set path c back to false after exploring through b, the algorithm would think a-c is a cycle 
        self.path[i] = False
        self.visited[i] = True

        return False

