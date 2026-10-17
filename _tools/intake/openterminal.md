# OpenTerminal intake

Source: [README](https://github.com/ErTasselli/OpenTerminal), [tree](https://github.com/ErTasselli/OpenTerminal/tree/main).

## What it is
- A local, terminal-style trading dashboard built on free public market data ([README](https://github.com/ErTasselli/OpenTerminal)).
- Stack: Next.js 15, React 19, TypeScript, Tailwind 4, Zustand, TanStack Query. Backend is Node/Express with SQLite ([README](https://github.com/ErTasselli/OpenTerminal)).
- Charts use lightweight-charts, D3 (treemap) and Recharts ([README](https://github.com/ErTasselli/OpenTerminal)).
- License is MIT ([README](https://github.com/ErTasselli/OpenTerminal)). Reuse is fine with the notice kept.

## How it handles time
Chief's note assumed more than the page shows. Here is what is documented, and what is not.
- The Chart widget has 8 timeframes, from 1D to MAX ([README](https://github.com/ErTasselli/OpenTerminal)). The page does not list all eight.
- Chart types: candlestick, bar, line, area. Indicators: SMA, EMA, VWAP, Bollinger, RSI, MACD ([tree](https://github.com/ErTasselli/OpenTerminal/tree/main)).
- A hover legend shows OHLC, volume and each indicator at the candle under the cursor ([README](https://github.com/ErTasselli/OpenTerminal)).
- Streams: quotes refresh about every second, the heatmap every few seconds. Cache is stale-while-revalidate ([README](https://github.com/ErTasselli/OpenTerminal)).
- Panels: drag-and-drop widgets (react-grid-layout). Layout is saved locally ([README](https://github.com/ErTasselli/OpenTerminal)). Twelve widgets, including a Calendar of dated events with forecast vs actual ([tree](https://github.com/ErTasselli/OpenTerminal/tree/main)).
- Not documented: a zoom control, a range selector, linked time axes between panels. lightweight-charts supports zoom and pan itself, but that is my knowledge, not this repo's claim.
- The time model is one price series per symbol. It is not a multi-scale story timeline.

## A fabula assembler on this model
Provisional name: **TIMELINE DECK**.

Our data today ([fabula.json](../worldview/fabula.json)): 87 nodes (43 events, 14 systems, 9 places, 6 characters, 6 factions, 5 eras, 4 perspectives), 172 links, 12 setting layers. Only era 2 holds most events (33). Era 3 has 3, era 4 has 11, era 5 has 2. Many nodes have no year.

Mapping:
- **Eras as zoom levels.** Top zoom shows five era bands. Click one and the axis zooms to it. Era 1 is dated (Moon Severance, 2099). Era 2 has no calendar spine, so it uses event order (`ord`).
- **Movements (M1-M6) as sub-bands** inside era 2.
- **Character lanes.** One row per character, events as marks on the row.
- **Parallel world lanes.** The 4 perspective nodes and the places become lanes that run beside the main line.
- **Causal edges** (`causal-*` links) draw as arcs between event marks.
- **Panels.** Timeline, node detail with source line, and layer list (S1-S12), all linked to one cursor.

Reuse vs build:
- Reuse from OpenTerminal: the widget-grid idea, the hover legend idea, saved layout, and code under MIT (Workspace, Zustand store pattern).
- Build ourselves: an ordinal-and-dated axis, era zoom, lanes, causal arcs, and the loader for fabula.json.
- Do not reuse the market providers, portfolio, or the AI route.

First slice: one static page from fabula.json. Five era bands, era 2 expanded to its 33 events ordered by `ord`, hover shows desc and source:line. No server, no framework.

## License check
MIT per README. LICENSE file is in the tree ([tree](https://github.com/ErTasselli/OpenTerminal/tree/main)). Keep the copyright notice if code is copied.

## Verdict: BORROW THE IDEAS
The repo is a finance app with one time series per chart. Its stack (Next, Express, SQLite) is heavier than our static-page tools. Take the panel workspace and hover legend. Build the time display ourselves.

## Unverified
- The eight timeframe names, zoom behavior, and whether panels share a time axis. I read only the README and the root tree, not source.
- Screenshots were not viewed.
