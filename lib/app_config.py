import os
import yaml
from helpers.singleton import Singleton


@Singleton
class AppConfig:
    def __init__(self):
        root_dir = os.path.dirname(os.path.abspath(__file__))
        conf_file_path = os.path.join(root_dir, "../", "config.yaml")
        self.conf = yaml.load(open(conf_file_path), Loader=yaml.FullLoader)
        print(f"Loaded config from: {conf_file_path}")