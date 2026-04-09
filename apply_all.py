#!/usr/bin/env python3
"""
apply_all.py — applies ALL portfolio changes to the clean original index.html
1. Identity rebranding (Arham -> Jeevan)
2. Meta/SEO updates
3. Splash screen CSS + HTML + JS
4. Dev Mode CSS + HTML + JS
5. SYSTEM_THOUGHTS.log moving card stream (replaces testimonials)
"""
import re

UTF8 = 'utf-8'

with open('index.html', 'r', encoding=UTF8) as f:
    h = f.read()

# ============================================================
# 1. IDENTITY REBRANDING
# ============================================================
h = h.replace('Arham43-ops', 'jeevan-charugundla')
h = h.replace('Arham43', 'jeevan-charugundla')
h = h.replace('arham43-ops', 'jeevan-charugundla')

# Name replacements (careful order: longer first)
h = h.replace('Arham Shaikh', 'Jeevan Charugundla')
h = h.replace('Arham', 'Jeevan')
h = h.replace('arham', 'jeevan')

# Title
h = h.replace('Full Stack Developer', 'AI Product Engineer')
h = h.replace('full-stack developer', 'AI Product Engineer')

# GitHub / social links
h = h.replace('github.com/Arham43-ops', 'github.com/jeevan-charugundla')
h = h.replace('github.com/arham43-ops', 'github.com/jeevan-charugundla')
h = h.replace('@Arham43-ops', '@jeevan-charugundla')

# Meta description – patch title tag
h = re.sub(
    r'(<title>)[^<]*(</title>)',
    r'\g<1>Jeevan Charugundla | AI Product Engineer\g<2>',
    h
)
# og:title
h = re.sub(
    r'(property="og:title"\s+content=")[^"]*(")',
    r'\g<1>Jeevan Charugundla | AI Product Engineer\g<2>',
    h
)
# og:url
h = re.sub(
    r'(property="og:url"\s+content=")[^"]*(")',
    r'\g<1>https://jeevan-charugundla.github.io\g<2>',
    h
)
# twitter:title
h = re.sub(
    r'(name="twitter:title"\s+content=")[^"]*(")',
    r'\g<1>Jeevan Charugundla | AI Product Engineer\g<2>',
    h
)

# ============================================================
# 2. SPLASH SCREEN CSS  (inject before </style>)
# ============================================================
SPLASH_CSS = r"""
        /* ===== SPLASH SCREEN ===== */
        #splash-screen {
            position: fixed; inset: 0; z-index: 99999;
            background: #FFFDF5;
            display: flex; align-items: center; justify-content: center;
            overflow: hidden;
        }
        .splash-corner {
            position: absolute; width: 40px; height: 40px;
            border: 4px solid #000;
        }
        .splash-corner--tl { top: 24px; left: 24px; border-right: none; border-bottom: none; }
        .splash-corner--tr { top: 24px; right: 24px; border-left: none; border-bottom: none; }
        .splash-corner--bl { bottom: 24px; left: 24px; border-right: none; border-top: none; }
        .splash-corner--br { bottom: 24px; right: 24px; border-left: none; border-top: none; }
        .splash-geo-sq {
            position: absolute; width: 28px; height: 28px;
            border: 3px solid #000; background: #FBFF48;
        }
        .splash-geo-circle {
            position: absolute; width: 22px; height: 22px;
            border-radius: 50%; border: 3px solid #000;
        }
        #splash-name-wrap {
            position: relative; display: inline-block; line-height: 1;
        }
        #splash-name-outline {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 800;
            font-size: clamp(72px, 18vw, 200px);
            line-height: 1; letter-spacing: -0.03em;
            color: transparent;
            -webkit-text-stroke: 3px #000;
            position: relative; z-index: 1; white-space: nowrap;
        }
        #splash-name-fill {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 800;
            font-size: clamp(72px, 18vw, 200px);
            line-height: 1; letter-spacing: -0.03em;
            color: #121212;
            -webkit-text-stroke: 3px #000;
            position: absolute; top: 0; left: 0;
            white-space: nowrap;
            clip-path: inset(0 100% 0 0);
            text-shadow: none;
        }
        #splash-label {
            font-family: 'JetBrains Mono', monospace;
            font-size: clamp(10px, 2vw, 14px);
            letter-spacing: 0.3em; text-transform: uppercase;
            color: #000; margin-top: 18px; text-align: center;
            opacity: 0;
        }
        @keyframes splash-fill-lr {
            0%   { clip-path: inset(0 100% 0 0); }
            100% { clip-path: inset(0 0% 0 0); }
        }
        @keyframes splash-pop {
            0%   { transform: scale(1); }
            50%  { transform: scale(1.04); }
            100% { transform: scale(1); }
        }
        @keyframes splash-label-in {
            0%   { opacity: 0; transform: translateY(6px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes splash-exit {
            0%   { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-100%); opacity: 0; }
        }
        #splash-screen.do-exit {
            animation: splash-exit 0.55s cubic-bezier(0.76, 0, 0.24, 1) forwards;
            pointer-events: none;
        }
"""

