# -*- coding: utf-8 -*-
"""text_to_graphGenerator .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-g8R5i7ZjkOMzOfM3rl7JEtePnT6BYzP
"""

!pip install graphviz

import graphviz

#simple graph tree
dot = graphviz.Digraph()
dot.node('A', 'Node A')
dot.node('B', 'Node B')
dot.edge('A', 'B', 'Edge 1')
dot.edge('B', 'A', 'Edge 2')

dot.render('graph', view=True)

#text to flowchart diagram
from graphviz import Digraph

def text_to_flowchart(text):
    # Split text into lines
    lines = text.strip().split('\n')

    # Create a new Digraph object
    dot = Digraph()

    # Add nodes and edges based on the text
    for line in lines:
        parts = line.split('->')
        from_node = parts[0].strip()
        to_node = parts[1].strip() if len(parts) > 1 else None

        dot.node(from_node)

        if to_node:
            dot.node(to_node)
            dot.edge(from_node, to_node)

    return dot

# Example text
example_text = """
Blue box - man
Red ellipse - woman
Blue line - Father/Child relation
Red line - Mother/Child relation
Green line - Spouse relation
Orange line - Ancestors (other) children
Violet line - Ancestors (other) spouse
"""

# Generate flowchart from text
flowchart1 = text_to_flowchart(example_text)

# Render and save the flowchart diagram
flowchart1.render('flowchart1_diagram', format='png', cleanup=True)

#text to family tree hierarchical graph
from graphviz import Digraph

def create_family_tree(family_members):
    dot = Digraph()

    # Add nodes for each family member
    for member, relationships in family_members.items():
        dot.node(member)

        # Add edges to represent relationships
        for relationship, related_members in relationships.items():
            for related_member in related_members:
                dot.edge(member, related_member, label=relationship)

    return dot

def main():
    # Define the family members and their relationships
    family_members = {
        "John": {"Spouse": ["Mary"], "Child": ["Alice", "Bob"]},
        "Mary": {"Spouse": ["John"], "Child": ["Alice", "Bob"]},
        "Alice": {"Parent": ["John", "Mary"]},
        "Bob": {"Parent": ["John", "Mary"]}
    }

    # Generate the family tree
    family_tree = create_family_tree(family_members)

    # Render and save the family tree diagram
    family_tree.render('family_tree_diagram', format='png', cleanup=True)
    print("Family tree diagram generated successfully.")

if __name__ == "__main__":
    main()





