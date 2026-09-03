---
type: ssot_05_operations
category: legacy_styleguide_2024
version: 1.0.0
last_updated: 2026-09-03
status: PROMOTED 2026-09-03 from _broodengine (archived) — historical convention doc, superseded in practice by the SSOT creation guide and the Obsidian YAML standard; kept as the ancestor record
purpose: "The May 2024 markdown style guide and hierarchical naming conventions that the SSOT conventions grew out of — frontmatter, delimiters, LLM-ingestion formatting, Engine.Subsystem naming."
dependencies: ["📐ssot_SSOT_CREATION", "📐 ssot_writing_guide"]
trunk: BLACK
provenance:
  origin: "_ARCHIVE/_broodengine/styleguide.md (8.6 KB, 2024-05-25) + higherarchical_naming_conventions.md (3.4 KB, 2024-05-24)"
  note: "Two files concatenated verbatim below their own headings. AI-assisted originals. Nothing edited."
---

# 📐 SSOT: LEGACY STYLEGUIDE (2024) — the ancestor of the house conventions

Read the current rules in `📐ssot_SSOT_CREATION.md` and `📐 ssot_writing_guide.md`. This document is the record of where they came from.

---

# PART A · Markdown style guide (2024-05-25)

### Markdown Style Guide for Hierarchical Naming, Frontmatter, and LLM Ingestion

This style guide will help you create and manage Markdown files that are organized, searchable, and ready for ingestion into a Large Language Model (LLM). The guide covers hierarchical naming conventions, the use of frontmatter, and best practices for LLM ingestion.

---

