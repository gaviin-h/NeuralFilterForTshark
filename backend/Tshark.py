import subprocess

class Tshark:
    p=subprocess
    def start(self, interface):
        proc = self.p.Popen(['tshark', '-i', interface, '-c', '1500'], stdout=subprocess.PIPE)
        return proc

    def stop(self):
        self.p.terminate()
        return self.p.Popen.poll()