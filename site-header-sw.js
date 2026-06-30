const VERSION = 'ts-v49-committed-svg-files';
const BASE = self.registration.scope;

const FILES = {
  1:'shield-with-cross-svgrepo-com (1).svg',2:'factory-building-svgrepo-com.svg',3:'quality-5-svgrepo-com.svg',4:'quality-5-svgrepo-com.svg',5:'quality-5-svgrepo-com.svg',6:'plane-svgrepo-com (1).svg',7:'stopwatch-svgrepo-com.svg',8:'handshake-svgrepo-com.svg',9:'person-with-headset-thin-outline-symbol-in-a-circle-svgrepo-com (1).svg',10:'speech-bubbles-conversation-svgrepo-com (1).svg',
  11:'computer-monitor-svgrepo-com.svg',12:'review-checkmark-svgrepo-com.svg',13:'design-svgrepo-com.svg',14:'computer-monitor-svgrepo-com.svg',15:'sketch-svgrepo-com.svg',16:'review-checkmark-svgrepo-com.svg',17:'quality-5-svgrepo-com.svg',18:'fabric-material-svgrepo-com.svg',19:'design-svgrepo-com.svg',20:'factory-building-svgrepo-com.svg',21:'sewing-machine-sew-svgrepo-com (1).svg',22:'scissors-svgrepo-com.svg',23:'needle-svgrepo-com.svg',24:'paint-roller-svgrepo-com.svg',25:'airport-baggage-conveyor-svgrepo-com.svg',26:'airport-baggage-conveyor-svgrepo-com.svg',27:'box-svgrepo-com.svg',28:'plane-svgrepo-com (1).svg',
  29:'tshirt-svgrepo-com (2).svg',30:'cotton-polo-shirt-svgrepo-com.svg',31:'sweatshirt-svgrepo-com.svg',32:'construction-worker-svgrepo-com.svg',33:'shirt-svgrepo-com.svg',34:'team-uniform-svgrepo-com.svg',35:'paralympic-swimming-silhouette-svgrepo-com.svg',36:'boxing-shorts-svgrepo-com.svg',37:'boxing-shorts-svgrepo-com.svg',38:'doctor-female-svgrepo-com.svg',39:'doctor-female-svgrepo-com.svg',40:'cap-svgrepo-com.svg',41:'jacket-svgrepo-com.svg',42:'shopping-bag-svgrepo-com.svg',43:'team-uniform-svgrepo-com.svg',
  44:'barcode-sticker-svgrepo-com.svg',45:'barcode-sticker-svgrepo-com.svg',46:'tag-2-svgrepo-com.svg',47:'barcode-sticker-svgrepo-com.svg',48:'barcode-sticker-svgrepo-com.svg',49:'box-svgrepo-com.svg',50:'shopping-bag-svgrepo-com.svg',51:'barcode-sticker-svgrepo-com.svg',52:'print-products-svgrepo-com (1).svg',53:'print-products-svgrepo-com (1).svg',54:'print-products-svgrepo-com (1).svg',55:'print-products-svgrepo-com (1).svg',56:'needle-svgrepo-com.svg',57:'fabric-material-svgrepo-com.svg',58:'fabric-material-svgrepo-com.svg',59:'fabric-material-svgrepo-com.svg',60:'bamboo-svgrepo-com.svg',61:'fabric-material-svgrepo-com.svg',62:'keep-dry-svgrepo-com.svg',63:'fabric-material-svgrepo-com.svg',64:'germs-svgrepo-com.svg',65:'sun-cream-sun-protection-svgrepo-com.svg',
  66:'construction-worker-svgrepo-com.svg',67:'doctor-female-svgrepo-com.svg',68:'hotel-reception-svgrepo-com.svg',69:'team-uniform-svgrepo-com.svg',70:'boxing-shorts-svgrepo-com.svg',71:'shirt-svgrepo-com.svg',72:'shopping-bag-svgrepo-com.svg',73:'facebook-svgrepo-com.svg',74:'rock-and-roll-concert-svgrepo-com.svg',75:'bamboo-svgrepo-com.svg',76:'recycling-arrows-svgrepo-com.svg',77:'recycling-arrows-svgrepo-com.svg',78:'recycling-arrows-svgrepo-com.svg',79:'recycling-arrows-svgrepo-com.svg',80:'recycling-arrows-svgrepo-com.svg',81:'water-drop-svgrepo-com.svg',82:'recycling-arrows-svgrepo-com.svg',83:'computer-monitor-svgrepo-com.svg',84:'computer-monitor-svgrepo-com.svg',85:'downloads-svgrepo-com.svg',86:'book-svgrepo-com.svg',87:'book-svgrepo-com.svg',88:'book-svgrepo-com.svg',89:'search-alt-2-svgrepo-com.svg',90:'person-with-headset-thin-outline-symbol-in-a-circle-svgrepo-com (1).svg',91:'person-with-headset-thin-outline-symbol-in-a-circle-svgrepo-com (1).svg',92:'whatsapp-svgrepo-com.svg',93:'email-svgrepo-com.svg',94:'shield-with-cross-svgrepo-com (1).svg',95:'email-svgrepo-com.svg',96:'person-with-headset-thin-outline-symbol-in-a-circle-svgrepo-com (1).svg'
};

