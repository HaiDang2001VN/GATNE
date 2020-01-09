import os
from threading import Lock, Thread

from walk import RWGraph
from utils import get_G_from_edges

class Walker:
    def __init__(self,network_data, num_walks, walk_length, schema, node_type):
        super().__init__()
        self.network_data = network_data
        self.num_walks = num_walks
        self.walk_length = walk_length
        self.schema = schema
        self.node_type = node_type
        self.walks = []
        for layer_id in network_data:
            self.walks.append(None)
    
    def _walk(self, layer_id, index):
        tmp_data = self.network_data[layer_id]
        # start to do the random walk on a layer

        layer_walker = RWGraph(get_G_from_edges(tmp_data), node_type=self.node_type)
        layer_walks = layer_walker.simulate_walks(self.num_walks, self.walk_length, schema=self.schema)
        self.walks[index] = layer_walks

    def walk(self):
        ths = []
        index = 0
        for layer_id in self.network_data:
            th = Thread(target=self._walk, args=(layer_id, index,))
            index += 1
            ths.append(th)
            th.start()
        for th in ths:
            th.join()
        return self.walks