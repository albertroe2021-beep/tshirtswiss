import re
from pathlib import Path


def parse_copy_file(path):
    sections = {}
    current = None
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line.startswith('### '):
            current = line[4:].strip()
            sections[current] = {}
        elif current and line.startswith('-'):
            match = re.match(r'-\s*(CTA 1|CTA 2|H1|H2|Intro|Title|Button Text|Text):\s*(.*)', line)
            if match:
                key = match.group(1)
                value = match.group(2).strip()
                sections[current][key] = value
    return sections


def get_title_slug(name):
    return name.lower().replace('&', 'and').replace(' ', '-').replace('/', '-').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')


def english_page_copy():
    return parse_copy_file(Path('WEBSITE_COPY_EN.md'))


def german_page_copy():
    return parse_copy_file(Path('WEBSITE_COPY_DE.md'))


def build_service_copy(slug, lang):
    if lang == 'en':
        titles = {
            'screen-printing': ('Screen printing for premium apparel', 'High-precision screen printing for sharp logos and durable color coverage.'),
            'embroidery': ('Professional embroidery for premium branding', 'Swiss-managed embroidery for precise logo application and premium craftsmanship.'),
            'sublimation-printing': ('Sublimation printing for technical apparel', 'Durable dye-sublimation for activewear, teamwear and promotional items.'),
            'heat-transfer-printing': ('Heat transfer printing for custom branding', 'Flexible transfer printing for crisp design details on apparel and accessories.'),
            'private-label-manufacturing': ('Private label apparel manufacturing', 'End-to-end production for bespoke private label collections and custom packaging.'),
            'oem-clothing-production': ('OEM clothing production for brands', 'Reliable OEM manufacturing with Swiss oversight and scalable apparel execution.'),
            'custom-labels': ('Custom labels and branding solutions', 'Premium labels and tags designed for brand identity, packaging and garment finishing.'),
            'hang-tags': ('Branded hang tags for apparel', 'High-quality hang tags for premium presentation and professional merchandising.'),
            'packaging-solutions': ('Packaging solutions for apparel delivery', 'Smart packaging that protects garments and reflects your brand story.'),
            'product-development': ('Apparel product development support', 'Technical guidance from prototypes to production-ready apparel collections.'),
            'sampling': ('Sampling services for apparel projects', 'Sample runs and prototypes to verify fit, materials and finishing before full production.'),
            'quality-control': ('Quality control for every production stage', 'Rigorous inspection and testing ensures consistent premium results.'),
            'worldwide-shipping': ('Worldwide shipping for Swiss-managed apparel', 'Reliable international logistics with clear tracking and safe delivery.'),
        }
    else:
        titles = {
            'siebdruck': ('Siebdruck für Premium-Bekleidung', 'Hochpräziser Siebdruck für klare Logos und langlebige Farbbeständigkeit.'),
            'stickerei': ('Professionelle Stickerei für Premium-Branding', 'Schweizerisch gesteuerte Stickerei für präzise Logos und hochwertige Ausführung.'),
            'sublimationsdruck': ('Sublimationsdruck für Funktionsbekleidung', 'Langlebiger Sublimationsdruck für Sport- und Teamwear sowie Merch.'),
            'transferdruck': ('Transferdruck für individuelles Branding', 'Flexibler Transferdruck für scharfe Designs auf Apparel und Accessoires.'),
            'private-label-fertigung': ('Private-Label-Fertigung für Bekleidung', 'End-to-end-Produktion für individuelle Private-Label-Kollektionen.'),
            'oem-bekleidungsproduktion': ('OEM-Bekleidungsproduktion für Marken', 'Zuverlässige OEM-Fertigung mit Schweizer Qualitätssteuerung.'),
            'etiketten-labels': ('Custom Labels & Etiketten', 'Premium-Etiketten und Labels für Markenidentität und hochwertige Ausführung.'),
            'hang-tags': ('Hang Tags für Premium-Bekleidung', 'Hochwertige Hang Tags für professionelle Marken- und Verkaufspräsentation.'),
            'verpackungsgeloesungen': ('Verpackungslösungen für Bekleidung', 'Sichere Verpackungen, die Produkte schützen und Marke stärken.'),
            'produktentwicklung': ('Produktentwicklung für Apparel-Projekte', 'Technische Begleitung von der Idee bis zur produktionsreifen Kollektion.'),
            'musterproduktion': ('Musterproduktion für Bekleidungsprojekte', 'Sample Runs und Prototypen zur Überprüfung von Passform und Material.'),
            'qualitaetskontrolle': ('Qualitätskontrolle in jedem Produktionsschritt', 'Gründliche Prüfung für konsistent hochwertige Ergebnisse.'),
            'weltweiter-versand': ('Weltweiter Versand für Schweizer Bekleidung', 'Verlässliche internationale Logistik mit sicherer Lieferung.'),
        }
    return titles.get(slug, (slug.replace('-', ' ').title(), 'Premium apparel services with Swiss-managed production and reliable quality.'))


