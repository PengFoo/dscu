"""
file: BaseNode
author: fupeng
date: 2017/5/5


"""
from conf import *


class Node(object):
    """
    the node is a node of the pipeline, while the pipeline is a computational graph.
    each node could run independently, and it would check dependency before running. if dependency not satisfied, it
    would **run and only run the direct father node** first.
    ** the dependency check process is a recursion process*

    IMPORTANT: now the dependency check is based on the output file of the node, for the node which may not have an
     output file, you are still supposed to write an empty file as one node's finishing signal.
    """
    def __init__(self, name='', filenames=None, father_nodes=None):
        self.name = name
        self.father_nodes = []
        if father_nodes:
            self.father_nodes = father_nodes
        if filenames:
            self.filenames = [path + i for i in filenames]
        else:
            self.filenames = [path + name]

    def run(self):
        logging.info('starting run node {node_name}'.format(node_name=self.name))
        self.check_father()
        self.do_run()
        if self.filenames:
            for filename in self.filenames:
                if not os.path.exists(filename):
                    logging.error('node {node_name} does not exists after run the node'.format(node_name=self.name))
                    raise RuntimeError('node {node_name} does not exists after run the node'.format(node_name=self.name))

    def check_father(self):
        logging.info('checking dependency for {node_name}'.format(node_name=self.name))
        father_nodes = self.father_nodes or []
        for father_node in father_nodes:
            for filename in father_node.filenames:
                if not os.path.exists(filename):
                    logging.info('Dependency node {node_name} not satisfied yet, got to run it, {filename} not exists'
                                 .format(node_name=father_node.name, filename=filename))
                    father_node.run()
        logging.info('dependency satisfied for {node_name}!'.format(node_name=self.name))

    def do_run(self):
        raise RuntimeError('method not implemented!')

    def write_empty_file(self):
        for filename in self.filenames:
            with open(filename, 'w+') as f:
                f.write('done')

