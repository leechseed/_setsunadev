CREATE TABLE characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    role TEXT,
    tags TEXT, -- Comma-separated values
    emotional_state TEXT,
    desire TEXT,
    truth TEXT,
    lie_they_believe TEXT,
    arc_type TEXT,
    occupation TEXT,
    relationship_web TEXT, -- JSON blob
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
