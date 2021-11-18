import subprocess

class Tshark:
    p=subprocess
    def start(self, interface):
        self.p.Popen(['tshark', '-i', interface], stdout=subprocess.PIPE)
        return self.p

    def stop(self):
        self.p.terminate()
        return self.p.Popen.poll()