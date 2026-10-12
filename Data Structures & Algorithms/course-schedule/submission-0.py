class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cg = defaultdict(list)

        for course0, course1 in prerequisites:
            cg[course0].append(course1) #course0 needs course1 to be already taken

        states = [0] * numCourses

        def dfs(course):
            #bad ending:
            #reached a course that is already in dfs explored path
            if states[course] == 1: return False
            if states[course] == 2: return True #end visiting state, already visited and closed

            states[course] = 1 #currently visiting
            for dep in cg[course]:
                if not dfs(dep): return False #early exit

            states[course] = 2
            return True

        #all paths needs to return True
        for course in range(numCourses):
            if not dfs(course): return False

        return True


        