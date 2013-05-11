#!/usr/bin/env python

import json, node, link, random

if __name__ == "__main__":
    nodes = []
    links = []

    for i in range(30):
        x = random.randint(100, 500)
        y = random.randint(100, 350)
        xfact = random.uniform(.1, 20)
        yfact = random.uniform(.1, 20)
        nodes.append(node.Node(i, str(i), x, y, xfact, yfact))
        
    print nodes

    for i in range(30):
        s = random.randint(0, len(nodes)-1)
        t = random.randint(0, len(nodes)-1)
        if s == t:
            i -= 1
            continue

        w = random.randint(77, 200)
        print s, t
        links.append(link.Link(nodes[s], nodes[t], w))

    data = {"nodes": nodes,
            "links": links}

    filename = raw_input("Save to what filename? ")
    
    with open(filename, 'w') as fout:
        fout.write(json.dumps(data))

             