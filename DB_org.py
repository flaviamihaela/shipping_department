import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("shipment_database.db")
DATA_DIR = Path("data")

def load_csvs():
    df0 = pd.read_csv(DATA_DIR / "shipping_data_0.csv")

    df1 = pd.read_csv(DATA_DIR / "shipping_data_1.csv")
    df2 = pd.read_csv(DATA_DIR / "shipping_data_2.csv")

    # spreadsheet 0
    df0 = df0.rename(columns={
        "origin_warehouse": "origin",
        "destination_store": "destination",
        "product_quantity": "quantity"
    })[["origin", "destination", "product", "quantity"]]

    # spreadsheets 1 and 2
    qty = (
        df1.groupby(["shipment_identifier", "product"])
           .size()
           .reset_index(name="quantity")
    )
    locs = df2[["shipment_identifier", "origin_warehouse",
                "destination_store"]].drop_duplicates()
    df12 = (
        qty.merge(locs, on="shipment_identifier", how="left")
           .rename(columns={"origin_warehouse": "origin",
                            "destination_store": "destination"})
           [["origin", "destination", "product", "quantity"]]
    )

    return pd.concat([df0, df12], ignore_index=True)


def ensure_products(conn, products):
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM product;")
    name_to_id = {name: pid for pid, name in cur.fetchall()}

    for name in products:
        if name not in name_to_id:
            cur.execute("INSERT INTO product (name) VALUES (?);", (name,))
            name_to_id[name] = cur.lastrowid
    conn.commit()
    return name_to_id


def insert_shipments(conn, df, name_to_id):
    cur = conn.cursor()
    cur.executemany(
        """INSERT INTO shipment (product_id, quantity, origin, destination)
           VALUES (?, ?, ?, ?);""",
        [(name_to_id[row.product], int(row.quantity),
          row.origin, row.destination) for row in df.itertuples()]
    )
    conn.commit()

def main():
    df = load_csvs()
    conn = sqlite3.connect(DB_PATH)
    name_to_id = ensure_products(conn, df["product"].unique())
    insert_shipments(conn, df, name_to_id)
    conn.close()
    print("Loaded", len(df), "rows into shipment table.")


if __name__ == "__main__":
    main()
