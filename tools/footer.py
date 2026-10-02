import random
random.seed(7)

W, H = 800, 130

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
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "G": ["01111", "10000", "10000", "10011", "10001", "10001", "01111"],
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
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

footer = []
footer.append(BACKGROUND)

# ♡♡♡ Sparkles ♡♡♡
for x, y, color, seconds, delay in [
    (150, 28,  BLACK, 2.6, 0.0),
    (300, 98,  WHITE, 3.1, 0.7),
    (470, 24,  BLACK, 2.2, 1.4),
    (560, 96,  WHITE, 2.6, 0.3),
    (640, 30,  WHITE, 3.1, 1.0),
    (30,  60,  WHITE, 2.2, 1.8),
    (770, 64,  BLACK, 2.6, 0.5),
]:
    footer += twinkle(paint_plain(SPARKLE, x, y, 2, color), seconds, delay)

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

footer += petals(4, [HOT, PINK, BLACK, WHITE])

# ♡♡♡ Bow and Heart ♡♡♡
footer += paint(BOW, 70, 45, 4, {"1": BLACK, "2": INK})

heart_colors = {"1": BLACK, "2": PINK, "3": WHITE}
footer += bounce(paint(HEART, 695, 50, 5, heart_colors), 5)

# ♡♡♡ Message ♡♡♡
message = "THANKS FOR VISITING"
message_size = 4
message_left = (W - how_wide(message, message_size)) // 2
message_top = (H - 7 * message_size) // 2

footer.append('<g opacity="0.25">')
footer += write(message, message_left + message_size, message_top + message_size, message_size, BLACK)
footer.append('</g>')

footer += write(message, message_left, message_top, message_size, PINK)

# ♡♡♡ Lace trim ♡♡♡
footer.append(LACE)

svg = (
    f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    'xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">\n'
    + "\n".join(footer)
    + "\n</svg>"
)

with open("footer.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("footer.svg saved!")
