from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDUSTRIES_DIR = ROOT / 'wordpress' / 'pages' / 'industries'

industry_pages = {
    'construction-trades': {
        'name': 'Construction & Trades',
        'hero_title': 'Workwear That Works As Hard As You Do.',
        'hero_subtitle': 'Durable. Functional. Professional. Custom workwear for construction companies, tradespeople and industrial teams across Switzerland.',
        'hero_tags': [
            'Built for Tough Jobs',
            'Premium Fabrics & Materials',
            'Reinforced Durability',
            'Reliable Production & On-Time Delivery',
        ],
        'solutions': [
            ('Construction Companies', 'Professional workwear for building sites and project teams.'),
            ('Electricians', 'Durable clothing with practical pockets and protection.'),
            ('Plumbers', 'Comfortable gear built for the demands of plumbing and maintenance.'),
            ('Carpenters', 'Functional apparel for woodworkers and construction trades.'),
            ('Landscapers', 'Breathable, weather-ready clothing for outdoor crews.'),
            ('Industrial Teams', 'High-performance apparel for industrial and technical environments.'),
        ],
        'work_actions': [
            ('Large Construction Company', 'Zurich, Switzerland'),
            ('Electrical Contractors', 'Basel, Switzerland'),
            ('Industrial Maintenance', 'Bern, Switzerland'),
            ('Building & Renovation', 'Geneva, Switzerland'),
        ],
    },
    'healthcare': {
        'name': 'Healthcare',
        'hero_title': 'Apparel Designed for Care Teams and Clinical Settings.',
        'hero_subtitle': 'Comfortable, functional uniforms for healthcare, assisted living and clinical operations with Swiss-managed quality control.',
        'hero_tags': [
            'Comfortable Fabrics',
            'Easy Care & Hygiene',
            'Clear Professional Branding',
            'Reliable Production & Delivery',
        ],
        'solutions': [
            ('Hospitals', 'Durable uniforms for nursing, medical and support teams.'),
            ('Clinics', 'Clean, functional apparel for outpatient and therapy staff.'),
            ('Care Homes', 'Comfortable, practical uniforms for senior care teams.'),
            ('Medical Labs', 'Precise, reliable workwear with professional fit.'),
            ('Dental Practices', 'Branded garments for clinical and reception staff.'),
            ('Pharma Teams', 'Controlled apparel suitable for regulated environments.'),
        ],
        'work_actions': [
            ('Hospital Uniform Program', 'Zurich, Switzerland'),
            ('Clinic Care Team', 'Basel, Switzerland'),
            ('Laboratory Staff', 'Bern, Switzerland'),
            ('Dental Practice Team', 'Lausanne, Switzerland'),
        ],
    },
    'hospitality': {
        'name': 'Hospitality',
        'hero_title': 'Uniforms That Feel Comfortable and Look Professional.',
        'hero_subtitle': 'Premium hospitality apparel for hotels, restaurants and event teams that supports Swiss service standards.',
        'hero_tags': [
            'Refined Fabrics',
            'Comfortable All-Day Wear',
            'Curated Brand Presentation',
            'Swiss-managed Production',
        ],
        'solutions': [
            ('Hotel Staff', 'Polished uniforms for front desk, concierge and hospitality teams.'),
            ('Restaurant Teams', 'Durable chef and service apparel with great fit.'),
            ('Event Staff', 'Flexible, branded workwear for live events and catering.'),
            ('Spa & Wellness', 'Comfortable uniforms with a premium look.'),
            ('Café Crews', 'Casual yet refined apparel for foodservice teams.'),
            ('Conference Teams', 'Consistent employee apparel for large-scale events.'),
        ],
        'work_actions': [
            ('Hotel Team Apparel', 'Lucerne, Switzerland'),
            ('Restaurant Uniform Set', 'Basel, Switzerland'),
            ('Event Catering Crew', 'Geneva, Switzerland'),
            ('Spa & Wellness Team', 'Zug, Switzerland'),
        ],
    },
    'sports-fitness': {
        'name': 'Sports & Fitness',
        'hero_title': 'Performance Apparel for Swiss Teams and Active Brands.',
        'hero_subtitle': 'Technical sportswear and active apparel built for training, teamwear and fitness programs with premium manufacturing quality.',
        'hero_tags': [
            'Breathable Performance',
            'Team Branding',
            'Durable Fabrics',
            'Fast, Reliable Delivery',
        ],
        'solutions': [
            ('Training Teams', 'Performance apparel for clubs and corporate teams.'),
            ('Gyms & Studios', 'Functional activewear for fitness and coaching.'),
            ('Yoga & Pilates', 'Soft, flexible apparel for mindful movement.'),
            ('Running Clubs', 'Branded gear built for comfort and breathability.'),
            ('Cycle Teams', 'Technical apparel for endurance and speed.'),
            ('Community Sports', 'Reliable uniforms for amateur and youth teams.'),
        ],
        'work_actions': [
            ('Team Training Kit', 'Zurich, Switzerland'),
            ('Gym Staff Apparel', 'Basel, Switzerland'),
            ('Running Club Uniforms', 'Bern, Switzerland'),
            ('Fitness Brand Launch', 'Lausanne, Switzerland'),
        ],
    },
    'combat-sports': {
        'name': 'Combat Sports',
        'hero_title': 'Fight-Ready Apparel for Combat Teams and Clubs.',
        'hero_subtitle': 'Technical training apparel and branded fight gear crafted for MMA, boxing and combat sports teams.',
        'hero_tags': [
            'Durable Fabrics',
            'Bold Branding',
            'High Mobility',
            'Swiss Production Standards',
        ],
        'solutions': [
            ('MMA Clubs', 'Technical shorts and tops for mixed martial arts teams.'),
            ('Boxing Gyms', 'Durable apparel for coaches and fighters.'),
            ('Wrestling Teams', 'Strong, flexible gear for intense training.'),
            ('Fight Events', 'Merch and uniforms for competition staff and athletes.'),
            ('Training Camps', 'Reliable apparel for camp schedules and routines.'),
            ('Fightwear Branding', 'Bold garments built for combat sport identities.'),
        ],
        'work_actions': [
            ('MMA Team Apparel', 'Zurich, Switzerland'),
            ('Boxing Club Kit', 'Basel, Switzerland'),
            ('Wrestling Program', 'Bern, Switzerland'),
            ('Event Team Gear', 'Geneva, Switzerland'),
        ],
    },
    'corporate-apparel': {
        'name': 'Corporate Apparel',
        'hero_title': 'Executive Uniforms Built for Swiss Business.',
        'hero_subtitle': 'Branded corporate clothing designed for offices, sales teams and premium workplace experiences.',
        'hero_tags': [
            'Professional Finishes',
            'Smart Comfort',
            'Consistent Brand Identity',
            'Reliable Quality Control',
        ],
        'solutions': [
            ('Office Teams', 'Smart uniforms for day-to-day business wear.'),
            ('Sales Staff', 'Polished apparel for customer-facing teams.'),
            ('Executive Uniforms', 'Premium garments for leadership and hospitality.'),
            ('Conference Apparel', 'Consistent branded dress for events.'),
            ('Retail Teams', 'Branded clothing for stores and showrooms.'),
            ('Corporate Gifts', 'Premium apparel for client and partner gifting.'),
        ],
        'work_actions': [
            ('Office Uniform Program', 'Zurich, Switzerland'),
            ('Sales Team Apparel', 'Basel, Switzerland'),
            ('Event Staffing Kit', 'Bern, Switzerland'),
            ('Retail Team Clothing', 'Lausanne, Switzerland'),
        ],
    },
    'ecommerce-brands': {
        'name': 'Ecommerce Brands',
        'hero_title': 'Branded Apparel for E-commerce and Retail Success.',
        'hero_subtitle': 'Ready-to-sell apparel and merchandise for online brands, subscription boxes and retail launches.',
        'hero_tags': [
            'Retail-Ready Finish',
            'Brand Consistency',
            'High-Quality Production',
            'Scalable Manufacturing',
        ],
        'solutions': [
            ('Brand Launches', 'Branded apparel for online store introductions.'),
            ('Subscription Boxes', 'Premium apparel packaged for direct-to-consumer delivery.'),
            ('Retail Collections', 'Ready-to-sell garments for e-commerce brands.'),
            ('Influencer Merchandise', 'Strong quality for promotional product lines.'),
            ('Customer Giveaways', 'Attractive branded apparel for loyalty activations.'),
            ('Packaging Integration', 'Apparel production paired with premium packaging.'),
        ],
        'work_actions': [
            ('Ecommerce Launch Kit', 'Zurich, Switzerland'),
            ('Subscription Box Apparel', 'Basel, Switzerland'),
            ('Retail Brand Collection', 'Bern, Switzerland'),
            ('Influencer Merch Range', 'Lausanne, Switzerland'),
        ],
    },
    'events-merchandise': {
        'name': 'Events & Merchandise',
        'hero_title': 'Merchandise Made for Events, Brands and Campaigns.',
        'hero_subtitle': 'Premium event apparel and branded merchandise for conferences, festivals and activations.',
        'hero_tags': [
            'Event-Ready Quality',
            'Strong Brand Impact',
            'Fast Production',
            'Reliable Delivery',
        ],
        'solutions': [
            ('Trade Shows', 'Branded apparel for exhibitions and conferences.'),
            ('Festivals', 'Durable merchandise for large crowd events.'),
            ('Corporate Events', 'Professional apparel for staff and attendees.'),
            ('Sports Events', 'Team and volunteer apparel for competitions.'),
            ('Promotional Campaigns', 'High-quality merchandise for activations.'),
            ('VIP Gifts', 'Premium branded apparel for guest gifting.'),
        ],
        'work_actions': [
            ('Trade Show Apparel', 'Zurich, Switzerland'),
            ('Festival Team Gear', 'Basel, Switzerland'),
            ('Corporate Event Apparel', 'Bern, Switzerland'),
            ('Sports Activation Kit', 'Geneva, Switzerland'),
        ],
    },
}

