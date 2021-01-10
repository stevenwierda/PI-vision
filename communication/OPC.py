from opcua import Client
from opcua import ua

import time


class OPC():
    def __init__(self, args):
        self.arg = args
        self.serverIP = "OPC.tcp://" + self.arg.username + ":4080"
        self.client = Client(self.serverIP)
        self.client.connect()

    def setValue(self, node, value):
        self.node = self.client.get_node(node)
        self.node.set_value(value)

    def getValue(self, node):
        self.node = self.client.get_node(node)
        return self.node.get_value()
