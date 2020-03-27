"""
An array based implementation of A Suffix Tree, constructed using Ukkonens algorithm. This particular implementation
is very Object Orientated, using subclasses for Nodes, Edges and Suffix's.
As expected, Ukkonens algorithm was complicated and difficult to implement. To help me in doing so, I took advantage of
Online resources, particularly: https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-engl
-ish.  I mention this so as to explain some discrepancies between terminology used in the theoretics (lectures) and the
implementation conventions and considerations.
"""


class SuffixTree:

    class Node:
        """
        A class for nodes within the suffix tree
        """

        def __init__(self):
            """
            index in the Suffix Tree's self.nodes array. Like other implementations, is initialised to be negative if
            the suffix link is non-existent
            """
            self.suffix_link_node = -1

    class Edge:
        """A class edge in the suffix tree.
        param: first_char: index of start of string part represented by this edge
        param: last_char: index of end of string part represented by this edge
        param: source_node_index: index of source node of edge
        param: dest_node_index: index of destination node of edge
        """

        def __init__(self, first_char_index, last_char_index, source_node_index, dest_node_index, string):
            self.label = string[first_char_index:last_char_index]  # the edge label, which is crucial later for lcps
            self.first_char_index = first_char_index
            self.last_char_index = last_char_index
            self.source_node_index = source_node_index
            self.dest_node_index = dest_node_index

        def dest_node(self):
            """
            A function for returning destination node in the Suffix Tree in the form of an integer.
            This is essential for the algorithm described in the lcps method
            return: in integer format, as it is required for other methods
            """
            return int(self.dest_node_index)

        @property
        def length(self):
            return self.last_char_index - self.first_char_index

    class SubString:
        """
        Represents a SubString that lies within the from first_char_index to last_char_index. We introduce this class
        as we are able to represent any incomplete or completed substring in the tree as a sequence of SubString objects
        starting from node0.
        attributes: source node index: the index of the node in the suffix Tree's which is where the suffix starts from
                    first char index: the index of string[1...n] from which the suffix starts
                    last char index: the index of the string[1...k] at which the SubString ends
        """

        def __init__(self, source_node_index, first_char_index, last_char_index):
            self.source_node_index = source_node_index
            self.first_char_index = first_char_index
            self.last_char_index = last_char_index

        @property
        def length(self):
            return self.last_char_index - self.first_char_index

        def explicit(self):
            """A suffix is explicit if it ends on a node. first_char_index is set greater than last_char_index
            to indicate this.
            """
            return self.first_char_index > self.last_char_index

        def implicit(self):
            return self.last_char_index >= self.first_char_index

    def __init__(self, string):
        """
        standard python object initialisation. Note that edge information is stored in dictionary, nodes are housed in
        an array
        """
        self.string = string
        self.N = len(string) - 1
        self.nodes = [self.Node()]
        # since one of the most frequent tasks we will be required to do in lcps method is to search the edge stemming
        # from a particular node, I chose to simplify this by inserting into a dictionary (which is also my favourite
        # data structure). Whilst this aids the simplicity of such a search, and provides an opportunity to use a
        # structure I really like, this does hinder the run time, as we must now consider the cost of inserting edges
        # within the dictionary
        self.edges = {}
        self.active = self.SubString(0, 0, -1)
        for i in range(len(string)):
            # begin phase i...
            self.__phase(i)

    def __phase(self, last_char_index):
        """
        The 'phase' subroutine of Ukkonens Algorithm as dicussed in lectures.
        """
        # as the previously inserted node is
        last_parent_node = -1
        while True:
            parent_node = self.active.source_node_index
            if self.active.explicit() is True:
                # if prefix is already in tree, we can stop. Within this implementation, we can use the 'showstopper'
                # rule by breaking the loop this early
                if (self.active.source_node_index, self.string[last_char_index]) in self.edges:
                    break
            else:
                # hash key is based on starting node number, and first character of substring
                edge = self.edges[self.active.source_node_index, self.string[self.active.first_char_index]]
                if self.string[edge.first_char_index + self.active.length + 1] == self.string[last_char_index]:
                    # prefix is already embedded within the tree, so again, we conclude the phase by breaking the
                    # while loop
                    break
                parent_node = self.__split_edge(edge, self.active)

            self.nodes.append(self.Node())
            edge = self.Edge(last_char_index, self.N, parent_node, len(self.nodes) - 1, self.string)
            self.__insert_edge(edge)

            # set up for when we are extending on an edge
            if last_parent_node > 0:
                self.nodes[last_parent_node].suffix_link_node = parent_node
            last_parent_node = parent_node

            if self.active.source_node_index == 0:
                self.active.first_char_index += 1
            else:
                self.active.source_node_index = self.nodes[self.active.source_node_index].suffix_link_node
            self.__canonize_suffix(self.active)
        if last_parent_node > 0:
            self.nodes[last_parent_node].suffix_link_node = parent_node
        self.active.last_char_index += 1
        self.__canonize_suffix(self.active)

    def __insert_edge(self, edge):
        """
        A function for inserting edge's into the Suffix Tree's edges dictionary. During development, the __phase(i)
        subroutine became difficult to debug, hence edge removals and insertions have been decomposed into separate,
        private methods.
        :param edge:
        :return:
        """
        self.edges[(edge.source_node_index, self.string[edge.first_char_index])] = edge

    def __remove_edge(self, edge):
        """
        A function for removing a given edge from the Suffix Tree's edges dictionary During development, the __phase(i)
        subroutine became difficult to debug, hence edge removals and insertions have been decomposed into separate,
        private methods.
        """
        self.edges.pop((edge.source_node_index, self.string[edge.first_char_index]))

    def __split_edge(self, edge, suffix):
        """
        A subroutine for splitting edges to create the 'branches' of the suffix tree. This is called as a subroutine
        of Ukkonens Algorithm during particular phases. This method also has the additional functionality of grabbing a
        node from
        :param edge:
        :param suffix:
        :return:
        """
        self.nodes.append(self.Node())
        e = self.Edge(edge.first_char_index, edge.first_char_index + suffix.length, suffix.source_node_index,
                 len(self.nodes) - 1, self.string)
        self.__remove_edge(edge)
        self.__insert_edge(e)
        self.nodes[e.dest_node_index].suffix_link_node = suffix.source_node_index  # need to add node for each edge
        edge.first_char_index += suffix.length + 1
        edge.source_node_index = e.dest_node_index
        self.__insert_edge(edge)
        return e.dest_node_index

    def __canonize_suffix(self, sub_suffix):
        """
        As mentioned in the file doc_string, this is an example of discrepancy between lecture terminology and
        online resources. This function takes as argument a SubString object, and returns it in the so-called
        'canonical form'. This representation 'requires that the origin node in the SubString object be the closest
        parent to the endpoint of the string'.
        Canonizes the suffix, walking along its suffix string until it
        is explicit or there are no more matched nodes.
        """

        if not sub_suffix.explicit():
            e = self.edges[sub_suffix.source_node_index, self.string[sub_suffix.first_char_index]]
            if e.length <= sub_suffix.length:
                sub_suffix.first_char_index += e.length + 1
                sub_suffix.source_node_index = e.dest_node_index
                self.__canonize_suffix(sub_suffix)

    def lcps(self, i, j):
        """
        A method for calculating L(i, j) described in the assignment spec
        algorithm: we first cover multiple edge cases in O(1) time. For example, if the first character
                   at string[i] != string[j] then we can trivially return 0. Similar edge cases include if
                   i == j then the suffix is the same, and if j == n then we similarly compare the final characters.
                   In the 'special' case that string[i] == string[j] we must traverse the suffix tree starting from the
                   root node. we traverse the edge label for the next k characters until we reach a node at which there
                   are branching paths, implying that: suffix1[k+1] != suffix2[k+1]. Due to the structure of the suffix
                   tree, this is quite easy to find. At this point, we know our lcps score must be k.
        return: length of longest common prefix to the suffix starting at i and j
        """
        # to account for 0 indexing...
        i -= 1
        j -= 1

        # as per assignment spec, we must have i less than j
        assert i <= j <= len(self.string)
        s1, s2 = self.string[i:], self.string[j:]

        #  O(1) general edge case check:
        if s1[0] != s2[0]:
            return 0
        # another edge case: if suffix's are of the same length, then they're the same!
        if len(s1) == len(s2):
            return len(s1)
        # yet another edge case: if j == len(string)-1: its either 0 or 1:
        if j == len(self.string) - 1:
            return 1 if s1[0] == s2[0] else 0

        # specific case in which lcps > 0:
        return self.__lcps_score(s1, s2)

    def __lcps_score(self, s1, s2):
        """
        A function for traversing the Suffix Tree to compute the lcps score
        :param s1: suffix 1, string[i...n]
        :param s2: suffix 2, string[j...n]
        :return: the lcps score defined within the assignment spec.
        """
        curr_node, i = 0, 0

        while i < len(s1):
            edge1 = self.edges.get((curr_node, s1[i]))
            edge2 = self.edges.get((curr_node, s2[i]))

            if edge1.dest_node_index != edge2.dest_node_index:
                break

            i += edge1.length+1

        if i == len(s1):
            # remove the $
            return i-1

        return i


