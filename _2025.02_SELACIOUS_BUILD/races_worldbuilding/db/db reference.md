## races

- race_id
- name
- epithet
- overview
  x- sexual_paradigm
  x- cultural_roots

## factions

- faction_id
- race_id → races.race_id
- name
  x- philosophy

## sects

- sect_id
- faction_id → factions.faction_id
- name
  x- gender
  x- role
  x- style
  x- traits

## identity_roles

- role_id
- race_id → races.race_id
  x- identity_type (femboy, robot, non_sexed)
- name
  x- description

## rituals

- ritual_id
- race_id → races.race_id
- name
  x- description

## taboos

- taboo_id
- race_id → races.race_id
  x- description

## race_relations

- relation_id
- race_id → races.race_id
- related_race_id → races.race_id
  x- relation_type (admired, feared, envied, mocked, etc.)
  x- commentary

## race_tags

- tag_id
- race_id → races.race_id
- tag