trust_logos = [
    'Implenia',
    'HRS Real Estate AG',
    'WALO',
    'Frutiger',
    'BÜRGI',
    'STRABAG',
]

qa_items = [
    ('What is the minimum order quantity (MOQ)?', 'MOQ depends on product type and materials. We support both small sample runs and larger production orders.'),
    ('Can you add our company logo?', 'Yes, we apply logos through printing, embroidery or labels based on the product and application.'),
    ('Do you offer high-visibility workwear?', 'Yes, we produce hi-vis apparel with reflective details for safety and compliance.'),
    ('How long is the production time?', 'Production timelines depend on order size and complexity, but we prioritize fast, reliable delivery.'),
]


def build_html(data):
    name = data['name']
    title = data['hero_title']
    subtitle = data['hero_subtitle']
    hero_tags = data['hero_tags']
    solutions = data['solutions']
    work_actions = data['work_actions']

    solution_cards_html = '\n'.join(
        f'<article class="solution-card"><strong>{label}</strong><p>{description}</p></article>'
        for label, description in solutions
    )

    hero_tags_html = '\n'.join(
        f'<div class="hero-tag"><span>{label}</span></div>'
        for label in hero_tags
    )

    work_actions_html = '\n'.join(
        f'<article class="case-card"><div class="case-copy"><strong>{label}</strong><span>{description}</span></div></article>'
        for label, description in work_actions
    )

    faq_html = '\n'.join(
        f'<div class="faq-item"><button type="button"><span>{question}</span><span>+</span></button><div class="faq-answer"><p>{answer}</p></div></div>'
        for question, answer in qa_items
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} | TShirtSwiss.ch</title>
  <style>
