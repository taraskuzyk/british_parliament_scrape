import dataclasses

from status import Status


@dataclasses.dataclass
class Petition:
    name: str
    url: str
    text: str
    status: Status
