---
title: "Running a JSX file in VSCode"
uuid: ec2a8ac2-efbd-43ca-bd4a-e678e8bf29de
created: 2026-03-09
updated: 2026-03-09
trunk: BLACK
messages: 26
chars: 12264
artifacts: 0
generated_files: 0
tools: [view]
source: claude.ai-export-2026-08-15
---

# Running a JSX file in VSCode

> **Conversation Overview**

The person is a VSCode user working on a React JSX file called `leechseed_system_explorer.jsx` and needed help getting it running in the browser as quickly and painlessly as possible. Claude recommended Vite as the preferred method and walked them through the full setup process step by step.

The session involved troubleshooting a series of sequential setup errors: running `npm run dev` from the wrong directory, a missing React/React-DOM installation, a `main.js` vs `main.jsx` naming mismatch, `index.html` referencing the old filename, the root div having `id="app"` instead of `id="root"`, and finally missing `import React from 'react'` in both `main.jsx` and `leechseed_system_explorer.jsx` itself. Each error was resolved one at a time with copy-paste-ready drop-in file contents. The person explicitly preferred full file drop-ins over partial diffs or explanations. The project lives at `C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/` and runs on `http://localhost:5174/` (port 5173 was already in use). The JSX file references a character named Victoria "Tori" Midnight and uses `useState` and `useMemo` from React.

---
## 🧑 Papi  <sub>2026-03-09 05:09:46</sub>

whats the easiest and most painless way to just run this .jsx file? can you do whatever you need to do? I use VScode. if there's a way to to it in there that would be nice. but what would be the preferred method

---

## 🤖 Claude  <sub>2026-03-09 05:10:05</sub>

```
This block is not supported on your current device yet.
```

This is a React component. The fastest, most painless way — especially since you're already in VSCode — is **Vite**. One-time setup, then any future `.jsx` files just drop in and run instantly.

Here's the full setup:

---

## Option 1: Vite (Recommended — VSCode-native, ~2 min setup)

**One-time setup** (do this once, reuse forever):

```bash
# In your terminal (VSCode integrated terminal works fine)
npm create vite@latest leechseed-explorer -- --template react
cd leechseed-explorer
npm install
```

Then:
1. Drop your `leechseed_system_explorer.jsx` into `src/`
2. Open `src/main.jsx` and change the import to point to your file:
   ```jsx
   import App from './leechseed_system_explorer'
   ```
3. Run:
   ```bash
   npm run dev
   ```
4. Open `http://localhost:5173` — live reload included.

That's it. Every time you want to run it, just `npm run dev` from that folder.

---

## Option 2: VSCode Extension (Zero terminal, truly painless)

