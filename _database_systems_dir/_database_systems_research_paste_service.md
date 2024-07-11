# Database Systems Design Concepts
Pulled from fireship video on SurrealDB
https://youtu.be/C7WFwgDRStM?si=d-sCARgRHYv9rBDU

## 1. Relational Paradigm
- A design framework that organizes data into tables (or relations) where each row represents a record and each column represents a data field.
- Uses a structured query language (SQL) and supports ACID properties, ensuring reliable transaction processing.

## 2. Relational Database
- A database that uses the relational model as its foundation.
- Typically managed by a relational database management system (RDBMS).
- Common operations include queries, updates, and schema modifications, all managed through SQL.

## 3. Schemafull
- Describes databases that require a predefined schema to organize data structure.
- Includes defining tables, columns, datatypes, and relationships before data can be added to the database.

## 4. Joins
- Operations in SQL that allow for combining rows from two or more tables based on a related column between them.
- Types include inner, left, right, and full joins, each serving different needs in data querying.

## 5. Record Links
- The references that connect different data records within a database.
- Often implemented as foreign keys in relational databases or as document references in non-relational systems.

## 6. ACID (Atomicity, Consistency, Isolation, Durability)
- A set of properties that guarantee reliable processing of database transactions.
- Ensure that transactions are processed reliably and that the database remains in a consistent state even in the event of failures.

## 7. New SQL
- Refers to modern relational databases that maintain the ACID guarantees of traditional SQL databases.
- Also offers the scalability and flexibility that modern applications require, often through distributed architectures.

## 8. Scalable
- The ability of a database system to handle a growing amount of work or its capability to be enlarged to accommodate that growth.
- Scalability can be achieved by scaling up (more powerful hardware) or scaling out (more machines).

## 9. Single Node
- A database system configured on a single machine or server.
- Can limit scalability and fault tolerance but simplifies management and reduces hardware costs.

## 10. Single Node in Memory
- A database system where all data is stored in the main memory (RAM) of a single server.
- Allows for high-speed data access and processing but requires mechanisms to ensure durability and fault tolerance.

## 11. Single Node on Disk
- A traditional database setup where data is stored on the hard disk of a single server.
- While slower than in-memory databases, it offers greater data durability and typically lower costs.

## 12. Persistence Layers
- The component of a database system that manages the storage of data in a durable and efficient manner.
- Ensures that data is saved to non-volatile storage, making it persistent across sessions.

## 13. Multiple Persistence Layers
- A database design that uses more than one persistence mechanism.
- Typically optimizes for different types of workloads (e.g., real-time processing and long-term storage), enhancing performance and scalability.

## 14. Multi-Tenant
- A database architecture that allows multiple customers or users (tenants) to be served by a single instance of a database or software application.
- Isolates or shares data among tenants as per configuration.

## 15. Multi-Model Database
- A database that supports storing data in more than one form, such as documents, graphs, and key-value pairs, in a single database system.
- Provides flexibility in how data is stored and accessed.

## 16. Document Paradigm
- A non-relational model that organizes data into documents rather than tables or rows.
- Each document stores related information together and is identifiable by a unique key.
- Commonly used in NoSQL databases.

## 17. Schemaless
- Describes databases that do not require a predefined schema to allow data storage.
- Data can be stored in various formats, and the structure can be defined or altered on the fly.

## 18. Embedded
- A database system embedded within an application.
- Allows the application to manage data locally without relying on a separate database management system.

## 19. Full Text Search
- A technique within databases that can search textual data to find matches against complete words and phrases rather than values of a specific column.

## 20. Realtime
- A feature of database systems where data updates and changes are immediately available to users and applications.
- Supports scenarios such as live dashboards and instant notifications.

## 21. Graph Paradigm
- A model that represents data as nodes and edges.
- Nodes typically represent entities and edges represent relationships between them.
- Facilitates operations like graph traversal and finding shortest paths.

## 22. Graph Connections
- The links between nodes in a graph database, representing relationships like friendships, networks, or hierarchies.
- Crucial for traversing and querying graph data.

## 23. Graph Traversal
- A process of visiting nodes in a graph database to retrieve or update data based on relationships.
- Uses algorithms like depth-first search or breadth-first search.

## 24. Temporal
- A feature in some databases that allows tracking and managing data across different points in time.
- Useful for scenarios that require audit capabilities or historical data analysis.

## 25. Unstructured Data
- Data that does not adhere to a specific format or structure, such as text, images, and video.
- Managing unstructured data often requires more flexible data models and indexing strategies.

## 26. Events
- In database systems, events are significant occurrences that systems respond to, such as updates or changes in the data.
- Often trigger processes like logging or notifications.

## 27. Geospatial Data
- Data related to geographic positions on Earth.
- Geospatial databases handle such data and provide querying based on location and distance.

## 28. Analytics Views
- Special database constructs that are optimized for analysis and querying.
- Often used in business intelligence and data warehousing.

## 29. Surreal DB
- A newer multi-model database that combines graph, document, and relational paradigms.
- Offers SQL and NoSQL capabilities in a single, scalable, real-time system.
