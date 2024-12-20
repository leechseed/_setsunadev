# Here is a draft of the process order of taking wicked sources and processing them for the purpose of placing them into the next edition of the X_1 build

1. Generate a full and comprehensive summary of the book
   1. Provide an extensive and highly detailed overview of _book_. The summary must cover the most important concept of each chapter. Each important concept must be broken down into its most finite of parts.
      1. use chatgpt's standard summarizer
2. Generate a full and comprehensive summary of the book using Summary_Template
   1. Provide a comprehensive and detailed overview of the above text using the Summary_Template
3. Combine the two summaries
   1. Use the following data below to create a more comprehensive and nuanced document
4. Create additional data

   1. fully elaborate, contextualize, and provide additional supporting information for the following text.

5. Split the propositions and models into their own .md files
   1. use wicked_markdown_split.py
6. rename each .md file properly
7. From that summary, extract propositions and models

   1. Provide a comprehensive and detailed overview of the data below using the **wicked_model_template**. just provide the document. do not clutter with your conversational replies.

8. Add YAML data
   1.
9. Properly align model/framework to core competency
   1. "map Author's frameworks/models to the provided CORE categories based on the primary focus of each framework, aligning it with the domain that best captures its narrative function"
10. clean up meta data (titles, YAML, etc)
11. create table of contents
12. create visual aides
    1. Repost the entire document below with all the mermaid diagrams. keeping consistent structure and formatting. just provide the document. do not clutter with your conversational replies.
    2. use **mermaid_notation_template**
    3. fill out mindmaps
