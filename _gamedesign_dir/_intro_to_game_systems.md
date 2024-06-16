
### Cheat Sheet: Attributes and Mechanics in Game Objects

**Basic Concepts:**
1. **Game Object**: Any individual object in a game that performs actions. Examples: ground block, character.
2. **Attributes**: Values that influence rules/mechanics. Examples: texture, collision, movement speed, hit points.
3. **Mechanics**: Rules that govern the usage of game objects. Examples: movement, firing, collision damage.

**Mechanics vs. Attributes:**
- **Mechanics**: Encoded rules (e.g., movement rules).
- **Attributes**: Data values (e.g., movement speed).

**Analogy:**
- **Nouns (Attributes)**: Represent data objects in games.
- **Verbs (Mechanics)**: Represent actions or rules applied to data objects.
- **Microsystems**: Sentences (small functional units).
- **Macrosystems**: Chapters (larger systems).
- **Games**: Stories (complete experiences).

**Example - Chess:**
- **Squares**: Objects with rules about piece placement.
- **Pieces**: Objects with specific mechanics and attributes.
  - **King**:
    - **Mechanic**: Moves in 8 directions, 1 space.
    - **Attribute**: Movement distance = 1.
    - **Additional Mechanics**: Check and checkmate rules.
  - **Queen**:
    - **Mechanic**: Moves in 8 directions, up to 8 spaces.
    - **Attribute**: Movement distance = 8.

**Example - Galaga:**
- **Player’s Spaceship Mechanics**:
  - Moves side to side.
  - Fires projectiles.
  - Takes damage on collision.
- **Player’s Spaceship Attributes**:
  - Moving speed.
  - Firing rate.
  - Hit points.
- **Impact of Attribute Changes**:
  - Slower movement = harder game.
  - Faster firing rate = easier game.
  
**Listing Attributes:**
1. **Simple Games**: Few or no attributes (e.g., Checkers).
2. **Complex Games**: Many attributes, some visible, some hidden, some derived.
3. **Steps to Create Attributes**:
   - Analyze the object closely.
   - Define attributes before mechanics if possible.
   - Consider differences between instances of the object.

---

   ├── Attributes
   │   ├── Texture
   │   ├── Collision
   │   ├── Movement Speed
   │   └── Hit Points
   └── Mechanics
       ├── Movement Rules
       ├── Firing
       └── Collision Damage

Chess
   ├── King
   │   ├── Mechanic: Moves in 8 directions (1 space)
   │   ├── Attribute: Movement Distance = 1
   │   └── Additional Mechanics: Check, Checkmate
   └── Queen
       ├── Mechanic: Moves in 8 directions (up to 8 spaces)
       └── Attribute: Movement Distance = 8


Galaga
   ├── Player’s Spaceship Mechanics
   │   ├── Move Side to Side
   │   ├── Fire Projectiles
   │   └── Take Damage on Collision
   └── Player’s Spaceship Attributes
       ├── Moving Speed
       ├── Firing Rate
       └── Hit Points
---


# Game Mechanics and Attributes Boilerplate

## Movement Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Walk                   | Basic movement in any direction                              | Speed, Stamina             |
| Run                    | Faster movement in any direction                             | Speed, Stamina, Acceleration|
| Jump                   | Vertical movement                                            | Jump Height, Jump Speed    |
| Climb                  | Movement on vertical surfaces                                | Climb Speed, Stamina       |
| Swim                   | Movement in water                                            | Swim Speed, Breath Capacity|
| Fly                    | Aerial movement                                              | Flight Speed, Altitude     |

## Combat Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Melee Attack           | Close-range physical attack                                  | Damage, Attack Speed       |
| Ranged Attack          | Long-range attack using projectiles                          | Damage, Range, Accuracy    |
| Magic Attack           | Attack using magical abilities                               | Damage, Mana Cost, Cooldown|
| Defense                | Ability to reduce or block incoming damage                   | Armor, Block Rate          |
| Dodge                  | Quick movement to avoid attacks                              | Dodge Speed, Cooldown      |
| Heal                   | Restore health to self or allies                             | Heal Amount, Cooldown      |

## Interaction Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Pick Up                | Collecting items from the environment                        | Carry Capacity, Pick Up Speed|
| Open                   | Interacting with doors, chests, etc.                         | Interaction Time           |
| Talk                   | Engaging in dialogue with NPCs                               | Charisma, Influence        |
| Trade                  | Exchanging items with NPCs or other players                  | Negotiation Skill, Wealth  |
| Use                    | Utilizing items or equipment                                 | Efficiency, Durability     |

