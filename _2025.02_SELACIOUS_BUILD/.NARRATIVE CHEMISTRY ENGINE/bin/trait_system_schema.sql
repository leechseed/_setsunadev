
CREATE TABLE traits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    modifier_type TEXT,
    modifier_value INTEGER,
    duration INTEGER,
    description TEXT,
    is_temporary BOOLEAN DEFAULT 0
);


CREATE TABLE character_traits (
    character_id INTEGER NOT NULL,
    trait_id INTEGER NOT NULL,
    acquired_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    PRIMARY KEY (character_id, trait_id),
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
    FOREIGN KEY (trait_id) REFERENCES traits(id) ON DELETE CASCADE
);
