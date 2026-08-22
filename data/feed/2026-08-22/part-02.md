# X-FEED 2026-08-22 part 2/8 | items: 4

## @emollick — 4 шт.

T=2090683545068978254 | @emollick | 2026-08-21T06:12+00:00 | L1450 RT74 C79 V245951 | post
URL=https://x.com/emollick/status/2090683545068978254
TEXT: I asked GPT-5.6 Sol to create the most Claude-y possible parody image and what it came up with is pretty great and dead-on. https://t.co/h1X4txvELC
--
T=2090867191511986622 | @emollick | 2026-08-21T18:22+00:00 | L788 RT27 C55 V130647 | post
URL=https://x.com/emollick/status/2090867191511986622
TEXT: Now, back to Claude Fable 5: "I asked GPT-5.6 Sol to create the most Claude-y possible parody image and it came up with this. Come out fighting." https://t.co/x7HygtTdCA
QUOTED @emollick: I asked GPT-5.6 Sol to create the most Claude-y possible parody image and what it came up with is pretty great and dead-on. https://t.co/h1X4txvELC
--
T=2090926132790985153 | @emollick | 2026-08-21T22:16+00:00 | L474 RT39 C54 V19028 | post
URL=https://x.com/emollick/status/2090926132790985153
TEXT: Its going to be an era of contradictions.

Polls will show everyone hates AI overall but also everyone will secretly use AI all the time. AI companies will be underwater in public opinion but also many people will feel strongly attached to their own favorite model &amp; care about it
--
T=2091001394534707474 | @emollick | 2026-08-22T03:15+00:00 | L15 RT0 C2 V3662 | thread(2)
URL=https://x.com/emollick/status/2091001394534707474
TEXT: Fable: "I want a twigl shader that renders Lost Carcosa from The King in Yellow."

(Shaders are procedurally generated using math alone)
https://t.co/ARC8ZhygTi

Along the shore the cloud waves break,
The twin suns sink behind the lake,
The shadows lengthen
        In Carcosa
[->] Along the shore the cloud waves break,
The twin suns sink behind the lake,
The shadows lengthen
        In Carcosa.
Strange is the night where black stars rise,
And strange moons circle through the skies
But stranger still is
        Lost Carcosa.
Songs that the Hyades shall sing,
Where flap the tatters of the King,
Must die unheard in
        Dim Carcosa.
Song of my soul, my voice is dead;
Die thou, unsung, as tears unshed
Shall dry and die in
        Lost Carcosa.

// LOST CARCOSA — https://t.co/oirnILHfXn, mode: classic (WebGL 1.0)
// Along the shore the cloud waves break. Twin suns sink behind Lake Hali.
// Black stars rise. Strange moons circle. The towers are also beneath the water.

precision highp float;
uniform vec2 resolution;
uniform float time;

#define T time

vec3 SA, SB, M1, M2; // twin suns, two moons
float CX, GL, GK;    // camera sway, the glance, which glance

float hash(vec2 p){ p=fract(p*vec2(127.1,311.7)); p+=dot(p,p+19.19); return fract(p.x*p.y); }
float noise(vec2 p){
  vec2 i=floor(p), f=fract(p); f=f*f*(3.-2.*f);
  return mix(mix(hash(i),hash(i+vec2(1,0)),f.x), mix(hash(i+vec2(0,1)),hash(i+1.),f.x), f.y);
}
float fbm(vec2 p){ float a=.5,s=0.; for(int i=0;i<4;i++){ s+=a*noise(p); p=mat2(1.6,1.2,-1.2,1.6)*p+5.2; a*=.5; } return s; }
float fbm2(vec2 p){ float a=.5,s=0.; for(int i=0;i<2;i++){ s+=a*noise(p); p=mat2(1.6,1.2,-1.2,1.6)*p+5.2; a*=.5; } return s; }

// fog is sulfur toward the suns, bruise-violet elsewhere
vec3 fogColor(vec3 rd){
  float s=max(dot(normalize(vec3(rd.x,0.,rd.z)), normalize(vec3(SA.x,0.,SA.z))),0.);
  return mix(vec3(.20,.11,.19), vec3(.78,.46,.13), pow(s,3.));
}

vec3 skyBase(vec3 rd){
  float el=rd.y;
  vec3 c=mix(vec3(.72,.46,.13), vec3(.36,.31,.11), smoothstep(-.05,.13,el));
  c=mix(c, vec3(.07,.04,.11), smoothstep(.06,.48,el));
  // a faint luminous haze, so the black stars have something to be holes in
  float az=atan(rd.x,rd.z);
  float neb=fbm(vec2(az*2.5,el*5.)+vec2(T*.004,0.));
  c+=vec3(.13,.07,.18)*neb*smoothstep(.04,.35,el);
  // tatters: ragged yellow streamers dragged across the upper sky
  float tat=fbm(vec2(az*5.+T*.012, el*16.+T*.004));
  c=mix(c, vec3(.72,.58,.16), smoothstep(.56,.82,tat)*.35*smoothstep(.14,.32,el)*smoothstep(.75,.45,el));
  return c;
}

