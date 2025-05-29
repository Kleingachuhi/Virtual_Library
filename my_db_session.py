from database import SessionLocal

def get_session():
    """
    Returns a new session instance. 
    Use it to interact with the database. 
    """

    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
