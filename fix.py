import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content = """            <div class="grid sm:grid-cols-2 gap-6">

                <!-- Room 1 -->
                <div class="vid-card glass fade-in" data-d="1">
                    <div class="vid-thumb" style="background:#0D1726;">
                        <video src="Video/room1.mp4" autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>
                        <div style="position:absolute;top:10px;left:10px;" class="hud-badge">ROOM 1</div>
                    </div>
                    <div class="p-4">
                        <h4 class="font-orbitron text-[0.82rem] font-bold mb-2" style="color: rgba(13, 23, 38, 1);">Room 1</h4>
                        <p style="font-size:0.76rem;color: rgba(13, 23, 38, 0.7);line-height:1.6;">3D Environment view of Room 1 playing automatically in a loop.</p>
                    </div>
                </div>

                <!-- Room 2 -->
                <div class="vid-card glass fade-in" data-d="2">
                    <div class="vid-thumb" style="background:#0D1726;">
                        <video src="Video/room2.mp4" autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>
                        <div style="position:absolute;top:10px;left:10px;" class="hud-badge">ROOM 2</div>
                    </div>
                    <div class="p-4">
                        <h4 class="font-orbitron text-[0.82rem] font-bold mb-2" style="color: rgba(13, 23, 38, 1);">Room 2</h4>
                        <p style="font-size:0.76rem;color: rgba(13, 23, 38, 0.7);line-height:1.6;">3D Environment view of Room 2 playing automatically in a loop.</p>
                    </div>
                </div>

                <!-- Room 3 -->
                <div class="vid-card glass fade-in" data-d="3">
                    <div class="vid-thumb" style="background:#0D1726;">
                        <video src="Video/room3.mp4" autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>
                        <div style="position:absolute;top:10px;left:10px;" class="hud-badge">ROOM 3</div>
                    </div>
                    <div class="p-4">
                        <h4 class="font-orbitron text-[0.82rem] font-bold mb-2" style="color: rgba(13, 23, 38, 1);">Room 3</h4>
                        <p style="font-size:0.76rem;color: rgba(13, 23, 38, 0.7);line-height:1.6;">3D Environment view of Room 3 playing automatically in a loop.</p>
                    </div>
                </div>

                <!-- Room 4 -->
                <div class="vid-card glass fade-in" data-d="4">
                    <div class="vid-thumb" style="background:#0D1726;">
                        <video src="Video/room4.mp4" autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;"></video>
                        <div style="position:absolute;top:10px;left:10px;" class="hud-badge">ROOM 4</div>
                    </div>
                    <div class="p-4">
                        <h4 class="font-orbitron text-[0.82rem] font-bold mb-2" style="color: rgba(13, 23, 38, 1);">Room 4</h4>
                        <p style="font-size:0.76rem;color: rgba(13, 23, 38, 0.7);line-height:1.6;">3D Environment view of Room 4 playing automatically in a loop.</p>
                    </div>
                </div>

            </div>\n"""

# lines[1478] is <div class="grid sm:grid-cols-2 gap-6">
# lines[1664] is </div>
lines = lines[:1478] + [new_content] + lines[1665:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
