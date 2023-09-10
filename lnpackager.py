"""
# LNPackager

### By Genius_um / [MazeGroup](http://mazegroup.rf.gd/) - 2023

`Version 0.0.1`

---

LNPackager is a Python Module for make Neuronnal Nodes

and make Package for train they.
"""

import random
import copy

class Node():
    """
    A node as a value and a marge value.

    At a generation, this value change

    for a random value between the marge.
    """
    def __init__(self, value:int=0, marge:int=10):
        self.value_original = value
        self.value = copy.deepcopy(value)
        self.marge = marge
    
    def generate(self):
        """
        At a generation, the value change

        for a random value between the marge.
        """
        self.value = random.randint(self.value_original - self.marge, self.value_original + self.marge)

def MultiplesNodes(number:int=100, values:int=0, marges:int=10):
    """
    You can make multiples nodes

    with this function and choose
    
    there values and marges.
    """
    nodes_list = []
    for index in range(number):
        nodes_list.append(Node(values, marges))
    return nodes_list

class LNPackage():
    """
    Package class.

    Learning types :

    - ctr (Check To Result)

    More your attemps and nodes numbers

    is big, more is your waiting time.
    """
    def __init__(self, pathname:str, learningtype:str, nodes:list, validresults:list, attemps:int):
        self.learning_types = [
            "ctr" # Check To Result
        ]

        if learningtype.lower() in self.learning_types:
            self.lnp_name = pathname
            self.learning_type = learningtype
            self.nodes_originals = nodes
            self.nodes = copy.deepcopy(nodes)  # Utilise une copie profonde
            self.valid_result = validresults
            self.train_result = []
            self.attemps = attemps
        else:
            self.learning_type = self.learning_types[0]

    def train(self, logger:bool=False):
        """
        Training : you can log the

        advencement of your train but

        it's more low.

        ---

        CTR Method Training :

        For attemps:
            For nodes:
                Generate nodes values

                Choose random operator

                Result calculated with operator
        """
        if self.learning_type == self.learning_types[0]:
            all_operations_logger = []
            for attemp in range(self.attemps):
                for node in self.nodes:
                    node.generate()
                result = 0
                operations_logger = []
                for node in self.nodes:
                    if node.value != 0:
                        operation = random.randint(1, 4)
                        if operation == 1:
                            result += node.value
                        elif operation == 2:
                            result -= node.value
                        elif operation == 3:
                            result *= node.value
                        elif operation == 4:
                            result /= node.value
                        result = round(result)
                        operations_logger.append([node.value, operation, result])
                if (result == self.valid_result) and (operations_logger != []):
                    all_operations_logger.append(operations_logger)
                    if logger:
                        print(f"Attemps completed : {round(attemp * 100 / self.attemps, 2)}% | Valid Result")
                else:
                    if logger:
                        print(f"Attemps completed : {round(attemp * 100 / self.attemps, 2)}% | Invalid Result")
            self.train_result = all_operations_logger
    
    def make(self):
        """
        Make .lnp package file

        Syntax :
        ```text
        l-type-<training type>;valid-result:<valid result>;attemps:<attemps>;
        (!<node initial value>;~<node marge>;)<...>
        [[!<node value generated>;#<random operator>;?<result>;]<... * Nodes numbers>]<...>
        ```
        """
        file = open(f"{self.lnp_name}.lnp", "w")
        file.write(f"l-type-{self.learning_type};valid-result:{self.valid_result};attemps:{self.attemps};\n")
        for node in self.nodes_originals:
            value_ = node.value
            marge_ = node.marge
            file.write(f"(!{value_};~{marge_};)")
        file.write("\n")
        for operation in self.train_result:
            value = operation[0]
            operator = operation[1]
            result = operation[2]
            file.write(f"[!{value};#{operator};?{result};]")
        file.close()
