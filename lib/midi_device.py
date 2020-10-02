import mido
from threading import Thread
from time import sleep
import subprocess
import re


class MidiDevice:
    def __init__(self, port_substring):
        self.port = None
        self.port_name = None
        self.management_thread = Thread(
            name=f"{port_substring} Connection",
            target=self.__manage_connection,
            args=[port_substring],
        )
        self.management_thread.start()

    def iter_pending(self):
        if self.port:
            return self.port.iter_pending()
        else:
            return iter(())

    def connected(self):
        return self.port is not None

    def __manage_connection(self, port_substring):
        while True:
            # Detect if device is here
            # mido.get_input_names causes a memory leak
            aconnect_process = subprocess.run(
                ["aconnect", "-l"], stdout=subprocess.PIPE, universal_newlines=True
            )
            matching_ports = re.findall(r" {4}\d+ '([^']+)\'", aconnect_process.stdout)
            matching_ports = [x for x in matching_ports if port_substring in x]

            if len(matching_ports) == 0:
                if self.port:
                    print(f"Lost connection to {self.port_name}")
                    self.port.close()
                    self.port = None
                    self.port_name = None

            elif len(matching_ports) > 1:
                raise LookupError(f"Found multiple devices with the substring {port_substring}")

            elif len(matching_ports) == 1 and self.port is None:
                self.port_name = matching_ports[0]
                print(f"Connected to {self.port_name}")
                self.port = mido.open_input(self.port_name)

            del aconnect_process
            sleep(0.2)