// stars as absences: dark cores with a pale rim
vec3 blackStars(vec3 c, vec3 rd){
  vec2 sp=vec2(atan(rd.x,rd.z)+T*.005, asin(clamp(rd.y,-1.,1.))-T*.0025);
  vec2 g=sp*15.;
  vec2 id=floor(g), f=fract(g)-.5;
  float h=hash(id);
  vec2 o=(vec2(hash(id+3.1),hash(id+7.7))-.5)*.6;
  float d=length(f-o);
  float r=.05+.1*hash(id+1.3);
  float vis=step(.58,h)*smoothstep(.03,.22,rd.y)*(.8+.2*sin(T*.4+h*50.));
  float core=smoothstep(r,r*.5,d);
  float ring=exp(-pow((d-r)/(r*.35),2.));
  c*=1.-core*vis*.97;
  c+=ring*vis*vec3(.55,.5,.75)*.2;
  return c;
}

vec3 hyades(vec3 rd){
  vec3 hc=normalize(vec3(.62, .22+.003*T, 1.));
  vec3 c=vec3(0.);
  for(int i=0;i<9;i++){
    float fi=float(i);
    vec3 sd=normalize(hc+vec3(hash(vec2(fi,1.))-.5, (hash(vec2(fi,2.))-.5)*.6, 0.)*.14);
    float d=length(rd-sd);
    float tw=.7+.3*sin(T*1.3+fi*5.);
    vec3 col = i==0 ? vec3(1.,.35,.2) : vec3(.95,.92,.85);
    c+=col*exp(-d*d*9.e4)*tw*(.6+.6*hash(vec2(fi,3.)));
  }
  return c*smoothstep(-.02,.06,rd.y);
}

vec3 suns(vec3 rd){
  float a=length(rd-SA), b=length(rd-SB);
  vec3 c=vec3(1.,.32,.07)*exp(-a*5.5)*.5;       // swollen red glow
  c+=vec3(1.,.85,.55)*exp(-b*11.)*.4;            // small white glow
  float dA=smoothstep(.074,.068,a);
  float dB=smoothstep(.033,.029,b);
  c+=vec3(1.2,.32,.05)*dA*(1.-.55*smoothstep(.035,.074,a)); // limb-darkened
  c+=vec3(1.5,1.3,1.)*dB;
  return c;
}

vec3 moon(vec3 c, vec3 rd, vec3 md, float r, vec3 col, vec2 ph){
  float d=length(rd-md);
  float disc=smoothstep(r,r-.004,d);
  float dark=smoothstep(r*1.03,r*1.03-.004,length(rd-md-vec3(ph*r,0.)));
  float mot=.78+.4*fbm2((rd.xy-md.xy)*45.+vec2(3.,1.));
  vec3 mc=col*mot*(1.-dark*.9);
  c=mix(c,mc,disc);
  c+=col*exp(-d*25.)*.12;
  return c;
}

// skyline height as a function of azimuth: tiered bases, domes, spires
float towers(float az, float sc, float seed, float hmul, float dens){
  float x=az*sc+seed*7.31;
  float id=floor(x), f=fract(x)-.5;
  float h1=hash(vec2(id,seed)), h2=hash(vec2(id*1.7,seed+4.2)), h3=hash(vec2(id*.3,seed+9.1)), h4=hash(vec2(id*2.3,seed+1.7));
  float w=.3+.55*h2;
  float hh=(.004+.10*pow(h1,2.))*hmul*step(1.-dens,h3);
  float r=abs(f)/(w*.5);
  float base =hh*.5*smoothstep(1.,.95,r);
  float upper=hh*.35*smoothstep(.6,.55,r);
  float third=hh*.15*smoothstep(.32,.28,r);
  float dome =hh*.3*sqrt(max(0.,1.-r*r/.36))*step(.45,h4);
  float spire=hh*.7*smoothstep(.09,.05,abs(r-(h4-.5)*.4))*step(h4,.45);
  return base+upper+third+dome+spire;
}

vec2 king(float az, float el){
  float ka=-.75+1.5*hash(vec2(GK,13.));
  float x=az-ka;
  float H=.27+.06*hash(vec2(GK,5.));
  float u=clamp(el/H,0.,1.);
  float w=mix(.05,.034,u);                                   // a column of robe
  w+=.02*(1.-u)*fbm(vec2(el*50.,GK*3.));                     // ragged edge
  w=mix(w,.006,smoothstep(.84,.9,u));                        // neck
  float robe=smoothstep(w+.003,w-.003,abs(x))*step(el,H*.9)*step(0.,el);
  float holes=smoothstep(.5,.62,fbm(vec2(x*70.+GK*7.,el*5.)))*pow(1.-u,2.)*1.4;  // tatters hang open
  robe*=clamp(1.-holes,0.,1.);
  float head=smoothstep(.017,.014,length(vec2(x,el-H*.92)*vec2(1.,1.15)));
  return vec2(robe,head);
}

// everything at infinity. seed>0 means we are looking into the lake.
vec3 scene(vec3 rd, float seed){
  vec3 c=skyBase(rd);
  c=blackStars(c,rd);
  c+=suns(rd);
  c+=hyades(rd);
  c=moon(c,rd,M1,.045,vec3(.72,.78,.6),vec2(.45,.15));
  float az=atan(rd.x,rd.z), el=rd.y;
  vec3 fc=fogColor(r …[обрезано — полный текст по ссылке]
LINKS: https://twigl.app?ol=true&ss=-P-bSSQZADUyG4yjrpbB ; http://twigl.app
--
