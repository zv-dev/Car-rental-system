
from Writer import Writer

class ConsoleWriter(Writer):

    def print(self, msg):
        for item in msg:
            if isinstance(item, dict):
                for key, value in item.items():
                    print(f"{key}: {value}", end=" ")
                print()