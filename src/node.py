class Node(object):
    name = ""

    x = 0.0
    w = 0.0
    b = 0.0

    run = True

    outputs = None
    name = ""

    def __init__(self, _output=None, _name=""):
        self.outputs = _output
        self.name = _name

    def __str__(self):
        return "Name: " + self.name + ", X: " + str(self.x) + ", W: "+ str(self.w) + ", B: " + str(self.b) + ", OUTPUT: " + str(self.outputs)