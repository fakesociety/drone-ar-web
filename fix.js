const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// 1. Replace tailwind text colors
html = html.replace(/text-gray-[345]00/g, 'text-gray-800');
html = html.replace(/text-gray-[12]00/g, 'text-gray-900');
html = html.replace(/text-white/g, 'text-gray-900');

// 2. Bump up the opacities of rgba(13, 23, 38, opacity)
html = html.replace(/rgba\(13,\s*23,\s*38,\s*([0-9.]+)\)/g, (match, opStr) => {
    let op = parseFloat(opStr);
    if (op < 0.3) op = 0.5;
    else if (op < 0.5) op = 0.7;
    else if (op < 0.7) op = 0.85;
    else if (op < 0.9) op = 0.95;
    else op = 1.0;
    return `rgba(13, 23, 38, ${op})`;
});

// Also check the green/blue accents if they are too transparent
html = html.replace(/rgba\(33,\s*134,\s*118,\s*([0-9.]+)\)/g, (match, opStr) => {
    let op = parseFloat(opStr);
    if (op < 0.4 && op >= 0.15) op = 0.6; // keep very faint ones (like 0.05) faint, but bump medium ones
    else if (op >= 0.4 && op < 0.7) op = 0.85;
    return `rgba(33, 134, 118, ${op})`;
});

fs.writeFileSync('index.html', html);
console.log('Fixed text contrast');