## Environmental Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Weather Effects        | Impact of weather on gameplay                                | Visibility, Movement Penalty|
| Day/Night Cycle        | Changes in game environment based on time                    | Visibility, Enemy Behavior |
| Terrain Interaction    | Movement and actions based on terrain type                   | Speed Penalty, Stamina Drain|
| Hazard Avoidance       | Navigating environmental dangers                             | Reflexes, Health Impact    |

## Resource Management Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Gather                 | Collecting resources from the environment                    | Gather Speed, Yield        |
| Craft                  | Creating items from raw materials                            | Crafting Speed, Quality    |
| Build                  | Constructing structures                                      | Build Speed, Durability    |
| Repair                 | Fixing damaged items or structures                           | Repair Speed, Efficiency   |

## Progression Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Level Up               | Increasing character level                                   | Experience Points, Skills  |
| Skill Upgrade          | Improving specific abilities                                 | Skill Points, Proficiency  |
| Unlock                 | Gaining access to new abilities or areas                     | Keys, Progress Milestones  |

## Social Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Friendship             | Building relationships with NPCs                             | Affinity, Trust            |
| Rivalry                | Competing with NPCs or other players                         | Influence, Respect         |
| Guild/Faction Join     | Becoming a member of a group                                 | Reputation, Loyalty        |

## Miscellaneous Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Stealth                | Moving or acting without being detected                      | Stealth Skill, Visibility  |
| Puzzle Solving         | Completing logic challenges                                  | Intelligence, Insight      |
| Exploration            | Discovering new areas                                        | Map Knowledge, Discovery Rate|

## Example of Attributes for a Generic "Person" Object:
| Attribute              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Health Points          | Overall health of the character                              |
| Stamina                | Energy available for actions                                 |
| Strength               | Physical power                                               |
| Agility                | Speed and reflexes                                           |
| Intelligence           | Mental acuity and problem-solving ability                    |
| Charisma               | Ability to influence others                                  |
| Armor                  | Defense against physical attacks                             |
| Mana                   | Energy available for magical abilities                       |
| Wealth                 | Amount of money or valuable items                            |
| Experience Points      | Progress towards the next level                              |

---

# Game Mechanics and Attributes for Grand Theft Auto V

---

## Movement Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Walk                   | Basic movement on foot                                       | Speed, Stamina             |
| Run                    | Faster movement on foot                                      | Speed, Stamina, Acceleration|
| Jump                   | Vertical movement                                            | Jump Height, Jump Speed    |
| Climb                  | Movement over obstacles                                      | Climb Speed, Stamina       |
| Swim                   | Movement in water                                            | Swim Speed, Breath Capacity|
| Drive                  | Operating vehicles                                           | Vehicle Speed, Handling, Acceleration|
| Fly                    | Operating aircraft                                           | Flight Speed, Altitude, Handling |

---

## Combat Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Melee Attack           | Close-range physical attack                                  | Damage, Attack Speed       |
| Ranged Attack          | Long-range attack using firearms                             | Damage, Range, Accuracy    |
| Explosive Attack       | Use of grenades, rockets, etc.                               | Damage, Blast Radius       |
| Defense                | Ability to reduce or block incoming damage                   | Armor, Cover Effectiveness |
| Dodge                  | Quick movement to avoid attacks                              | Dodge Speed, Cooldown      |
| Heal                   | Restore health using items                                   | Heal Amount, Cooldown      |

---

## Interaction Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Pick Up                | Collecting items from the environment                        | Carry Capacity, Pick Up Speed|
| Open                   | Interacting with doors, containers, etc.                     | Interaction Time           |
| Talk                   | Engaging in dialogue with NPCs                               | Charisma, Influence        |
| Trade                  | Buying and selling items with NPCs                           | Negotiation Skill, Wealth  |
| Use                    | Utilizing items or equipment                                 | Efficiency, Durability     |

---

## Environmental Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Weather Effects        | Impact of weather on gameplay                                | Visibility, Movement Penalty|
| Day/Night Cycle        | Changes in game environment based on time                    | Visibility, Enemy Behavior |
| Terrain Interaction    | Movement and actions based on terrain type                   | Speed Penalty, Stamina Drain|
| Hazard Avoidance       | Navigating environmental dangers (e.g., traffic, explosions) | Reflexes, Health Impact    |

---

## Resource Management Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Gather                 | Collecting resources from the environment                    | Gather Speed, Yield        |
| Craft                  | Creating items from raw materials (not prominent in GTA V)   | Crafting Speed, Quality    |
| Build                  | Constructing structures (not prominent in GTA V)             | Build Speed, Durability    |
| Repair                 | Fixing damaged vehicles or equipment                         | Repair Speed, Efficiency   |

