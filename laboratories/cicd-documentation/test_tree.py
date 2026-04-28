import pytest
from tree import Tree

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

def test_find_one():    
    assert tree.find(2).data == 2
    assert tree.find(3).data == 3
    assert tree.find(67) is None

def test_find_two():
    assert tree.find(4).data == 4
    assert tree.find(-1) is None