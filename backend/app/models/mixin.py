from datetime import datetime
from sqlalchemy import DateTime, Column

from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class Timestamp:
    create_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    update_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

