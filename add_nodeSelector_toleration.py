import yaml

output = []
toleration = {'tolerations': [{
    'key': 'node-role.kubernetes.io/master',
    'operator': 'Exists',
    'effect': 'NoSchedule'
}]}

node_selector = {'nodeSelector': 
    {'cpu.node': 'true'}
}

with open('original.yaml','r') as input_file:
    all_files = yaml.load_all(input_file)

    for f in all_files:
        if f['kind'] == 'Deployment' or f['kind'] == 'StatefulSet':
            f['spec']['template']['spec'].update(toleration)
            f['spec']['template']['spec'].update(node_selector)
        output.append(f)
        

with open('output.yaml', 'w') as output_file:
    yaml.dump_all(output, output_file)