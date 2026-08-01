# AeroRescue — Autonomous Drone Navigation

Project showcase website for an autonomous search-and-rescue drone developed at Ruppin Academic Center. The project combines Deep Reinforcement Learning, YOLOv11, Visual SLAM, NVIDIA Isaac Sim, and Isaac Lab.

## Website sections

- Training Environment
- Spatial Perception and depth-image compression
- Hierarchical flight and navigation control
- Human Detection
- Visual SLAM
- Mission Dashboard
- Research Team

## Technology

- Static HTML, CSS, and JavaScript
- Tailwind CSS via CDN
- Google Fonts: Orbitron and Inter
- H.264 MP4 media optimized for web playback

## Required deployment files

```text
index.html
Assets/
```

Only the optimized `*.web.mp4` videos referenced by `index.html` are required for deployment. Original source videos, working files, and unused design exports should not be included in the final hosted version.

## Run locally

Serve the project directory through a local HTTP server. For example:

```powershell
python -m http.server 4173
```

Then open `http://localhost:4173/`.



## Deployment

The site can be hosted directly with GitHub Pages from the repository root. No build step is required. After deployment, verify navigation, media playback, and external profile links on the final HTTPS URL.