# ============================================================
# 3. DEV MODE CSS
# ============================================================
DEV_CSS = r"""
        /* ===== DEV MODE STYLES ===== */
        #dev-backdrop {
            display: none; position: fixed; inset: 0;
            background: rgba(0,0,0,0.55); z-index: 9000;
        }
        #dev-backdrop.visible { display: block; }
        #dev-confirm {
            display: none; position: fixed; inset: 0; z-index: 9100;
            align-items: center; justify-content: center;
        }
        #dev-confirm.visible { display: flex; }
        #dev-confirm-box {
            background: #FFFDF5; border: 4px solid #000;
            box-shadow: 6px 6px 0 #000;
            padding: 40px 48px; text-align: center; min-width: 340px;
            position: relative;
        }
        @keyframes dev-snap-in {
            0%  { transform: scale(0.93) translate(-2px,2px); opacity:0; }
            60% { transform: scale(1.02); opacity:1; }
            100%{ transform: scale(1); opacity:1; }
        }
        #dev-confirm-box.jitter {
            animation: dev-snap-in 0.12s cubic-bezier(.36,.07,.19,.97) both,
                       dev-jitter 0.2s linear 1 0.12s;
        }
        @keyframes dev-jitter {
            0%,100%{ transform:translate(0,0); }
            25%    { transform:translate(-1px,1px); }
            50%    { transform:translate(1px,-1px); }
            75%    { transform:translate(-1px,-1px); }
        }
        #dev-confirm-title {
            font-family:'Space Grotesk',sans-serif; font-weight:800;
            font-size:2rem; letter-spacing:-0.02em; line-height:1;
            margin-bottom:10px; border-bottom:3px solid #000; padding-bottom:10px;
        }
        #dev-confirm-sub { font-family:'JetBrains Mono',monospace; font-size:0.75rem; color:#555; margin-bottom:18px; }
        #dev-confirm-q   { font-family:'JetBrains Mono',monospace; font-weight:700; font-size:1rem; margin-bottom:28px; letter-spacing:0.05em; }
        .dev-btn {
            font-family:'JetBrains Mono',monospace; font-weight:700; font-size:0.9rem;
            padding:8px 28px; border:3px solid #000; cursor:pointer;
            transition:transform 0.08s,box-shadow 0.08s; box-shadow:3px 3px 0 #000;
            letter-spacing:0.06em;
        }
        .dev-btn:hover { transform:translate(2px,2px); box-shadow:1px 1px 0 #000; }
        .dev-btn:active { transform:translate(3px,3px); box-shadow:none; }
        .dev-btn-yes { background:#121212; color:#fff; }
        .dev-btn-yes:hover { background:#000; }
        .dev-btn-no  { background:#FFFDF5; color:#000; cursor:none; }
        #dev-console { display:none; position:fixed; inset:0; z-index:9200; align-items:center; justify-content:center; }
        #dev-console.visible { display:flex; }
        #dev-console-box {
            background:#0a0a0a; border:4px solid #000;
            box-shadow:8px 8px 0 #33FF57;
            width:min(90vw,780px); max-height:88vh;
            display:flex; flex-direction:column; overflow:hidden;
        }
        @keyframes dev-console-in { 0%{transform:scale(0.96);opacity:0;} 100%{transform:scale(1);opacity:1;} }
        #dev-console-box { animation:dev-console-in 0.18s cubic-bezier(0.19,1,0.22,1) forwards; }
        #dev-console-header {
            display:flex; align-items:center; justify-content:space-between;
            padding:10px 18px; border-bottom:3px solid #1a1a1a; background:#111;
        }
        #dev-console-title {
            font-family:'JetBrains Mono',monospace; font-weight:700;
            font-size:0.78rem; color:#33FF57; letter-spacing:0.12em;
            display:flex; align-items:center; gap:8px;
        }
        #dev-status-dot {
            width:8px; height:8px; border-radius:50%; background:#33FF57;
            display:inline-block; animation:blink-dot 1.1s step-end infinite;
        }
        @keyframes blink-dot { 0%,100%{opacity:1;} 50%{opacity:0;} }
        #dev-exit-btn {
            font-family:'JetBrains Mono',monospace; font-size:0.7rem; font-weight:700;
            color:#ff4444; background:transparent; border:2px solid #ff4444;
            padding:3px 12px; cursor:pointer; letter-spacing:0.1em;
            transition:background 0.1s,color 0.1s;
        }
        #dev-exit-btn:hover { background:#ff4444; color:#fff; }
        #dev-output {
            flex:1; overflow-y:auto; padding:18px 20px 8px;
            font-family:'JetBrains Mono',monospace; font-size:0.82rem;
            color:#e0e0e0; line-height:1.7;
            scrollbar-width:thin; scrollbar-color:#33FF57 #111;
        }
        .dev-line-prompt{color:#33FF57;} .dev-line-cmd{color:#FBFF48;}
        .dev-line-out{color:#c8c8c8;} .dev-line-err{color:#ff4444;} .dev-line-key{color:#FF70A6;}
        .dev-blink-cursor::after { content:'_'; animation:blink-dot 0.8s step-end infinite; color:#33FF57; }
        #dev-cmds {
            display:flex; flex-wrap:wrap; gap:8px; padding:12px 20px;
            border-top:3px solid #1a1a1a; background:#0e0e0e;
        }
        .dev-cmd-btn {
            font-family:'JetBrains Mono',monospace; font-size:0.78rem; font-weight:700;
            padding:5px 14px; border:2px solid #33FF57; background:transparent; color:#33FF57;
            cursor:pointer; letter-spacing:0.08em;
            transition:background 0.08s,color 0.08s,transform 0.08s,box-shadow 0.08s;
            box-shadow:2px 2px 0 #33FF57;
        }
        .dev-cmd-btn:hover { background:#33FF57; color:#0a0a0a; transform:translate(2px,2px); box-shadow:none; }
        .dev-cmd-btn.exit-cmd { border-color:#ff4444; color:#ff4444; box-shadow:2px 2px 0 #ff4444; }
        .dev-cmd-btn.exit-cmd:hover { background:#ff4444; color:#fff; }
        @keyframes dev-glitch { 0%{filter:none;} 10%{filter:hue-rotate(180deg) invert(1);} 20%{filter:none;} }
        .glitch-flash { animation:dev-glitch 0.15s steps(1) forwards; }
        @keyframes dev-console-out { 0%{transform:scale(1);opacity:1;} 100%{transform:scale(0.94);opacity:0;} }
        #dev-console-box.closing { animation:dev-console-out 0.2s cubic-bezier(0.76,0,0.24,1) forwards; }

        /* ===== SYSTEM_THOUGHTS CARD STREAM ===== */
        @keyframes thought-ltr {
            0%   { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        @keyframes thought-rtl {
            0%   { transform: translateX(-50%); }
            100% { transform: translateX(0); }
        }
        .thought-row { overflow: hidden; position: relative; }
        .thought-track { display: flex; align-items: stretch; width: max-content; will-change: transform; }
        .thought-row:hover .thought-track { animation-play-state: paused; }
        .thought-card {
            flex-shrink: 0;
            width: 280px;
            background: #0f0f0f;
            border: 3px solid rgba(255,255,255,0.1);
            margin-right: 20px;
            padding: 22px 22px 18px;
            position: relative;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.15s, box-shadow 0.15s, border-color 0.15s;
        }
        .thought-card:hover {
            transform: scale(1.03) rotate(0.5deg);
        }
        .thought-card .tc-top-bar {
            position: absolute; top: 0; left: 0; width: 100%; height: 3px;
        }
        .thought-card .tc-header {
            display: flex; justify-content: space-between; align-items: flex-start;
            margin-bottom: 12px;
        }
        .thought-card .tc-id {
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700; font-size: 0.7rem;
            letter-spacing: 0.12em; text-transform: uppercase;
        }
        .thought-card .tc-tag {
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700; font-size: 0.65rem;
            padding: 2px 7px; border: 1px solid;
            text-transform: uppercase; letter-spacing: 0.1em;
        }
        .thought-card .tc-text {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.82rem; line-height: 1.6;
            color: rgba(255,255,255,0.85);
            font-weight: 500;
        }
        .thought-card .tc-hint {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.68rem; margin-top: 14px;
            opacity: 0; transition: opacity 0.15s;
            display: flex; align-items: center; gap: 4px;
        }
        .thought-card:hover .tc-hint { opacity: 1; }
        .tc-cursor { animation: blink-dot 0.8s step-end infinite; }
"""

