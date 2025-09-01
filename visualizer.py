import json
import sys,os
import mermaid_builder
import mermaid_builder.flowchart
import mermaid as md
from mermaid.graph import Graph
from record import Record
from tree import Tree
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import datetime as dt
from datetime import datetime

OUTPUT_FOLDER = os.getcwd()
ROOT_PARENT: str | None

def awk(instring, index, delimiter):
    try:
        return [instring, instring.split(delimiter)[index - 1]][max(0, min(1, index))]
    except:
        return ""

def generate_tree(data: list) -> Tree:
    """Generates tree from record list
    """

    record_tree = Tree(data[0], [])

    remaining = [item for item in data if item != record_tree._root]
    while remaining:
        next_remaining = []
        for item in remaining:
            inserted = _insert_record(record_tree, item)
            if not inserted:
                next_remaining.append(item)
        if len(next_remaining) == len(remaining):
            print("Could not insert some nodes")
            for item in next_remaining:
                print(f"{item.span_id} parent: {item.parent_id}")
            break
        remaining = next_remaining

    return record_tree

def remove_duplicates(tree: Tree, node: Tree) -> None:
    """Remove nodes that have same name as their parent."""
    # Recursively process children first (post-order traversal)
    for child in list(node._subtrees):  # Copy to avoid mutation during iteration
        remove_duplicates(tree, child)

    # Skip the root node
    if node == tree:
        return

    # Find the parent node structurally
    parent = tree.get_parent_record(node)
    if parent and parent._root.name == node._root.name:
        # Reparent all children of node to parent
        parent._subtrees.remove(node)
        parent._subtrees.extend(node._subtrees)

def delete_node(tree: Tree, node: Tree) -> None:
    """Delete the node. Cannot delete the root of a tree.
    """
    if tree._subtrees == []:
        tree._root = None
    else:
        parent_node = tree.get_parent_record(node)
        parent_node._subtrees.remove(node)
        parent_node._subtrees.extend(node._subtrees)

def _get_ids_from_list(data: list) -> list:
    id_list = []
    for item in data:
        id_list.append(item.span_id)
    return id_list

def _insert_record(root: Tree, value: Record) -> None:
    if root._root.span_id == value.parent_id:
        new_node = Tree(value, [])
        root._subtrees.append(new_node)
        return True
    else:
        for subtree in root._subtrees:
            if _insert_record(subtree, value):
                return True
        return False

def load_from_file(file_path: str) -> dict:
    """Load python dictionary from json file
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return convert_to_record_list(data['records'])

def convert_to_record_list(data: dict) -> list:
    """Convert dictionary to list of records.
    """
    global ROOT_PARENT
    data_list = []
    count = 0
    for item in list(data):
        mermaid_id = "id" + str(count)
        count += 1
        if 'trace.id' in item:
            data_list.append(Record(item['dt.entity.service.entity.name'], item['trace.id'], item['span.id'],

                                    item['span.parent_id'], item['duration'],item['start_time'], item['end_time'], mermaid_id ))
    ROOT_PARENT = data_list[0].parent_id
    return data_list

def convert_to_gantt(data: dict) -> str:
    """Convert dictionary data to GANTT chart representation of waterfall trace chart
    """
    root_title = data[0].name


def get_sections(data: dict, root: str) -> str:
    """Get the records that will serve as the sections of the chart.
    """
    rows = []

def write2file(filename,message):
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            file.write(message)
    else:
        with open(filename, 'w') as file:
            file.write(message)

def print_tree(node: Tree, fileName,level=0):
    if node is None:
        return

    indentation = "  " * level  # Adjust indentation as needed
    print(f"{indentation}|-- {node._root.name}")
    write2file(fileName,f"{indentation}|-- {node._root.name}\n")

    for child in node._subtrees:
        print_tree(child, fileName, level + 1)

def str_tree(node: Tree, level=0) -> str:
    if node is None:
        return ''
    tree_str = ''
    indentation = "  " * level  # Adjust indentation as needed
    tree_str = tree_str + f"{indentation}|-- {node._root.name}\n"
    for child in node._subtrees:
        tree_str = tree_str + str_tree(child, level + 1)
    return tree_str

def generate_flow(data_tree: Tree) -> mermaid_builder.flowchart.Chart:
    """Generate str representation of mermaid flow chart from list
    """
    chart = mermaid_builder.flowchart.Chart(title = 'flowchart')
    data = data_tree.convert_to_list()
    for record in data:
        chart.add_node(mermaid_builder.flowchart.Node(title = record._root.name, id = record._root.mermaid_id))
        if record._root.parent_id != ROOT_PARENT:
            #print(record._root.span_id)
            chart.add_link_between(src = mermaid_builder.flowchart.Node(data_tree.get_parent_record(record)._root.mermaid_id),
                                   dest = mermaid_builder.flowchart.Node(record._root.mermaid_id))

    return chart

if __name__ == "__main__":

    #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    #file_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    file_path = input("Please enter file path:")
    path=os.path.dirname(file_path)
    timestamp= datetime.now().strftime("%Y-%m-%d-%H-%M")
    IndentFileName=str(os.path.basename(file_path).replace('.json','_'+timestamp+'_indent.txt'))
    ChartFileName=os.path.basename(file_path).replace('.json','_'+timestamp+'_mermaid.txt')
    IndentFileName=path+"\\output\\"+IndentFileName
    ChartFileName=path+"\\output\\"+ChartFileName

    data = load_from_file(file_path)
    my_tree = generate_tree(data)
    print_tree(my_tree,IndentFileName)
    chart = generate_flow(my_tree)
    print(str(chart))
    #remove_duplicates(my_tree, my_tree)
    #print_tree(my_tree,ChartFileName)

    chart = generate_flow(my_tree)
    write2file(ChartFileName,str(chart))
    #render = md.Mermaid(str(chart))
    #print(len(my_tree))


