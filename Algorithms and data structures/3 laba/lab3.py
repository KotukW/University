from xml.etree import ElementTree

def treeFindSolution(root):
    global qstn
    choice = qstn[int(root.tag[1])-1]
    for element in root:
        x = element.attrib['id']
        if element.tag == "Answer" and element.attrib['id'] == choice:
            print(element.text)
        elif element.attrib['id'] == choice:
            treeFindSolution(element)

global qstn
tree = ElementTree.parse("3 laba\\tree.xml")
root = tree.getroot()
qstn = input()
treeFindSolution(root)