# Inject CSS before </style>
h = h.replace('    </style>\n</head>', SPLASH_CSS + DEV_CSS + '    </style>\n</head>', 1)

# ============================================================
# 4. SPLASH HTML (inject right after <body ...>)
# ============================================================
SPLASH_HTML = """
    <!-- ===== SPLASH SCREEN ===== -->
    <div id="splash-screen" aria-hidden="true">
        <div class="splash-corner splash-corner--tl"></div>
        <div class="splash-corner splash-corner--tr"></div>
        <div class="splash-corner splash-corner--bl"></div>
        <div class="splash-corner splash-corner--br"></div>
        <div class="splash-geo-sq" style="top:10%;left:7%;transform:rotate(-8deg);"></div>
        <div class="splash-geo-sq" style="bottom:12%;right:8%;transform:rotate(12deg);background:#33FF57;"></div>
        <div class="splash-geo-circle" style="top:15%;right:9%;background:#FBFF48;"></div>
        <div class="splash-geo-circle" style="bottom:16%;left:9%;background:#FF70A6;"></div>
        <div style="text-align:center;">
            <div id="splash-name-wrap">
                <div id="splash-name-outline">JEEVAN</div>
                <div id="splash-name-fill">JEEVAN</div>
            </div>
            <div id="splash-label">AI Product Engineer</div>
        </div>
    </div>
    <!-- ===== END SPLASH SCREEN ===== -->
"""