const LEGACY = {'icon-swiss-cross':1,'icon-factory':2,'icon-award-check':3,'icon-box-plane':6,'icon-handshake':8,'icon-chat':10,'icon-tshirt':29,'icon-clipboard-check':4,'icon-package':27,'icon-mail':93,'icon-phone':91,'icon-location':94};

const PHRASES = [
 ['Swiss Quality Standards',1],['Factory Direct Pricing',2],['Strict Quality Control',4],['Worldwide Shipping',6],['Swiss Managed',1],['Factory in Thailand',2],['Premium Quality',3],['Long-Term Partner',8],['Long Term Partner',8],['Dedicated Account Manager',9],['Consultation',10],['Product Development',11],['Design Review',12],['Pattern Making',13],['CAD Design',14],['Tech Pack',15],['Sampling',16],['Sample Approval',17],['Fabric Selection',18],['Trims Selection',19],['Production',20],['Sewing',21],['Cutting',22],['Embroidery',23],['Screen Printing',24],['Heat Transfer',25],['Sublimation',26],['Packaging',27],['Dispatch',28],
 ['T-Shirts',29],['T Shirt',29],['Polos',30],['Hoodies',31],['Hoodies & Sweatshirts',31],['Workwear',32],['Corporate Apparel',33],['Sportswear',34],['Rashguards',35],['MMA Shorts',36],['Muay Thai Shorts',37],['Medical Scrubs',38],['Healthcare Uniforms',39],['Caps & Headwear',40],['Jackets',41],['Jackets & Softshells',41],['Tote Bags',42],['Promotional Merchandise',43],['Private Label',44],['Custom Labels',45],['Hang Tags',46],['Woven Labels',47],['Neck Labels',48],['Custom Packaging',49],['Fold & Bag',50],['Barcode Labelling',51],
 ['DTG Printing',52],['Puff Print',53],['Silicone Print',54],['Reflective Print',55],['Puff Embroidery',56],['Cotton',57],['Organic Cotton',58],['Polyester',59],['Bamboo',60],['Recycled Fabric',61],['Moisture Wicking',62],['Stretch Fabric',63],['Anti-Bacterial',64],['Antibacterial',64],['UPF Protection',65],['Construction',66],['Healthcare',67],['Hospitality',68],['Fitness',69],['Sports & Fitness',69],['Combat Sports',70],['Corporate',71],['Ecommerce Brands',72],['Influencer Brands',73],['Events & Merchandise',74],['Sustainability',75],['Eco-Friendly',76],['Recycled Materials',77],['Ethical Manufacturing',78],['Carbon Reduction',79],['Waste Reduction',80],['Water Saving',81],['Renewable Energy',82],['Blog',83],['FAQ',84],['Downloads',85],['Case Studies',86],['Guides',87],['Resources',88],['Search',89],['Contact',90],['Phone',91],['WhatsApp',92],['Email',93],['Switzerland Office',94],['Request a Quote',95],['Schedule a Call',96],['Fabric',18],['Materials',18],['Garments',29],['Quality Control',4],['Shipping',6]
].sort((a,b)=>b[0].length-a[0].length);

