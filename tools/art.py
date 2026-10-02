import math
import random
random.seed(7)

W, H = 800, 220

# ♡♡♡ Palette ♡♡♡
PINK = "#f0428f"
HOT = "#ff7fb6"
BLUSH = "#ffd3e5"
BLACK = "#1c1119"
INK = "#3a2434"
WHITE = "#ffffff"

# ♡♡♡ Background and Lace ♡♡♡
BACKGROUND = f"""
    <defs>
        <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%"   stop-color="#ffe6f0"/>
        <stop offset="55%"  stop-color="#ffd3e5"/>
        <stop offset="100%" stop-color="#ffbcd8"/>
        </linearGradient>

        <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">
            <rect x="4"  y="4"  width="2" height="2" fill="{WHITE}"/>
            <rect x="16" y="16" width="2" height="2" fill="{WHITE}"/>
        </pattern>

        <pattern id="lace" width="16" height="16" patternUnits="userSpaceOnUse">
            <rect width="16" height="6" fill="{BLACK}"/>
            <rect x="7" y="2"  width="2"  height="2" fill="{HOT}"/>
            <rect x="0" y="6"  width="16" height="2" fill="{BLACK}"/>
            <rect x="2" y="8"  width="12" height="2" fill="{BLACK}"/>
            <rect x="4" y="10" width="8"  height="2" fill="{BLACK}"/>
            <rect x="7" y="14" width="2"  height="2" fill="{BLACK}"/>
        </pattern>
    </defs>

    <rect width="{W}" height="{H}" fill="url(#sky)"/>
    <rect width="{W}" height="{H}" fill="url(#dots)" opacity="0.6"/>
    """

LACE = f"""
    <rect width="{W}" height="16" fill="url(#lace)"/>
    <rect width="{W}" height="16" fill="url(#lace)" transform="translate(0,{H}) scale(1,-1)"/>
    """

def paint(picture, left, top, size, colors):
    pixels = []
    for row_number, row in enumerate(picture):
        for col_number, dot in enumerate(row):
            if dot in colors:
                x = left + col_number * size
                y = top + row_number * size
                pixels.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{colors[dot]}"/>')
    return pixels

def paint_plain(picture, left, top, size, color):
    return paint(picture, left, top, size, {"1": color})

def bounce(pixels, hop, delay=0.0, seconds=1.6):
    return (
        ['<g>'] + pixels +
        [f'<animateTransform attributeName="transform" type="translate" '
         f'values="0,0; 0,-{hop}; 0,0" dur="{seconds}s" begin="{delay}s" '
         'repeatCount="indefinite" calcMode="discrete"/>', '</g>']
    )

def twinkle(pixels, seconds, delay=0.0):
    return (
        ['<g>'] + pixels +
        [f'<animate attributeName="opacity" values="1;0.15;1" dur="{seconds}s" '
         f'begin="{delay}s" repeatCount="indefinite"/>', '</g>']
    )

# ♡♡♡ Little Pictures ♡♡♡
BOW = [
    "11.........11",
    "1211.....1121",
    "122211.112221",
    "1222211122221",
    "1222211122221",
    "122211.112221",
    "1211.111.1121",
    "11..11.11..11",
    "...11...11...",
    "..11.....11..",
]

HEART = [
    ".11.11.",
    "1321221",
    "1222221",
    ".12221.",
    "..121..",
    "...1...",
]

SPARKLE = [
    "..1..",
    "..1..",
    "11.11",
    "..1..",
    "..1..",
]

LETTERS = {
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "-": ["00000", "00000", "00000", "01110", "00000", "00000", "00000"],
    "#": ["01010", "11111", "01010", "01010", "01010", "11111", "01010"],
    "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "00000", "00100"],
}

def write(text, left, top, size, color):
    pixels = []
    x = left
    for letter in text:
        pixels += paint_plain(LETTERS[letter], x, top, size, color)
        x += 6 * size
    return pixels

def how_wide(text, size):
    return len(text) * 6 * size - size

def accent_mark(letter_left, top, size, color):
    return [
        f'<rect x="{letter_left + 3*size}" y="{top - 3*size}" width="{size}" height="{size}" fill="{color}"/>',
        f'<rect x="{letter_left + 2*size}" y="{top - 2*size}" width="{size}" height="{size}" fill="{color}"/>',
    ]

banner = []
banner.append(BACKGROUND)

# ♡♡♡ Sparkles ♡♡♡
for x, y, color, seconds, delay in [
    (180, 40,  BLACK, 2.6, 0.0),
    (300, 26,  WHITE, 3.1, 0.7),
    (520, 32,  BLACK, 2.2, 1.4),
    (240, 182, WHITE, 2.6, 0.3),
    (420, 186, BLACK, 3.1, 1.0),
    (612, 176, WHITE, 2.2, 1.8),
    (40,  176, BLACK, 2.6, 0.5),
    (770, 184, WHITE, 3.1, 1.2),
]:
    banner += twinkle(paint_plain(SPARKLE, x, y, 2, color), seconds, delay)