body_open = h.find('<body')
body_close = h.find('>', body_open) + 1
h = h[:body_close] + SPLASH_HTML + h[body_close:]

# ============================================================
# 5. NAV LOGO — add id="dev-logo"
# ============================================================
h = h.replace(
    'class="bg-neo-white border-2 border-black px-4 py-1 text-2xl font-black shadow-hard hover:bg-neo-yellow transition-all hover:translate-x-1 hover:translate-y-1 hover:shadow-none cursor-hover">\n                Jeevan.dev',
    'id="dev-logo" class="bg-neo-white border-2 border-black px-4 py-1 text-2xl font-black shadow-hard hover:bg-neo-yellow transition-all hover:translate-x-1 hover:translate-y-1 hover:shadow-none cursor-hover">\n                JEEVAN.dev'
)
# fallback pattern
h = h.replace(
    'href="#"\n                class="bg-neo-white border-2 border-black px-4 py-1 text-2xl font-black',
    'href="#" id="dev-logo"\n                class="bg-neo-white border-2 border-black px-4 py-1 text-2xl font-black'
)

# ============================================================
# 6. DEV MODE HTML (after </nav>)
# ============================================================
DEV_HTML = """
    <!-- ===== DEV MODE OVERLAY ===== -->
    <div id="dev-backdrop"></div>
    <div id="dev-confirm" role="dialog" aria-modal="true">
        <div id="dev-confirm-box" class="jitter">
            <div id="dev-confirm-title">ENTER DEV MODE</div>
            <div id="dev-confirm-sub">This will unlock interactive controls.</div>
            <div id="dev-confirm-q">Are you sure?</div>
            <div style="display:flex;gap:16px;justify-content:center;">
                <button class="dev-btn dev-btn-yes" id="dev-yes">[ YES ]</button>
                <button class="dev-btn dev-btn-no"  id="dev-no" >[ NO  ]</button>
            </div>
        </div>
    </div>
    <div id="dev-console" role="dialog" aria-modal="true">
        <div id="dev-console-box">
            <div id="dev-console-header">
                <div id="dev-console-title"><span id="dev-status-dot"></span> DEV_MODE: ACTIVE</div>
                <button id="dev-exit-btn">[ EXIT ]</button>
            </div>
            <div id="dev-output"></div>
            <div id="dev-cmds">
                <button class="dev-cmd-btn" data-cmd="whoami">whoami</button>
                <button class="dev-cmd-btn" data-cmd="skills">skills</button>
                <button class="dev-cmd-btn" data-cmd="projects">projects</button>
                <button class="dev-cmd-btn" data-cmd="contact">contact</button>
                <button class="dev-cmd-btn exit-cmd" data-cmd="exit">exit</button>
            </div>
        </div>
    </div>
    <!-- ===== END DEV MODE ===== -->
"""
h = h.replace('</nav>\n', '</nav>\n' + DEV_HTML, 1)

