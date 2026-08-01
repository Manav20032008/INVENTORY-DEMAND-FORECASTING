from config.config_loader import ConfigLoader

config = ConfigLoader.load_yaml("config/model_config.yaml")
print(config)