def read_file_nums(filename):
    """
    A function for reading the second of the two input files, that is, the one containing the i, j pairs.
    :param filename:
    return: a multi dim list, pairs: which contains in each sub_list a valid i, j pair
    """
    pairs = []

    with open(filename) as f:
        for line in f:
            line_pair = []
            for num in line.split():
                line_pair.append(int(num))
            pairs.append(line_pair)
    return pairs


def read_file_string(filename):
    """
    A function for reading the first of the two input files, that is the one containing string[1....n]
    param filename:
    return: contents of file as a string:
    """
    string = ''
    with open(filename) as f:
        for line in f:
            string += line
    return string


def driver(file1, file2):
    """
    A main function for driving task1 of assignment2. Takes as input the two files given from the command line
    param file1: file containing string[1...n]
    param file2: fil containing pairs i, j on each line
    return: output_lcps.txt file as per the assignment spec
    """
    string = read_file_string(file1) + '$'  # 'regularise's the string by convention
    pairs = read_file_nums(file2)
    tree = SuffixTree(string)

    output = open('output_lcps', 'w+')

    for pair in pairs:
        i = pair[0]
        j = pair[1]
        lcps = tree.lcps(i, j)

        outputline = str(i) + '\t' + str(j) + '\t' + str(lcps) + '\n'
        output.write(outputline)
    output.close()


if __name__ == '__main__':
    import sys
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    driver(file1, file2)