#### Table of Contents
1. [Hierarchical Naming Conventions](#hierarchical-naming-conventions)
2. [Frontmatter Metadata](#frontmatter-metadata)
3. [Consistent Structure](#consistent-structure)
4. [Explicit Section Delimiters](#explicit-section-delimiters)
5. [Inline Annotations and Comments](#inline-annotations-and-comments)
6. [Standardized Terminology](#standardized-terminology)
7. [Data Formatting for LLM Ingestion](#data-formatting-for-llm-ingestion)
8. [Contextual Embeddings](#contextual-embeddings)
9. [Content Segmentation](#content-segmentation)
10. [Version Control and Updates](#version-control-and-updates)
11. [Bringing It All Together](#bringing-it-all-together)

---

### Hierarchical Naming Conventions

Use a hierarchical naming convention to reflect the nested structure of your systems. This helps maintain clarity and organization.

**Example:**
```markdown
/Engine
    /Physics
        collision.mdboil
        rigidbody.md
    /Audio
        sound.md
        music.md
    /Lighting
        shadows.md
        globalillumination.md
```

### Frontmatter Metadata

Include frontmatter at the beginning of each Markdown file to store metadata. This metadata can be used for indexing and searching.

**Example:**
```markdown
---
title: "Collision Detection"
tags: ["physics", "collision"]
system: "Physics"
subsystem: "Collision"
version: "1.2"
summary: "Overview of the collision detection system in the physics engine."
date: "2024-05-24"
---
```

### Consistent Structure

Ensure that all Markdown files follow a consistent structure. This includes having a standard way to format headers, lists, code blocks, and other elements.

**Example:**
```markdown
# Collision Detection

## Introduction

Collision detection is a crucial component of the physics engine...

## Algorithms

### Bounding Volume Hierarchy (BVH)

BVH is a common technique for accelerating collision detection...

## Optimization

Various optimization techniques can be applied to improve performance...
```

### Explicit Section Delimiters

Use explicit delimiters for sections within a document. This can be done using Markdown headers or custom markers.

**Example:**
```markdown
# Collision Detection

<!-- Section: Introduction -->
## Introduction

Collision detection is a crucial component of the physics engine...

<!-- Section: Algorithms -->
## Algorithms

### Bounding Volume Hierarchy (BVH)

BVH is a common technique for accelerating collision detection...

<!-- Section: Optimization -->
## Optimization

Various optimization techniques can be applied to improve performance...
```

### Inline Annotations and Comments

Add inline annotations and comments to provide additional context or explanations.

**Example:**
```markdown
# Collision Detection

<!-- 
This section covers the basics of collision detection, including algorithms and optimization techniques.
The content is divided into the following subsections:
1. Introduction
2. Algorithms
3. Optimization
-->

## Introduction

Collision detection is a crucial component of the physics engine...

## Algorithms

### Bounding Volume Hierarchy (BVH)

BVH is a common technique for accelerating collision detection...

## Optimization

Various optimization techniques can be applied to improve performance...
```

### Standardized Terminology

Develop a glossary of standardized terms and use them consistently across all documents.

**Example:**
```markdown
---
title: "Glossary"
tags: ["reference", "terminology"]
---

# Glossary

## Collision Detection

The process of detecting when two or more physical objects in a game environment intersect or come into contact...

## Bounding Volume Hierarchy (BVH)

A data structure used to accelerate collision detection by organizing objects into a tree of bounding volumes...
```

### Data Formatting for LLM Ingestion

Prepare your Markdown content for ingestion by ensuring it is well-structured and clean. Use consistent formatting and tokenization.

**Example:**
```markdown
---
title: "Collision Detection"
tags: ["physics", "collision"]
system: "Physics"
subsystem: "Collision"
version: "1.2"
summary: "Overview of the collision detection system in the physics engine."
---

# Collision Detection

## Introduction

Collision detection is a crucial component of the physics engine...

## Algorithms

### Bounding Volume Hierarchy (BVH)

BVH is a common technique for accelerating collision detection...

## Optimization

Various optimization techniques can be applied to improve performance...
```

### Contextual Embeddings

Use embeddings to capture the meaning and relationships between different parts of the text.

**Example:**
```markdown
---
title: "Collision Detection"
tags: ["physics", "collision"]
system: "Physics"
subsystem: "Collision"
version: "1.2"
summary: "Overview of the collision detection system in the physics engine."
embeddings: ["collision detection", "BVH", "optimization"]
---

# Collision Detection

## Introduction

Collision detection is a crucial component of the physics engine...

## Algorithms

### Bounding Volume Hierarchy (BVH)

BVH is a common technique for accelerating collision detection...

## Optimization

Various optimization techniques can be applied to improve performance...
```

### Content Segmentation

Segment large documents into smaller, manageable chunks. This helps the LLM process and understand each part without being overwhelmed.

**Example:**
```markdown
# Collision Detection

## Part 1: Introduction

Collision detection is a crucial component of the physics engine...

## Part 2: Algorithms

### Bounding Volume Hierarchy (BVH)

BVH is a common technique for accelerating collision detection...

## Part 3: Optimization

Various optimization techniques can be applied to improve performance...
```

### Version Control and Updates

Keep track of versions and updates to your documents using version control systems like Git. Maintain a changelog for reference.

**Example:**
```markdown
---
title: "Collision Detection"
tags: ["physics", "collision"]
system: "Physics"
subsystem: "Collision"
version: "1.2"
summary: "Overview of the collision detection system in the physics engine."
date: "2024-05-24"
---

# Collision Detection

## Change Log

- **Version 1.2**: Updated optimization techniques.
- **Version 1.1**: Added BVH algorithms section.
- **Version 1.0**: Initial release.
```

### Bringing It All Together

By combining hierarchical naming conventions, frontmatter metadata, consistent structure, explicit section delimiters, inline annotations, standardized terminology, proper data formatting, contextual embeddings, content segmentation, and version control, you can create a robust and well-organized documentation system that is ready for LLM ingestion.

**Comprehensive Example:**

```markdown
---
title: "Collision Detection"
tags: ["physics", "collision"]
system: "Physics"
subsystem: "Collision"
version: "1.2"
summary: "Overview of the collision detection system in the physics engine."
date: "2024-05-24"
embeddings: ["collision detection", "BVH", "optimization"]
---

# Collision Detection

<!-- 
This document covers the basics of collision detection, including algorithms and optimization techniques.
The content is divided into the following sections:
1. Introduction
2. Algorithms
3. Optimization
-->

## Introduction

Collision detection is a crucial component of the physics engine...

## Algorithms

### Bounding Volume Hierarchy (BVH)

BVH is a common technique for accelerating collision detection...

## Optimization

Various optimization techniques can be applied to improve performance...

## Change Log

- **Version 1.2**: Updated optimization techniques.
- **Version 1.1**: Added BVH algorithms section.
- **Version 1.0**: Initial release.
```

By following this style guide, you can ensure that your Markdown documentation is well-organized, easily searchable, and ready for effective ingestion into an LLM.

---

# PART B · Hierarchical naming conventions (2024-05-24)





Avoiding confusion in naming systems that have nested subsystems, especially in complex projects like a game engine, requires a clear and consistent naming convention. Here are some strategies to help you maintain clarity:

### 1. **Hierarchical Naming Conventions**
Use a hierarchical naming convention to reflect the nested structure of your systems. This involves prefixing subsystem names with their parent system names.

- **Example:**
  - `Engine.Physics.Collision`
  - `Engine.Physics.RigidBody`
  - `Engine.Audio.Sound`
  - `Engine.Audio.Music`
  - `Engine.Lighting.Shadows`
  - `Engine.Lighting.GlobalIllumination`

### 2. **Namespace Organization**
Organize your code into namespaces or modules that correspond to the different systems and subsystems. This approach helps keep related components together and avoids name collisions.

- **Example:**
  - `namespace Engine.Physics { class Collision { ... } }`
  - `namespace Engine.Audio { class Sound { ... } }`
  - `namespace Engine.Lighting { class Shadows { ... } }`

### 3. **Descriptive Names**
Use descriptive names that clearly indicate the purpose and scope of each system or subsystem. Avoid abbreviations unless they are universally understood within your team or project.

- **Example:**
  - `PhysicsEngine.CollisionDetection`
  - `SoundEngine.AudioPlayer`
  - `LightingSystem.ShadowMapping`

### 4. **Documentation**
Maintain thorough documentation that describes the structure and relationships between different systems. This can include diagrams, README files, and inline comments in the code.

- **Example:**
  - A README.md file at the root of each system’s directory explaining its purpose and components.
  - Inline comments that describe the role of each class and method.

### 5. **Consistent Suffixes and Prefixes**
Use consistent suffixes or prefixes to denote different types of systems and subsystems. This helps in quickly identifying the nature of a component.

- **Example:**
  - `PhysicsSystem_`
  - `SoundSystem_`
  - `LightingSystem_`
  - `PhysicsSubsystem_`
  - `AudioSubsystem_`

### 6. **Code Organization**
Organize your directory structure to mirror the hierarchical nature of your systems. This helps in keeping the codebase organized and makes it easier to locate files.

- **Example:**
  ```
  /Engine
      /Physics
          Collision.cs
          RigidBody.cs
      /Audio
          Sound.cs
          Music.cs
      /Lighting
          Shadows.cs
          GlobalIllumination.cs
  ```

### 7. **Use of Interfaces and Base Classes**
Define interfaces or base classes for common functionality shared among systems. This helps in maintaining a consistent structure and makes it clear what the core responsibilities of each system are.

- **Example:**
  ```csharp
  public interface IEngineSystem
  {
      void Initialize();
      void Update();
  }

  public class PhysicsSystem : IEngineSystem
  {
      public void Initialize() { ... }
      public void Update() { ... }
  }

  public class AudioSystem : IEngineSystem
  {
      public void Initialize() { ... }
      public void Update() { ... }
  }
  ```

By applying these strategies, you can create a clear and manageable naming system that helps avoid confusion in complex projects with nested systems.