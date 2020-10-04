import os
from lib.led import LCD_1in44
from lib.led import LCD_Config
from helpers.singleton import Singleton
from PIL import Image, ImageDraw, ImageFont, ImageColor

# try:
@Singleton
class LcdManager:
    def __init__(self):
        self.LCD = LCD_1in44.LCD()

        Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  # SCAN_DIR_DFT = D2U_L2R
        success = self.LCD.LCD_Init(Lcd_ScanDir)
        self.LCD.LCD_Clear()

        root_dir = os.path.dirname(os.path.abspath(__file__))
        boot_image_path = os.path.join(root_dir, "../", "assets", "images", "boot-image.bmp")

        image = Image.open(boot_image_path)
        self.LCD.LCD_ShowImage(image, 0, 0)

    # # font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)
    # print "***draw line"
    # draw.line([(0, 0), (127, 0)], fill="BLUE", width=5)
    # draw.line([(127, 0), (127, 127)], fill="BLUE", width=5)
    # draw.line([(127, 127), (0, 127)], fill="BLUE", width=5)
    # draw.line([(0, 127), (0, 0)], fill="BLUE", width=5)
    # print "***draw rectangle"
    # draw.rectangle([(18, 10), (110, 20)], fill="RED")

    # print "***draw text"
    # draw.text((33, 22), "WaveShare ", fill="BLUE")
    # draw.text((32, 36), "Electronic ", fill="BLUE")
    # draw.text((28, 48), "1.44inch LCD ", fill="BLUE")

    # LCD.LCD_ShowImage(image, 0, 0)
    # LCD_Config.Driver_Delay_ms(500)

    # image = Image.open("time.bmp")
    # LCD.LCD_ShowImage(image, 0, 0)