# ============================================================
# 7. REPLACE TESTIMONIALS SECTION with MOVING CARD STREAM
# ============================================================
# Find the testimonials section by its id
sec_start = h.find('<section id="reports"')
sec_end   = h.find('</section>', sec_start) + len('</section>')

def card(log_id, tag, color, shadow_color, text):
    return f"""
                <div class="thought-card" data-log="{log_id}"
                     style="box-shadow:4px 4px 0 {shadow_color}; border-color:rgba(255,255,255,0.12);"
                     onmouseenter="this.style.boxShadow='2px 2px 0 {shadow_color}'"
                     onmouseleave="this.style.boxShadow='4px 4px 0 {shadow_color}'">
                    <div class="tc-top-bar" style="background:{color};"></div>
                    <div class="tc-header">
                        <span class="tc-id" style="color:{color};">{log_id}</span>
                        <span class="tc-tag" style="color:{color};border-color:{color}40;background:{color}18;">[{tag}]</span>
                    </div>
                    <div class="tc-text">{text}</div>
                    <div class="tc-hint" style="color:{color};">expanding log...<span class="tc-cursor">_</span></div>
                </div>"""

cards = {
    'LOG_001': ('#FF2D78', '#FF2D78', 'AI',      "Most AI apps fail not because of bad models, but because of weak product thinking."),
    'LOG_002': ('#A855F7', '#A855F7', 'SYSTEMS',  "If it doesn't work in real-time, it's not ready for users."),
    'LOG_003': ('#F97316', '#F97316', 'PRODUCT',  "Shipping something imperfect beats designing something perfect forever."),
    'LOG_004': ('#A855F7', '#A855F7', 'SYSTEMS',  "Latency is a UX problem, not just a backend problem."),
    'LOG_005': ('#FF2D78', '#FF2D78', 'AI',       "AI is easy to demo. Hard to ship reliably."),
    'LOG_006': ('#F97316', '#F97316', 'PRODUCT',  "I don't just build apps. I build systems that run them."),
    'LOG_007': ('#33FF57', '#33FF57', 'SYSTEMS',  "If it's not deployed, it doesn't exist."),
}

def row(ids, speed, direction):
    items = ''.join(card(i, cards[i][2], cards[i][0], cards[i][1], cards[i][3]) for i in ids)
    anim = f'thought-{"ltr" if direction == "ltr" else "rtl"} {speed}s linear infinite'
    return f"""
        <div class="thought-row py-4" style="border-top:1px solid rgba(255,255,255,0.07);">
            <div class="thought-track" style="animation:{anim};">{items}{items}</div>
        </div>"""

row1 = row(['LOG_001','LOG_003','LOG_005','LOG_006'], 35, 'ltr')
row2 = row(['LOG_002','LOG_004','LOG_007','LOG_001'], 48, 'rtl')
row3 = row(['LOG_005','LOG_006','LOG_007','LOG_003'], 26, 'ltr')

