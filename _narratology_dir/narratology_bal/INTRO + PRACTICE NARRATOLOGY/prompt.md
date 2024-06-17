```json
TASK: TL;DR/SUMMARY of TEXT in JSON. JSON keys: "titles" (array of strings): 2-5 appropriate titles for TEXT; "tags" (string): tag cloud; "entities" (array of {"name", "description"} objects): named entities, including persons, organizations, processes, etc. their detailed description and relationships; "short_summaries" (array of strings): one-two sentence summaries of TEXT; "style" (string): type, sentiment and writing style of TEXT; "arguments" (array of strings): 5-10 main arguments of TEXT; "summary" (string): detailed summary of TEXT
```
## TL;DR/SUMMARY of TEXT in JSON

```json
{
  "titles": [
    "Title 1",
    "Title 2",
    "Title 3",
    "Title 4"
  ],
  "tags": "tag1, tag2, tag3, tag4, tag5",
  "entities": [
    {
      "name": "Entity 1",
      "description": "Description of entity 1."
    },
    {
      "name": "Entity 2",
      "description": "Description of entity 2."
    },
    {
      "name": "Entity 3",
      "description": "Description of entity 3."
    }
  ],
  "short_summaries": [
    "Short summary 1.",
    "Short summary 2."
  ],
  "style": "Style description; the type, sentiment, and writing style of the text.",
  "arguments": [
    "Argument 1.",
    "Argument 2.",
    "Argument 3.",
    "Argument 4.",
    "Argument 5."
  ],
  "summary": "A detailed summary of the text."
}
