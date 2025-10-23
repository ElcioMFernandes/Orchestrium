import uuid, datetime, dataclasses

@dataclasses.dataclass
class Task:
    id: str
    name: str
    content: str
    created: datetime.datetime
    updated: datetime.datetime

    def __post_init__(self):
        if self.created is None:
            self.created = datetime.datetime.now(datetime.timezone.utc)
        if self.updated is None:
            self.updated = datetime.datetime.now(datetime.timezone.utc)

    @classmethod
    def create(cls, content: str, name: str) -> "Task":
        return cls(id=str(uuid.uuid4()), content=content, name=name, created=cls.created, updated=cls.updated)
    
    def dict(self) -> dict:
        return dataclasses.asdict(self)