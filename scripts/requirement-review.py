"""
An LLM-powered engineering requirements reviewer. Given a requirement ID, it will generate feedback and post it as a Notion comment.
"""
from notion_client import Client
from decouple import config
from typing import List, Optional
import json
import openai
from pydantic import BaseModel
from typing import List


class Requirement(BaseModel):
    name: Optional[str] = None
    collection: Optional[str] = None
    parent: Optional[List[str]] = None
    type: Optional[str] = None
    stakeholder: Optional[List[str]] = None
    system: Optional[List[str]] = None
    qualifier: Optional[str] = None
    description: Optional[str] = None
    rationale: Optional[str] = None
    verification_method: Optional[List[str]] = None
    child: Optional[List[str]] = None


class SystemGPT:
    def __init__(self, notion: Client, database_id: str):
        self.notion = notion
        self.database_id = database_id

    def fetch_all_rows(self) -> List[dict]:
        """Fetches all rows from a Notion database by handling pagination."""
        start_cursor: Optional[str] = None
        all_rows: List[dict] = []

        while True:
            response: dict = self.notion.databases.query(
                **{
                    "database_id": self.database_id,
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

    def get_requirement_name_by_id(self, id: str) -> str:
        page = self.notion.pages.retrieve(id)
        name_title_list = page["properties"]["Name"].get("title", [])
        name = name_title_list[0]["plain_text"] if name_title_list else None
        return name

    def get_requirements(self) -> List[Requirement]:
        pages = self.fetch_all_rows()

        requirements: List[Requirement] = []
        for page in pages:
            name_title_list = page["properties"]["Name"].get("title", [])
            name = name_title_list[0]["plain_text"] if name_title_list else None
            print(f"Processing ID: {name}")

            collection_select = page["properties"]["Collection"].get("select")
            if collection_select:
                collection = collection_select.get("name")
            else:
                collection = None
            print(collection)

            parent = [
                self.get_requirement_name_by_id(parent["id"])
                for parent in page["properties"]["Parent"]["relation"]
            ]
            print(parent)

            type_select = page["properties"]["Type"].get("select")
            if type_select:
                tyype = type_select.get("name")
            else:
                tyype = None
            print(tyype)

            stakeholder = [
                stakholder["name"]
                for stakholder in page["properties"]["Stakeholder"]["multi_select"]
            ]
            print(stakeholder)

            system = [
                stakholder["name"]
                for stakholder in page["properties"]["System"]["multi_select"]
            ]
            print(system)

            qualifier = page["properties"]["Qualifier"]["select"]["name"]

            print(qualifier)

            description = page["properties"]["Description"]["rich_text"][0][
                "plain_text"
            ]
            print(description)

            rationale = page["properties"]["Rationale"]["rich_text"][0]["plain_text"]
            print(rationale)

            verification_method = [
                method["name"]
                for method in page["properties"]["Verification Method"]["multi_select"]
            ]
            print(verification_method)

            child = [
                self.get_requirement_name_by_id(child["id"])
                for child in page["properties"]["Child"]["relation"]
            ]
            print(child)

            requirement = Requirement(
                name=name,
                collection=collection,
                parent=parent,
                type=tyype,
                stakeholder=stakeholder,
                system=system,
                qualifier=qualifier,
                description=description,
                rationale=rationale,
                verification_method=verification_method,
                child=child,
            )

            requirements.append(requirement)
            json_string = json.dumps(requirements, default=lambda o: o.dict(), indent=4)

            # Write to file
            with open("requirements.json", "w") as file:
                file.write(json_string)

        return requirements


if __name__ == "__main__":
    NOTION_KEY: str = config("NOTION_KEY")
    NOTION_REQUIREMENTS_DATABASE_ID: str = config("NOTION_REQUIREMENTS_DATABASE_ID")
    notion: Client = Client(auth=NOTION_KEY)

    controller = SystemGPT(notion, NOTION_REQUIREMENTS_DATABASE_ID)
    print("Fetching requirements...")
    requirements = controller.get_requirements()

    json.dump(requirements, "output.json", indent=4)
    print("Output saved to file")
