W, H = 800, 24

# ♡♡♡ Palette ♡♡♡
PINK = "#f0428f"
HOT = "#ff7fb6"
BLACK = "#1c1119"
WHITE = "#ffffff"

def paint(picture, left, top, size, colors):
    pixels = []
    for row_number, row in enumerate(picture):
        for col_number, dot in enumerate(row):
            if dot in colors:
                x = left + col_number * size
                y = top + row_number * size
                pixels.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{colors[dot]}"/>')
    return pixels

def bounce(pixels, hop, delay=0.0, seconds=1.6):
    return (
        ['<g>'] + pixels +
        [f'<animateTransform attributeName="transform" type="translate" '
         f'values="0,0; 0,-{hop}; 0,0" dur="{seconds}s" begin="{delay}s" '
         'repeatCount="indefinite" calcMode="discrete"/>', '</g>']
    )

# ♡♡♡ Little Pictures ♡♡♡
HEART = [
    ".11.11.",
    "1321221",
    "1222221",
    ".12221.",
    "..121..",
    "...1...",
]

divider = []

# ♡♡♡ Dotted line ♡♡♡
# no background on purpose, so it sits nicely on GitHub light AND dark mode
heart_size = 3
heart_width = 7 * heart_size
heart_left = (W - heart_width) // 2
gap = 24                                    # empty space on each side of the heart

for x in range(0, W, 24):
    if heart_left - gap < x + 24 and x < heart_left + heart_width + gap:
        continue                            # leave room around the heart
    divider.append(f'<rect x="{x + 4}" y="11" width="10" height="2" fill="{PINK}"/>')
    divider.append(f'<rect x="{x + 18}" y="10" width="4" height="4" fill="{HOT}"/>')

# ♡♡♡ Heart ♡♡♡
heart_colors = {"1": BLACK, "2": PINK, "3": WHITE}
divider += bounce(paint(HEART, heart_left, 5, heart_size, heart_colors), 3)

svg = (
    f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    'xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">\n'
    + "\n".join(divider)
    + "\n</svg>"
)

with open("divider.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("divider.svg saved!")
