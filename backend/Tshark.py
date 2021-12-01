import subprocess

class Tshark:
    p=subprocess
    def start(self, interface):
        proc = self.p.Popen(['tshark', '-i', interface, '-c', '10000'], stdout=subprocess.PIPE)
        return proc

    def stop(self):
        self.proc
        return self.p.Popen.poll()