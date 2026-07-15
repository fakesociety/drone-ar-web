# Drone RL — Autonomous Drone Navigation

Project showcase website for an autonomous search-and-rescue drone developed at Ruppin Academic Center. The project combines Deep Reinforcement Learning, YOLOv11, Visual SLAM, NVIDIA Isaac Sim, and Isaac Lab.

## Website sections

- Research Team
- Training Environment
- Spatial Perception and depth-image compression
- Hierarchical flight and navigation control
- Human Detection
- Visual SLAM
- Mission Dashboard
- Mobile AR experience

## Technology

- Static HTML, CSS, and JavaScript
- Tailwind CSS via CDN
- A-Frame 1.4.0 and MindAR 1.2.5, loaded only when AR is launched
- Google Fonts: Orbitron and Inter
- H.264 MP4 media optimized for web playback

## Required deployment files

```text
index.html
targets.mind
white_drone.glb
Assets/
```

Only the optimized `*.web.mp4` videos referenced by `index.html` are required for deployment. Original source videos, working files, and unused design exports should not be included in the final hosted version.

## Run locally

Serve the project directory through a local HTTP server. For example:

```powershell
python -m http.server 4173
```

Then open `http://localhost:4173/`.

## AR requirements

The AR experience requires:

- A secure context (`HTTPS` in production; `localhost` is accepted for development)
- Camera permission
- Internet access when AR is opened, because A-Frame and MindAR are loaded from CDNs
- `targets.mind` and `white_drone.glb` in the project root

The AR libraries and drone model are loaded on demand after the user selects **Launch AR**, keeping the initial page load lightweight.

## Deployment

The site can be hosted directly with GitHub Pages from the repository root. No build step is required. After deployment, verify navigation, media playback, external profile links, and the AR experience on the final HTTPS URL.
