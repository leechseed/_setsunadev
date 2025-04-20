
CREATE TABLE relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id INTEGER NOT NULL,
    target_id INTEGER NOT NULL,
    relationship_type TEXT, -- e.g., friend, rival, sibling, etc.
    trust INTEGER DEFAULT 50, -- 0 to 100 scale
    tension INTEGER DEFAULT 0, -- 0 to 100 scale
    intimacy INTEGER DEFAULT 0, -- 0 to 100 scale
    history_log TEXT, -- Freeform log or JSON string
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_id) REFERENCES characters(id) ON DELETE CASCADE,
    FOREIGN KEY (target_id) REFERENCES characters(id) ON DELETE CASCADE
);
