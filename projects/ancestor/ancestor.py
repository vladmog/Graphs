
# def earliest_ancestor(ancestors, starting_node):
#     pass

# ---------------------------------------------------

from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):

    # GET PARENTS FUNCT
    def get_parents(node):
        parents = []
        for ancestor in ancestors:
            if ancestor[1] == node:
                parents.append(ancestor[0])
        return parents


    # RETURN `-1` IF INPUT HAS NO PARENTS
    if len(get_parents(starting_node)) == 0:
        return -1


    # FIND PATHS FUNCT
    paths = []
    def find_paths(ancestors, vertex, path=None):
        if path is None:
            path = []
            
        path = path + [vertex]

        parents = get_parents(vertex)
        if len(parents) == 0:
            paths.append(path)

        else:
            for parent in parents:
                find_paths(ancestors, parent, path)


    # INVOKE FIND PATHS
    find_paths(ancestors, starting_node)

    print(paths)


    # ASSIGN LONGEST PATH AND (IF HAS ONE) ITS TIE
    longest_path_len = 0
    longest_path = []
    tied_path = []

    for path in paths:
        if len(path) > longest_path_len:
            longest_path = path
            longest_path_len = len(path)
        elif len(path) == longest_path_len:
            tied_path = path


    # RETURN PATH WITH SMALLER OLDEST ANCESTOR
    if len(tied_path) == 0:
        return longest_path[-1]
    elif longest_path[-1] > tied_path[-1]:
        return tied_path[-1]
    else:
        return longest_path[-1]







test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8)] << If more than three tied paths, result is inaccurate
print(earliest_ancestor(test_ancestors, 6))