NEW_SECTION = f"""<section id="reports" class="py-20 bg-neo-black border-t-4 border-black overflow-hidden relative">

        <!-- Section header -->
        <div class="max-w-7xl mx-auto px-4 mb-10">
            <div class="flex items-center gap-2 bg-white/5 border-2 border-white/10 p-4 inline-flex shadow-hard shadow-neo-green/20">
                <div class="flex gap-2">
                    <div class="h-3 w-3 bg-red-500 rounded-full border border-black"></div>
                    <div class="h-3 w-3 bg-yellow-500 rounded-full border border-black"></div>
                    <div class="h-3 w-3 bg-green-500 rounded-full border border-black"></div>
                </div>
                <h2 class="font-mono text-white text-xl font-bold ml-4 tracking-tighter">SYSTEM_THOUGHTS.log</h2>
                <div class="ml-8 px-2 bg-neo-green text-black text-[10px] font-black uppercase">[ LIVE_FEED ]</div>
            </div>
        </div>

        <!-- Fade edge masks -->
        <div class="pointer-events-none absolute inset-y-20 left-0 w-24 z-10"
             style="background:linear-gradient(to right,#0a0a0a 0%,transparent 100%);"></div>
        <div class="pointer-events-none absolute inset-y-20 right-0 w-24 z-10"
             style="background:linear-gradient(to left,#0a0a0a 0%,transparent 100%);"></div>

        {row1}
        {row2}
        {row3}

    </section>"""

h = h[:sec_start] + NEW_SECTION + h[sec_end:]

# ============================================================
# 8. SPLASH ORCHESTRATOR JS  (before </body>)
# ============================================================
SPLASH_JS = """
    <!-- ===== SPLASH ORCHESTRATOR ===== -->
    <script>
    (function () {
        var splash   = document.getElementById('splash-screen');
        var fill     = document.getElementById('splash-name-fill');
        var label    = document.getElementById('splash-label');
        function after(ms, fn) { setTimeout(fn, ms); }
        function addClass(el, cls) { el.classList.add(cls); }
        document.body.style.overflow = 'hidden';
        after(300, function () {
            fill.style.animation = 'splash-fill-lr 0.9s cubic-bezier(0.76,0,0.24,1) forwards';
        });
        after(1350, function () {
            fill.style.animation += ', splash-pop 0.35s cubic-bezier(0.36,0.07,0.19,0.97) 0.9s both';
        });
        after(1400, function () {
            label.style.animation = 'splash-label-in 0.4s cubic-bezier(0.25,1,0.5,1) forwards';
        });
        after(2000, function () {
            addClass(splash, 'do-exit');
        });
        after(2550, function () {
            splash.remove();
            document.body.style.overflow = '';
        });
    })();
    </script>
    <!-- ===== END SPLASH ORCHESTRATOR ===== -->
"""

