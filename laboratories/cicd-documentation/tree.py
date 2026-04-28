from node import Node

##
# @class Tree
# @brief Clasa pentru gestionarea unui arbore binar de căutare (Binary Search Tree).
#
class Tree:
    """ Tree class for binary tree """

    ##
    # @brief Constructorul clasei Tree.
    # Initializează rădăcina arborelui ca fiind nulă.
    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    ##
    # @brief Returnează nodul rădăcină al arborelui.
    # @return Node: Obiectul rădăcină sau None dacă arborele este gol.
    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    ##
    # @brief Adaugă o valoare nouă în arbore.
    # @param data (int): Valoarea care urmează să fie inserată.
    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    ##
    # @brief Metodă recursivă internă pentru inserarea datelor.
    # @param data (int): Datele de adăugat.
    # @param node (Node): Nodul curent de la care pornește căutarea poziției.
    def _add(self, data, node):
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    ##
    # @brief Caută o valoare specifică în arbore.
    # @param data (int): Valoarea căutată.
    # @return Node: Nodul găsit sau None dacă valoarea nu există.
    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    ##
    # @brief Metodă recursivă internă pentru găsirea unui nod.
    # @param data (int): Valoarea căutată.
    # @param node (Node): Nodul curent explorat.
    # @return Node: Nodul cu datele potrivite.
    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    ##
    # @brief Șterge întregul arbore prin resetarea rădăcinii.
    def deleteTree(self):
        self.root = None

    ##
    # @brief Afișează conținutul arborelui (Inorder).
    def printTree(self):
        if self.root is not None:
            self._printInorderTree(self.root)

    ##
    # @brief Parcurge și afișează arborele în inordine (stânga, rădăcină, dreapta).
    # @param node (Node): Nodul curent.
    def _printInorderTree(self, node):
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    ##
    # @brief Parcurge și afișează arborele în preordine (rădăcină, stânga, dreapta).
    # @param node (Node): Nodul curent.
    def _printPreorderTree(self, node):
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    ##
    # @brief Parcurge și afișează arborele în postordine (stânga, dreapta, rădăcină).
    # @param node (Node): Nodul curent.
    def _printPostorderTree(self, node):
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')