function urlFor(ref) { return BASE + encodeURI(FILES[ref] || FILES[4]); }
function icon(ref) { return '<img class="icon-svg ts-mapped-icon" alt="" aria-hidden="true" data-svg-ref="'+ref+'" src="'+urlFor(ref)+'">'; }
function esc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

function addStyle(html) {
  const css = '<style id="ts-mapped-svg-file-style">.svg-defs{display:none!important}.ts-mapped-icon{display:inline-block;object-fit:contain}.top-ico .ts-mapped-icon{width:17px;height:17px}.trust-icon .ts-mapped-icon,.feature-icon .ts-mapped-icon,.cat-icon .ts-mapped-icon,.icon .ts-mapped-icon,.ico .ts-mapped-icon{width:52px;height:52px}.process-icon .ts-mapped-icon,.step-icon .ts-mapped-icon{width:38px;height:38px}.contact-item .ts-mapped-icon{width:16px;height:16px}</style>';
  return html.includes('ts-mapped-svg-file-style') ? html : html.replace('</head>', css + '</head>');
}

function replaceInBlock(block, ref) {
  const iconHolder = /(<(?:span|div)[^>]*class=["'][^"']*(?:top-ico|trust-icon|feature-icon|cat-icon|process-icon|step-icon|icon|ico)[^"']*["'][^>]*>)[\s\S]*?(<\/(?:span|div)>)/i;
  if (iconHolder.test(block)) return block.replace(iconHolder, '$1' + icon(ref) + '$2');
  const anySvg = /<svg\b[\s\S]*?<\/svg>|<img\b[^>]*\.svg[^>]*>/i;
  return anySvg.test(block) ? block.replace(anySvg, icon(ref)) : block;
}

function phraseMap(html) {
  for (const [phrase, ref] of PHRASES) {
    const q = esc(phrase);
    const block = new RegExp('(<(?:article|div|li|a)[^>]*class=["\\'][^"\\']*(?:card|item|step|tile|feature|trust|resource|process|value|service|product|industry)[^"\\']*["\\'][^>]*>[\\s\\S]{0,1800}?'+q+'[\\s\\S]{0,1800}?<\\/(?:article|div|li|a)>)','gi');
    html = html.replace(block, m => replaceInBlock(m, ref));
    const iconBeforeText = new RegExp('(<(?:span|div)[^>]*class=["\\'][^"\\']*(?:top-ico|trust-icon|feature-icon|cat-icon|process-icon|step-icon|icon|ico)[^"\\']*["\\'][^>]*>)[\\s\\S]*?(<\\/(?:span|div)>)(?=[\\s\\S]{0,320}?'+q+')','gi');
    html = html.replace(iconBeforeText, '$1' + icon(ref) + '$2');
  }
  return html;
}

function transform(html) {
  html = addStyle(html);
  html = html.replace(/<svg\s+class=["']svg-defs["'][\s\S]*?<\/svg>\s*/i, '');
  html = html.replace(/<svg\b[^>]*>\s*<use\s+href=["']#([^"']+)["']\s*><\/use>\s*<\/svg>/gi, (m,id) => LEGACY[id] ? icon(LEGACY[id]) : m);
  html = html.replace(/<img\b[^>]*src=["'][^"']*\.svg[^"']*["'][^>]*>/gi, icon(4));
  return phraseMap(html);
}

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('message', e => { if (e.data && e.data.type === 'SKIP_WAITING') self.skipWaiting(); });
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const u = new URL(req.url);
  const isHtml = req.mode === 'navigate' || u.pathname.endsWith('.html') || u.pathname.endsWith('/');
  if (!isHtml) return;
  e.respondWith(fetch(req, { cache: 'no-store' }).then(res => {
    const t = res.headers.get('content-type') || '';
    if (!t.includes('text/html')) return res;
    return res.text().then(body => new Response(transform(body), {status: res.status, statusText: res.statusText, headers: {'content-type':'text/html; charset=utf-8','cache-control':'no-store'}}));
  }).catch(() => fetch(req)));
});
