import breadpy.settings
from sqlalchemy import create_engine

engine = create_engine(
    breadpy.settings.DATABASE_ENGINE_URL,
    pool_recycle=1800,
    )