def build_main_section_copies(page_type, title, lang, copy):
    if lang == 'en':
        if page_type == 'home':
            return [
                ('Swiss-managed production for premium apparel', 'TShirtSwiss blends Swiss oversight with Thai manufacturing expertise to deliver reliable, premium apparel production.'),
                ('Trusted by Swiss businesses and European brands', 'Our clients value the consistency, speed and quality of our factory-direct apparel manufacturing.'),
                ('Product categories for Swiss B2B customers', 'From workwear to private label collections, our production is built for Swiss brands and corporate teams.'),
                ('Quality assurance at every stage', 'Every order is reviewed against Swiss standards from sampling to final shipment.'),
                ('Start your premium apparel project', 'Request a quote, review product options, and begin a reliable manufacturing partnership.'),
            ]
        if page_type == 'products':
            return [
                ('Products built for Swiss business', 'Our product range is optimized for Swiss B2B apparel, including corporate wear, uniforms and event merchandise.'),
                ('Premium materials and reliable production', 'We source fabrics and finishes that match premium Swiss expectations and durable end-use.'),
                ('Customization and branding', 'Our product teams support logos, embroidery, printing and bespoke design details.'),
                ('Scalable production and delivery', 'From small runs to larger volumes, we manage the production timeline and logistics with care.'),
                ('Explore products that fit your needs', 'Choose the right category for your brand, event or team with clear industry-aligned options.'),
            ]
        if page_type == 'industries':
            return [
                ('Industries that trust premium apparel', 'Swiss companies across healthcare, hospitality, sports and corporate sectors choose our production network.'),
                ('Industry-specific product solutions', 'We match the right apparel categories to each sector with tailored material and finishing options.'),
                ('Swiss-managed quality control', 'Each industry order is inspected to ensure reliability, compliance and professional presentation.'),
                ('Efficient production for branded apparel', 'Our process minimizes handoff risk and delivers apparel on schedule for your campaigns.'),
                ('Start the conversation with our team', 'Tell us your industry needs and we will recommend the ideal apparel solution.'),
            ]
        if page_type == 'services':
            return [
                ('Swiss-managed apparel services', 'Our service portfolio supports every premium apparel production need from print to packaging.'),
                ('Precision and quality in execution', 'Each service is delivered with Swiss project management and consistent manufacturing control.'),
                ('Comprehensive support for brands', 'We handle samples, production planning, customization and logistics from one partner.'),
                ('Designed for Swiss B2B customers', 'Our services are built around Swiss expectations for quality, reliability and transparency.'),
                ('Ready to start your apparel service project', 'Request a quote today and begin a premium manufacturing workflow.'),
            ]
        return [
            ('Swiss-managed premium apparel production', 'TShirtSwiss combines Swiss project management and Thai manufacturing for premium apparel results.'),
            ('Quality control and reliable delivery', 'Our process ensures consistent finishing, strong branding and dependable logistics.'),
            ('Designed for Swiss business customers', 'We work with Swiss brands, teams and product developers to create tailored apparel collections.'),
            ('Premium manufacturing at scale', 'From prototypes to full production, we maintain high standards for every order.'),
            ('Start your next apparel project', 'Contact us to discuss your requirements and receive a quote for premium apparel manufacturing.'),
        ]
    else:
        if page_type == 'home':
            return [
                ('Schweizerisch geführte Premium-Bekleidungsfertigung', 'TShirtSwiss vereint Schweizer Projektsteuerung mit thailändischer Fertigungskompetenz für verlässliche Premium-Produktion.'),
                ('Verlässliche Fertigung für Schweizer Unternehmen', 'Unsere Kunden schätzen die Konsistenz, Geschwindigkeit und Qualität unserer fabrikdirekten Produkte.'),
                ('Produktkategorien für Schweizer B2B-Kunden', 'Von Workwear bis Private Label liefern wir Kategorien, die für Schweizer Marken und Teams entwickelt wurden.'),
                ('Qualitätskontrolle in jedem Produktionsschritt', 'Jeder Auftrag wird nach Schweizer Standards geprüft – von Mustern bis zur finalen Auslieferung.'),
                ('Starten Sie Ihr Premium-Bekleidungsprojekt', 'Fordern Sie ein Angebot an, prüfen Sie Produktoptionen und starten Sie eine zuverlässige Produktionspartnerschaft.'),
            ]
        if page_type == 'products':
            return [
                ('Produktkategorien für Schweizer B2B-Kunden', 'Unsere Produktpalette ist optimiert für Schweizer Geschäftskunden, von Corporate Apparel bis Veranstaltungswaren.'),
                ('Premium-Materialien und verlässliche Produktion', 'Wir verwenden Stoffe und Veredelungen, die Premium-Ansprüche und lange Haltbarkeit erfüllen.'),
                ('Personalisierung und Branding', 'Wir unterstützen Logos, Stickereien, Druck und maßgeschneiderte Details für Ihr Erscheinungsbild.'),
                ('Skalierbare Produktion und Lieferung', 'Von kleinen Auflagen bis zu größeren Mengen steuern wir Zeitplan und Logistik sorgfältig.'),
                ('Entdecken Sie passende Produktlösungen', 'Wählen Sie die richtige Kategorie für Ihre Marke, Ihr Event oder Ihr Team.'),
            ]
        if page_type == 'industries':
            return [
                ('Branchen, die auf Premium-Apparel vertrauen', 'Schweizer Unternehmen aus Healthcare, Gastgewerbe, Sport und Corporate setzen auf unsere hochwertige Produktion.'),
                ('Branchenspezifische Produktlösungen', 'Wir stimmen die richtigen Bekleidungskategorien auf jede Branche ab – mit passenden Materialien und Veredelungen.'),
                ('Schweizer Qualitätskontrolle', 'Jeder Branchenauftrag wird geprüft, damit Zuverlässigkeit, Compliance und Darstellung stimmen.'),
                ('Effiziente Produktion für Markenbekleidung', 'Unser Prozess minimiert Risiken und liefert Termineinhaltung für Ihre Projekte.'),
                ('Starten Sie das Gespräch mit unserem Team', 'Teilen Sie uns Ihren Bedarf mit und wir empfehlen die passende Bekleidungslösung.'),
            ]
        if page_type == 'services':
            return [
                ('Schweizerisch geführte Bekleidungsservices', 'Unser Serviceangebot deckt jeden Bedarf ab – von Druck über Veredelung bis Versand.'),
                ('Präzision und Qualität in der Ausführung', 'Jeder Service wird mit Schweizer Projektsteuerung und Fertigungskontrolle geliefert.'),
                ('Umfassende Unterstützung für Marken', 'Wir organisieren Muster, Produktionsplanung, Personalisierung und Logistik aus einer Hand.'),
                ('Für Schweizer B2B-Kunden entwickelt', 'Unsere Services entsprechen den Erwartungen an Verlässlichkeit, Transparenz und Qualität.'),
                ('Bereit für Ihr Apparel-Serviceprojekt', 'Fordern Sie ein Angebot an und starten Sie eine hochwertige Fertigungspartnerschaft.'),
            ]
        return [
            ('Schweizerisch geführte Premium-Bekleidungsproduktion', 'TShirtSwiss vereint Schweizer Management und thailändische Fertigung für hochwertige Kleidung.'),
            ('Qualitätskontrolle und zuverlässige Lieferung', 'Unser Prozess sichert ein konsistentes Finish, starkes Branding und gesicherte Logistik.'),
            ('Für Schweizer Geschäftskunden gemacht', 'Wir arbeiten mit Marken, Teams und Produktentwicklern für maßgeschneiderte Kollektionen.'),
            ('Premium-Fertigung von Prototyp bis Serie', 'Ob Muster oder Vollproduktion – wir sorgen für hohe Standards in jedem Schritt.'),
            ('Starten Sie Ihr nächstes Bekleidungsprojekt', 'Kontaktieren Sie uns, um Ihre Anforderungen zu besprechen und ein Angebot zu erhalten.'),
        ]


