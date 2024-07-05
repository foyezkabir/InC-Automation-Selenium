from enum import Enum


class DeviceView(str, Enum):
    MOBILE = "2"
    DESKTOP = "1"

    def __str__(self) -> str:
        return self.value


class Browsers(str, Enum):
    Chrome = "chrome"
    Firefox = "firefox"
    InternetExplorer = "internetExplorer"
    Edge = "edge"
