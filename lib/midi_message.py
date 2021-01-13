import re
from lib.app_config import AppConfig

class MidiMessage:
    def __init__(self, msg, from_synthesia=False):
        self.msg = msg
        self.note = msg.note

        self.velocity = msg.velocity
        self.brightness = min(max(self.velocity / 100, 0.20), 1.0)  # Value between 0.15 and 1.0

        self.channel = re.search(r"channel=(\d+)", str(self.msg)).group(1)
        self.type = msg.type
        self.from_synthesia = from_synthesia

    def is_black_key(self):
        return (self.note % 12) in [1, 3, 6, 8, 10]

    def keyboard_position(self):
        if self.note > 92:
            note_offset = 2
        elif self.note > 55:
            note_offset = 1
        else:
            note_offset = 0

        pos = (self.note - 20) * 2 - note_offset
        if AppConfig.instance().conf['invert']:
            pos = AppConfig.instance().conf.get('pixel_count') - pos

        return pos

    def is_right_hand(self):
        return self.channel == "12"

    def is_left_hand(self):
        return self.channel == "11"

    def __str__(self):
        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        octave = self.note // len(notes)
        note = notes[self.note % len(notes)]

        return f"{'[synth]' if self.from_synthesia else '[piano]'} {self.type} {note}{octave} ch.{self.channel} velocity={self.velocity}"
