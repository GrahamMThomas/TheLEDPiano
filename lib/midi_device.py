import mido


class MidiDevice:
    def __init__(self, port_substring):
        self.port_name = self.__get_full_port_name(port_substring)
        self.midi = mido.open_input(self.port_name)

    def __get_full_port_name(self, port_substring):
        matching_ports = [x for x in mido.get_input_names() if port_substring in x]
        if len(matching_ports) == 0:
            raise LookupError(f"Unable to find connected midi device containing: {port_substring}")
        if len(matching_ports) > 1:
            raise LookupError(f"Found multiple midi devices containing: {port_substring}")
        return matching_ports[0]