def build_page_copy(lang_copy, path_parts, lang):
    page_type = 'generic'
    subpage = ''
    if len(path_parts) == 1:
        title = path_parts[-1].replace('-', ' ').title()
    else:
        title = path_parts[-2].replace('-', ' ').title()
    if title == 'Home':
        title = 'Swiss-managed premium apparel manufacturing in Thailand' if lang == 'en' else 'Schweizerisch geführte Premium-Bekleidungsfertigung in Thailand'
    elif title == 'Products':
        page_type = 'products'
    elif title == 'Industries':
        page_type = 'industries'
    elif title == 'Services':
        page_type = 'services'
    elif title == 'Request A Quote':
        page_type = 'quote'
    elif title in ['Contact', 'Kontakt']:
        page_type = 'contact'
    elif title in ['Case Studies', 'Case Studies']:
        page_type = 'case studies'
    elif title == 'Faq':
        page_type = 'faq'
    elif title == 'Resources':
        page_type = 'resources'
    elif title == 'Blog':
        page_type = 'blog'
    elif title == 'About Us':
        page_type = 'about us'
    elif title == 'Production':
        page_type = 'production'

    if 'industries' in path_parts and len(path_parts) > 3:
        page_type = 'industry'
        subpage = path_parts[-2]
    if 'products' in path_parts and len(path_parts) > 3:
        page_type = 'product'
        subpage = path_parts[-2]
    if 'services' in path_parts and len(path_parts) > 3:
        page_type = 'service'
        subpage = path_parts[-2]

    if page_type == 'product':
        if lang == 'en':
            mapping = {
                'custom-t-shirts': 'Custom T-Shirts',
                'custom-polos': 'Custom Polos',
                'hoodies-sweatshirts': 'Hoodies & Sweatshirts',
                'jackets-softshells': 'Jackets & Softshells',
                'workwear': 'Workwear',
                'healthcare-uniforms': 'Healthcare Uniforms',
                'medical-scrubs': 'Medical Scrubs',
                'corporate-apparel': 'Corporate Apparel',
                'sportswear': 'Sportswear',
                'rashguards': 'Rashguards',
                'mma-shorts': 'MMA Shorts',
                'muay-thai-shorts': 'Muay Thai Shorts',
                'caps-headwear': 'Caps & Headwear',
                'tote-bags': 'Tote Bags',
                'promotional-merchandise': 'Promotional Merchandise',
                'private-label-clothing': 'Private Label Clothing',
            }
        else:
            mapping = {
                'individualisierte-t-shirts': 'Individualisierte T-Shirts',
                'individualisierte-poloshirts': 'Individualisierte Poloshirts',
                'hoodies-sweatshirts': 'Hoodies & Sweatshirts',
                'jacken-softshells': 'Jacken & Softshells',
                'workwear': 'Workwear',
                'healthcare-uniformen': 'Healthcare Uniformen',
                'medizinische-kitteltaschen': 'Medizinische Kitteltaschen',
                'corporate-apparel': 'Corporate Apparel',
                'sportswear': 'Sportswear',
                'rashguards': 'Rashguards',
                'mma-shorts': 'MMA Shorts',
                'muay-thai-shorts': 'Muay Thai Shorts',
                'caps-headwear': 'Caps & Headwear',
                'tragetaschen': 'Tragetaschen',
                'werbeartikel': 'Werbeartikel',
                'private-label-bekleidung': 'Private Label Bekleidung',
            }
        title = mapping.get(subpage, title)
    elif page_type == 'industry':
        if lang == 'en':
            mapping = {
                'construction-trades': 'Construction & Trades',
                'healthcare': 'Healthcare',
                'hospitality': 'Hospitality',
                'sports-fitness': 'Sports & Fitness',
                'combat-sports': 'Combat Sports',
                'corporate-apparel': 'Corporate Apparel',
                'events-merchandise': 'Events & Merchandise',
                'ecommerce-brands': 'Ecommerce Brands',
            }
        else:
            mapping = {
                'bau-handwerk': 'Bau & Handwerk',
                'healthcare': 'Healthcare',
                'gastgewerbe': 'Gastgewerbe',
                'sport-fitness': 'Sport & Fitness',
                'kampfsport': 'Kampfsport',
                'corporate-apparel': 'Corporate Apparel',
                'events-merchandise': 'Events & Merchandise',
                'ecommerce-brands': 'Ecommerce Brands',
            }
        title = mapping.get(subpage, title)
    elif page_type == 'service':
        if lang == 'en':
            mapping = {
                'screen-printing': 'Screen Printing',
                'embroidery': 'Embroidery',
                'sublimation-printing': 'Sublimation Printing',
                'heat-transfer-printing': 'Heat Transfer Printing',
                'private-label-manufacturing': 'Private Label Manufacturing',
                'oem-clothing-production': 'OEM Clothing Production',
                'custom-labels': 'Custom Labels',
                'hang-tags': 'Hang Tags',
                'packaging-solutions': 'Packaging Solutions',
                'product-development': 'Product Development',
                'sampling': 'Sampling',
                'quality-control': 'Quality Control',
                'worldwide-shipping': 'Worldwide Shipping',
            }
        else:
            mapping = {
                'siebdruck': 'Siebdruck',
                'stickerei': 'Stickerei',
                'sublimationsdruck': 'Sublimationsdruck',
                'transferdruck': 'Transferdruck',
                'private-label-fertigung': 'Private Label Fertigung',
                'oem-bekleidungsproduktion': 'OEM-Bekleidungsproduktion',
                'etiketten-labels': 'Etiketten & Labels',
                'hang-tags': 'Hang Tags',
                'verpackungsgeloesungen': 'Verpackungslösungen',
                'produktentwicklung': 'Produktentwicklung',
                'musterproduktion': 'Musterproduktion',
                'qualitaetskontrolle': 'Qualitätskontrolle',
                'weltweiter-versand': 'Weltweiter Versand',
            }
        title = mapping.get(subpage, title)
    
    hero = {'H1': title, 'H2': None, 'Intro': None}
    if page_type == 'home':
        hero['H1'] = lang_copy.get('Hero', {}).get('H1', hero['H1'])
        hero['H2'] = lang_copy.get('Hero', {}).get('H2', '')
        hero['Intro'] = lang_copy.get('Hero', {}).get('H2', '')
    elif page_type == 'product':
        if lang == 'en':
            section_key = title
        else:
            section_key = title
        hero['H1'] = lang_copy.get(section_key, {}).get('H1', hero['H1'])
        hero['H2'] = lang_copy.get(section_key, {}).get('H2', '')
        hero['Intro'] = lang_copy.get(section_key, {}).get('Intro', '')
    elif page_type == 'industry':
        hero['H1'] = lang_copy.get(title, {}).get('H1', hero['H1'])
        hero['H2'] = lang_copy.get(title, {}).get('H2', '')
        hero['Intro'] = lang_copy.get(title, {}).get('Intro', '')
    elif page_type == 'faq':
        hero['H1'] = 'FAQ' if lang == 'en' else 'FAQ'
        hero['H2'] = lang_copy.get('FAQ', {}).get('H2', 'Frequently asked questions about Swiss-managed apparel manufacturing' if lang == 'en' else 'Häufige Fragen zur Schweizerisch geführten Bekleidungsproduktion')
        hero['Intro'] = 'Find answers to common questions about production, quality and logistics.' if lang == 'en' else 'Antworten auf häufige Fragen zur Produktion, Qualität und Logistik.'
    elif page_type == 'quote':
        hero['H1'] = 'Request a Quote' if lang == 'en' else 'Angebot anfragen'
        hero['H2'] = lang_copy.get('Quote CTA', {}).get('H2', 'Start your premium apparel project' if lang == 'en' else 'Starten Sie Ihr Premium-Bekleidungsprojekt')
        hero['Intro'] = 'Share your project details and we will respond with a tailored production quote.' if lang == 'en' else 'Teilen Sie Ihre Projektanforderungen mit uns und wir senden Ihnen ein individuelles Angebot.'
    elif page_type == 'contact':
        hero['H1'] = 'Contact' if lang == 'en' else 'Kontakt'
        hero['H2'] = 'Speak with our Swiss-managed apparel production team.' if lang == 'en' else 'Sprechen Sie mit unserem Schweizer Bekleidungsproduktionsteam.'
        hero['Intro'] = 'Email us or request a quote to start your premium apparel project.' if lang == 'en' else 'Schreiben Sie uns oder fordern Sie ein Angebot an, um Ihr Premium-Bekleidungsprojekt zu starten.'
    elif page_type == 'about us':
        hero['H1'] = 'About Us' if lang == 'en' else 'Über uns'
        hero['H2'] = 'Swiss-managed apparel manufacturing with premium service.' if lang == 'en' else 'Schweizerisch geführte Bekleidungsfertigung mit Premium-Service.'
        hero['Intro'] = 'We combine Swiss project management and Thai production to deliver reliable premium apparel.' if lang == 'en' else 'Wir verbinden Schweizer Projektmanagement mit thailändischer Fertigung für verlässliche Premium-Bekleidung.'
    elif page_type == 'production':
        hero['H1'] = 'Production' if lang == 'en' else 'Produktion'
        hero['H2'] = 'Premium manufacturing and quality control for Swiss apparel orders.' if lang == 'en' else 'Premium-Fertigung und Qualitätskontrolle für Schweizer Bekleidungsaufträge.'
        hero['Intro'] = 'Our production process is designed to deliver consistent, high-quality apparel with Swiss oversight.' if lang == 'en' else 'Unser Produktionsprozess liefert konsistente, hochwertige Bekleidung mit Schweizer Aufsicht.'
    elif page_type == 'case studies':
        hero['H1'] = 'Case Studies' if lang == 'en' else 'Case Studies'
        hero['H2'] = 'Examples of premium apparel projects and manufacturing partnerships.' if lang == 'en' else 'Beispiele für Premium-Bekleidungsprojekte und Fertigungspartnerschaften.'
        hero['Intro'] = 'Explore how Swiss-managed production supports quality apparel for brands and teams.' if lang == 'en' else 'Erfahren Sie, wie Schweizerisch geführte Produktion Premium-Bekleidung für Marken und Teams liefert.'
    elif page_type == 'resources':
        hero['H1'] = 'Resources' if lang == 'en' else 'Ressourcen'
        hero['H2'] = 'Guides, FAQs and resources for premium apparel production.' if lang == 'en' else 'Leitfäden, FAQs und Ressourcen für Premium-Bekleidungsproduktion.'
        hero['Intro'] = 'Find helpful content for planning, sampling and ordering apparel production.' if lang == 'en' else 'Finden Sie hilfreiche Inhalte für Planung, Muster und Bekleidungsproduktion.'
    elif page_type == 'blog':
        hero['H1'] = 'Blog' if lang == 'en' else 'Blog'
        hero['H2'] = 'Insights and updates from Swiss-managed apparel manufacturing.' if lang == 'en' else 'Einblicke und Neuigkeiten aus der Schweizer Bekleidungsfertigung.'
        hero['Intro'] = 'Read articles on apparel production, branding and premium operations.' if lang == 'en' else 'Lesen Sie Artikel zu Bekleidungsproduktion, Branding und Premium-Operations.'
    else:
        hero['H2'] = hero['H2'] or ('Premium apparel production with Swiss quality control.' if lang == 'en' else 'Premium-Bekleidungsproduktion mit Schweizer Qualitätskontrolle.')
        hero['Intro'] = hero['Intro'] or ('Swiss-managed apparel production designed for reliable quality and delivery.' if lang == 'en' else 'Schweizerisch geführte Bekleidungsproduktion für verlässliche Qualität und Lieferung.')

    return hero, page_type, title