---

## Progression Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Level Up               | Increasing character level (through missions)                | Experience Points, Skills  |
| Skill Upgrade          | Improving specific abilities (e.g., shooting, driving)       | Skill Points, Proficiency  |
| Unlock                 | Gaining access to new abilities or areas                     | Keys, Progress Milestones  |

---

## Social Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Friendship             | Building relationships with NPCs                             | Affinity, Trust            |
| Rivalry                | Competing with NPCs or other players                         | Influence, Respect         |
| Gang/Faction Join      | Becoming a member of a group                                 | Reputation, Loyalty        |

---

## Miscellaneous Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Stealth                | Moving or acting without being detected                      | Stealth Skill, Visibility  |
| Puzzle Solving         | Completing logic challenges                                  | Intelligence, Insight      |
| Exploration            | Discovering new areas                                        | Map Knowledge, Discovery Rate|

---

## Example of Attributes for a Generic "Person" Object in GTA V:
| Attribute              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Health Points          | Overall health of the character                              |
| Stamina                | Energy available for actions                                 |
| Strength               | Physical power                                               |
| Agility                | Speed and reflexes                                           |
| Intelligence           | Mental acuity and problem-solving ability                    |
| Charisma               | Ability to influence others                                  |
| Armor                  | Defense against physical attacks                             |
| Wealth                 | Amount of money or valuable items                            |
| Experience Points      | Progress towards the next level                              |
| Driving Skill          | Proficiency in operating vehicles                            |
| Shooting Skill         | Proficiency in using firearms                                |

---

This table provides a structured and extensive list of mechanics and attributes specifically tailored to "Grand Theft Auto V," which can be used as a reference or starting point for understanding the game's design elements.



---

# Game Mechanics and Attributes for Helldivers 2

---

## Movement Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Walk                   | Basic movement on foot                                       | Speed, Stamina             |
| Sprint                 | Faster movement on foot                                      | Speed, Stamina, Acceleration|
| Jump                   | Vertical movement                                            | Jump Height, Jump Speed    |
| Roll                   | Quick evasive movement                                       | Roll Distance, Cooldown    |
| Jetpack                | Aerial movement using a jetpack                              | Flight Speed, Fuel Capacity|

---

## Combat Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Melee Attack           | Close-range physical attack                                  | Damage, Attack Speed       |
| Ranged Attack          | Long-range attack using firearms                             | Damage, Range, Accuracy    |
| Grenade Throw          | Use of explosive projectiles                                 | Damage, Blast Radius       |
| Defense                | Ability to reduce or block incoming damage                   | Armor, Block Rate          |
| Dodge                  | Quick movement to avoid attacks                              | Dodge Speed, Cooldown      |
| Revive                 | Restore health to fallen allies                              | Revive Speed, Cooldown     |

---

## Interaction Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Pick Up                | Collecting items from the environment                        | Carry Capacity, Pick Up Speed|
| Activate               | Interacting with mission objectives                          | Activation Time            |
| Call Down              | Summoning equipment and reinforcements from orbit            | Cooldown, Precision        |
| Use                    | Utilizing items or equipment                                 | Efficiency, Durability     |

---

## Environmental Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Weather Effects        | Impact of weather on gameplay                                | Visibility, Movement Penalty|
| Day/Night Cycle        | Changes in game environment based on time                    | Visibility, Enemy Behavior |
| Terrain Interaction    | Movement and actions based on terrain type                   | Speed Penalty, Stamina Drain|
| Hazard Avoidance       | Navigating environmental dangers (e.g., traps, hostile terrain)| Reflexes, Health Impact    |

---

## Resource Management Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Gather                 | Collecting resources from the environment                    | Gather Speed, Yield        |
| Craft                  | Creating items from raw materials (not prominent in Helldivers 2)| Crafting Speed, Quality    |
| Ammo Management        | Ensuring sufficient ammunition                               | Ammo Capacity, Reload Speed|
| Repair                 | Fixing damaged equipment or vehicles                         | Repair Speed, Efficiency   |

---

## Progression Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Level Up               | Increasing character level (through missions)                | Experience Points, Skills  |
| Skill Upgrade          | Improving specific abilities (e.g., shooting, driving)       | Skill Points, Proficiency  |
| Unlock                 | Gaining access to new abilities or equipment                 | Keys, Progress Milestones  |

---

## Social Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Squad Coordination     | Teamwork and strategy with other players                     | Communication, Coordination|
| Reputation             | Building standing within the Helldivers community            | Affinity, Trust            |
| Rivalry                | Competing with other squads                                  | Influence, Respect         |

---

