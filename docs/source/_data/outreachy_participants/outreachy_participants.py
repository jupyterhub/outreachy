import json
from datetime import datetime
from pathlib import Path
from textwrap import dedent

import jsonschema
from jsonschema import validate

# Set filepath to participants data file
data_path = Path(__file__).resolve().parent
participants_data_file = data_path.joinpath("participants.json")
participants_schema_file = data_path.joinpath("participants.schema.json")

# Set path to save output file in. Create a tmp dir if it doesn't exist.
docs_path = data_path.parent.parent
tmp_path = docs_path.joinpath("tmp")
tmp_path.mkdir(exist_ok=True)

# Read in json defining Outreachy participants
with open(participants_data_file) as f:
    participants_data = json.load(f)

# Read in the JSON schema file
with open(participants_schema_file) as f:
    participants_schema = json.load(f)

# Validate the data against the schema
try:
    validate(participants_data, participants_schema)
except jsonschema.exceptions.ValidationError as err:
    raise err

# Sort cohorts in reverse chronological order
participants_data = sorted(
    participants_data,
    key=lambda x: datetime.strptime(x["round"], "%B, %Y").strftime("%Y-%m"),
    reverse=True,
)

for role in ["interns", "mentors", "community_coordinators"]:
    output_path = tmp_path.joinpath(f"{role}.txt")
    markdown = ""

    for participants in participants_data:
        # Sort participants into alphabetical order
        participants[role] = sorted(participants[role], key=lambda x: x["name"])

        # Begin MyST definition of grid with cards
        grid_md = dedent(
            """
            `````{{grid}} 1 2 3 3
            :gutter: 3
            :class-container: contributor-grid

            {card_md}
            `````
        """
        )

        # Add cards to the grid for each participant
        card_md = ""
        for person in participants[role]:
            card_md += dedent(
                f"""
                ````{{grid-item-card}}
                :class-header: bg-light
                :text-align: center

                **{person['name']}**

                ^^^

                ```{{image}} https://github.com/{person['github_handle']}.png?size=125
                ```

                [@{person['github_handle']}](https://github.com/{person['github_handle']})

                +++
                {f"[Read their blog!]({person['blog_url']})" if "blog_url" in person.keys() else ""}
                ````
            """
            )

        # Add the markdown for the sphinx design cards into the grid and add
        # cohort year as title
        grid_md = grid_md.format(card_md=card_md)
        final_md = f"### {participants['round']}\n" + grid_md
        markdown += final_md

    output_path.write_text(markdown + "\n")