def section_copies(page_type, title, slug, lang, copy):
    if page_type == 'product':
        return [
            (f'{title} overview', copy.get('Intro') or f'Our Swiss-managed production combines premium fabrics and precise craftsmanship for {title.lower()}.'),
            ('Swiss quality and craft', f'Each {title.lower()} order is produced with controlled processes, accurate fit and reliable finishing.'),
            ('Customization and branding', f'We support printing, embroidery and premium detailing to make your apparel brand-ready.'),
            ('Production & inspection', f'Swiss oversight ensures every {title.lower()} run is reviewed for quality and consistency.'),
            ('Packaging and delivery', f'Delivery is organized to meet Swiss B2B expectations with secure packaging and reliable logistics.'),
        ]
    if page_type == 'industry':
        return [
            (f'{title} solutions for Swiss brands', copy.get('Intro') or f'Tailored apparel solutions for the {title.lower()} sector, designed for reliability and presentation.'),
            ('Recommended product categories', 'We match the right apparel mix to your sector with workwear, uniforms and brand merchandise.'),
            ('Swiss-managed quality standards', 'Every order follows Swiss quality checks to deliver dependable apparel for your industry.'),
            ('Design and function', 'We balance functional construction with premium presentation for professional teams.'),
            ('Fast project briefing and quote', 'Start with a clear brief and we will recommend the ideal production plan for your business.'),
        ]
    if page_type == 'service':
        h1, intro = build_service_copy(slug, lang)
        return [
            (h1, intro),
            ('How our service works', 'Swiss-managed processes guide every stage from sample to finished apparel production.'),
            ('Quality & consistency', 'Our service is built around premium materials, precision workmanship and inspection.'),
            ('Brand-friendly execution', 'We ensure your labels, prints and packaging reflect your premium brand identity.'),
            ('Next steps', 'Request a quote to discuss your service requirements and production schedule.'),
        ]
    if page_type == 'home':
        return build_main_section_copies('home', title, lang, copy)
    if page_type == 'products':
        return build_main_section_copies('products', title, lang, copy)
    if page_type == 'industries':
        return build_main_section_copies('industries', title, lang, copy)
    if page_type == 'services':
        return build_main_section_copies('services', title, lang, copy)
    if page_type == 'quote':
        return [
            ('Start your premium apparel project', 'Submit your project details and receive a tailored quote for manufacturing and delivery.' if lang == 'en' else 'Senden Sie Ihre Projektangaben und erhalten Sie ein individuelles Angebot.'),
            ('Swiss-managed project planning', 'We review fabrics, quantities and timelines to create a realistic production plan.' if lang == 'en' else 'Wir prüfen Stoffe, Mengen und Zeitpläne für einen realistischen Fertigungsplan.'),
            ('Reliable quality and delivery', 'Our team ensures the final apparel meets Swiss standards before shipment.' if lang == 'en' else 'Unser Team stellt sicher, dass die Bekleidung vor dem Versand Schweizer Standards erfüllt.'),
        ]
    if page_type == 'contact':
        return [
            ('Reach our Swiss production team', 'Contact us to discuss your premium apparel project and ask about timelines or samples.' if lang == 'en' else 'Kontaktieren Sie uns, um Ihr Premium-Bekleidungsprojekt zu besprechen oder Fragen zu stellen.'),
            ('What happens next', 'We will follow up with a tailored proposal, production options and estimated delivery dates.' if lang == 'en' else 'Wir melden uns mit einem maßgeschneiderten Vorschlag, Produktionsoptionen und Lieferdaten.'),
            ('Office and support', 'Swiss HQ plus Thailand manufacturing support means local oversight and international execution.' if lang == 'en' else 'Schweizer HQ und thailändische Fertigungsunterstützung für lokale Steuerung und internationale Ausführung.'),
        ]
    if page_type == 'about us':
        return [
            ('Our Swiss-managed story', 'We combine Swiss leadership with Thai manufacturing experience to build premium apparel.' if lang == 'en' else 'Wir verbinden Schweizer Führung mit thailändischer Fertigungserfahrung für Premium-Bekleidung.'),
            ('A premium partner for brands', 'Swiss oversight ensures consistent quality, brand-safe execution and reliable delivery.' if lang == 'en' else 'Schweizer Aufsicht sorgt für gleichbleibende Qualität, markensichere Umsetzung und zuverlässige Lieferung.'),
            ('Global production with local focus', 'Our process is designed for Swiss standards and international apparel demand.' if lang == 'en' else 'Unser Prozess ist auf Schweizer Standards und internationale Bekleidungsanforderungen ausgerichtet.'),
        ]
    if page_type in ['case studies', 'resources', 'blog', 'faq', 'production']:
        return [
            ('Premium content and insights', 'Explore the expertise and experience behind our Swiss-managed apparel projects.' if lang == 'en' else 'Entdecken Sie die Expertise hinter unseren schweizerisch geführten Bekleidungsprojekten.'),
            ('Practical guidance for apparel production', 'Find useful information on production, quality and project planning.' if lang == 'en' else 'Finden Sie hilfreiche Informationen zu Produktion, Qualität und Projektplanung.'),
        ]
    return [
        ('Premium apparel production', 'Swiss-managed quality, Thai manufacturing and reliable delivery for your apparel project.' if lang == 'en' else 'Schweizerisch geführte Qualität, thailändische Fertigung und verlässliche Lieferung für Ihr Bekleidungsprojekt.'),
        ('Quality-oriented process', 'Every project is guided to meet premium expectations and consistent results.' if lang == 'en' else 'Jedes Projekt wird auf Premium-Erwartungen und konsistente Ergebnisse ausgerichtet.'),
    ]