## Miscellaneous Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Stealth                | Moving or acting without being detected                      | Stealth Skill, Visibility  |
| Mission Completion     | Achieving objectives in missions                             | Mission Success Rate, Rewards|
| Exploration            | Discovering new areas and secrets                            | Map Knowledge, Discovery Rate|

---

## Example of Attributes for a Generic "Helldiver" Object:
| Attribute              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Health Points          | Overall health of the character                              |
| Stamina                | Energy available for actions                                 |
| Strength               | Physical power                                               |
| Agility                | Speed and reflexes                                           |
| Intelligence           | Tactical and strategic thinking                              |
| Armor                  | Defense against physical attacks                             |
| Ammo                   | Amount of ammunition available                               |
| Experience Points      | Progress towards the next level                              |
| Shooting Skill         | Proficiency in using firearms                                |
| Explosives Skill       | Proficiency in using grenades and other explosives           |
| Repair Skill           | Efficiency in fixing equipment                               |

---

This table provides a structured and extensive list of mechanics and attributes specifically tailored to "Helldivers 2," which can be used as a reference or starting point for understanding the game's design elements.


---
# Game Mechanics and Attributes for Baldur's Gate 3

---

## Movement Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Walk                   | Basic movement on foot                                       | Speed, Stamina             |
| Run                    | Faster movement on foot                                      | Speed, Stamina, Acceleration|
| Jump                   | Vertical and horizontal movement                             | Jump Distance, Jump Height |
| Climb                  | Movement on vertical surfaces                                | Climb Speed, Stamina       |
| Dash                   | Quick burst of speed during combat                           | Speed, Cooldown            |
| Teleport               | Magical instant movement                                     | Range, Cooldown, Mana Cost |

---

## Combat Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Melee Attack           | Close-range physical attack                                  | Damage, Attack Speed       |
| Ranged Attack          | Long-range attack using bows or spells                       | Damage, Range, Accuracy    |
| Spellcasting           | Using magical abilities to attack or assist                  | Spell Power, Mana Cost, Cooldown|
| Sneak Attack           | Stealthy attack causing additional damage                    | Damage, Stealth, Critical Hit Rate|
| Defense                | Ability to reduce or block incoming damage                   | Armor, Block Rate          |
| Dodge                  | Quick movement to avoid attacks                              | Dodge Speed, Cooldown      |
| Healing                | Restore health to self or allies                             | Heal Amount, Mana Cost, Cooldown|

---

## Interaction Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Pick Up                | Collecting items from the environment                        | Carry Capacity, Pick Up Speed|
| Lockpicking            | Opening locked doors and chests                              | Lockpicking Skill, Tool Quality|
| Disarm Trap            | Neutralizing traps to prevent damage                         | Trap Disarm Skill, Tool Quality|
| Dialogue               | Engaging in conversations with NPCs                          | Charisma, Persuasion, Deception|
| Trade                  | Buying and selling items with NPCs                           | Negotiation Skill, Wealth  |
| Use                    | Utilizing items or equipment                                 | Efficiency, Durability     |

---

## Environmental Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Weather Effects        | Impact of weather on gameplay                                | Visibility, Movement Penalty|
| Day/Night Cycle        | Changes in game environment based on time                    | Visibility, Enemy Behavior |
| Terrain Interaction    | Movement and actions based on terrain type                   | Speed Penalty, Stamina Drain|
| Hazard Avoidance       | Navigating environmental dangers (e.g., traps, hazards)      | Reflexes, Health Impact    |

---

## Resource Management Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Gather                 | Collecting resources from the environment                    | Gather Speed, Yield        |
| Craft                  | Creating items from raw materials                            | Crafting Speed, Quality    |
| Build                  | Constructing structures                                      | Build Speed, Durability    |
| Repair                 | Fixing damaged items or equipment                            | Repair Speed, Efficiency   |
| Manage Spell Slots     | Allocating limited spellcasting resources                    | Spell Slot Efficiency, Recovery Rate |

---

## Progression Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Level Up               | Increasing character level                                   | Experience Points, Skills  |
| Skill Upgrade          | Improving specific abilities                                 | Skill Points, Proficiency  |
| Unlock                 | Gaining access to new abilities or areas                     | Keys, Progress Milestones  |

---

## Social Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Friendship             | Building relationships with NPCs                             | Affinity, Trust            |
| Rivalry                | Competing with NPCs or other players                         | Influence, Respect         |
| Party Management       | Coordinating actions and strategies with party members       | Leadership, Coordination   |

---

## Miscellaneous Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Stealth                | Moving or acting without being detected                      | Stealth Skill, Visibility  |
| Puzzle Solving         | Completing logic challenges                                  | Intelligence, Insight      |
| Exploration            | Discovering new areas and secrets                            | Map Knowledge, Discovery Rate|

