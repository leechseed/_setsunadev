# Fields Needing Expansion into Dedicated Tables

## races

- [x] sexual_paradigm → **Create `sexual_paradigms` table**
- [x] cultural_roots → **Create `cultural_roots` table**

## factions

- [x] philosophy → **Create `faction_philosophies` table**

## sects

- [x] gender → **Consider gender types as ENUM or `sect_genders` lookup table**
- [x] role → **Create `sect_roles` table**
- [x] style → **Create `sect_styles` table**
- [x] traits → **Create `sect_traits` table**

## identity_roles

- [x] identity_type → **Create `identity_types` table (femboy, robot, non_sexed)**
- [x] description → **Move to `identity_type_descriptions` table or expand**

## rituals

- [x] description → **Consider splitting into `ritual_steps`, `stimuli`, or `orgasmic_difficulty_rating` fields**

## taboos

- [x] description → **Break into `taboo_type`, `offense_trigger`, or `punishment_method`**

## race_relations

- [x] relation_type → **Create `relation_types` table (admired, feared, etc.)**
- [x] commentary → **Create `commentary_themes` or `relation_contexts`**