def replace_first(pattern, repl, text, flags=0):
    return re.sub(pattern, repl, text, count=1, flags=flags)


def apply_page_content(html, hero, sections, lang):
    html = re.sub(r'<title>.*?</title>', f'<title>{hero["H1"]}</title>', html, flags=re.DOTALL)
    hero_block = re.search(r'(<section class="hero">.*?</section>)', html, flags=re.DOTALL)
    if hero_block:
        hero_html = hero_block.group(1)
        hero_html = replace_first(r'<h1>.*?</h1>', f'<h1>{hero["H1"]}</h1>', hero_html, flags=re.DOTALL)
        hero_html = replace_first(r'<p>.*?</p>', f'<p>{hero["Intro"]}</p>', hero_html, flags=re.DOTALL)
        if 'CTA 1' in hero:
            href = '/pages-de/request-a-quote/' if lang == 'de' else '/pages/request-a-quote/'
            hero_html = re.sub(r'(<a[^>]*class="button"[^>]*>)(.*?)(</a>)', lambda m: m.group(1) + hero['CTA 1'] + m.group(3), hero_html, count=1, flags=re.DOTALL)
            hero_html = re.sub(r'<div class="section-footer">.*?</div>', f'<div class="section-footer"><a class="button" href="{href}">{hero["CTA 1"]}</a></div>', hero_html, count=1, flags=re.DOTALL)
        html = html.replace(hero_block.group(1), hero_html)
    sections_html = re.findall(r'(<section class="section">.*?</section>)', html, flags=re.DOTALL)
    for idx, block in enumerate(sections_html):
        if idx >= len(sections):
            break
        heading, paragraph = sections[idx]
        new_block = replace_first(r'<h2>.*?</h2>', f'<h2>{heading}</h2>', block, flags=re.DOTALL)
        new_block = replace_first(r'<p>.*?</p>', f'<p>{paragraph}</p>', new_block, flags=re.DOTALL)
        html = html.replace(block, new_block, 1)
    return html


def main():
    en_copy = english_page_copy()
    de_copy = german_page_copy()
    root = Path('wordpress')
    for html_path in sorted(root.rglob('index.html')):
        rel = html_path.relative_to(root)
        parts = rel.parts
        lang = 'de' if parts[0] == 'pages-de' else 'en'
        page_parts = list(parts)[1:-1]  # skip pages or pages-de and index.html
        hero, page_type, title = build_page_copy(de_copy if lang == 'de' else en_copy, page_parts, lang)
        hero['CTA 1'] = 'Angebot anfragen' if lang == 'de' else 'Request a Quote'
        sections = section_copies(page_type, title, page_parts[-1] if page_parts else 'home', lang, de_copy if lang == 'de' else en_copy)
        html = html_path.read_text(encoding='utf-8')
        updated = apply_page_content(html, hero, sections, lang)
        html_path.write_text(updated, encoding='utf-8')
        print(f'Updated {html_path}')


if __name__ == '__main__':
    main()