# ============================================================
# 9. DEV MODE JS
# ============================================================
DEV_JS = """
    <!-- ===== DEV MODE JS ===== -->
    <script>
    (function () {
        var backdrop    = document.getElementById('dev-backdrop');
        var confirm_    = document.getElementById('dev-confirm');
        var confirmBox  = document.getElementById('dev-confirm-box');
        var consoleWrap = document.getElementById('dev-console');
        var consoleBox  = document.getElementById('dev-console-box');
        var output      = document.getElementById('dev-output');
        var logo        = document.getElementById('dev-logo');
        var btnYes      = document.getElementById('dev-yes');
        var btnNo       = document.getElementById('dev-no');
        var btnExit     = document.getElementById('dev-exit-btn');
        var cmdBtns     = document.querySelectorAll('.dev-cmd-btn');
        var isOpen = false, idleTimer = null, clickCount = 0, clickTimer = null;
        function show(el) { el.classList.add('visible'); }
        function hide(el) { el.classList.remove('visible'); }
        function addLine(html) {
            var p = document.createElement('p'); p.innerHTML = html;
            output.appendChild(p); output.scrollTop = output.scrollHeight;
        }
        function typeLines(lines, done) {
            var i = 0;
            function next() {
                if (i >= lines.length) { if (done) done(); return; }
                var l = lines[i++]; addLine(l.text); setTimeout(next, l.pause || 50);
            } next();
        }
        function addCursor() {
            var p = document.createElement('p');
            p.className = 'dev-line-prompt dev-blink-cursor'; p.id = 'dev-cursor-line'; p.innerHTML = '&#10095; ';
            output.appendChild(p); output.scrollTop = output.scrollHeight;
        }
        function removeCursor() { var c = document.getElementById('dev-cursor-line'); if (c) c.remove(); }
        function resetIdle() {
            clearTimeout(idleTimer);
            idleTimer = setTimeout(function () {
                if (isOpen) { removeCursor(); addLine('<span class="dev-line-out">awaiting input...</span>'); addCursor(); }
            }, 3500);
        }
        if (logo) logo.addEventListener('click', function (e) {
            e.preventDefault(); if (isOpen) return;
            show(backdrop); show(confirm_);
            confirmBox.classList.remove('jitter'); void confirmBox.offsetWidth; confirmBox.classList.add('jitter');
        });
        btnNo.addEventListener('mousemove', function (e) {
            var r = btnNo.getBoundingClientRect();
            btnNo.style.transform = 'translate('+(-( e.clientX-r.left-r.width/2)*0.4)+'px,'+(-(e.clientY-r.top-r.height/2)*0.4)+'px) translate(2px,2px)';
        });
        btnNo.addEventListener('mouseleave', function () { btnNo.style.transform = ''; });
        btnNo.addEventListener('click', function () { hide(backdrop); hide(confirm_); });
        backdrop.addEventListener('click', function () { if (!isOpen) { hide(backdrop); hide(confirm_); } });
        btnYes.addEventListener('click', function () {
            hide(confirm_);
            document.body.classList.add('glitch-flash');
            setTimeout(function () { document.body.classList.remove('glitch-flash'); }, 160);
            setTimeout(function () {
                isOpen = true; show(consoleWrap); output.innerHTML = '';
                typeLines([
                    {text:'<span class="dev-line-prompt">&#10095; </span><span class="dev-line-cmd">dev_mode --active</span>', pause:60},
                    {text:'<span class="dev-line-out">welcome, user.</span>', pause:60},
                    {text:'<span class="dev-line-out">try commands below.</span>', pause:80},
                    {text:'', pause:0}
                ], function () { addCursor(); resetIdle(); });
            }, 120);
        });
        function closeConsole() {
            isOpen = false; clearTimeout(idleTimer); removeCursor();
            addLine('<span class="dev-line-prompt">&#10095; </span><span class="dev-line-cmd">exit</span>');
            addLine('<span class="dev-line-out">Closing dev mode...</span>');
            setTimeout(function () {
                consoleBox.classList.add('closing');
                setTimeout(function () {
                    hide(consoleWrap); hide(backdrop);
                    consoleBox.classList.remove('closing');
                    void consoleBox.offsetWidth;
                }, 220);
            }, 300);
        }
        btnExit.addEventListener('click', closeConsole);
        var commands = {
            whoami: function () {
                typeLines([
                    {text:'<span class="dev-line-out">Jeevan</span>',pause:40},
                    {text:'<span class="dev-line-out">AI Product Engineer</span>',pause:40},
                    {text:'<span class="dev-line-out">Builder of scalable, real-world systems.</span>',pause:60},
                    {text:'', pause:30},
                    {text:'<span class="dev-line-key">STATUS:</span> <span class="dev-line-out">building</span>',pause:40},
                    {text:'<span class="dev-line-key">MODE:</span> <span class="dev-line-out">focused</span>',pause:0}
                ], function () { addCursor(); resetIdle(); });
            },
            skills: function () {
                typeLines([
                    {text:'<span class="dev-line-out">React &bull; Node.js &bull; Python &bull; AI/ML</span>',pause:40},
                    {text:'<span class="dev-line-out">APIs &bull; WebRTC &bull; PostgreSQL &bull; MongoDB</span>',pause:40},
                    {text:'<span class="dev-line-out">Docker &bull; Git &bull; Linux &bull; Systems Design</span>',pause:0}
                ], function () { addCursor(); resetIdle(); });
            },
            projects: function () {
                addLine('<span class="dev-line-out">Opening deployed systems...</span>');
                setTimeout(function () {
                    closeConsole();
                    setTimeout(function () { var el = document.getElementById('projects'); if (el) el.scrollIntoView({behavior:'smooth'}); }, 250);
                }, 600);
            },
            contact: function () {
                typeLines([
                    {text:'<span class="dev-line-key">EMAIL:</span> <span class="dev-line-out"><a href="mailto:jeevan.charu06@gmail.com" style="color:#FBFF48;text-decoration:underline;">jeevan.charu06@gmail.com</a></span>',pause:40},
                    {text:'<span class="dev-line-key">STATUS:</span> <span class="dev-line-out">Available for opportunities</span>',pause:0}
                ], function () { addCursor(); resetIdle(); });
            },
            exit: closeConsole
        };
        cmdBtns.forEach(function (btn) {
            btn.addEventListener('click', function () {
                var cmd = btn.getAttribute('data-cmd');
                removeCursor(); resetIdle();
                clickCount++; clearTimeout(clickTimer);
                clickTimer = setTimeout(function () { clickCount = 0; }, 800);
                if (clickCount >= 4) {
                    clickCount = 0;
                    addLine('<span class="dev-line-prompt">&#10095; </span><span class="dev-line-cmd">' + cmd + '</span>');
                    addLine('<span class="dev-line-err">slow down, system processing...</span>');
                    addCursor(); return;
                }
                if (!commands[cmd]) {
                    addLine('<span class="dev-line-prompt">&#10095; </span><span class="dev-line-cmd">' + cmd + '</span>');
                    addLine('<span class="dev-line-err">invalid command</span>'); addCursor(); return;
                }
                if (cmd !== 'exit') addLine('<span class="dev-line-prompt">&#10095; </span><span class="dev-line-cmd">' + cmd + '</span>');
                commands[cmd]();
            });
        });
    })();
    </script>
    <!-- ===== END DEV MODE JS ===== -->
"""

