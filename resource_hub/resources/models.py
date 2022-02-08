from enum import Enum
from datetime import datetime
from resource_hub.settings import db


class ResourceType(Enum):
    Article = 1
    Documentation = 2
    Recording = 3
    Tutorial = 4


class Resource(db.Model):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(ResourceType))
    subject = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    modified_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __str__(self):
        return self.subject

    def __repr__(self):
        return '<Resource %r>' % self.subject
