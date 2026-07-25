# X-FEED 2026-07-25 part 4/14 | items: 5

## @emollick (продолжение)

T=2080709278441033746 | @emollick | 2026-07-24T17:38+00:00 | L731 RT31 C19 V82052 | thread(2)
URL=https://x.com/emollick/status/2080709278441033746
TEXT: I had access to Opus 5 before release and found it to be a good model if a quirky one. On shorter tasks, it could match or beat Fable levels of performance, at longer tasks it seemed less ambitious &amp; would not deliver as complete a set of work.

Here is its neo-gothic shader. https://t.co/FvhUXkYR2V
[->] Shader: 

// ===========================================================================
//  DROWNED CHOIR  ·  mk II
//  an endless neo-gothic city sunk in a storm sea, with the flooded nave
//  of arches you drift down
//
//  https://t.co/oirnILHfXn  ▸  set mode to "classic"  ▸  paste this whole file
//  drag the mouse to look around; everything else drives itself
//
//  knobs:  WAVEA  swell height        STEPS  quality / framerate
//          ARCHP  arch frequency      LODD   distance detail cuts out
// ===========================================================================
precision highp float;

uniform vec2  resolution;
uniform vec2  mouse;
uniform float time;

#define PI    3.14159265359
#define SEC   0.78539816339        // 45 degrees, the octagon step
#define CELL  30.0                 // city block size
#define WAVEA 5.5                  // swell amplitude
#define FAR   210.0
#define MARG  2.0                  // clearance of geometry from its cell wall
#define STEPS 104
#define LODD  105.0
#define ARCHP 0.40                 // hash threshold: lower = more arches

float T;        // time
float bolt;     // lightning intensity this frame
float boltAz;   // azimuth of this frame's strike
vec3  RO;       // camera, for distance based detail
const vec3 SUN = vec3(0.3366, 0.0865, 0.9377);

/* ------------------------------------------------- hash / noise ---------- */
float h11(float n){ return fract(sin(n*91.3458)*43758.5453); }
float h21(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7)))*43758.5453); }

float vn(vec2 p){
  vec2 i = floor(p), f = fract(p);
  f = f*f*(3.0 - 2.0*f);
  return mix(mix(h21(i),                h21(i + vec2(1.0, 0.0)), f.x),
             mix(h21(i + vec2(0.0,1.0)), h21(i + vec2(1.0, 1.0)), f.x), f.y);
}
float fbm(vec2 p){
  float s = 0.0, a = 0.5;
  mat2 m = mat2(0.8, 0.6, -0.6, 0.8);
  for(int i = 0; i < 4; i++){ s += a*vn(p); p = m*p*2.03; a *= 0.5; }
  return s;
}

/* ------------------------------------------------- ocean ----------------- */
// coarse field: long smooth swells that sharpen into cusped crests
float seaLo(vec2 p){
  float h = 0.0, a = 1.0, f = 0.055, s = 0.0;
  vec2 d = normalize(vec2(1.0, 0.34));
  mat2 R = mat2(0.54, 0.84, -0.84, 0.54);
  for(int i = 0; i < 5; i++){
    float x  = dot(p, d)*f + T*(0.85 + 2.4*sqrt(f));
    float sw = 0.5 + 0.5*sin(x);              // rolling swell
    float cw = 1.0 - abs(sin(x)); cw *= cw;   // choppy cusp
    h += (mix(sw, cw, float(i)*0.25) - 0.42)*a;
    s += a;
    a *= 0.56; f *= 2.13; d = R*d; p += d*9.0;
  }
  return h/s*WAVEA;
}
// detail field: only sampled at the hit point, for normals and foam
float seaHi(vec2 p){
  float h = seaLo(p), a = 0.55, f = 1.6;
  vec2 d = normalize(vec2(-0.42, 1.0));
  mat2 R = mat2(0.71, 0.70, -0.70, 0.71);
  for(int i = 0; i < 4; i++){
    float x = dot(p, d)*f + T*(1.3 + 2.0*sqrt(f)) + vn(p*f*0.4)*2.6;
    float w = 1.0 - abs(sin(x)); w *= w;
    h += (w - 0.4)*a;
    a *= 0.55; f *= 2.06; d = R*d;
  }
  return h;
}

/* ------------------------------------------------- the city -------------- */
// octagon support function: level sets are regular octagons, dirt cheap
float oct2(vec2 p){ p = abs(p); return max(max(p.x, p.y), (p.x + p.y)*0.7071068); }

// three populations: drowned stumps, mid towers, cathedral spires
float cellH(vec2 id){
  float a = h21(id + 0.17);
  float b = h21(id.yx*1.71 + 4.13);
  return mix(mix(-4.0 + 10.0*b, 12.0 + 24.0*b, step(0.30, a)),
             32.0 + 48.0*b, step(0.78, a));
}
void cellInfo(vec2 xz, out vec2 id, out vec3 par, out vec2 off){
  id = floor(xz/CELL);
  float b = h21(id.yx*1.71 + 4.13);
  float c = h21(id*3.07 - 2.31);
  float sp = (0.30 + 0.55*c)*step(0.22, h21(id*7.7 + 1.3));  // some snapped off
  par = vec3(cellH(id), 2.2 + 1.3*c, sp);
  off = (vec2(b, c) - 0.5)*0.7;
}

