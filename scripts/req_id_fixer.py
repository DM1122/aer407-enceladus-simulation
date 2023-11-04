"""
A script to change underscores '_' for hyphens '-' of all requirement IDs in the Notion requirements database

Example:

ENC-LDR_COM-Data_Handling -> ENC-LDR-COM-Data-Handling
"""
from notion_client import Client
from decouple import config
from typing import List, Optional
from tqdm import tqdm

NOTION_DATABASE_ID: str = "a52b24e1172b4fd8b8febe5f03176598"


def fetch_all_rows(notion: Client, database_id: str) -> List[dict]:
    """Fetches all rows from a Notion database by handling pagination."""
    start_cursor: Optional[str] = None
    all_rows: List[dict] = []

    while True:
        response: dict = notion.databases.query(
            **{
                "database_id": database_id,
                "start_cursor": start_cursor,
                "page_size": 100,  # max page size allowed by the API
            }
        )
        all_rows.extend(response["results"])

        # Check if there's a next page
        start_cursor = response.get("next_cursor")
        if not start_cursor:
            break

    return all_rows


if __name__ == "__main__":
    print("Running requirement ID fixer...")

    NOTION_TOKEN: str = config("NOTION_TOKEN")
    notion: Client = Client(auth=NOTION_TOKEN)

    all_rows: List[dict] = fetch_all_rows(notion, NOTION_DATABASE_ID)

    consent: str = input(
        f"{len(all_rows)} requirements were found. Irreversible modifications will be made. Do you want to continue? (Y/N): "
    )
    if consent.lower() != "y":
        print("No changes made. Exiting.")
        exit()

    for row in tqdm(all_rows, desc="Updating rows", unit="row"):
        title_property = row["properties"]["Name"]["title"]
        if title_property:  # Check if the title list is not empty
            name: str = title_property[0]["text"]["content"]
            if "_" in name:
                new_name: str = name.replace("_", "-")
                notion.pages.update(
                    **{
                        "page_id": row["id"],
                        "properties": {"Name": [{"text": {"content": new_name}}]},
                    }
                )

    print("All underscores in the 'Name' column have been replaced with hyphens.")

    input("Done. Press any key to quit.")
