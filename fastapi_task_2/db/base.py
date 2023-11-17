from sqlalchemy.ext.declarative import declarative_base

from fastapi_task_2.db.models import load_all_models

Base = declarative_base()
metadata = Base.metadata
load_all_models()
