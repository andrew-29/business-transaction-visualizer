from record import Record

class Tree:
    """Implementation of tree data structure since for some reason python has no built-in tree class

    Private Instance Attributes:
    -_root: The item stored at the tree's root or None if the tree is empty
    -_subtrees: a list of the tree's subtrees

    Representation Invariants
    - If self._root is None then self._subtrees is an empty list
    """
    _root: Record | None
    _subtrees: list['Tree'] # type: ignore

    def __init__(self, root: object | None, subtrees: list['Tree']) -> None: # type: ignore
        """Initialize the tree
        """
        self._root = root
        self._subtrees = subtrees

    def __len__(self):
        if self.is_empty():         # tree is empty
            return 0
        elif self._subtrees == []:  # tree is a single item
            return 1
        else:                       # tree has at least one subtree
            size = 1  # count the root
            for subtree in self._subtrees:
                size += subtree.__len__()
            return size

    def __contains__(self, node: 'Tree') -> bool:
        if self._root == node._root:
            return True
        else:
            for subtree in self._subtrees:
                return subtree.__contains__(node)
            return False

    def is_empty(self):
        """Return if the tree is empty
        """
        return self._root is None

    def get_parent_record(self, node: 'Tree') -> 'Tree': # type: ignore
        """Precondition:
                -Both target node and target parent node are in the tree
                -Target node is not source node
        """
        for child in self._subtrees:
            if child == node:
                return self
            result = child.get_parent_record(node)
            if result:
                return result
        return None

    def convert_to_list(self) -> list:
        """Return a list of nodes contained in the tree
        """
        if self.is_empty():
            return []
        elif self._subtrees == []:
            return [self]
        else:
            tree_list = [self]
            for subtree in self._subtrees:
                tree_list = tree_list + subtree.convert_to_list()
            return tree_list

