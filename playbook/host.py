#!/usr/bin/env python3

# http://docs.ansible.com/ansible/developing_inventory.html
host_map = {
    "mlk8s": {
        "hosts": [
            "ml-node1.senses-ai.com",
            "ml-node2.senses-ai.com",
            "ml-node3.senses-ai.com",
        ]
    },
    "dev" : {
        "hosts": [
            "dev01.senses-ai.com",
            "dev02.senses-ai.com",
        ]
    },
    "all": {
        "children": ["mlk8s"]
    },
}

import json
print(json.dumps(host_map, indent=1))
