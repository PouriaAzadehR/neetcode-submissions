from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prerequisites_graph = dict()

        for prerequisite in prerequisites:
            prerequisites_graph.setdefault(prerequisite[1], []).append(prerequisite[0])
            prerequisites_graph.setdefault(prerequisite[0], [])

        # we need a dicrected graph without any undirected edge!

        is_undirected_edge_founded = [False]

        def dfs(starting_node, current_node):

            visited.add(current_node)

            if current_node == starting_node:
                is_undirected_edge_founded[0] = True
                return

            if current_node == None:
                current_node = starting_node

            for neighbor_node in prerequisites_graph[current_node]:
                if neighbor_node not in visited and not is_undirected_edge_founded[0]:
                    dfs(starting_node, neighbor_node)



        for node in prerequisites_graph.keys():
            visited = set()
            dfs(node, None)
            if is_undirected_edge_founded[0]:
                return False

        return True
