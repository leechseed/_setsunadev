---
title: 📊 NARRATIVE ASTROLOGY BIRTH CHART DATABASE SCHEMA
updated: 2025-05-19 12:28:37Z
created: 2025-05-19 12:28:35Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---

-- 📊 NARRATIVE ASTROLOGY BIRTH CHART DATABASE SCHEMA  
-- Purpose: To structure and store hybrid astrological-narrative character data for simulation, analysis, or narrative design.

CREATE TABLE characters (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    alias TEXT,
    role TEXT, -- e.g., Protagonist, Antagonist
    narrative_archetype TEXT,
    summary TEXT
);

CREATE TABLE birth_data (
    character_id INTEGER REFERENCES characters(id),
    birth_date DATE,
    birth_time TEXT,
    birth_location TEXT
);

CREATE TABLE zodiac_profile (
    character_id INTEGER REFERENCES characters(id),
    sun_sign TEXT,
    moon_sign TEXT,
    rising_sign TEXT,
    mercury_sign TEXT,
    venus_sign TEXT,
    mars_sign TEXT,
    jupiter_sign TEXT,
    saturn_sign TEXT,
    uranus_sign TEXT,
    neptune_sign TEXT,
    pluto_sign TEXT
);

CREATE TABLE element_balance (
    character_id INTEGER REFERENCES characters(id),
    fire_percent INTEGER,
    earth_percent INTEGER,
    air_percent INTEGER,
    water_percent INTEGER
);

CREATE TABLE modality_balance (
    character_id INTEGER REFERENCES characters(id),
    cardinal_percent INTEGER,
    fixed_percent INTEGER,
    mutable_percent INTEGER
);

CREATE TABLE notable_aspects (
    id INTEGER PRIMARY KEY,
    character_id INTEGER REFERENCES characters(id),
    aspect TEXT,         -- e.g., "Mars square Pluto"
    interpretation TEXT
);

CREATE TABLE temperament_profile (
    character_id INTEGER REFERENCES characters(id),
    core_identity TEXT,  -- Synthesized from Sun + Rising
    emotional_core TEXT, -- Synthesized from Moon + Venus
    cognitive_mode TEXT, -- Synthesized from Mercury
    relational_style TEXT,
    aggression_profile TEXT
);

CREATE TABLE narrative_profile (
    character_id INTEGER REFERENCES characters(id),
    motivation TEXT,
    goal TEXT,
    flaw TEXT,
    conflict_internal TEXT,
    conflict_external TEXT,
    transformation_arc TEXT,
    theme_alignment TEXT,
    symbolism TEXT
);

CREATE TABLE visual_design (
    character_id INTEGER REFERENCES characters(id),
    sigil_motif TEXT,
    color_palette TEXT,
    costume_notes TEXT,
    architecture_style TEXT
);