Install the **[ES6 React/Redux Snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets)** — actually, for *running* JSX directly, the better extension is **[vscode-preview-server](https://marketplace.visualstudio.com/items?itemName=yuichinukiyama.vscode-preview-server)** — but it doesn't handle JSX natively without a bundler anyway. You'd still need Vite or similar under the hood.

---

## The Real Answer

**Vite is the preferred method, full stop.** It's what the React ecosystem uses, it's instant hot reload, zero config, and once the folder exists you never touch setup again — just open the folder in VSCode, hit the terminal, `npm run dev`, and you're live in the browser. Future characters/components just swap into `src/`.

Want me to scaffold the whole Vite project and drop your file in with the correct wiring so it's truly ready to run?

---

## 🧑 Papi  <sub>2026-03-09 05:14:53</sub>

➜ npm run dev
npm error Missing script: "dev"
npm error
npm error To see a list of scripts, run:
npm error   npm run
npm error A complete log of this run can be found in: C:\Users\U01_LEECHSEED\AppData\Local\npm-cache\_logs\2026-03-09T05_14_18_151Z-debug-0.log
(.venv)  ~\Desktop\_setsunadev :: git(main)                                                3.11.8 01:14:18 
➜ npm run dev
npm error Missing script: "dev"
npm error
npm error To see a list of scripts, run:
npm error   npm run
npm error A complete log of this run can be found in: C:\Users\U01_LEECHSEED\AppData\Local\npm-cache\_logs\2026-03-09T05_14_46_828Z-debug-0.log
(.venv)  ~\Desktop\_setsunadev :: git(main)                                                3.11.8 01:14:46 
➜

---

## 🤖 Claude  <sub>2026-03-09 05:14:57</sub>

You ran `npm run dev` in the wrong folder — you're still in `_setsunadev` instead of the new Vite project folder.

Run this:

```bash
cd leechseed-explorer
npm run dev
```

If the `leechseed-explorer` folder doesn't exist there, it may have been created somewhere else. Check with:

```bash
ls
```

or look in your home directory / wherever your terminal was pointed when you ran `npm create vite@latest`. Find the folder, `cd` into it, then `npm run dev`.

---

## 🧑 Papi  <sub>2026-03-09 05:15:30</sub>

```
[plugin:vite:import-analysis] Failed to resolve import "react" from "src/leechseed_system_explorer.jsx". Does the file exist?
```


```
C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/src/leechseed_system_explorer.jsx:1:34
```


```
1  |  import { useState, useMemo } from "react";
   |                                     ^
2  |  const VICTORIA = {
3  |    meta: { character_id: "victoria_midnight", character_name: 'Victoria "Tori" Midnight', ip: "overexitout", tier: 3, ...
```


```
    at TransformPluginContext._formatLog (file:///C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/node_modules/vite/dist/node/chunks/config.js:28999:43)
    at TransformPluginContext.error (file:///C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/node_modules/vite/dist/node/chunks/config.js:28996:14)
    at normalizeUrl (file:///C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/node_modules/vite/dist/node/chunks/config.js:27119:18)
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async file:///C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/node_modules/vite/dist/node/chunks/config.js:27177:32
    at async Promise.all (index 0)
    at async TransformPluginContext.transform (file:///C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/node_modules/vite/dist/node/chunks/config.js:27145:4)
    at async EnvironmentPluginContainer.transform (file:///C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/node_modules/vite/dist/node/chunks/config.js:28797:14)
    at async loadAndTransform (file:///C:/Users/U01_LEECHSEED/Desktop/_setsunadev/leechseed-explorer/node_modules/vite/dist/node/chunks/config.js:22670:26)
```

Click outside, press Esc key, or fix the code to dismiss. You can also disable this overlay by setting `server.hmr.overlay` to `false` in `vite.config.js`.

---

## 🤖 Claude  <sub>2026-03-09 05:15:32</sub>

You forgot to install React. Just run this in the `leechseed-explorer` folder:

```bash
npm install react react-dom
```

Then `npm run dev` again. That's it.

---

## 🧑 Papi  <sub>2026-03-09 05:18:32</sub>

ok its jost showing a blank white page

---

## 🤖 Claude  <sub>2026-03-09 05:18:35</sub>

Your file uses `export default` but `main.jsx` probably still has the old Vite template import. Open `src/main.jsx` and make sure it looks exactly like this:

```jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import LeechseedExplorer from './leechseed_system_explorer'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <LeechseedExplorer />
  </StrictMode>
)
```

Save it, the page should reload and show the app.

---

## 🧑 Papi  <sub>2026-03-09 05:18:59</sub>

ok give me a copy paste drop in of the full complete altered main.jsx

---

## 🤖 Claude  <sub>2026-03-09 05:19:01</sub>

```jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import LeechseedExplorer from './leechseed_system_explorer'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <LeechseedExplorer />
  </StrictMode>
)
```

That's the entire file. Copy, paste, replace, save.

---

## 🤖 Claude  <sub>2026-03-09 05:20:12</sub>

The file is named `main.js` not `main.jsx`. In VSCode's Explorer panel, just rename it:

**`main.js` → `main.jsx`**

Then refresh the browser. Done.

---

## 🧑 Papi  <sub>2026-03-09 05:21:05</sub>

Port 5173 is in use, trying another one...
  VITE v7.3.1  ready in 264 ms
  ➜  Local:   http://localhost:5174/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
1:20:53 AM [vite] (client) Pre-transform error: Failed to load url /src/main.js (resolved id: /src/main.js). Does the file exist?
1:20:53 AM [vite] (client) Pre-transform error: Failed to load url /src/main.js (resolved id: /src/main.js). Does the file exist? (x2)

---

## 🤖 Claude  <sub>2026-03-09 05:21:09</sub>

Vite is still looking for `main.js` because `index.html` references it. Open `index.html` in the project root and change this line:

```html
<script type="module" src="/src/main.js"></script>
```

to:

```html
<script type="module" src="/src/main.jsx"></script>
```

Save, refresh. That's the last one.

---

## 🧑 Papi  <sub>2026-03-09 05:23:16</sub>

its just the blank white page now. did i downlod the proper version of vite

---

## 🤖 Claude  <sub>2026-03-09 05:23:19</sub>

The setup is fine, the page is just blank because there's likely a runtime error. Open your browser's dev console (**F12 → Console tab**) and paste whatever red errors you see there.

---

## 🧑 Papi  <sub>2026-03-09 05:23:36</sub>

Uncaught Error: Target container is not a DOM element.
    createRoot React
    <anonymous> main.jsx:4

---

## 🤖 Claude  <sub>2026-03-09 05:23:39</sub>

Open `index.html` in the project root and make sure there's a `<div id="root">` inside the `<body>`. It should look like this:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Leechseed Explorer</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

Paste that as your entire `index.html`, save, refresh.

---

## 🧑 Papi  <sub>2026-03-09 05:24:17</sub>

just give me the corrected drop in

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>leechseed-explorer</title>
  </head>
  <body>
    <div id="app"></div>
	<script type="module" src="/src/main.jsx"></script>
  </body>
</html>

---

## 🤖 Claude  <sub>2026-03-09 05:24:20</sub>

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>leechseed-explorer</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

The only change was `id="app"` → `id="root"`.

---

## 🧑 Papi  <sub>2026-03-09 05:25:04</sub>

Uncaught ReferenceError: React is not defined
    <anonymous> main.jsx:6

---

## 🤖 Claude  <sub>2026-03-09 05:25:06</sub>

Add the React import to the top of `main.jsx`. Full file:

```jsx
import React from 'react'
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import LeechseedExplorer from './leechseed_system_explorer'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <LeechseedExplorer />
  </StrictMode>
)
```

---

## 🧑 Papi  <sub>2026-03-09 05:25:19</sub>

give me the full main.jsx file fixed

---

## 🤖 Claude  <sub>2026-03-09 05:25:22</sub>

```jsx
import React from 'react'
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import LeechseedExplorer from './leechseed_system_explorer'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <LeechseedExplorer />
  </StrictMode>
)
```

---

## 🧑 Papi  <sub>2026-03-09 05:26:24</sub>

[vite] connected from window b888585c-1c57-40cc-bcd0-0948cce15cce:67:11
[vite] new window visibility hidden b888585c-1c57-40cc-bcd0-0948cce15cce:63:12
[vite] ping successful b888585c-1c57-40cc-bcd0-0948cce15cce:69:12
[vite] connected from window 0337cbb5-c860-4799-849e-6a3c0e02f1b8:67:11
[vite] new window visibility hidden 0337cbb5-c860-4799-849e-6a3c0e02f1b8:63:12
[vite] new window visibility visible 0337cbb5-c860-4799-849e-6a3c0e02f1b8:63:12
[vite] ping successful 0337cbb5-c860-4799-849e-6a3c0e02f1b8:69:12
[vite] connecting... client:733:9
Download the React DevTools for a better development experience: https://react.dev/link/react-devtools react-dom-client.development.js:28004:17
Uncaught ReferenceError: React is not defined
    LeechseedExplorer leechseed_system_explorer.jsx:513
    React 10
    performWorkUntilDeadline scheduler.development.js:45
leechseed_system_explorer.jsx:513:3
An error occurred in the <LeechseedExplorer> component. Consider adding an error boundary to your tree to customize error handling behavior. Visit https://react.dev/link/error-boundaries to learn more about error boundaries.

---

## 🤖 Claude  <sub>2026-03-09 05:26:27</sub>

The JSX file itself also needs the React import. Add this as the very first line of `leechseed_system_explorer.jsx`:

```jsx
import React from 'react'
```

So the top of that file becomes:

```jsx
import React from 'react'
import { useState, useMemo } from "react";
```

Save, refresh.