---

## Example of Attributes for a Generic "Character" Object in Baldur's Gate 3:
| Attribute              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Health Points          | Overall health of the character                              |
| Stamina                | Energy available for actions                                 |
| Strength               | Physical power                                               |
| Dexterity              | Agility and reflexes                                         |
| Constitution           | Endurance and vitality                                       |
| Intelligence           | Mental acuity and problem-solving ability                    |
| Wisdom                 | Perception and insight                                       |
| Charisma               | Ability to influence others                                  |
| Armor Class            | Defense against physical attacks                             |
| Mana                   | Energy available for magical abilities                       |
| Experience Points      | Progress towards the next level                              |
| Spellcasting Ability   | Proficiency in using spells                                  |
| Stealth Skill          | Proficiency in moving undetected                             |
| Lockpicking Skill      | Proficiency in unlocking doors and chests                    |
| Persuasion Skill       | Proficiency in convincing others                             |
| Perception Skill       | Ability to notice hidden things                              |

---

This table provides a structured and extensive list of mechanics and attributes specifically tailored to "Baldur's Gate 3," which can be used as a reference or starting point for understanding the game's design elements.

---

# Game Mechanics and Attributes for Baldur's Gate 3

---

## Movement Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Walk                   | Basic movement on foot                                       | Speed, Stamina             |
| Run                    | Faster movement on foot                                      | Speed, Stamina, Acceleration|
| Jump                   | Vertical and horizontal movement                             | Jump Distance, Jump Height |
| Climb                  | Movement on vertical surfaces                                | Climb Speed, Stamina       |
| Dash                   | Quick burst of speed during combat                           | Speed, Cooldown            |
| Teleport               | Magical instant movement                                     | Range, Cooldown, Mana Cost |

---

## Combat Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Melee Attack           | Close-range physical attack                                  | Damage, Attack Speed       |
| Ranged Attack          | Long-range attack using bows or spells                       | Damage, Range, Accuracy    |
| Spellcasting           | Using magical abilities to attack or assist                  | Spell Power, Mana Cost, Cooldown|
| Sneak Attack           | Stealthy attack causing additional damage                    | Damage, Stealth, Critical Hit Rate|
| Defense                | Ability to reduce or block incoming damage                   | Armor, Block Rate          |
| Dodge                  | Quick movement to avoid attacks                              | Dodge Speed, Cooldown      |
| Healing                | Restore health to self or allies                             | Heal Amount, Mana Cost, Cooldown|

---

## Interaction Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Pick Up                | Collecting items from the environment                        | Carry Capacity, Pick Up Speed|
| Lockpicking            | Opening locked doors and chests                              | Lockpicking Skill, Tool Quality|
| Disarm Trap            | Neutralizing traps to prevent damage                         | Trap Disarm Skill, Tool Quality|
| Dialogue               | Engaging in conversations with NPCs                          | Charisma, Persuasion, Deception|
| Trade                  | Buying and selling items with NPCs                           | Negotiation Skill, Wealth  |
| Use                    | Utilizing items or equipment                                 | Efficiency, Durability     |

---

## Environmental Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Weather Effects        | Impact of weather on gameplay                                | Visibility, Movement Penalty|
| Day/Night Cycle        | Changes in game environment based on time                    | Visibility, Enemy Behavior |
| Terrain Interaction    | Movement and actions based on terrain type                   | Speed Penalty, Stamina Drain|
| Hazard Avoidance       | Navigating environmental dangers (e.g., traps, hazards)      | Reflexes, Health Impact    |

---

## Resource Management Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Gather                 | Collecting resources from the environment                    | Gather Speed, Yield        |
| Craft                  | Creating items from raw materials                            | Crafting Speed, Quality    |
| Build                  | Constructing structures                                      | Build Speed, Durability    |
| Repair                 | Fixing damaged items or equipment                            | Repair Speed, Efficiency   |
| Manage Spell Slots     | Allocating limited spellcasting resources                    | Spell Slot Efficiency, Recovery Rate |

---

## Progression Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Level Up               | Increasing character level                                   | Experience Points, Skills  |
| Skill Upgrade          | Improving specific abilities                                 | Skill Points, Proficiency  |
| Unlock                 | Gaining access to new abilities or areas                     | Keys, Progress Milestones  |

---

## Social Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Friendship             | Building relationships with NPCs                             | Affinity, Trust            |
| Rivalry                | Competing with NPCs or other players                         | Influence, Respect         |
| Party Management       | Coordinating actions and strategies with party members       | Leadership, Coordination   |

---

