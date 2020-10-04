import board
import neopixel
from helpers.singleton import Singleton
from lib.app_config import AppConfig
from helpers.functions import hex_to_rgb
from time import sleep


@Singleton
class LightStrip:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(
            board.D18,
            AppConfig.instance().conf["pixel_count"],
            brightness=AppConfig.instance().conf["brightness"],
            pixel_order="GRB",
        )
        self.pixels.fill((0, 0, 0))  # Clear Board
        self.synthesia_pixels = [(0, 0, 0) for _ in range(AppConfig.instance().conf["pixel_count"])]
        self.in_song = False

    def set_led(self, msg, color):
        adjusted_color = tuple([int(val * msg.brightness) for val in color])

        pos = msg.keyboard_position()

        if msg.from_synthesia:
            self.pixels[pos] = adjusted_color
            self.synthesia_pixels[pos] = adjusted_color
        elif self.in_song:
            if self.synthesia_pixels[pos] == (0, 0, 0):
                self.pixels[pos] = hex_to_rgb(AppConfig.instance().conf["colors"]["error"])
            else:
                self.pixels[pos] = adjusted_color
        else:
            self.pixels[pos] = adjusted_color

    def off_led(self, msg):
        # If piano played this note but synthesia originally played it. Do nothing
        pos = msg.keyboard_position()
        if not msg.from_synthesia and self.synthesia_pixels[pos] != (0, 0, 0):
            self.pixels[pos] = self.synthesia_pixels[pos]
            return

        self.pixels[pos] = (0, 0, 0)
        self.synthesia_pixels[pos] = (0, 0, 0)

    def start_synthesia_song(self):
        self.in_song = True

    def end_synthesia_song(self):
        self.synthesia_pixels = [(0, 0, 0) for _ in range(AppConfig.instance().conf["pixel_count"])]
        self.in_song = False

    def play_boot_sequence(self):
        # trail_len = 10
        for x in range(len(self.pixels)):
            self.pixels[x] = (255, 255, 255)
            sleep(0.01)
        self.pixels.fill((0, 0, 0))
