# stream_replace.ps1 — replaces reports section with horizontal scroll stream
$file = 'index.html'
$lines = Get-Content $file -Raw

# ---- new section HTML ----
$newSection = @'
    <section id="reports" class="py-20 bg-neo-black border-t-4 border-black overflow-hidden relative">

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
        <div class="pointer-events-none absolute inset-y-0 left-0 w-24 z-10"
             style="background:linear-gradient(to right,#0a0a0a 0%,transparent 100%);"></div>
        <div class="pointer-events-none absolute inset-y-0 right-0 w-24 z-10"
             style="background:linear-gradient(to left,#0a0a0a 0%,transparent 100%);"></div>

        <!-- ROW 1 — speed 32s, left→right -->
        <div class="thought-row mb-0 border-t border-white/10" data-dir="ltr" data-speed="32">
            <div class="thought-track flex items-center gap-0 py-4" style="animation:thought-ltr 32s linear infinite;">
                <!-- set A -->
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_001">
                    <span class="text-[#FF2D78] font-bold mr-2">LOG_001</span><span class="text-[#FF2D78]/60 mr-3 text-xs font-bold border border-[#FF2D78]/30 px-1">[AI]</span><span>Most AI apps fail not because of bad models, but because of weak product thinking.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_003">
                    <span class="text-[#F97316] font-bold mr-2">LOG_003</span><span class="text-[#F97316]/60 mr-3 text-xs font-bold border border-[#F97316]/30 px-1">[PRODUCT]</span><span>Shipping something imperfect beats designing something perfect forever.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_005">
                    <span class="text-[#FF2D78] font-bold mr-2">LOG_005</span><span class="text-[#FF2D78]/60 mr-3 text-xs font-bold border border-[#FF2D78]/30 px-1">[AI]</span><span>AI is easy to demo. Hard to ship reliably.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_006">
                    <span class="text-[#F97316] font-bold mr-2">LOG_006</span><span class="text-[#F97316]/60 mr-3 text-xs font-bold border border-[#F97316]/30 px-1">[PRODUCT]</span><span>I don't just build apps. I build systems that run them.</span>
                </span>
                <!-- set B (seamless duplicate) -->
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_001">
                    <span class="text-[#FF2D78] font-bold mr-2">LOG_001</span><span class="text-[#FF2D78]/60 mr-3 text-xs font-bold border border-[#FF2D78]/30 px-1">[AI]</span><span>Most AI apps fail not because of bad models, but because of weak product thinking.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_003">
                    <span class="text-[#F97316] font-bold mr-2">LOG_003</span><span class="text-[#F97316]/60 mr-3 text-xs font-bold border border-[#F97316]/30 px-1">[PRODUCT]</span><span>Shipping something imperfect beats designing something perfect forever.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_005">
                    <span class="text-[#FF2D78] font-bold mr-2">LOG_005</span><span class="text-[#FF2D78]/60 mr-3 text-xs font-bold border border-[#FF2D78]/30 px-1">[AI]</span><span>AI is easy to demo. Hard to ship reliably.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_006">
                    <span class="text-[#F97316] font-bold mr-2">LOG_006</span><span class="text-[#F97316]/60 mr-3 text-xs font-bold border border-[#F97316]/30 px-1">[PRODUCT]</span><span>I don't just build apps. I build systems that run them.</span>
                </span>
            </div>
        </div>

        <!-- ROW 2 — speed 46s, right→left, different thoughts -->
        <div class="thought-row mb-0 border-t border-white/10" data-dir="rtl" data-speed="46">
            <div class="thought-track flex items-center gap-0 py-4" style="animation:thought-rtl 46s linear infinite;">
                <!-- set A -->
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_002">
                    <span class="text-[#A855F7] font-bold mr-2">LOG_002</span><span class="text-[#A855F7]/60 mr-3 text-xs font-bold border border-[#A855F7]/30 px-1">[SYSTEMS]</span><span>If it doesn't work in real-time, it's not ready for users.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_004">
                    <span class="text-[#A855F7] font-bold mr-2">LOG_004</span><span class="text-[#A855F7]/60 mr-3 text-xs font-bold border border-[#A855F7]/30 px-1">[SYSTEMS]</span><span>Latency is a UX problem, not just a backend problem.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_007">
                    <span class="text-[#33FF57] font-bold mr-2">LOG_007</span><span class="text-[#33FF57]/60 mr-3 text-xs font-bold border border-[#33FF57]/30 px-1">[SYSTEMS]</span><span>If it's not deployed, it doesn't exist.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_001">
                    <span class="text-[#FF2D78] font-bold mr-2">LOG_001</span><span class="text-[#FF2D78]/60 mr-3 text-xs font-bold border border-[#FF2D78]/30 px-1">[AI]</span><span>Most AI apps fail not because of bad models, but because of weak product thinking.</span>
                </span>
                <!-- set B -->
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_002">
                    <span class="text-[#A855F7] font-bold mr-2">LOG_002</span><span class="text-[#A855F7]/60 mr-3 text-xs font-bold border border-[#A855F7]/30 px-1">[SYSTEMS]</span><span>If it doesn't work in real-time, it's not ready for users.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_004">
                    <span class="text-[#A855F7] font-bold mr-2">LOG_004</span><span class="text-[#A855F7]/60 mr-3 text-xs font-bold border border-[#A855F7]/30 px-1">[SYSTEMS]</span><span>Latency is a UX problem, not just a backend problem.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_007">
                    <span class="text-[#33FF57] font-bold mr-2">LOG_007</span><span class="text-[#33FF57]/60 mr-3 text-xs font-bold border border-[#33FF57]/30 px-1">[SYSTEMS]</span><span>If it's not deployed, it doesn't exist.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_001">
                    <span class="text-[#FF2D78] font-bold mr-2">LOG_001</span><span class="text-[#FF2D78]/60 mr-3 text-xs font-bold border border-[#FF2D78]/30 px-1">[AI]</span><span>Most AI apps fail not because of bad models, but because of weak product thinking.</span>
                </span>
            </div>
        </div>

        <!-- ROW 3 — speed 24s, left→right, fastest -->
        <div class="thought-row border-t border-b border-white/10" data-dir="ltr" data-speed="24">
            <div class="thought-track flex items-center gap-0 py-4" style="animation:thought-ltr 24s linear infinite;">
                <!-- set A -->
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_005">
                    <span class="text-[#FF2D78] font-bold mr-2">LOG_005</span><span class="text-[#FF2D78]/60 mr-3 text-xs font-bold border border-[#FF2D78]/30 px-1">[AI]</span><span>AI is easy to demo. Hard to ship reliably.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_006">
                    <span class="text-[#F97316] font-bold mr-2">LOG_006</span><span class="text-[#F97316]/60 mr-3 text-xs font-bold border border-[#F97316]/30 px-1">[PRODUCT]</span><span>I don't just build apps. I build systems that run them.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_007">
                    <span class="text-[#33FF57] font-bold mr-2">LOG_007</span><span class="text-[#33FF57]/60 mr-3 text-xs font-bold border border-[#33FF57]/30 px-1">[SYSTEMS]</span><span>If it's not deployed, it doesn't exist.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_003">
                    <span class="text-[#F97316] font-bold mr-2">LOG_003</span><span class="text-[#F97316]/60 mr-3 text-xs font-bold border border-[#F97316]/30 px-1">[PRODUCT]</span><span>Shipping something imperfect beats designing something perfect forever.</span>
                </span>
                <!-- set B -->
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_005">
                    <span class="text-[#FF2D78] font-bold mr-2">LOG_005</span><span class="text-[#FF2D78]/60 mr-3 text-xs font-bold border border-[#FF2D78]/30 px-1">[AI]</span><span>AI is easy to demo. Hard to ship reliably.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_006">
                    <span class="text-[#F97316] font-bold mr-2">LOG_006</span><span class="text-[#F97316]/60 mr-3 text-xs font-bold border border-[#F97316]/30 px-1">[PRODUCT]</span><span>I don't just build apps. I build systems that run them.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_007">
                    <span class="text-[#33FF57] font-bold mr-2">LOG_007</span><span class="text-[#33FF57]/60 mr-3 text-xs font-bold border border-[#33FF57]/30 px-1">[SYSTEMS]</span><span>If it's not deployed, it doesn't exist.</span>
                </span>
                <span class="thought-item font-mono text-sm whitespace-nowrap px-8 text-white/80 border-r border-white/10 cursor-none"
                      data-log="LOG_003">
                    <span class="text-[#F97316] font-bold mr-2">LOG_003</span><span class="text-[#F97316]/60 mr-3 text-xs font-bold border border-[#F97316]/30 px-1">[PRODUCT]</span><span>Shipping something imperfect beats designing something perfect forever.</span>
                </span>
            </div>
        </div>

    </section>