## Miscellaneous Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Stealth                | Moving or acting without being detected                      | Stealth Skill, Visibility  |
| Puzzle Solving         | Completing logic challenges                                  | Intelligence, Insight      |
| Exploration            | Discovering new areas and secrets                            | Map Knowledge, Discovery Rate|

---

## Example of Attributes for a Generic "Character" Object in Baldur's Gate 3:
| Attribute              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Health Points          | Overall health of the character                              |
| Stamina                | Energy available for actions                                 |
| Strength               | Physical power                                               |
| Dexterity              | Agility and reflexes                                         |
| Constitution           | Endurance and vitality                                       |
| Intelligence           | Mental acuity and problem-solving ability                    |
| Wisdom                 | Perception and insight                                       |
| Charisma               | Ability to influence others                                  |
| Armor Class            | Defense against physical attacks                             |
| Mana                   | Energy available for magical abilities                       |
| Experience Points      | Progress towards the next level                              |
| Spellcasting Ability   | Proficiency in using spells                                  |
| Stealth Skill          | Proficiency in moving undetected                             |
| Lockpicking Skill      | Proficiency in unlocking doors and chests                    |
| Persuasion Skill       | Proficiency in convincing others                             |
| Perception Skill       | Ability to notice hidden things                              |

---

This table provides a structured and extensive list of mechanics and attributes specifically tailored to "Baldur's Gate 3," which can be used as a reference or starting point for understanding the game's design elements.

---

# Game Mechanics and Attributes for Hearts of Iron IV

---

## Military Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Division Management    | Organizing and deploying military divisions                  | Division Size, Composition |
| Combat                 | Engaging enemy forces in battle                              | Attack Power, Defense Power, Morale|
| Supply Management      | Ensuring troops are well-supplied                            | Supply Efficiency, Logistics|
| Naval Warfare          | Conducting battles at sea                                    | Fleet Size, Ship Types, Naval Experience|
| Air Warfare            | Conducting air battles and strategic bombing                 | Aircraft Types, Air Superiority|
| Strategic Planning     | Planning and executing military strategies                   | Planning Bonus, Command Power|

---

## Economic Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Resource Management    | Managing and allocating resources                            | Resource Production, Resource Efficiency|
| Industry Management    | Building and managing factories and infrastructure           | Factory Output, Infrastructure Level|
| Trade                  | Trading resources with other countries                       | Trade Efficiency, Trade Relations|
| Research and Development | Advancing technology and equipment                         | Research Speed, Innovation Level|

---

## Political Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Government Management  | Running the government and enacting policies                 | Political Power, Stability|
| Diplomacy              | Managing relations with other countries                      | Diplomatic Influence, Relations|
| Ideology               | Promoting and maintaining a political ideology               | Ideological Support, Party Popularity|
| Factions               | Forming and managing alliances                               | Faction Strength, Cooperation|

---

## Social Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| National Unity         | Maintaining national morale and unity                        | National Unity, War Support|
| Population Management  | Managing civilian and military populations                   | Population Size, Recruitment Rate|
| Resistance             | Handling occupied territories and resistance movements       | Resistance Strength, Compliance|

---

## Resource Management Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Resource Gathering     | Extracting resources from the environment                    | Resource Production Rate, Extraction Efficiency|
| Resource Allocation    | Distributing resources to various sectors                    | Allocation Efficiency, Priority Levels|
| Resource Trading       | Exchanging resources with other nations                      | Trade Agreements, Resource Surplus|

---

## Technology Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Research               | Advancing technologies                                       | Research Speed, Tech Tree Progress|
| Technology Sharing     | Sharing technological advancements with allies               | Cooperation Level, Shared Knowledge|
| Equipment Production   | Manufacturing military equipment                             | Production Speed, Quality|

---

## Progression Mechanics


---

# Game Mechanics and Attributes for Hearts of Iron IV

---

## Military Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Division Management    | Organizing and deploying military divisions                  | Division Size, Composition |
| Combat                 | Engaging enemy forces in battle                              | Attack Power, Defense Power, Morale|
| Supply Management      | Ensuring troops are well-supplied                            | Supply Efficiency, Logistics|
| Naval Warfare          | Conducting battles at sea                                    | Fleet Size, Ship Types, Naval Experience|
| Air Warfare            | Conducting air battles and strategic bombing                 | Aircraft Types, Air Superiority|
| Strategic Planning     | Planning and executing military strategies                   | Planning Bonus, Command Power|

---

## Economic Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Resource Management    | Managing and allocating resources                            | Resource Production, Resource Efficiency|
| Industry Management    | Building and managing factories and infrastructure           | Factory Output, Infrastructure Level|
| Trade                  | Trading resources with other countries                       | Trade Efficiency, Trade Relations|
| Research and Development | Advancing technology and equipment                         | Research Speed, Innovation Level|