# ♡♡♡ Bow and Hearts ♡♡♡
banner += paint(BOW, 692, 26, 4, {"1": BLACK, "2": INK})

heart_colors = {"1": BLACK, "2": PINK, "3": WHITE}
banner += bounce(paint(HEART, 96, 124, 4, heart_colors), 5)
banner += bounce(paint(HEART, 680, 150, 3, heart_colors), 4, delay=0.8)

# ♡♡♡ Fireworks ♡♡♡
def firework(x, y, color, delay, sparks=10, reach=54, seconds=2.8):
    pixels = []
    for i in range(sparks):
        angle = 2 * math.pi * i / sparks
        path = []
        for step in range(6):
            t = step / 5
            dx = round(math.cos(angle) * reach * t / 4) * 4
            dy = round(math.sin(angle) * reach * t / 4) * 4 + round(6 * t * t)
            path.append(f"{dx},{dy}")
        pixels.append(
            f'<rect x="{x}" y="{y}" width="4" height="4" fill="{color}" opacity="0">'
            f'<animateTransform attributeName="transform" type="translate" '
            f'values="{"; ".join(path)}" keyTimes="0;0.1;0.2;0.3;0.4;0.5" '
            f'dur="{seconds}s" begin="{delay}s" repeatCount="indefinite" calcMode="discrete"/>'
            f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.45;0.6;1" '
            f'dur="{seconds}s" begin="{delay}s" repeatCount="indefinite" calcMode="discrete"/>'
            '</rect>'
        )
    return pixels

banner += firework(70, 60, PINK, 0.0, reach=48)
banner += firework(70, 60, BLACK, 0.0, sparks=6, reach=24)
banner += firework(745, 110, HOT, 1.4, sparks=8, reach=36)
banner += firework(745, 110, BLACK, 1.4, sparks=6, reach=18)

# ♡♡♡ Petals ♡♡♡
def petals(how_many, colors):
    pixels = []
    for _ in range(how_many):
        x = random.randrange(0, W)
        color = random.choice(colors)
        seconds = round(random.uniform(7, 14), 1)
        head_start = round(random.uniform(0, seconds), 1)
        sway = random.randint(-60, 60)
        pixels.append(
            f'<g>'
            f'<rect x="{x}" y="-8" width="4" height="4" fill="{color}"/>'
            f'<rect x="{x + 4}" y="-4" width="4" height="4" fill="{color}"/>'
            f'<animateTransform attributeName="transform" type="translate" '
            f'values="0,0; {sway // 2},{H // 2}; {sway},{H + 16}" '
            f'dur="{seconds}s" begin="-{head_start}s" repeatCount="indefinite"/>'
            f'</g>'
        )
    return pixels

banner += petals(7, [HOT, PINK, BLACK, WHITE])

# ♡♡♡ Name ♡♡♡
name = "MONICA MOURA"
name_size = 7
name_left = (W - how_wide(name, name_size)) // 2
name_top = 68
o_left = name_left + 1 * 6 * name_size

banner.append('<g opacity="0.25">')
banner += write(name, name_left + name_size, name_top + name_size, name_size, BLACK)
banner += accent_mark(o_left + name_size, name_top + name_size, name_size, BLACK)
banner.append('</g>')

banner += write(name, name_left, name_top, name_size, PINK)
banner += accent_mark(o_left, name_top, name_size, PINK)

# ♡♡♡ Subtitle ♡♡♡
subtitle = "BACKEND DEVELOPER - C# / .NET"
subtitle_size = 3
subtitle_left = (W - how_wide(subtitle, subtitle_size)) // 2
subtitle_top = 148
banner += write(subtitle, subtitle_left, subtitle_top, subtitle_size, BLACK)

underline_width = 90
underline_left = (W - underline_width) // 2
underline_top = subtitle_top + 7 * subtitle_size + 12
banner.append(
        f'<rect x="{underline_left}" y="{underline_top}" width="{underline_width}" height="3" fill="{PINK}"/>'
)

cursor_left = underline_left + underline_width + 4
cursor_top = underline_top - 7
banner.append(
    f'<rect x="{cursor_left}" y="{cursor_top}" width="8" height="10" fill="{BLACK}">'
    '<animate attributeName="opacity" values="1;0" dur="1s" '
    'repeatCount="indefinite" calcMode="discrete"/>'
    '</rect>'
)

# ♡♡♡ Lace trim ♡♡♡
banner.append(LACE)

svg = (
    f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    'xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">\n'
    + "\n".join(banner)
    + "\n</svg>"
)

with open("banner.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("banner.svg saved!")
