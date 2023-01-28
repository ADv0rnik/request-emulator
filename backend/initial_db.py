from app.db.init_db import init_db
from app.db.session import SessionLocal


def init():
    db = SessionLocal()
    init_db(db)


def main():
    print("RUN INITIALIZATION")
    init()
    print("FINISH INITIALIZATION")


if __name__ == "__main__":
    main()
