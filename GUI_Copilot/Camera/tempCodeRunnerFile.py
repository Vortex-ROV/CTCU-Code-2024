def run(self):
        # receive data from server
        self.frame = self.client.recv()
        return self.frame