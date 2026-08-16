---
title: "Extract YouTube playlist links to table"
uuid: 3f9d2c13-91de-446f-942d-09147a491110
created: 2026-02-13
updated: 2026-02-17
trunk: BLACK
messages: 8
chars: 4279
artifacts: 0
generated_files: 1
tools: [Claude in Chrome:computer, Claude in Chrome:javascript_tool, Claude in Chrome:navigate, Claude in Chrome:read_page, Claude in Chrome:tabs_context_mcp, create_file, present_files, str_replace]
source: claude.ai-export-2026-08-15
---

# Extract YouTube playlist links to table

> **Conversation Overview**

The user requested help extracting all YouTube video links from a specific TTRPG research playlist by Ragoons GG and organizing them into a table format. The playlist contained 104 videos focused on tabletop role-playing game design, theory, and gamemastering techniques. Claude successfully connected to the user's Chrome browser through the Claude in Chrome extension and navigated to the YouTube playlist. Using JavaScript automation, Claude scrolled through the entire playlist to load all videos and extracted the complete list of video titles and URLs. The extracted data was organized into a comprehensive markdown table with video numbers, titles, and YouTube links. Upon the user's request, Claude enhanced the table by adding a "Done" column with empty checkboxes (☐) that the user can mark as complete (☑) to track their progress through the playlist. The final deliverable was a well-formatted markdown file containing all 104 videos with tracking capabilities for the user's viewing progress.

**Tool Knowledge**

For YouTube playlist extraction using Claude in Chrome, the approach required first scrolling to load all playlist content since YouTube uses lazy loading. The JavaScript solution `window.scrollTo(0, document.documentElement.scrollHeight)` with a 1-second delay between scrolls successfully loaded all 104 videos. The selector `ytd-playlist-video-renderer a#video-title` effectively captured all video elements, and extracting the `title` attribute and `href` attribute provided clean video titles and URLs. When constructing YouTube URLs, using `'https://www.youtube.com' + el.getAttribute('href').split('&')[0]` removed unnecessary URL parameters while preserving the core video link. The async function pattern with `await new Promise(resolve => setTimeout(resolve, 1000))` was essential for allowing YouTube's dynamic content to fully load between scroll actions. This method proved more reliable than attempting to extract video data from the initial page load, which only showed the first few videos in the playlist.

**Files produced**

- [ttrpg_research_playlist.md](../files/2026-02-13_ttrpg-research-playlistmd.md)

---
## 🧑 Papi  <sub>2026-02-13 03:14:08</sub>

can you extract all the youtube links in this playlist and put it in a table

https://youtube.com/playlist?list=PLVZmmO-QfA5jd0wmPxjT_N7Uidhqackhj&si=Iqif1SDJClQrFKno

---

## 🤖 Claude  <sub>2026-02-13 03:14:31</sub>

I'll help you extract all the YouTube links from that playlist and put them in a table.
```
This block is not supported on your current device yet.
```

I don't currently have a Chrome browser connected to extract the playlist contents directly. However, I can help you with a couple of alternative approaches:

1. **If you can connect Chrome**: You can install the "Claude in Chrome" extension and connect it, then I can browse the playlist and extract all the video links for you.

2. **Manual extraction**: You could open the playlist, scroll to load all videos, then copy the page source or share a screenshot, and I can help format it into a table.

3. **Using YouTube Data API**: If you're comfortable with a technical approach, I could write a Python script that uses the YouTube Data API to fetch all videos from the playlist programmatically.

Which approach would work best for you?

---

## 🧑 Papi  <sub>2026-02-13 03:15:06</sub>

1.

---

## 🤖 Claude  <sub>2026-02-13 03:15:11</sub>

Great! Let me help you get set up with Claude in Chrome.

**To connect Chrome:**

1. **Install the extension** (if you haven't already):
   - Go to the Chrome Web Store and search for "Claude in Chrome" or visit the Anthropic website
   - Click "Add to Chrome" to install the extension

2. **Connect to this conversation**:
   - Once installed, click the Claude extension icon in your Chrome toolbar
   - You should see an option to connect to this conversation
   - Click "Connect" to link your browser

Once you've connected Chrome, let me know and I'll be able to browse that YouTube playlist and extract all the video links into a table for you!

---

## 🧑 Papi  <sub>2026-02-13 03:18:56</sub>

uh well idk if its connected but it says it is

---

## 🤖 Claude  <sub>2026-02-13 03:22:00</sub>

Perfect! Let me check the connection and then navigate to that YouTube playlist.
```
This block is not supported on your current device yet.
```

Great! Chrome is connected. Now let me navigate to that YouTube playlist.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good! The playlist loaded. It shows ".ttrpg.research" by Ragoons GG with 104 videos. I can see the first few videos are visible. Now I need to scroll down to load all the videos in the playlist so I can extract all the links. Let me scroll down to load more videos.
```
This block is not supported on your current device yet.
```

Let me use JavaScript to extract all the video links from the playlist more efficiently:
```
This block is not supported on your current device yet.
```

Let me fix that JavaScript:
```
This block is not supported on your current device yet.
```

Great! I got the first 100 videos. Let me get the remaining 4 videos:
```
This block is not supported on your current device yet.
```

Let me get the complete list without truncation:
```
This block is not supported on your current device yet.
```

Perfect! Now I have all 104 videos. Let me create a table with all the YouTube links:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Perfect! I've extracted all 104 videos from the ".ttrpg.research" playlist and created a table with the video titles and YouTube URLs. The file is ready for download!

---

## 🧑 Papi  <sub>2026-02-13 03:22:25</sub>

can you add an extra column with a checkbox in it to mark what ive done as i go

---

## 🤖 Claude  <sub>2026-02-13 03:25:19</sub>

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Let me do this more efficiently by recreating the file with checkboxes:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Perfect! I've added a "Done" column with checkboxes (☐) for all 104 videos. You can mark them as complete by changing ☐ to ☑ as you watch each video!