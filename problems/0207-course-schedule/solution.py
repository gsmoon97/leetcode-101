class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Formulate the problem into cycle detection in directed graph
        
        # Construct adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            course, prereq = pair
            graph[prereq].append(course)  # what course does this course depend on? (prereq -> course)

        # States: 0 = unvisited, 1 = visiting, 2 = visited
        states = [0 for _ in range(numCourses)]
        
        def has_cycle(course):
            # DFS to detect a cycle starting from course.
            if states[course] == 1:  # has been visited in this cycle before (back edge)
                return True
            if states[course] == 2:  # has been verified that there is no cycle
                return False

            states[course] = 1  # mark to keep track of visited courses
            
            for prq in graph[course]:
                if has_cycle(prq):
                    return True
            
            states[course] = 2  # verified that there is no cycle
            return False

        # iterate through all the courses
        for i in range(numCourses):
            if states[i] == 0:  # check only if they have not been visited before
                if has_cycle(i):
                    return False
        return True