:root {{
  color-scheme: light;
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  color: #111;
  background: #f4f4f4;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: #f4f4f4; color: #111; }}
a {{ color: inherit; text-decoration: none; }}
img {{ max-width: 100%; height: auto; display: block; }}
.page-shell {{ display: flex; flex-direction: column; min-height: 100vh; }}
.topbar {{ background: #111; color: #f4f4f4; font-size: .9rem; }}
.topbar .wrapper {{ max-width: 1280px; margin: 0 auto; padding: 12px 24px; display: flex; justify-content: space-between; gap: 16px; align-items: center; flex-wrap: wrap; }}
.topbar-group {{ display: flex; flex-wrap: wrap; gap: 18px; align-items: center; }}
.topbar-item {{ display: inline-flex; align-items: center; gap: 8px; opacity: .85; }}
.topbar-item strong {{ color: #fff; font-weight: 700; }}
.topbar-links {{ display: flex; gap: 14px; }}
.topbar-links a {{ color: #f4f4f4; opacity: .8; padding: 6px 10px; border-radius: 999px; }}
.topbar-links a:hover {{ opacity: 1; }}
.site-header {{ background: #fff; position: sticky; top: 0; z-index: 30; box-shadow: 0 20px 60px rgba(0, 0, 0, .08); }}
.site-header .wrapper {{ max-width: 1280px; margin: 0 auto; padding: 22px 24px; display: flex; align-items: center; justify-content: space-between; gap: 20px; flex-wrap: wrap; }}
.brand {{ font-size: 1.05rem; font-weight: 800; letter-spacing: .18em; text-transform: uppercase; color: #111; }}
.nav {{ display: flex; gap: 24px; flex-wrap: wrap; font-size: .95rem; }}
.nav a {{ color: #111; opacity: .85; transition: opacity .2s, color .2s; }}
.nav a:hover {{ opacity: 1; color: #D52B1E; }}
.cta-button {{ padding: 14px 26px; background: #D52B1E; color: #fff; border-radius: 999px; font-weight: 700; box-shadow: 0 18px 40px rgba(213, 43, 30, .18); }}
main {{ flex: 1; max-width: 1280px; margin: 0 auto; padding: 28px 24px 60px; }}
.breadcrumb {{ display: flex; gap: 10px; flex-wrap: wrap; align-items: center; font-size: .9rem; color: #555; margin: 20px 0 16px; }}
.breadcrumb a {{ opacity: .8; }}
.breadcrumb span {{ opacity: .55; }}
.hero {{ display: grid; grid-template-columns: 1.05fr .95fr; gap: 36px; align-items: center; min-height: calc(100vh - 180px); padding: 40px 0 32px; }}
.hero-copy {{ max-width: 620px; }}
.hero-eyebrow {{ font-size: .8rem; letter-spacing: .26em; text-transform: uppercase; color: #D52B1E; font-weight: 700; margin-bottom: 18px; }}
.hero-title {{ font-size: clamp(3rem, 4.4vw, 4.8rem); line-height: 1; margin: 0; color: #111; }}
.hero-subtitle {{ margin: 24px 0 0; font-size: 1.24rem; line-height: 1.75; color: #222; max-width: 44rem; }}
.hero-text {{ margin: 24px 0 0; font-size: 1rem; line-height: 1.8; color: #4d4d4d; max-width: 42rem; }}
.hero-actions {{ display: flex; flex-wrap: wrap; gap: 16px; margin-top: 32px; }}
.hero-actions a {{ display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 16px 28px; border-radius: 999px; font-weight: 700; transition: transform .2s, box-shadow .2s; }}
.hero-actions a.primary {{ background: #D52B1E; color: #fff; }}
.hero-actions a.secondary {{ border: 1px solid rgba(17, 17, 17, .12); background: #fff; color: #111; }}
.hero-tags {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; margin-top: 32px; }}
.hero-tag {{ padding: 18px 20px; background: #fff; border-radius: 22px; border: 1px solid rgba(17, 17, 17, .08); box-shadow: 0 18px 45px rgba(17, 17, 17, .05); }}
.hero-tag span {{ font-size: .95rem; color: #111; font-weight: 700; }}
.hero-visual {{ border-radius: 30px; overflow: hidden; box-shadow: 0 35px 90px rgba(17, 17, 17, .12); }}
.hero-visual img {{ width: 100%; height: auto; display: block; }}
.section {{ padding: 72px 0; }}
.section--white {{ background: #fff; }}
.section__inner {{ display: grid; gap: 34px; max-width: 1280px; margin: 0 auto; }}
.section--split .section__inner {{ grid-template-columns: 1fr 1fr; align-items: center; }}
.section-title h2 {{ margin: 0 0 14px; font-size: clamp(2.4rem, 3vw, 3.2rem); line-height: 1.05; font-weight: 800; color: #111; }}
.section-title p {{ margin: 0; color: #555; line-height: 1.75; font-size: 1rem; max-width: 46rem; }}
.trust-logos {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 24px; align-items: center; margin-top: 28px; }}
.trust-logos span {{ color: #555; font-size: .95rem; opacity: .8; text-align: center; }}
.solution-grid {{ display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); margin-top: 28px; }}
.solution-card {{ background: #fff; border-radius: 24px; padding: 28px; border: 1px solid rgba(17, 17, 17, .08); box-shadow: 0 18px 45px rgba(17, 17, 17, .05); }}
.solution-card strong {{ display: block; margin-bottom: 14px; font-size: 1rem; color: #111; }}
.solution-card p {{ margin: 0; color: #555; line-height: 1.75; font-size: .95rem; }}
.split-grid {{ display: grid; gap: 32px; grid-template-columns: 1.4fr .6fr; align-items: start; }}
.feature-copy h3 {{ margin: 0 0 18px; font-size: clamp(2rem, 2.3vw, 2.5rem); line-height: 1.05; color: #111; }}
.feature-copy p {{ margin: 0 0 24px; color: #555; line-height: 1.75; font-size: 1rem; max-width: 46rem; }}
.bullet-list {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 14px; }}
.bullet-list li {{ display: flex; gap: 16px; align-items: flex-start; color: #444; line-height: 1.7; }}
.bullet-list li::before {{ content: '•'; color: #D52B1E; font-weight: 800; margin-top: 4px; }}
.quote-card {{ background: #111; color: #fff; border-radius: 30px; padding: 32px; display: grid; gap: 22px; box-shadow: 0 30px 80px rgba(17, 17, 17, .16); }}
.quote-card h3 {{ margin: 0; font-size: 1.5rem; line-height: 1.2; }}
.quote-card p {{ margin: 0; color: rgba(255,255,255,.82); line-height: 1.8; }}
.quote-card ul {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }}
.quote-card li {{ display: flex; gap: 12px; align-items: flex-start; color: rgba(255,255,255,.9); }}
.quote-card li::before {{ content: '✓'; color: #D52B1E; margin-top: 2px; }}
.quote-card a {{ display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 14px 24px; background: #D52B1E; color: #fff; border-radius: 999px; font-weight: 700; margin-top: 14px; width: fit-content; }}
.feature-row {{ display: grid; gap: 18px; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); margin-top: 26px; }}
.feature-tile {{ background: #fff; border-radius: 24px; padding: 24px; border: 1px solid rgba(17, 17, 17, .08); box-shadow: 0 18px 45px rgba(17, 17, 17, .05); }}
.feature-tile strong {{ display: block; margin-bottom: 12px; font-size: 1rem; color: #111; }}
.feature-tile p {{ margin: 0; color: #555; line-height: 1.75; font-size: .95rem; }}
.work-grid {{ display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); margin-top: 28px; }}
.case-card {{ background: #fff; border-radius: 24px; padding: 24px; border: 1px solid rgba(17, 17, 17, .08); box-shadow: 0 18px 45px rgba(17, 17, 17, .05); display: flex; flex-direction: column; justify-content: space-between; min-height: 170px; gap: 18px; }}
.case-copy strong {{ display: block; font-size: 1rem; color: #111; }}
.case-copy span {{ color: #555; line-height: 1.7; font-size: .95rem; }}
.faq-grid {{ display: grid; gap: 16px; margin-top: 24px; }}
.faq-item {{ background: #fff; border-radius: 24px; border: 1px solid rgba(17, 17, 17, .09); overflow: hidden; box-shadow: 0 18px 45px rgba(17, 17, 17, .05); }}
.faq-item button {{ width: 100%; display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 22px 24px; font-size: 1rem; border: 0; background: transparent; cursor: pointer; color: #111; }}
.faq-answer {{ padding: 0 24px 24px; color: #555; font-size: .95rem; line-height: 1.75; display: none; }}
.faq-item.open .faq-answer {{ display: block; }}
.footer {{ background: #111; color: #e2e2e2; padding: 48px 24px 56px; }}
.footer .wrapper {{ max-width: 1280px; margin: 0 auto; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }}
.footer h3 {{ margin: 0 0 18px; font-size: 1rem; color: #fff; }}
.footer p, .footer a {{ margin: 0; color: #c8c8c8; line-height: 1.8; font-size: .95rem; }}
.footer a:hover {{ opacity: 1; }}
@media (max-width: 1060px) {{ .hero {{ grid-template-columns: 1fr; }} .split-grid {{ grid-template-columns: 1fr; }} .section--split .section__inner {{ grid-template-columns: 1fr; }} }}
@media (max-width: 780px) {{ main {{ padding: 24px 18px 40px; }} .site-header .wrapper, .topbar .wrapper {{ padding: 18px; }} .nav {{ gap: 14px; }} .hero-title {{ font-size: 2.8rem; }} .hero-tags {{ grid-template-columns: 1fr; }} .trust-logos {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} .feature-row {{ grid-template-columns: 1fr; }} .work-grid {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
<div class="page-shell">
  <div class="topbar">
    <div class="wrapper">
      <div class="topbar-group">
        <div class="topbar-item"><strong>Swiss Managed</strong></div>
        <div class="topbar-item"><strong>Factory in Thailand</strong></div>
        <div class="topbar-item"><strong>Premium Quality</strong></div>
        <div class="topbar-item"><strong>Worldwide Shipping</strong></div>
      </div>
      <div class="topbar-links">
        <a href="#">DE</a>
        <a href="#">EN</a>
      </div>
    </div>
  </div>
  <header class="site-header">
    <div class="wrapper">
      <div class="brand">TShirtSwiss.ch</div>
      <nav class="nav">
        <a href="/pages/products/">Products</a>
        <a href="/pages/industries/">Industries</a>
        <a href="/pages/services/">Services</a>
        <a href="/pages/about-us/">About</a>
        <a href="/pages/production/">Production</a>
        <a href="/pages/contact/">Contact</a>
      </nav>
      <a class="cta-button" href="/pages/request-a-quote/">Request a Quote</a>
    </div>
  </header>
  <main>
    <nav class="breadcrumb">
      <a href="/pages/home/">Home</a>
      <span>›</span>
      <a href="/pages/industries/">Industries</a>
      <span>›</span>
      <span>{name}</span>
    </nav>
    <section class="hero">
      <div class="hero-copy">
        <div class="hero-eyebrow">{name.upper()}</div>
        <h1 class="hero-title">{title}</h1>
        <p class="hero-subtitle">{subtitle}</p>
        <div class="hero-actions">
          <a class="primary" href="/pages/request-a-quote/">Request a Quote</a>
          <a class="secondary" href="/pages/products/">View Products</a>
        </div>
        <div class="hero-tags">{hero_tags_html}</div>
      </div>
      <div class="hero-visual">
        <img src="https://via.placeholder.com/1200x900?text={name.replace(' ', '+')}+Hero" alt="{name} hero image">
      </div>
    </section>

    <section class="section section--white">
      <div class="section__inner">
        <div class="section-title">
          <h2>Trusted by Swiss businesses across industries</h2>
          <p>Our clients rely on Swiss-managed apparel production for consistent quality, clear communication and timely delivery.</p>
        </div>
        <div class="trust-logos">
          {''.join(f'<span>{logo}</span>' for logo in trust_logos)}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section__inner">
        <div class="section-title">
          <h2>Solutions for every team and role</h2>
          <p>Custom apparel categories tailored to the way your industry works, from design to delivery.</p>
        </div>
        <div class="solution-grid">{solution_cards_html}</div>
      </div>
    </section>

    <section class="section section--white section--split">
      <div class="section__inner">
        <div class="feature-copy">
          <p class="eyebrow">Built for performance</p>
          <h3>Workwear That Delivers Safety, Comfort and Durability.</h3>
          <p>We combine Swiss quality standards with expert manufacturing in Thailand to deliver apparel that meets the demands of your daily operations.</p>
          <ul class="bullet-list">
            <li>Strong, durable fabrics for heavy use</li>
            <li>Reinforced stitching and stress points</li>
            <li>High visibility options for safety-critical roles</li>
            <li>Custom branding with embroidery or printing</li>
            <li>Functional designs with practical pockets</li>
            <li>Comfortable fit for all-day performance</li>
          </ul>
        </div>
        <div class="quote-card">
          <h3>Request a Quote</h3>
          <p>Get your custom workwear quote in 24 hours.</p>
          <ul>
            <li>Tell us your needs</li>
            <li>Receive expert advice</li>
            <li>Get your personalized quote</li>
            <li>On-time production & delivery</li>
          </ul>
          <a href="/pages/request-a-quote/">Request a Quote</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section__inner">
        <div class="section-title">
          <h2>Designed for your industry standards</h2>
          <p>Premium apparel solutions that align with your safety, durability and brand requirements.</p>
        </div>
        <div class="feature-row">
          <div class="feature-tile"><strong>Safety First</strong><p>High-visibility options and protective features for demanding environments.</p></div>
          <div class="feature-tile"><strong>All Weather</strong><p>Workwear designed to perform in every season and condition.</p></div>
          <div class="feature-tile"><strong>Easy Care</strong><p>Apparel built to stay reliable and low-maintenance through repeated use.</p></div>
          <div class="feature-tile"><strong>Team Identity</strong><p>Custom branding for a polished, professional look.</p></div>
          <div class="feature-tile"><strong>Sustainable Options</strong><p>Eco-friendly fabrics and finishes are available for responsible brands.</p></div>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="section__inner">
        <div class="section-title">
          <h2>Real projects. Real results.</h2>
          <p>See how Swiss-managed apparel manufacturing supports strong, consistent outcomes for your industry.</p>
        </div>
        <div class="work-grid">{work_actions_html}</div>
      </div>
    </section>

    <section class="section">
      <div class="section__inner">
        <div class="section-title">
          <h2>Common questions</h2>
          <p>Answers to the most frequent questions about production, timelines and custom apparel.</p>
        </div>
        <div class="faq-grid">{faq_html}</div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="wrapper">
      <div>
        <h3>About</h3>
        <p>Swiss-managed premium apparel manufacturing in Thailand.</p>
      </div>
      <div>
        <h3>Contact</h3>
        <p>swiss@tshirtswiss.ch<br>+41 79 000 00 00</p>
      </div>
      <div>
        <h3>Office</h3>
        <p>Swiss HQ + Thailand Factory</p>
      </div>
    </div>
  </footer>
</div>
<script>
document.querySelectorAll('.faq-item button').forEach(function(button) {{
  button.addEventListener('click', function() {{
    var item = button.closest('.faq-item');
    if (item) {{
      item.classList.toggle('open');
    }}
  }});
}});
</script>
</body>
</html>'''


def main():
    INDUSTRIES_DIR.mkdir(parents=True, exist_ok=True)

    for slug, data in industry_pages.items():
        page_dir = INDUSTRIES_DIR / slug
        page_dir.mkdir(parents=True, exist_ok=True)
        file_path = page_dir / 'index.html'
        file_path.write_text(build_html(data), encoding='utf-8')
        print(f'Updated {file_path}')


if __name__ == '__main__':
    main()
