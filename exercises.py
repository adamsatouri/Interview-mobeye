def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """

    # Write your code here
    if len(s1) != len(s2) :
        return False

    s1_hash , s2_hash = {} , {} 

    for i in range(len(s1)):
        if s1[i] in s1_hash:
            s1_hash[s1[i]]+=1
        else:
            s1_hash[s1[i]]=1

        if s2[i] in s2_hash:
            s2_hash[s2[i]]+=1
        else:
            s2_hash[s2[i]]=1
            
    return (s1_hash == s2_hash)
    pass


def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """

    # Write your code here
    if len(string) == 0 :
        return True

    count = 0

    for i in string:
        if count < 0:
            return False
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

    if count == 0:
        return True
    else:   
        return False
    


def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """

    # Write your code here
    from queue import Queue
    def check(x,y):
        return ((x > -1 and x < nr) and (y > -1 and y < nc) and (maze[x][y] != 0))

    def get_parent(current_node):
        current_level = level[current_node[0]][current_node[1]]
        for i in range(4):
            x_translated , y_translated = current_node[0] + dx[i] , current_node[1] + dy[i]
            if (x_translated > -1 and x_translated < nr) and ( y_translated > -1 and y_translated < nc) and level[x_translated][y_translated] == current_level-1:
                current_node  = (x_translated , y_translated)
                return current_node 




    nr = len(maze)
    nc = len(maze[0])
    nlevel = 0

    level = [[-1 for col in range(nc)] for row in range(nr)]

    level[start[0]][start[1]] = nlevel

    q = Queue()

    q.put(start)

    dx,dy = [0,0,1,-1],[1,-1,0,0]

    reached = False

    while not q.empty() and not reached:
        
        current_node = q.get()
        for i in range(4):
            x_translated , y_translated = current_node[0] + dx[i] , current_node[1] + dy[i]
            if check(x_translated,y_translated) and level[x_translated][y_translated] == -1:
                q.put((x_translated,y_translated))
                level[x_translated][y_translated] = level[current_node[0]][current_node[1]] + 1
                if x_translated == end[0] and y_translated == end[1]:
                    reached = True 
                    break

    if not reached: 
        return False

    
    output = [end]
    current_node = end
    while current_node  != start :
        current_node  = get_parent(current_node)
        output.append(current_node)
        
    return output[::-1]