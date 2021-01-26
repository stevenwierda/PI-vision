from opcua import Client
from opcua import ua


class OPC():
    def __init__(self, args):
        self.arg = args
        #self.serverIP = "opc.tcp://" + self.arg.ip + ":4080"
        self.serverIP = "opc.tcp://192.168.1.10:4840"

        self.client = Client(self.serverIP)
        self.client.connect()

    def setValue(self, node, value):
        self.node = self.client.get_node(node)
        dv = ua.DataValue(ua.Variant(value, ua.VariantType.Float))
        dv.ServerTimestamp = None
        dv.SourceTimestamp = None
        self.node.set_value(dv)

    def getValue(self, node):
        self.node = self.client.get_node(node)
        value = self.node.get_value()
        print(value)
        #return self.node.get_value()

    def disconnect(self):
        self.client.disconnect()
