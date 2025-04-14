class Grand_father:
    def showGrandFather(self):
        print("A")

class Father(Grand_father):
    def showFather(self):
        print("B")

class Child(Father):
    def showChild(self):
        print("c")

child=Child()
child.showChild()
child.showFather()
child.showGrandFather()