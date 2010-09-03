import breadpy.settings
from sqlalchemy import create_engine
from sqlalchemy.engine import reflection

engine = create_engine(
    breadpy.settings.DATABASE_ENGINE_URL,
    pool_recycle=1800,
    )

inspector = reflection.Inspector.from_engine(engine)