---

## Political Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Government Management  | Running the government and enacting policies                 | Political Power, Stability|
| Diplomacy              | Managing relations with other countries                      | Diplomatic Influence, Relations|
| Ideology               | Promoting and maintaining a political ideology               | Ideological Support, Party Popularity|
| Factions               | Forming and managing alliances                               | Faction Strength, Cooperation|

---

## Social Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| National Unity         | Maintaining national morale and unity                        | National Unity, War Support|
| Population Management  | Managing civilian and military populations                   | Population Size, Recruitment Rate|
| Resistance             | Handling occupied territories and resistance movements       | Resistance Strength, Compliance|

---

## Resource Management Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Resource Gathering     | Extracting resources from the environment                    | Resource Production Rate, Extraction Efficiency|
| Resource Allocation    | Distributing resources to various sectors                    | Allocation Efficiency, Priority Levels|
| Resource Trading       | Exchanging resources with other nations                      | Trade Agreements, Resource Surplus|

---

## Technology Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Research               | Advancing technologies                                       | Research Speed, Tech Tree Progress|
| Technology Sharing     | Sharing technological advancements with allies               | Cooperation Level, Shared Knowledge|
| Equipment Production   | Manufacturing military equipment                             | Production Speed, Quality|

---

## Progression Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| National Focus         | Completing national focuses to gain bonuses                  | Focus Progress, National Benefits|
| Achievements           | Completing specific objectives and milestones                | Achievement Progress, Rewards|

---

## Example of Attributes for a Generic "Nation" Object in Hearts of Iron IV:
| Attribute              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Manpower               | Available population for military service                    |
| Political Power        | Ability to influence and enact policies                      |
| Stability              | Overall stability of the nation                              |
| War Support            | Public support for war efforts                               |
| Resources              | Availability of key resources (e.g., oil, steel)             |
| Industrial Capacity    | Ability to produce goods and equipment                       |
| Military Experience    | Experience gained from military operations                   |
| Diplomatic Influence   | Ability to influence other nations                           |
| Research Speed         | Rate at which new technologies are developed                 |
| National Unity         | Degree of unity and morale within the country                |
| Infrastructure Level   | Quality and extent of national infrastructure                |
| Faction Strength       | Power and influence of alliances                             |

---

This table provides a structured and extensive list of mechanics and attributes specifically tailored to "Hearts of Iron IV," which can be used as a reference or starting point for understanding the game's design elements.

---

# Game Mechanics and Attributes for League of Legends

---

## Champion Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Basic Attacks          | Standard attacks performed by champions                      | Attack Damage, Attack Speed|
| Abilities              | Unique skills used by champions                              | Ability Power, Cooldown, Mana Cost|
| Ultimate Abilities     | Powerful skills with longer cooldowns                        | Ultimate Power, Cooldown, Mana Cost|
| Passive Abilities      | Innate skills that provide bonuses                           | Passive Effect, Trigger Conditions|
| Movement               | Champion movement around the map                             | Movement Speed, Dash Distance|

---

## Combat Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Damage                 | Inflicting harm on enemies                                   | Physical Damage, Magic Damage, True Damage|
| Defense                | Reducing or mitigating incoming damage                       | Armor, Magic Resist, Shield Strength|
| Healing                | Restoring health to self or allies                           | Heal Amount, Heal Rate, Cooldown|
| Crowd Control          | Disabling or hindering enemy actions                         | Stun Duration, Slow Percentage, Knockup Duration|
| Summoner Spells        | Special abilities chosen before the match                    | Spell Effect, Cooldown|

---

## Resource Management Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Mana Management        | Using and regenerating mana                                  | Mana Pool, Mana Regen Rate|
| Energy Management      | Using and regenerating energy                                | Energy Pool, Energy Regen Rate|
| Resource Gathering     | Collecting gold and experience from minions and monsters     | Gold Earned, Experience Gained|

---

## Strategic Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Vision Control         | Placing wards to gain vision of the map                      | Ward Duration, Vision Range|
| Map Awareness          | Monitoring and reacting to events on the map                 | Awareness Skill, Reaction Time|
| Objective Control      | Securing objectives like Dragon and Baron                    | Objective Damage, Securing Efficiency|

---

## Team Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Team Coordination      | Working effectively with teammates                           | Communication, Coordination|
| Role Fulfillment       | Performing the duties of assigned roles (e.g., support, carry)| Role-Specific Skills, Adaptability|
| Team Fights            | Coordinated combat involving multiple team members           | Team Fight Effectiveness, Engagement Strategy|

