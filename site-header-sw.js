const CACHE_BUST = 'ts-global-header-v1';

const css = `
.ts-topbar,.ts-header{font-family:Inter,Arial,Helvetica,sans-serif}.ts-topbar{background:#070707;color:#fff;font-size:12px}.ts-topbar *,.ts-header *{box-sizing:border-box}.ts-wrap{width:min(1280px,calc(100% - 64px));margin:0 auto}.ts-topbar .ts-wrap{display:flex;justify-content:space-between;align-items:center;gap:22px;min-height:45px}.ts-top-items{display:flex;gap:48px;align-items:center;flex-wrap:wrap}.ts-top-item{display:flex;align-items:center;gap:10px;color:#e8e8e8}.ts-top-ico{color:#e1111a;font-weight:900}.ts-langs{display:flex;gap:10px;align-items:center;color:#f2f2f2}.ts-header{background:#fff;box-shadow:0 8px 30px rgba(0,0,0,.08);position:sticky;top:0;z-index:9999}.ts-header .ts-wrap{height:108px;display:flex;align-items:center;justify-content:space-between;gap:28px}.ts-logo{text-decoration:none;color:#111;line-height:.9;font-weight:900;font-size:34px;letter-spacing:-1.2px;flex:0 0 auto}.ts-logo span{color:#e1111a}.ts-logo small{display:block;margin-top:10px;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:#111;font-weight:700}.ts-nav{display:flex;align-items:center;gap:28px;font-weight:800;font-size:12px;text-transform:uppercase}.ts-nav-item{position:relative}.ts-nav-trigger{display:inline-flex;align-items:center;gap:8px;padding:42px 0;color:#111;text-decoration:none;cursor:pointer}.ts-nav-trigger::after{content:'⌄';font-size:12px}.ts-dropdown{position:absolute;top:100%;left:-22px;min-width:250px;background:#fff;border:1px solid rgba(17,17,17,.08);border-radius:0 0 12px 12px;box-shadow:0 26px 60px rgba(0,0,0,.16);padding:12px 0;opacity:0;visibility:hidden;transform:translateY(12px);transition:opacity .18s ease,transform .18s ease,visibility .18s ease;z-index:100;text-transform:none}.ts-nav-item:hover .ts-dropdown,.ts-nav-item:focus-within .ts-dropdown{opacity:1;visibility:visible;transform:translateY(0)}.ts-dropdown a{display:block;padding:11px 22px;font-size:13px;font-weight:750;line-height:1.25;color:#1d1d1d!important;text-decoration:none!important;white-space:nowrap}.ts-dropdown a:hover{background:#f7f7f7;color:#e1111a!important}.ts-dropdown.ts-wide{min-width:560px;display:grid;grid-template-columns:1fr 1fr;padding:12px}.ts-dropdown.ts-wide a{border-radius:6px}.ts-dropdown.ts-services{min-width:520px;grid-template-columns:1fr 1fr}.ts-btn{display:inline-flex;align-items:center;gap:12px;background:#e1111a;color:#fff!important;text-decoration:none!important;font-weight:900;text-transform:uppercase;border-radius:4px;padding:18px 26px;font-size:12px;letter-spacing:.02em;box-shadow:0 14px 26px rgba(225,17,26,.26)}@media(max-width:1180px){.ts-nav{gap:18px}.ts-nav-trigger{font-size:11px}.ts-dropdown.ts-wide,.ts-dropdown.ts-services{min-width:460px}}@media(max-width:1100px){.ts-nav{display:none}.ts-header .ts-wrap{height:auto;padding:22px 0}.ts-wrap{width:min(100% - 32px,1280px)}}@media(max-width:720px){.ts-topbar .ts-wrap{align-items:flex-start;flex-direction:column;padding:12px 0}.ts-top-items{gap:14px}.ts-logo{font-size:28px}}
`;

function p(path) {
  return new URL(path, self.registration.scope).href;
}

