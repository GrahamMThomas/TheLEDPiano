import time
from lib.midi_message import MidiMessage
from lib.app_config import AppConfig
from lib.light_strip import LightStrip
from lib.midi_device import MidiDevice
from helpers.functions import hex_to_rgb

CONFIG = AppConfig.instance().conf

synthesia = MidiDevice(CONFIG["devices"]["synthesia"])
piano = MidiDevice(CONFIG["devices"]["piano"])

light_strip = LightStrip.instance()


def play_note(msg):
    color_conf = CONFIG["colors"]
    color = color_conf["default"]

    if msg.is_left_hand() and msg.is_black_key():
        color = color_conf["left_black"]
    elif msg.is_left_hand() and not msg.is_black_key():
        color = color_conf["left"]
    elif msg.is_right_hand() and msg.is_black_key():
        color = color_conf["right_black"]
    elif msg.is_right_hand() and not msg.is_black_key():
        color = color_conf["right"]

    light_strip.set_led(msg, hex_to_rgb(color))


print("Started Piano Visualizer by CwakrJax!")
print("-" * 30)

while True:
    if not synthesia.connected():
        light_strip.end_synthesia_song()

    for raw_msg in synthesia.iter_pending():
        if raw_msg.type not in ["note_on", "note_off"]:
            light_strip.end_synthesia_song()
            continue
        else:
            if not light_strip.in_song:
                print("Synthesia Interaction Detected...")
            light_strip.start_synthesia_song()

        msg = MidiMessage(raw_msg, from_synthesia=True)
        print(msg)

        if raw_msg.type == "note_on":
            play_note(msg)
        elif raw_msg.type == "note_off":
            light_strip.off_led(msg)

    for raw_msg in piano.iter_pending():
        if raw_msg.type not in ["note_on", "note_off"]:
            continue
        msg = MidiMessage(raw_msg)
        print(msg)

        if raw_msg.type == "note_on":
            play_note(msg)
        elif raw_msg.type == "note_off":
            light_strip.off_led(msg)