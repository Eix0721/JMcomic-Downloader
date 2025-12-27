import yaml

show_download_log = True

def cfg_init () ->None:
    with open("config.yaml", mode="w", encoding="utf-8") as cfg:
        yaml.safe_load(cfg)
