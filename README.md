# ISAAC SAR — Search & Rescue Autonomous Drone
### NVIDIA Isaac Sim Research Project · AR Showcase Website

A professional, single-file project showcase website with AR visualization powered by **MindAR** + **A-Frame**, styled with **Tailwind CSS** and a Cyber-Industrial / Glassmorphism aesthetic.

---

## 📁 Required File Structure

```
drone-ar-web/
├── index.html          ← main site
├── white_drone.glb     ← AR drone model (~5 MB) — used in the live scene
├── targets.mind        ← compiled AR target from your poster
├── drone-ar.glb        ← optional Draco fallback (~10 MB)
└── Flying drone_.glb   ← original source model (~30 MB, not used in AR)
```

---

## 🚀 Setup Instructions

### 1. Drone model (`white_drone.glb`)

The AR scene loads **`white_drone.glb`** (~5 MB, no Draco). It is **embedded directly in the scene HTML** inside `buildArSceneHtml()` — do not inject `gltf-model` via JavaScript after load; A-Frame will not fire `model-loaded` reliably that way.

```html
<a-entity id="drone-root"
  gltf-model="url(white_drone.glb)"
  scale="0.06 0.06 0.06"
  position="0 0.15 0.12"
  ...>
```

- **Scale `0.06`** — model is ~2 units wide; at 0.06 it reads ~12 cm on the poster
- **No Draco** on `<a-scene>` — not needed for `white_drone.glb`
- **Brighter lights** in the scene so the white model is visible
- Debug shows **`loaded ✓`** only when the model actually renders (not just when the file fetch returns OK)

To change size, edit the `scale` attribute on `#drone-root` in `buildArSceneHtml()` inside `index.html`. If the drone is invisible after `loaded ✓`, try `0.15`.

### How `targets.mind` + `white_drone.glb` work together

1. **`targets.mind`** — image fingerprint of your **poster** (compile from the exact PNG/JPG you scan). Uses `targetIndex: 0`.
2. **`white_drone.glb`** — 3D drone, parented to the same tracked anchor in A-Frame.

When the camera sees a poster that matches `targets.mind`, MindAR shows everything on the `mindar-image-target` entity — green rings **and** the drone.

If the badge stays on **TARGET: SCANNING**, the poster in view does **not** match `targets.mind` → recompile from your Canva export (see step 2 below).

### 2. Generate / replace `targets.mind`

1. Go to **https://hiukim.github.io/mind-ar-js-doc/tools/compile**
2. Upload the poster/image you want the drone to appear on
3. Download the compiled `targets.mind` file
4. Place `targets.mind` in the root folder alongside `index.html`

### 3. Add Your YouTube Video IDs

In `index.html`, find the four `openVideo(...)` calls and replace the placeholder IDs:

```html
onclick="openVideo('YOUR_YOUTUBE_ID_1', 'Full Mission Simulation')"
```

YouTube video ID is the part after `?v=` in the URL, e.g. `dQw4w9WgXcQ`.

### 4. Customize the Team Section

Find the team cards near the bottom of `index.html` and replace placeholder names/roles with your actual team.

---

## 🌐 Deploy to GitHub Pages

```bash
# 1. Initialize git (if not already)
git init
git add .
git commit -m "Initial deploy: ISAAC SAR showcase"

# 2. Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/drone-ar-web.git
git branch -M main
git push -u origin main

# 3. Enable GitHub Pages
# Go to: Repository → Settings → Pages → Source: main / root → Save
# Your site will be live at: https://YOUR_USERNAME.github.io/drone-ar-web/
```

> ⚠️ **Important:** GitHub Pages serves over HTTPS. MindAR requires camera access which only works on HTTPS — so GitHub Pages is perfect for this.

Ensure **`white_drone.glb`** and **`targets.mind`** are committed and pushed — both are required for AR to work in production.

---

## 📱 AR Experience (Mobile)

### Local testing via HTTPS (localtunnel)

AR requires HTTPS for camera access. To test on your phone:

```powershell
# Terminal 1 — serve the project root (must stay running)
cd d:\isaac\drone-ar-web
npx serve .

# Terminal 2 — expose port 3000 over HTTPS
npx localtunnel --port 3000
```

Open the **https://\*.loca.lt** URL on your phone. On first visit, localtunnel shows a warning page — tap through it (enter your public IP if prompted). Then:

1. Hard-refresh the page (pull down or clear cache)
2. Tap **Launch AR Experience**
3. Allow camera when prompted
4. Point at the **full poster** that matches `targets.mind`

An on-screen **debug panel** (bottom-left) shows live status. Wait for **`white_drone.glb: loaded ✓`** (not just `OK`). **Tracking: TARGET FOUND** confirms the poster match.

> Console errors from `contentscript.js` (MetaMask or other extensions) are **not** from this site — ignore them.

### Production (GitHub Pages)

1. Open the site on your **phone browser** (Chrome on Android / Safari on iOS)
2. Click **"Launch AR Experience"**
3. Grant camera permission when prompted
4. Point the camera at your AR target poster — the drone will appear!

---

## 🎨 Customization Quick Reference

| What to change | Where in index.html |
|---|---|
| Project title / description | Hero section `<h1>` and `<p>` |
| Stats (94.7%, 4×, etc.) | Hero card mini-stats + Overview big-nums + Analytics bars |
| Team members | `#team` section cards |
| Color accent (default: `#76b900`) | CSS custom properties at top of `<style>` |
| Drone model scale in AR | `scale` on `#drone-root` in `buildArSceneHtml()` |
| AR lighting intensity | `intensity` on `<a-light>` elements |

---

## 🛠 Tech Stack

- **Tailwind CSS** (CDN) — utility-first styling
- **MindAR 1.2.5** — image tracking AR (requires A-Frame loaded first)
- **A-Frame 1.4.0** — 3D/WebXR scene
- **Google Fonts** — Orbitron + Inter
- Pure HTML/CSS/JS — zero build step, zero dependencies to install
