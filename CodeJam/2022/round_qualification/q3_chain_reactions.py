def read_input():
    n = int(input())
    for _ in range(n):
        
        yield int(input()), list(zip([int(v) for v in input().split(' ')], [int(v) - 1 for v in input().split(' ')]))


if __name__ == '__main__':
    for i, (n, nodes) in enumerate(read_input()):
        # n = number of nodes
        # nodes[node_index] = (node_value, next_node_index)
        # in_edges[node_index] = # number of edges going into node node_index
        # a node_index of -1 is the abyss
        unprocessed_incomming_nodes = [0]*n
        for (_, next_i) in nodes:
            if next_i != -1:
                unprocessed_incomming_nodes[next_i] += 1

        node_cache = [None]*n

        frontier = [i for i, c in enumerate(unprocessed_incomming_nodes) if c == 0]

        score = 0
        while frontier:
            #print(frontier)
            node_index = frontier[-1]
            frontier.pop()

            node_value, next_node_index = nodes[node_index]

            while True:
                #print(f'{node_index=}, {node_value=}')
                if next_node_index == -1:
                    score += node_value
                    break

                next_node_unprocessed = unprocessed_incomming_nodes[next_node_index]
                next_node_value, next_next_node_index = nodes[next_node_index]
                next_node_cache_value = node_cache[next_node_index]

                #print(f'{next_node_index=}, {next_node_value=}, {next_node_unprocessed=}, {next_node_cache_value=}')

                if next_node_unprocessed == 1:
                    if next_node_cache_value is not None:
                        # The next node has a populated cache
                        score += max(next_node_cache_value, node_value)
                        node_value = min(next_node_cache_value, node_value)

                    # Update current_node to be a merge of the current node and the next node
                    node_value = max(node_value, next_node_value)
                    node_index = next_node_index
                    next_node_index = next_next_node_index
                else:
                    if next_node_cache_value is not None:
                        # Update the cache and add the unused value to the score
                        score += max(next_node_cache_value, node_value)
                        node_cache[next_node_index] = min(next_node_cache_value, node_value)
                    else:
                        # Set empty cache to the current node value
                        node_cache[next_node_index] = node_value

                    unprocessed_incomming_nodes[next_node_index] = next_node_unprocessed - 1
                    break

        print(f'Case #{i + 1}: {score}')


