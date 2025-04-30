# 🕒 TickEngine Core – Narrative Simulation Engine

The TickEngine is the foundational timing mechanism that drives all simulation logic within the Narrative Simulation Engine. It manages the simulation's temporal flow, ensuring consistent updates across all systems using a discrete tick model.

---

## 🎯 Purpose

The TickEngine simulates the passage of time by:
- Advancing ticks in uniform durations
- Triggering time-based logic and downstream systems
- Logging the simulation’s temporal history

---

## ✅ Core Functional Requirements

| Feature           | Description |
|-------------------|-------------|
| `tick_duration`   | Defines the temporal scale of a single tick (e.g., 1 tick = 1000 years) |
| `tick_count`      | Tracks the number of ticks that have occurred |
| `advance_tick()`  | Core function that increments the tick counter and triggers updates |
| `reset_tick()`    | Resets tick state back to zero |
| `tick_log[]`      | Optional log storing a trace of tick events |
| `trigger_events()`| Integrates with the EventQueue to handle simulation events |

---

## 🧱 Class Structure (Pseudocode)

```python
class TickEngine:
    def __init__(self, tick_duration: int):
        self.tick_duration = tick_duration
        self.tick_count = 0
        self.tick_log = []

    def advance_tick(self):
        self.tick_count += 1
        self.tick_log.append(f"Tick {self.tick_count} occurred")
        self.trigger_events()

    def trigger_events(self):
        # interface with EventQueue here
        pass

    def reset_tick(self):
        self.tick_count = 0
        self.tick_log.clear()
```

---

## 🧪 Development Checklist

- [ ] Define simulation `tick_duration` and unit
- [ ] Implement `TickEngine` class with `advance_tick()` and `reset_tick()`
- [ ] Create structured `tick_log[]`
- [ ] Stub `trigger_events()` for future use
- [ ] Add logging integration with TimelineLog
- [ ] Write test loop: simulate 100 ticks and print logs

---

## 🔗 Dependencies

- `EventQueue`: for event resolution and triggering
- `TimelineLog`: for historical recordkeeping
- `GURPSCore`: for character/structure changes per tick

---

*This module is required before initializing any simulation runs and will serve as the temporal driver for all narrative operations.*
