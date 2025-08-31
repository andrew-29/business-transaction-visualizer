import json
import sys
import mermaid_builder
import mermaid_builder.flowchart
import mermaid as md
from mermaid.graph import Graph
from record import Record
from tree import Tree

def generate_tree(data: list) -> Tree:
    """Generates tree from record list
    """

    record_tree = Tree(data[0], [])

    """
    for item in data:
        _insert_record(record_tree, item)
    return record_tree
    """
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


def _get_ids_from_list(data: list) -> list:
    id_list = []
    for item in data:
        id_list.append(item.span_id)
    return id_list

def _insert_record(root: Tree, value: Record) -> bool:
    if root._root.span_id == value.parent_id:
        new_node = Tree(value, [])
        root._subtrees.append(new_node)
        return True
    else:
        for subtree in root._subtrees:
            if _insert_record(subtree, value):
                return True
        return False

def load_from_file(file_path: str) -> list:
    """Load python dictionary from json file
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return convert_to_record_list(data['records'])

def convert_to_record_list(data: dict) -> list:
    """Convert dictionary to list of records.
    """
    data_list = []
    count = 0
    for item in list(data):
        mermaid_id = "id" + str(count)
        count += 1
        if 'trace.id' in item:
            data_list.append(Record(item['dt.entity.service.entity.name'], item['trace.id'], item['span.id'],

                                    item['span.parent_id'], item['duration'],item['start_time'], item['end_time'], mermaid_id ))
    return data_list

def print_tree(node: Tree, level=0):
    if node is None:
        return

    indentation = "  " * level  # Adjust indentation as needed
    print(f"{indentation}|-- {node._root.name}")

    for child in node._subtrees:
        print_tree(child, level + 1)

def generate_flow(data: list, data_tree: Tree) -> mermaid_builder.flowchart.Chart:
    """Generate str representation of mermaid flow chart from list
    """
    chart = mermaid_builder.flowchart.Chart(title = 'flowchart')
    for record in data:
        chart.add_node(mermaid_builder.flowchart.Node(title = record.name, id = record.mermaid_id))
        print(record.parent_id, record.span_id)
        if isinstance(record.parent_id, str):
            print('hi')
            chart.add_link_between(src = mermaid_builder.flowchart.Node(data_tree.get_parent_record(record).mermaid_id),
                                   dest = mermaid_builder.flowchart.Node(record.mermaid_id))

    return chart

if __name__ == "__main__":
    file_path = input() #sys.argv[]
    data = load_from_file(file_path)
    my_tree = generate_tree(data)
    print(len(data))
    chart = generate_flow(data, my_tree)
    print(str(chart))
    render = md.Mermaid(str(chart))
    #print(len(my_tree))
    #print_tree(my_tree)


