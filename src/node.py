class Node(object):
    name = ""

    x = 0.0
    w = 0.0
    b = 0.0

    run = True

    inputs = None
    outputs = None
    name = ""

    def __init__(self, _input=None, _output=None, _name=""):
        self.inputs = _input
        self.outputs = _output
        self.name = _name

    def __str__(self):
        return "Name: " + self.name + ", X: " + str(self.x) + ", W: "+ str(self.w) + ", B: " + str(self.b)