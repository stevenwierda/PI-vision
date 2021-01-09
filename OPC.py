from opcua import Client
from opcua import ua

import time



class OPC():
    def __init__(self, args):
        self.arg = args
        self.clientCode = "OPC.tcp://"+ self.arg.username +":4080"

        self.client = Client(self.clientCode)