---

## Progression Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Leveling Up            | Gaining levels to unlock and upgrade abilities               | Experience Points, Level   |
| Item Building          | Purchasing items to enhance champion stats                   | Gold Cost, Item Stats      |
| Mastery and Runes      | Customizing champions with masteries and runes               | Mastery Points, Rune Effects|

---

## Environmental Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Jungle Mechanics       | Interacting with neutral monsters in the jungle              | Camp Respawn Time, Jungle Buffs|
| Terrain Interaction    | Navigating and utilizing terrain features                    | Movement Speed on Terrain, Vision Obstruction|

---

## Example of Attributes for a Generic "Champion" Object in League of Legends:
| Attribute              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Health Points          | Overall health of the champion                               |
| Mana                   | Energy available for casting abilities                       |
| Attack Damage          | Physical damage dealt by basic attacks                       |
| Ability Power          | Power of the champion's abilities                            |
| Armor                  | Defense against physical attacks                             |
| Magic Resist           | Defense against magical attacks                              |
| Movement Speed         | Rate of movement around the map                              |
| Attack Speed           | Frequency of basic attacks                                   |
| Cooldown Reduction     | Reduction in ability cooldown times                          |
| Critical Strike Chance | Probability of dealing critical damage                       |
| Health Regeneration    | Rate of health recovery over time                            |
| Mana Regeneration      | Rate of mana recovery over time                              |

---

This table provides a structured and extensive list of mechanics and attributes specifically tailored to "League of Legends," which can be used as a reference or starting point for understanding the game's design elements.


---


# Narratology Mechanics and Attributes for Literature

---

## Structural Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Plot                   | The sequence of events in a story                             | Plot Structure, Climax, Resolution|
| Setting                | The time and place where the story occurs                     | Time Period, Location, Environment|
| Narrative Structure    | The framework of the narrative                                | Linear, Non-linear, Circular|
| Chapters               | Divisions within the narrative                                | Chapter Length, Number of Chapters|

---

## Character Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Protagonist            | The main character of the story                               | Goals, Motivations, Flaws  |
| Antagonist             | The character opposing the protagonist                        | Goals, Motivations, Flaws  |
| Supporting Characters  | Secondary characters who support the main narrative           | Roles, Relationships, Development|
| Character Development  | The evolution of characters throughout the story              | Growth, Change, Arc        |

---

## Thematic Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Themes                 | The central topics or ideas explored in the narrative         | Major Themes, Sub-Themes   |
| Motifs                 | Recurrent elements that reinforce themes                      | Symbolism, Imagery         |
| Tone                   | The attitude or feeling conveyed by the narrative             | Mood, Atmosphere           |
| Moral                  | The lesson or message conveyed by the story                   | Moral Clarity, Complexity  |

---

## Narrative Techniques
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Point of View          | The perspective from which the story is told                  | First Person, Third Person, Omniscient|
| Dialogue               | Conversations between characters                              | Realism, Subtext, Dialect  |
| Foreshadowing          | Hints or clues about what will happen later in the story      | Subtlety, Frequency        |
| Flashbacks             | Scenes set in a time earlier than the main story              | Integration, Relevance     |
| Stream of Consciousness| A method of narration that describes the flow of thoughts     | Coherence, Fluidity        |

---

## Stylistic Mechanics
| Mechanic               | Description                                                  | Attributes                 |
|------------------------|--------------------------------------------------------------|----------------------------|
| Language               | The choice of words and style of expression                   | Diction, Syntax, Figurative Language|
| Narrative Pace         | The speed at which the story progresses                       | Tempo, Rhythm              |
| Symbolism              | The use of symbols to represent ideas or qualities            | Depth, Complexity          |
| Imagery                | Descriptive language that creates vivid sensory experiences   | Visual, Auditory, Tactile  |
| Irony                  | The expression of meaning through opposites                   | Verbal Irony, Situational Irony, Dramatic Irony|

---

## Structural Attributes for a Generic "Literary Work":
| Attribute              | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Title                  | The name of the literary work                                 |
| Author                 | The creator of the literary work                              |
| Genre                  | The category or type of story                                 |
| Length                 | The length of the work, measured in pages or word count       |
| Publication Date       | The date the work was first published                         |
| Audience               | The intended readers of the work                              |
| Historical Context     | The time period and cultural backdrop of the work             |
| Literary Devices       | Techniques used to enhance the narrative                      |
| Reception              | The critical and popular response to the work                 |

---

This table provides a structured and extensive list of mechanics and attributes specifically tailored to narratology in literature, which can be used as a reference or starting point for understanding and analyzing literary works.
