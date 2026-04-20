import sqlite3
import pandas as pd

schema = """
    drop table if exists suppliers;
    create table suppliers (
        id          integer primary key,
        name        text not null,
        country     text not null);
        """
supplier_data = [
    (1, "Acme Corp", "USA"),
    (2, "Globex Inc", "UK"),
    (3, "Initech", "USA"),
    (4, "Umbrella Corp", "Germany"),
    (5, "Soylent Corp", "USA"),
    (6, "Stark Industries", "USA"),]


def create_db(db_path: str) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.executescript(schema)
        conn.executemany(
            "insert into suppliers (id, name, country) values (?, ?, ?)",
            supplier_data,
        )
    print(f"Database created at {db_path} with suppliers table and sample data.")

def read_db(db_path: str) -> pd.DataFrame:
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query("select * from suppliers", conn)

if __name__ == "__main__":
    db_path = "suppliers.db"
    create_db("suppliers.db")
    df = read_db("suppliers.db")
    print(df)