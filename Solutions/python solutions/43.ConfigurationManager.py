import configparser
import os

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.parser = configparser.ConfigParser()

    def load(self):
        if not os.path.exists(self.filepath):
            print(f"Error: Configuration file '{self.filepath}' not found.")
            return False
        self.parser.read(self.filepath)
        return True

class DatabaseConfig(Config):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.settings = {}

    def load_and_validate(self):
        if not self.load():
            return None

        if "database" not in self.parser.sections():
            print("Error: Missing [database] section in configuration file.")
            return None

        db_section = self.parser["database"]
        required_keys = ["host", "port", "user", "password", "dbname"]
        validated_settings = {}

        for key in required_keys:
            if key not in db_section or db_section[key].strip() == "":
                print(f"Error: Missing or blank required key '{key}'.")
                return None
            validated_settings[key] = db_section[key]

        self.settings = validated_settings
        print("Database settings successfully loaded and validated.")
        return self.settings

if __name__ == "__main__":
    with open("db.ini", "w") as f:
        f.write("[database]\n")
        f.write("host = localhost\n")
        f.write("port = 5432\n")
        f.write("user = admin\n")
        f.write("password = secret\n")
        f.write("dbname = production_db\n")

    db_config = DatabaseConfig("db.ini")
    config_data = db_config.load_and_validate()
    if config_data:
        print(config_data)