function headerHtml() {
  return `
<div class="ts-topbar"><div class="ts-wrap"><div class="ts-top-items"><div class="ts-top-item"><span class="ts-top-ico">✚</span>Swiss Management</div><div class="ts-top-item"><span class="ts-top-ico">▣</span>Factory in Thailand</div><div class="ts-top-item"><span class="ts-top-ico">♡</span>Premium Quality</div><div class="ts-top-item"><span class="ts-top-ico">▱</span>Worldwide Shipping</div></div><div class="ts-langs"><span>DE</span><span>|</span><span>EN</span><span>⌄</span></div></div></div>
<header class="ts-header"><div class="ts-wrap"><a class="ts-logo" href="${p('')}"><strong>TShirt<span>Swiss</span>.ch</strong><small>Swiss-managed apparel manufacturing</small></a><nav class="ts-nav" aria-label="Main navigation"><div class="ts-nav-item"><a class="ts-nav-trigger" href="${p('pages/products/')}">Products</a><div class="ts-dropdown ts-wide"><a href="${p('pages/products/custom-t-shirts/')}">Custom T-Shirts</a><a href="${p('pages/products/custom-polos/')}">Custom Polos</a><a href="${p('pages/products/hoodies-sweatshirts/')}">Hoodies & Sweatshirts</a><a href="${p('pages/products/workwear/')}">Workwear</a><a href="${p('pages/products/corporate-apparel/')}">Corporate Apparel</a><a href="${p('pages/products/private-label-clothing/')}">Private Label Clothing</a><a href="${p('pages/products/sportswear/')}">Sportswear</a><a href="${p('pages/products/rashguards/')}">Rashguards</a><a href="${p('pages/products/mma-shorts/')}">MMA Shorts</a><a href="${p('pages/products/muay-thai-shorts/')}">Muay Thai Shorts</a><a href="${p('pages/products/healthcare-uniforms/')}">Healthcare Uniforms</a><a href="${p('pages/products/medical-scrubs/')}">Medical Scrubs</a><a href="${p('pages/products/caps-headwear/')}">Caps & Headwear</a><a href="${p('pages/products/jackets-softshells/')}">Jackets & Softshells</a><a href="${p('pages/products/tote-bags/')}">Tote Bags</a><a href="${p('pages/products/promotional-merchandise/')}">Promotional Merchandise</a></div></div><div class="ts-nav-item"><a class="ts-nav-trigger" href="${p('pages/industries/')}">Industries</a><div class="ts-dropdown"><a href="${p('pages/industries/construction-trades/')}">Construction & Trades</a><a href="${p('pages/industries/healthcare/')}">Healthcare</a><a href="${p('pages/industries/hospitality/')}">Hospitality</a><a href="${p('pages/industries/sports-fitness/')}">Sports & Fitness</a><a href="${p('pages/industries/combat-sports/')}">Combat Sports</a><a href="${p('pages/industries/corporate-apparel/')}">Corporate Apparel</a><a href="${p('pages/industries/events-merchandise/')}">Events & Merchandise</a><a href="${p('pages/industries/ecommerce-brands/')}">Ecommerce Brands</a><a href="${p('pages/industries/influencers-creator-brands/')}">Influencers & Creator Brands</a></div></div><div class="ts-nav-item"><a class="ts-nav-trigger" href="${p('pages/services/')}">Services</a><div class="ts-dropdown ts-wide ts-services"><a href="${p('pages/services/oem-clothing-production/')}">OEM Clothing Production</a><a href="${p('pages/services/private-label-manufacturing/')}">Private Label Manufacturing</a><a href="${p('pages/services/product-development/')}">Product Development</a><a href="${p('pages/services/sampling/')}">Sampling</a><a href="${p('pages/services/screen-printing/')}">Screen Printing</a><a href="${p('pages/services/embroidery/')}">Embroidery</a><a href="${p('pages/services/sublimation-printing/')}">Sublimation Printing</a><a href="${p('pages/services/heat-transfer-printing/')}">Heat Transfer Printing</a><a href="${p('pages/services/custom-labels/')}">Custom Labels</a><a href="${p('pages/services/hang-tags/')}">Hang Tags</a><a href="${p('pages/services/packaging-solutions/')}">Packaging Solutions</a><a href="${p('pages/services/quality-control/')}">Quality Control</a><a href="${p('pages/services/worldwide-shipping/')}">Worldwide Shipping</a></div></div><div class="ts-nav-item"><a class="ts-nav-trigger" href="${p('pages/about-us/')}">About Us</a><div class="ts-dropdown"><a href="${p('pages/about-us/')}">About Us</a><a href="${p('pages/production/')}">Our Process</a><a href="${p('pages/case-studies/')}">Case Studies</a><a href="${p('pages/contact/')}">Contact Us</a><a href="${p('pages/request-a-quote/')}">Request a Quote</a></div></div><div class="ts-nav-item"><a class="ts-nav-trigger" href="${p('pages/resources/')}">Resources</a><div class="ts-dropdown"><a href="${p('pages/resources/')}">Resources Hub</a><a href="${p('pages/resources/blog/')}">Blog</a><a href="${p('pages/resources/faq/')}">FAQ</a><a href="${p('pages/case-studies/')}">Case Studies</a></div></div></nav><a class="ts-btn" href="${p('pages/request-a-quote/')}">Request a Quote</a></div></header>`;
}

async function transformHtml(response) {
  const original = await response.text();
  let html = original;
  html = html.replace(/<style id="ts-global-header-css">[\s\S]*?<\/style>/i, '');
  html = html.replace(/<div class="topbar"[\s\S]*?<header class="(?:site-header|header)"[\s\S]*?<\/header>/i, headerHtml());
  if (!html.includes('class="ts-header"')) {
    html = html.replace(/<body([^>]*)>/i, `<body$1>${headerHtml()}`);
  }
  html = html.replace(/<\/head>/i, `<style id="ts-global-header-css">${css}</style></head>`);
  return new Response(html, {
    status: response.status,
    statusText: response.statusText,
    headers: {'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-cache'}
  });
}

self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;
  const acceptsHtml = request.mode === 'navigate' || (request.headers.get('accept') || '').includes('text/html');
  if (!acceptsHtml) return;
  event.respondWith(fetch(request).then(response => {
    const type = response.headers.get('content-type') || '';
    if (!type.includes('text/html')) return response;
    return transformHtml(response);
  }).catch(() => fetch(request)));
});