float tower(vec3 q, float H, float rad, float spr, float lod){
  float y   = q.y;
  vec2  qe  = q.xz + vec2(1e-4, 1e-4);
  float rho = oct2(q.xz);
  float ty  = clamp(y/H, 0.0, 1.0);
  float r   = rad*(1.0 - 0.5*ty) + 0.9*exp(-max(y + 3.0, 0.0)*0.45);  // taper + flared base

  float d = max(rho - r, y - H);                       // tapered octagonal shaft

  float L  = length(qe);
  float aa = atan(qe.y, qe.x);
  float ac = mod(aa, SEC) - SEC*0.5;                   // fold onto the corners
  vec2  fc = vec2(cos(ac), sin(ac))*L;
  float rt = rad*0.5;

  // pilasters running the full height at each corner
  d = min(d, max(length(vec2(fc.x - r*1.02, fc.y)) - 0.30, y - (H + 1.4)));

  // cornice under the top platform
  d = min(d, max(rho - (rt + 0.75), abs(y - H) - 0.38));

  // spire: octagonal pyramid as a max of slanted planes
  float sh = rad*(3.0 + 5.0*spr) + 5.0;
  float st = rt*0.7;
  float sd = max((rho*sh + (y - H)*st - st*sh)*inversesqrt(sh*sh + st*st), H - 0.3 - y);
  d = min(d, sd + 1000.0*step(spr, 0.02));

  if(lod > 0.5){
    // buttress fins wading down into the water
    float fin = max(abs(fc.y) - 0.34, fc.x - rad*2.5);
    fin = max(fin, y - (H*0.42 - (fc.x - rad)*3.2));
    fin = max(fin, rad*0.55 - fc.x);
    d = min(d, fin);

    // blind arcading: slender ribs up every face
    float af = mod(aa + SEC*0.5, SEC) - SEC*0.5;
    float fr = mod(af*L, 1.7) - 0.85;
    d = min(d, max(max(abs(fr) - 0.20, rho - (r + 0.22)),
                   max(y - (H - 0.6), r - 0.3 - rho)));

    // cornice bands
    d = min(d, max(rho - (rad*0.86 + 0.55), abs(y - H*0.30) - 0.30));
    d = min(d, max(rho - (rad*0.70 + 0.48), abs(y - H*0.62) - 0.28));

    // pinnacles ringing the top cornice
    float u = fc.x - (rt + 0.62), v = fc.y, w = y - H;
    float pr = 0.40*(1.0 - clamp(w/3.2, 0.0, 1.0));
    d = min(d, max(max(abs(u), abs(v)) - pr …[обрезано — полный текст по ссылке]
QUOTED @emollick: Fable: "create a visually interesting shader that can run in twigl-dot-app make it like an infinite city of neo-gothic towers partially drowned in a stormy ocean with large waves." "Make it better"

All of this is procedurally generated. https://t.co/ky0q5ho643
LINKS: http://twigl.app ; http://k.xxx
--
T=2080713231937552394 | @emollick | 2026-07-24T17:54+00:00 | L603 RT20 C17 V61199 | thread(2)
URL=https://x.com/emollick/status/2080713231937552394
TEXT: Opus 5 replaced Opus 4.8 for me, it was generally stronger in everything... except it shares some of the weird language quirks of Fable, including a love of density and FableSpeak.

I had it make a game where you build railroads in knock-off Middle Earth: https://t.co/LANn3xLBi8 https://t.co/d0dUwb0Ru7
[->] Here's the game code, MIT license if you want to edit or change anything: https://t.co/tHIUxceWLP
LINKS: https://perilous-ways.netlify.app/ ; https://github.com/emollick/perilous-ways
--
T=2080731915196194981 | @emollick | 2026-07-24T19:08+00:00 | L285 RT5 C11 V22186 | post
URL=https://x.com/emollick/status/2080731915196194981
TEXT: This is a big jump in ARC-AGI-3.
QUOTED @arcprize: Claude Opus 5 from @AnthropicAI is the new SOTA on ARC-AGI-3: 30.2%

The previous high score (7.8%) was set by GPT-5.6 Sol (Max)

Throughout our analysis, we observed novel behavior that allows Opus 5 to solve previously unbeaten environments, outperforming Fable https://t.co/Dg3uOTIgCg
--
T=2080829512275624173 | @emollick | 2026-07-25T01:36+00:00 | L137 RT2 C16 V13018 | post
URL=https://x.com/emollick/status/2080829512275624173
TEXT: Has Claude stopped showing full summarized thinking traces? See this before &amp; after

If so, it is actually a big loss, both for interpretability (seeing even a summarized thinking trace helps you diagnose errors in a way that you can't otherwise) and because they were insightful https://t.co/2yt8gxKTyt
--
T=2080876002444496942 | @emollick | 2026-07-25T04:41+00:00 | L36 RT0 C4 V7404 | post
URL=https://x.com/emollick/status/2080876002444496942
TEXT: Ha! It did it: "We introduce BenchBenchBenchBenchBench (BBBBB), an executable benchmark of AI-authored conformance suites for benchmark-evaluation metrics"

I really thought it would treat "now do benchbenchbenchbenchbench" as a joke, but Sol actually did reasonable experiments. https://t.co/LgVnxC8o2n
QUOTED @emollick: As a joke I prompted Codex "Build and run BenchBench, a benchmark of now good ai is at creating benchmarks. then figure out what benchbenchbench is and run that. and then write benchbenchbench up as a good arXiv paper." I got a PDF.

But the paper is actually kind of interesting? https://t.co/yIIEvBxGw7
--
