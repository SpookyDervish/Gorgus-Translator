import socket
import pickle

from player import Player


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.56.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def get_player(self) -> Player:
        return self.player

    def connect(self):
        """When we connect to something we want to send back a piece of information to the thing that connected to us.
        """

        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data: str):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))