const VERSION = 'ts-v47-new-mapped-icons-only';

self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') self.skipWaiting();
});

const iconSvg = {
  swiss: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M32 8l18 7v15c0 13-7.5 21.5-18 26-10.5-4.5-18-13-18-26V15l18-7z"/><path d="M32 20v24M20 32h24"/></svg>',
  factory: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M10 54h44"/><path d="M14 54V30l13 8v-8l13 8v-8l10 6v18"/><path d="M45 34V16h8v38"/><path d="M19 48h7M32 48h7"/></svg>',
  quality: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect x="19" y="16" width="26" height="38" rx="3"/><path d="M25 16h14l3 7H22l3-7z"/><path d="M24 37l6 6 12-15"/><path d="M25 53l-3 8 10-5 10 5-3-8"/></svg>',
  shipping: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M9 34l46-22-16 42-10-16-20-4z"/><path d="M29 38l26-26"/></svg>',
  handshake: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M12 36l12-13 9 9"/><path d="M52 36L40 23l-9 9"/><path d="M22 43l7 7c4 4 9 4 13 0l8-8"/><path d="M10 34l9 20M54 34l-9 20"/></svg>',
  chat: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M14 19h28a10 10 0 0 1 10 10v4a10 10 0 0 1-10 10H29l-13 10 2-11a10 10 0 0 1-4-8V29a10 10 0 0 1 10-10z"/><path d="M24 29h18M24 36h12"/></svg>',
  tshirt: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M21 12l11 6 11-6 14 9-8 13-6-3v25H21V31l-6 3-8-13 14-9z"/><path d="M26 15c2 4 4 6 6 6s4-2 6-6"/></svg>',
  package: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M9 20l23-10 23 10-23 11L9 20z"/><path d="M9 20v25l23 11 23-11V20"/><path d="M32 31v25"/></svg>',
  mail: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect x="10" y="18" width="44" height="30" rx="3"/><path d="M11 21l21 17 21-17"/></svg>',
  phone: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M49 41v8a5 5 0 0 1-5.5 5A39 39 0 0 1 26 47 38 38 0 0 1 15 36 39 39 0 0 1 8 18.5 5 5 0 0 1 13 13h8a4 4 0 0 1 4 3.5c.5 3.5 1.2 6.5 2.4 9.2a4 4 0 0 1-.9 4.3l-3.5 3.5a31 31 0 0 0 13 13l3.5-3.5a4 4 0 0 1 4.3-.9c2.7 1.2 5.7 1.9 9.2 2.4A4 4 0 0 1 49 41z"/></svg>',
  location: '<svg class="icon-svg ts-mapped-icon" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M32 56s18-14 18-31a18 18 0 1 0-36 0c0 17 18 31 18 31z"/><circle cx="32" cy="25" r="7"/></svg>'
};

const legacyUseMap = {
  'icon-swiss-cross': 'swiss',
  'icon-factory': 'factory',
  'icon-award-check': 'quality',
  'icon-box-plane': 'shipping',
  'icon-handshake': 'handshake',
  'icon-chat': 'chat',
  'icon-tshirt': 'tshirt',
  'icon-clipboard-check': 'quality',
  'icon-package': 'package',
  'icon-mail': 'mail',
  'icon-phone': 'phone',
  'icon-location': 'location'
};

function injectStyle(html) {
  const css = '<style id="ts-new-svg-icon-style">.ts-mapped-icon,.icon-svg{fill:none!important;stroke:#e1111a!important;stroke-width:2.6!important;stroke-linecap:round!important;stroke-linejoin:round!important}.top-ico .ts-mapped-icon{width:17px;height:17px}.trust-icon .ts-mapped-icon{width:32px;height:32px}.process-icon .ts-mapped-icon{width:38px;height:38px}.contact-item .ts-mapped-icon{width:16px;height:16px}</style>';
  if (html.includes('ts-new-svg-icon-style')) return html;
  return html.replace('</head>', css + '</head>');
}

function removeLegacyDefs(html) {
  return html.replace(/<svg\s+class=["']svg-defs["'][\s\S]*?<\/svg>\s*/i, '');
}

function replaceLegacyUses(html) {
  return html.replace(/<svg\b([^>]*)>\s*<use\s+href=["']#([^"']+)["']\s*><\/use>\s*<\/svg>/gi, function(match, attrs, id) {
    const key = legacyUseMap[id];
    return key && iconSvg[key] ? iconSvg[key] : match;
  });
}

function normalizeLegacyImageSvg(html) {
  return html.replace(/<img\b([^>]*?)src=["'][^"']*\.svg[^"']*["']([^>]*)>/gi, function(match) {
    return iconSvg.quality;
  });
}

function transform(html) {
  let out = html;
  out = injectStyle(out);
  out = removeLegacyDefs(out);
  out = replaceLegacyUses(out);
  out = normalizeLegacyImageSvg(out);
  return out;
}

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  const isHtml = request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname.endsWith('/');
  if (!isHtml) return;

  event.respondWith(
    fetch(request, { cache: 'no-store' }).then(response => {
      const type = response.headers.get('content-type') || '';
      if (!type.includes('text/html')) return response;
      return response.text().then(html => new Response(transform(html), {
        status: response.status,
        statusText: response.statusText,
        headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' }
      }));
    }).catch(() => fetch(request))
  );
});