'@

# ---- CSS to inject (before </style>) ----
$streamCss = @'

        /* ===== SYSTEM_THOUGHTS STREAM ===== */
        @keyframes thought-ltr {
            0%   { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        @keyframes thought-rtl {
            0%   { transform: translateX(-50%); }
            100% { transform: translateX(0); }
        }
        .thought-row { overflow: hidden; }
        .thought-track { will-change: transform; width: max-content; }
        .thought-row:hover .thought-track { animation-play-state: paused; }
        .thought-item {
            display: inline-flex; align-items: center;
            transition: opacity 0.12s, background 0.12s;
        }
        .thought-item:hover {
            opacity: 1 !important;
            background: rgba(255,255,255,0.04);
            outline: 1px solid rgba(255,255,255,0.08);
        }
        .thought-row:not(:hover) .thought-item { opacity: 0.7; }
'@

# Replace CSS placeholder
$lines_new = $lines -replace '(?s)(\/\* ===== DEV MODE STYLES)', "$streamCss`r`n        `$1"

# Replace the section
$lines_new = $lines_new -replace '(?s)(\s*<section id="reports".*?</section>)', "`n$newSection"

Set-Content $file -Value $lines_new -Encoding UTF8
Write-Host "Done. File size: $((Get-Item $file).Length) bytes"