# ============================================================
# 10. LOG CARD EXPAND JS
# ============================================================
LOG_JS = """
    <!-- ===== LOG CARD JS ===== -->
    <script>
    (function () {
        var LOG_CONTENT = {
            'LOG_001': "Most AI apps fail not because of bad models, but because of weak product thinking.",
            'LOG_002': "If it doesn't work in real-time, it's not ready for users.",
            'LOG_003': "Shipping something imperfect beats designing something perfect forever.",
            'LOG_004': "Latency is a UX problem, not just a backend problem.",
            'LOG_005': "AI is easy to demo. Hard to ship reliably.",
            'LOG_006': "I don't just build apps. I build systems that run them.",
            'LOG_007': "If it's not deployed, it doesn't exist."
        };
        // Create overlay dynamically
        var overlay = document.createElement('div');
        overlay.id = 'log-expand-overlay';
        overlay.style.cssText = 'display:none;position:fixed;inset:0;z-index:8000;align-items:center;justify-content:center;background:rgba(0,0,0,0.75);';
        overlay.innerHTML = '<div style="background:#0a0a0a;border:4px solid rgba(255,255,255,0.15);padding:40px 48px;min-width:320px;max-width:560px;box-shadow:8px 8px 0 #33FF57;font-family:JetBrains Mono,monospace;">'
            + '<div id="log-expand-label" style="color:#33FF57;font-size:0.75rem;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:16px;"></div>'
            + '<p id="log-expand-text" style="color:rgba(255,255,255,0.9);font-size:1.1rem;font-weight:700;line-height:1.6;"></p>'
            + '<button onclick="document.getElementById(\'log-expand-overlay\').style.display=\'none\'" style="margin-top:24px;font-family:JetBrains Mono,monospace;font-size:0.75rem;font-weight:700;color:rgba(255,255,255,0.5);border:1px solid rgba(255,255,255,0.2);padding:6px 18px;background:transparent;cursor:pointer;letter-spacing:0.1em;">[ CLOSE ]</button>'
            + '</div>';
        document.body.appendChild(overlay);
        overlay.addEventListener('click', function (e) { if (e.target === overlay) overlay.style.display = 'none'; });
        document.querySelectorAll('.thought-card').forEach(function (card) {
            card.addEventListener('click', function () {
                var id = card.getAttribute('data-log');
                document.getElementById('log-expand-label').textContent = 'reading ' + id + '...';
                document.getElementById('log-expand-text').textContent = LOG_CONTENT[id] || '';
                overlay.style.display = 'flex';
            });
        });
    })();
    </script>
    <!-- ===== END LOG CARD JS ===== -->
</body>"""

h = h.replace('</body>', SPLASH_JS + DEV_JS + LOG_JS)

# ============================================================
# WRITE OUTPUT
# ============================================================
with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(h)

print(f'Done. {len(h)} chars, {h.count("Arham")} remaining Arham refs')
# Quick check
import re as _re
broken_sample = _re.findall(r'[Ã¢â‚¬â„¢â€™]+', h[:5000])
print('Encoding check (should be empty):', broken_sample[:3])
