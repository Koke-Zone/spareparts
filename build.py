#!/usr/bin/env python3
"""
Al-Bais Motors — static site builder.

Edit the CONFIG below (phone, email, address, social links, domain),
then run:   python3 build.py
The finished website is written to the  dist/  folder — upload that folder.
"""
import json
import shutil
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

# ---------------------------------------------------------------------------
# CONFIG — change these and rebuild
# ---------------------------------------------------------------------------
CONFIG = {
    "name": "Al-Bais Motors",
    "tagline": "Motorcycle Spare Parts & Repair",
    "city": "Sukkur",
    "address": "Sukkur, Sindh, Pakistan",
    "phone_display": "0300 3100751",
    "phone_intl": "+923003100751",
    "whatsapp": "923003100751",            # digits only, with country code
    "email": "aliasad@gmail.com",           # form submissions arrive here
    "hours": "Open today until 8:00 PM",
    "hours_short": "Closes 8:00 PM",
    # Map shown on the contact page and the "Get directions" link
    "map_query": "Sukkur, Sindh, Pakistan",
    # The shop's Google Maps listing (used for "Review us on Google")
    "google_listing": "https://www.google.com/maps/place/Al-Bais+Shop/@27.3050744,68.401751,737m/data=!3m2!1e3!4b1!4m6!3m5!1s0x3935970035225ea7:0xba86d67ec56d0807!8m2!3d27.3050697!4d68.4043259!16s%2Fg%2F11zblzqdqn",
    # Social profiles — paste the full link; leave "" to hide the icon
    "facebook": "",
    "instagram": "",
    "tiktok": "",
    "youtube": "",
    # Your domain, used for SEO tags and the sitemap (no trailing slash)
    "site_url": "https://www.your-domain.com",
    "policy_updated": "12 November 2026",
}
CONFIG["form_endpoint"] = "https://formsubmit.co/ajax/" + CONFIG["email"]
CONFIG["wa_link"] = "https://wa.me/" + CONFIG["whatsapp"] + "?text=" + quote(
    "Hi Al-Bais Motors, I need help with my bike.")
CONFIG["map_embed"] = "https://www.google.com/maps?q=" + quote(CONFIG["map_query"]) + "&output=embed"
CONFIG["map_link"] = "https://www.google.com/maps/search/?api=1&query=" + quote(CONFIG["map_query"])


def wa(text):
    return "https://wa.me/" + CONFIG["whatsapp"] + "?text=" + quote(text)


# ---------------------------------------------------------------------------
# Icons (one SVG sprite, included once per page)
# ---------------------------------------------------------------------------
SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></symbol>
<symbol id="i-close" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
<symbol id="i-whatsapp" viewBox="0 0 24 24"><path d="M3.5 20.5l1.3-4A8.5 8.5 0 1 1 8 19.6z"/><path d="M9 8.5c.2-.4.6-.5.9-.4l.8 1.8c.1.3 0 .5-.2.7l-.5.5c.6 1.2 1.6 2.2 2.8 2.8l.5-.5c.2-.2.5-.3.7-.2l1.8.8c.2.3 0 .7-.4.9-.8.5-1.7.6-2.6.2a8 8 0 0 1-4.1-4.1c-.4-.9-.3-1.8.3-2.5z" stroke-width="1.4"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-list" viewBox="0 0 24 24"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/></symbol>
<symbol id="i-wrench" viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></symbol>
<symbol id="i-truck" viewBox="0 0 24 24"><path d="M1 4h14v11H1zM15 8h4l3 3v4h-7z"/><circle cx="5.5" cy="17.5" r="2"/><circle cx="18.5" cy="17.5" r="2"/></symbol>
<symbol id="i-tag" viewBox="0 0 24 24"><path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.2"/></symbol>
<symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></symbol>
<symbol id="i-chat" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></symbol>
<symbol id="i-star" viewBox="0 0 24 24"><path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></symbol>
<symbol id="i-share" viewBox="0 0 24 24"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></symbol>
<symbol id="i-link" viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></symbol>
<symbol id="i-engine" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></symbol>
<symbol id="i-brake" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/><circle cx="12" cy="6.5" r=".6"/><circle cx="17.5" cy="12" r=".6"/><circle cx="12" cy="17.5" r=".6"/><circle cx="6.5" cy="12" r=".6"/><path d="M18 4.5a10 10 0 0 1 2 3"/></symbol>
<symbol id="i-clutch" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><path d="M12 3v4M12 17v4M3 12h4M17 12h4"/></symbol>
<symbol id="i-chain" viewBox="0 0 24 24"><rect x="2" y="8" width="11" height="8" rx="4"/><rect x="11" y="8" width="11" height="8" rx="4"/></symbol>
<symbol id="i-electric" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9z"/></symbol>
<symbol id="i-tyre" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="5"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></symbol>
<symbol id="i-oil" viewBox="0 0 24 24"><path d="M12 2.7l5.7 5.7a8 8 0 1 1-11.3 0z"/><path d="M9 14a3 3 0 0 0 3 3"/></symbol>
<symbol id="i-accessory" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.7l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.7l7 4a2 2 0 0 0 2 0l7-4a2 2 0 0 0 1-1.7z"/><path d="M3.3 7L12 12l8.7-5M12 22V12"/></symbol>
<symbol id="i-filter" viewBox="0 0 24 24"><path d="M22 3H2l8 9.5V19l4 2v-8.5z"/></symbol>
<symbol id="i-cable" viewBox="0 0 24 24"><path d="M3 12c3-6 6 6 9 0s6 6 9 0"/><circle cx="3" cy="12" r="1"/><circle cx="21" cy="12" r="1"/></symbol>
<symbol id="i-facebook" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></symbol>
<symbol id="i-instagram" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6"/></symbol>
<symbol id="i-tiktok" viewBox="0 0 24 24"><path d="M14 3v11.5a4 4 0 1 1-4-4"/><path d="M14 3c.6 2.8 2.6 4.7 5.5 5"/></symbol>
<symbol id="i-youtube" viewBox="0 0 24 24"><path d="M22.5 6.4a2.8 2.8 0 0 0-2-2C18.9 4 12 4 12 4s-6.9 0-8.5.4a2.8 2.8 0 0 0-2 2A29 29 0 0 0 1 12a29 29 0 0 0 .5 5.6 2.8 2.8 0 0 0 2 2c1.6.4 8.5.4 8.5.4s6.9 0 8.5-.4a2.8 2.8 0 0 0 2-2A29 29 0 0 0 23 12a29 29 0 0 0-.5-5.6z"/><path d="M9.8 15.3l5.7-3.3-5.7-3.3z"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M4 4l16 16M20 4l-6.6 7.2M10.6 13.1L4 20"/></symbol>
</svg>"""

LOGO = """<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="12" fill="#e8491d"/><circle cx="24" cy="24" r="13" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="4 3.2"/><path d="M28.6 15.2a5.6 5.6 0 0 0-5.3 7.4L15 30.9a2.3 2.3 0 0 0 3.3 3.3l8.3-8.3a5.6 5.6 0 0 0 7.3-6.6l-3.2 3.2-2.8-.9-.9-2.8 3.2-3.2a5.6 5.6 0 0 0-1.6-.4z" fill="#fff"/></svg>"""

HERO_ART = """<svg viewBox="0 0 520 400" role="img" aria-label="Illustration of a motorcycle with spare parts">
  <defs>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#e8491d" stop-opacity=".35"/><stop offset="1" stop-color="#e8491d" stop-opacity="0"/></radialGradient>
  </defs>
  <circle cx="270" cy="210" r="190" fill="url(#glow)"/>
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <!-- wheels -->
    <circle cx="130" cy="290" r="72" stroke="#2b2f38" stroke-width="20"/>
    <circle cx="130" cy="290" r="50" stroke="#545b68" stroke-width="3"/>
    <circle cx="400" cy="290" r="72" stroke="#2b2f38" stroke-width="20"/>
    <circle cx="400" cy="290" r="50" stroke="#545b68" stroke-width="3"/>
    <g stroke="#6b7280" stroke-width="2">
      <path d="M130 240v100M80 290h100M95 255l70 70M165 255l-70 70"/>
      <path d="M400 240v100M350 290h100M365 255l70 70M435 255l-70 70"/>
    </g>
    <circle cx="130" cy="290" r="9" fill="#e8491d" stroke="none"/>
    <circle cx="400" cy="290" r="9" fill="#e8491d" stroke="none"/>
    <!-- frame -->
    <path d="M130 290l70-95h110l90 95" stroke="#cfd3da" stroke-width="10"/>
    <path d="M200 195l60 95h50l40-95" stroke="#9aa0ab" stroke-width="8"/>
    <!-- tank & seat -->
    <path d="M205 190c10-38 40-52 90-50 26 1 46 10 60 30l-12 22H210z" fill="#e8491d" stroke="none"/>
    <path d="M150 180c18-16 44-20 72-16l-8 26h-70z" fill="#1c1f26" stroke="#3a3f4a" stroke-width="3"/>
    <!-- engine block -->
    <rect x="240" y="225" width="78" height="56" rx="10" fill="#3a3f4a" stroke="none"/>
    <path d="M250 240h58M250 252h58M250 264h58" stroke="#6b7280" stroke-width="3"/>
    <!-- front fork & handle -->
    <path d="M400 290l-36-140" stroke="#cfd3da" stroke-width="9"/>
    <path d="M350 140l30-6 22 12" stroke="#cfd3da" stroke-width="7"/>
    <circle cx="372" cy="170" r="14" fill="#fff4d6" stroke="#e8491d" stroke-width="4"/>
    <!-- exhaust -->
    <path d="M270 300h-110" stroke="#9aa0ab" stroke-width="10"/>
  </g>
  <!-- floating parts -->
  <g transform="translate(60 70)">
    <circle r="34" fill="#1c1f26" stroke="#2f343e" stroke-width="2"/>
    <use href="#i-engine" x="-18" y="-18" width="36" height="36" stroke="#e8491d" stroke-width="2" fill="none"/>
  </g>
  <g transform="translate(470 80)">
    <circle r="30" fill="#1c1f26" stroke="#2f343e" stroke-width="2"/>
    <use href="#i-electric" x="-15" y="-15" width="30" height="30" stroke="#f5a623" stroke-width="2" fill="none"/>
  </g>
  <g transform="translate(265 50)">
    <circle r="26" fill="#1c1f26" stroke="#2f343e" stroke-width="2"/>
    <use href="#i-wrench" x="-13" y="-13" width="26" height="26" stroke="#fff" stroke-width="2" fill="none"/>
  </g>
</svg>"""


def i(name, extra=""):
    return f'<svg class="icon{extra}" aria-hidden="true"><use href="#i-{name}"></use></svg>'


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
NAV = [
    ("index.html", "Home"),
    ("products.html", "Spare Parts"),
    ("services.html", "Repair & Service"),
    ("bike-care-tips.html", "Bike Care Tips"),
    ("about.html", "About"),
    ("faq.html", "FAQ"),
    ("contact.html", "Contact"),
]


def socials_html():
    links = [
        (CONFIG["wa_link"], "whatsapp", "WhatsApp"),
        ("tel:" + CONFIG["phone_intl"], "phone", "Call"),
        ("mailto:" + CONFIG["email"], "mail", "Email"),
    ]
    for key, label in (("facebook", "Facebook"), ("instagram", "Instagram"), ("tiktok", "TikTok"), ("youtube", "YouTube")):
        if CONFIG[key]:
            links.append((CONFIG[key], key, label))
    out = []
    for href, ico, label in links:
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        out.append(f'<a href="{href}" aria-label="{label}"{ext}>{i(ico)}</a>')
    return '<div class="socials">' + "".join(out) + "</div>"


def header(slug):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == slug else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return f"""
<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar">
  <div class="container">
    <span>{i('pin')} {CONFIG['address']}</span>
    <span class="hide-sm">{i('clock')} {CONFIG['hours']}</span>
    <a href="tel:{CONFIG['phone_intl']}">{i('phone')} {CONFIG['phone_display']}</a>
  </div>
</div>
<header class="header">
  <div class="container">
    <a class="logo" href="index.html" aria-label="{CONFIG['name']} home">
      {LOGO}
      <span><strong>{CONFIG['name']}</strong><small>{CONFIG['tagline']}</small></span>
    </a>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>{''.join(items)}</ul>
      <div class="nav-cta">
        <a class="btn btn--wa" href="{CONFIG['wa_link']}" target="_blank" rel="noopener">{i('whatsapp')} WhatsApp us</a>
        <a class="btn btn--primary" href="get-a-quote.html">Get a parts quote</a>
      </div>
    </nav>
    <div class="header-actions">
      <a class="enquiry-link" href="enquiry.html" aria-label="My parts list">{i('list')}<span class="enquiry-count" data-enquiry-count hidden>0</span></a>
      <a class="btn btn--primary btn--sm" href="get-a-quote.html">Get a quote</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">{i('menu')}<span class="sr-only">Menu</span></button>
    </div>
  </div>
</header>"""


def footer():
    return f"""
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo" href="index.html">{LOGO}<span><strong>{CONFIG['name']}</strong><small>{CONFIG['tagline']}</small></span></a>
        <p>Spare parts for all popular motorcycles, and a workshop to fit them — in {CONFIG['city']}.</p>
        {socials_html()}
      </div>
      <div>
        <h4>Shop</h4>
        <ul>
          <li><a href="products.html">All spare parts</a></li>
          <li><a href="products.html?cat=engine">Engine parts</a></li>
          <li><a href="products.html?cat=brakes">Brakes</a></li>
          <li><a href="products.html?cat=electrical">Electrical &amp; lights</a></li>
          <li><a href="products.html?cat=tyres">Tyres &amp; tubes</a></li>
          <li><a href="enquiry.html">My parts list</a></li>
        </ul>
      </div>
      <div>
        <h4>Help</h4>
        <ul>
          <li><a href="services.html">Repair &amp; service</a></li>
          <li><a href="book-service.html">Book a service</a></li>
          <li><a href="get-a-quote.html">Get a parts quote</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="bike-care-tips.html">Bike care tips</a></li>
          <li><a href="feedback.html">Give feedback</a></li>
        </ul>
      </div>
      <div>
        <h4>Visit or call</h4>
        <ul>
          <li>{CONFIG['address']}</li>
          <li>{CONFIG['hours']}</li>
          <li><a href="tel:{CONFIG['phone_intl']}">{CONFIG['phone_display']}</a></li>
          <li><a href="mailto:{CONFIG['email']}">{CONFIG['email']}</a></li>
          <li><a href="{CONFIG['map_link']}" target="_blank" rel="noopener">Get directions →</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> {CONFIG['name']}. All rights reserved.</span>
      <span><a href="privacy-policy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="returns-warranty.html">Returns &amp; warranty</a> · <a href="delivery-policy.html">Delivery</a></span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{CONFIG['wa_link']}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{i('whatsapp')}<span>Chat on WhatsApp</span></a>
<div class="callbar">
  <a class="btn btn--primary" href="tel:{CONFIG['phone_intl']}">{i('phone')} Call now</a>
  <a class="btn btn--wa" href="{CONFIG['wa_link']}" target="_blank" rel="noopener">{i('whatsapp')} WhatsApp</a>
</div>"""


def schema():
    data = {
        "@context": "https://schema.org",
        "@type": ["AutoPartsStore", "MotorcycleRepair"],
        "name": CONFIG["name"],
        "description": "Motorcycle spare parts and repair in " + CONFIG["city"] + ".",
        "url": CONFIG["site_url"] + "/",
        "telephone": CONFIG["phone_intl"],
        "email": CONFIG["email"],
        "address": {"@type": "PostalAddress", "addressLocality": CONFIG["city"],
                    "addressRegion": "Sindh", "addressCountry": "PK"},
        "areaServed": CONFIG["city"],
        "priceRange": "$",
    }
    same = [CONFIG[k] for k in ("facebook", "instagram", "tiktok", "youtube") if CONFIG[k]]
    if same:
        data["sameAs"] = same
    return '<script type="application/ld+json">' + json.dumps(data) + "</script>"


def page(slug, title, description, body, scripts=(), noindex=False):
    site_js = json.dumps({
        "whatsapp": CONFIG["whatsapp"],
        "phoneIntl": CONFIG["phone_intl"],
        "phoneDisplay": CONFIG["phone_display"],
        "formEndpoint": CONFIG["form_endpoint"],
    })
    full_title = title if CONFIG["name"] in title else f"{title} | {CONFIG['name']}"
    url = CONFIG["site_url"] + "/" + ("" if slug == "index.html" else slug)
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    extra = "".join(f'<script src="assets/js/{s}" defer></script>' for s in scripts)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
{robots}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{CONFIG['name']}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#121419">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{schema() if slug == 'index.html' or slug == 'contact.html' else ''}
<script>window.SITE = {site_js};</script>
<!-- Analytics: paste Google Analytics / Meta Pixel code here -->
</head>
<body>
{SPRITE}
{header(slug)}
<main id="main">
{body}
</main>
{footer()}
{extra}<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(title, text, crumb):
    return f"""
<section class="page-hero">
  <div class="container">
    <ol class="breadcrumb"><li><a href="index.html">Home</a></li><li>{crumb}</li></ol>
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>"""


def honeypot():
    return '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'


BIKE_OPTIONS = "".join(f"<option>{b}</option>" for b in [
    "Honda CD 70", "Honda CG 125", "Honda Pridor", "Honda CB 150F", "Yamaha YBR 125",
    "Suzuki GD 110", "Suzuki GS 150", "Suzuki GR 150", "70cc (United, Road Prince, Unique & others)",
    "125cc (local brand)", "Other"])


def contact_fields(email_required=False):
    req = " required" if email_required else ""
    star = ' <span class="req">*</span>' if email_required else " (optional)"
    return f"""
      <div class="form-row">
        <div class="field"><label for="f-name">Your name <span class="req">*</span></label><input id="f-name" name="Name" autocomplete="name" required></div>
        <div class="field"><label for="f-phone">Phone / WhatsApp <span class="req">*</span></label><input id="f-phone" name="Phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="03XX XXXXXXX" pattern="[0-9+ ()-]{{10,16}}" required></div>
      </div>
      <div class="field"><label for="f-email">Email{star}</label><input id="f-email" name="Email" type="email" autocomplete="email"{req}></div>"""


def submit_block(label):
    return f"""
      {honeypot()}
      <div class="form-status" role="status" aria-live="polite"></div>
      <button class="btn btn--primary btn--block" type="submit">{label}</button>
      <p class="form-note">We reply by phone or WhatsApp, usually the same day. See our <a href="privacy-policy.html">privacy policy</a>.</p>"""


def share_block():
    url = quote(CONFIG["site_url"] + "/")
    return f"""
<div class="share">
  <strong>Share:</strong>
  <a href="https://wa.me/?text={quote('Motorcycle spare parts & repair in ' + CONFIG['city'] + ' — ' + CONFIG['name'] + ' ')}{url}" target="_blank" rel="noopener" aria-label="Share on WhatsApp">{i('whatsapp')}</a>
  <a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener" aria-label="Share on Facebook">{i('facebook')}</a>
  <a href="https://twitter.com/intent/tweet?url={url}&text={quote(CONFIG['name'] + ' — motorcycle parts & repair in ' + CONFIG['city'])}" target="_blank" rel="noopener" aria-label="Share on X">{i('x')}</a>
  <button type="button" data-share-copy aria-label="Copy link">{i('link')}</button>
  <button type="button" data-share-native aria-label="More sharing options">{i('share')}</button>
</div>"""


def cta_band(title="Need a part today?", text="Send your bike model and the part you need — we'll confirm price and stock on WhatsApp."):
    return f"""
<section class="section">
  <div class="container">
    <div class="cta-band">
      <div><h2>{title}</h2><p>{text}</p></div>
      <div class="btn-row">
        <a class="btn btn--light" href="{CONFIG['wa_link']}" target="_blank" rel="noopener">{i('whatsapp')} WhatsApp us</a>
        <a class="btn btn--ghost" href="tel:{CONFIG['phone_intl']}">{i('phone')} {CONFIG['phone_display']}</a>
      </div>
    </div>
  </div>
</section>"""


SERVICES = [
    ("wrench", "General service & tune-up", "Oil change, air filter clean, spark plug check, chain adjust and a full safety check."),
    ("engine", "Engine repair & overhaul", "Low pickup, smoke, noise or oil leaks — we diagnose and repair, from top overhaul to full rebuild."),
    ("brake", "Brakes", "Brake shoes, disc pads, cables and adjustment so your bike stops safely."),
    ("clutch", "Clutch & gearbox", "Clutch slip, hard gear shifts or jumping gears — plates, springs and cables fitted."),
    ("electric", "Electrical & self-start", "Battery, wiring, lights, indicators, horn, CDI and self-start problems."),
    ("chain", "Chain & sprocket", "Chain cleaning, adjustment and kit replacement for a smooth, quiet ride."),
    ("tyre", "Tyres & puncture", "Tyre and tube change, puncture repair and wheel balancing checks."),
    ("filter", "Carburetor & fuel", "Carburetor cleaning and tuning for steady idle and better mileage."),
]


def service_options():
    return "".join(f"<option>{s[1]}</option>" for s in SERVICES) + "<option>Not sure — please check my bike</option>"


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
PAGES = {}

PAGES["index.html"] = dict(
    title=f"{CONFIG['name']} — Motorcycle Spare Parts & Repair in {CONFIG['city']}",
    description=f"Genuine-quality motorcycle spare parts and expert repair in {CONFIG['city']}. Parts for Honda, Yamaha, Suzuki and all 70cc/125cc bikes. Call or WhatsApp {CONFIG['phone_display']}.",
    scripts=["products.js"],
    body=f"""
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow">{CONFIG['city']} · Spare parts &amp; workshop</span>
      <h1>Motorcycle parts &amp; repair, <span>done right.</span></h1>
      <p class="lead">From a new spark plug to a full engine overhaul — get the right part for your bike and a mechanic to fit it, all in one place.</p>
      <ul class="hero-badges">
        <li>{i('check')} Parts for all popular bikes</li>
        <li>{i('wrench')} Mechanic on site</li>
        <li>{i('clock')} {CONFIG['hours_short']}</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--wa" href="{wa('Hi Al-Bais Motors, I need a spare part. My bike: ')}" target="_blank" rel="noopener">{i('whatsapp')} Ask on WhatsApp</a>
        <a class="btn btn--primary" href="products.html">Browse parts {i('arrow')}</a>
        <a class="btn btn--ghost" href="tel:{CONFIG['phone_intl']}">{i('phone')} Call</a>
      </div>
    </div>
    <div class="hero-art">{HERO_ART}</div>
  </div>
</section>

<div class="info-strip">
  <div class="container">
    <div class="grid">
      <div class="info-item">{i('phone')}<div><strong>Call or WhatsApp</strong><a href="tel:{CONFIG['phone_intl']}">{CONFIG['phone_display']}</a></div></div>
      <div class="info-item">{i('pin')}<div><strong>Visit the shop</strong><a href="{CONFIG['map_link']}" target="_blank" rel="noopener">{CONFIG['address']}</a></div></div>
      <div class="info-item">{i('clock')}<div><strong>Opening hours</strong><span>{CONFIG['hours']}</span></div></div>
    </div>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Shop by category</span>
      <h2>Every part your bike needs</h2>
      <p class="lead">Pick a category to see common parts, or just send us your bike model — we stock far more than we can list.</p>
    </div>
    <div class="grid grid--4">
      {''.join(f'<a class="card card--link" href="products.html?cat={cid}"><span class="card-icon">{i(ico)}</span><h3>{name}</h3><span class="more">View parts {i("arrow")}</span></a>' for cid, name, ico in [
          ('engine','Engine Parts','engine'),('brakes','Brakes','brake'),('clutch','Clutch &amp; Gearbox','clutch'),('chain','Chain &amp; Sprockets','chain'),
          ('electrical','Electrical &amp; Lights','electric'),('tyres','Tyres &amp; Tubes','tyre'),('oils','Oils &amp; Lubricants','oil'),('body','Body &amp; Accessories','accessory')])}
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Popular parts</span>
      <h2>Most-asked-for parts</h2>
      <p class="lead">Tap <strong>Ask price</strong> to get today's price on WhatsApp, or add parts to your list and send them all at once.</p>
    </div>
    <div class="grid grid--3" data-products data-limit="6"></div>
    <p style="margin-top:28px"><a class="btn btn--ghost" href="products.html">See all parts {i('arrow')}</a></p>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Workshop</span>
      <h2>Repair &amp; service by experienced mechanics</h2>
      <p class="lead">Buy the part and get it fitted the same visit — no running between shops.</p>
    </div>
    <div class="grid grid--4">
      {''.join(f'<div class="card"><span class="card-icon">{i(ic)}</span><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in SERVICES[:4])}
    </div>
    <div class="btn-row" style="margin-top:28px">
      <a class="btn btn--primary" href="book-service.html">{i('calendar')} Book a service</a>
      <a class="btn btn--ghost" href="services.html">All services {i('arrow')}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">How it works</span>
      <h2>Your part in 3 easy steps</h2>
    </div>
    <div class="grid grid--3 steps">
      <div class="card step"><h3>Tell us your bike</h3><p>WhatsApp or call with your bike model and the part you need. A photo of the old part helps.</p></div>
      <div class="card step"><h3>Get price &amp; stock</h3><p>We confirm the right part, the price and whether it's in stock — before you travel.</p></div>
      <div class="card step"><h3>Collect or get it fitted</h3><p>Pick it up at the shop, or let our mechanic fit it while you wait.</p></div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container split">
    <div>
      <span class="eyebrow">Why riders choose us</span>
      <h2>Straight answers, the right part</h2>
      <ul class="list-check">
        <li>Parts for Honda, Yamaha, Suzuki and all local 70cc &amp; 125cc bikes</li>
        <li>Clear prices — ask before you buy, no surprises</li>
        <li>Mechanic on site to fit what you buy</li>
        <li>Quick replies on WhatsApp</li>
        <li>Honest advice on whether a part needs replacing or just repair</li>
      </ul>
      <a class="btn btn--primary" href="get-a-quote.html">Get a free parts quote</a>
    </div>
    <div>
      <span class="eyebrow">Bikes we cover</span>
      <h2>Parts for your bike</h2>
      <ul class="chips">
        <li>Honda CD 70</li><li>Honda CG 125</li><li>Honda Pridor</li><li>Honda CB 150F</li>
        <li>Yamaha YBR 125</li><li>Suzuki GD 110</li><li>Suzuki GS 150</li><li>Suzuki GR 150</li>
        <li>United</li><li>Road Prince</li><li>Unique</li><li>Super Power</li><li>Other 70cc / 125cc</li>
      </ul>
      <p style="margin-top:18px;color:var(--muted)">Don't see your bike? <a href="{wa('Hi Al-Bais Motors, do you have parts for my bike? Model: ')}" target="_blank" rel="noopener">Ask us on WhatsApp</a>.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Happy with us?</span>
      <h2>Tell other riders</h2>
      <p class="lead">A quick Google review helps other riders in {CONFIG['city']} find a shop they can trust.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="{CONFIG['google_listing']}" target="_blank" rel="noopener">{i('star')} Review us on Google</a>
        <a class="btn btn--ghost" href="feedback.html">Send private feedback</a>
      </div>
    </div>
    <div class="form-panel">
      <h2>Get offers on WhatsApp</h2>
      <p class="form-note" style="margin-bottom:16px">Be first to hear about new stock and seasonal offers. No spam — leave any time.</p>
      <form class="form" data-form data-subject="Offers sign-up" novalidate>
        <div class="form-row">
          <div class="field"><label for="o-name">Name <span class="req">*</span></label><input id="o-name" name="Name" autocomplete="name" required></div>
          <div class="field"><label for="o-phone">WhatsApp number <span class="req">*</span></label><input id="o-phone" name="WhatsApp" type="tel" inputmode="tel" placeholder="03XX XXXXXXX" pattern="[0-9+ ()-]{{10,16}}" required></div>
        </div>
        <div class="field"><label for="o-bike">Your bike</label><select id="o-bike" name="Bike"><option value="">Select…</option>{BIKE_OPTIONS}</select></div>
        <label class="check"><input type="checkbox" name="Consent" value="Yes, send me offers on WhatsApp" required> I agree to receive offers on WhatsApp.</label>
        {submit_block('Sign me up')}
      </form>
    </div>
  </div>
</section>
{cta_band()}
""")

PAGES["products.html"] = dict(
    title=f"Motorcycle Spare Parts in {CONFIG['city']}",
    description=f"Engine parts, brakes, clutch, chain kits, electrical, tyres and oils for Honda, Yamaha, Suzuki and local bikes. Ask today's price on WhatsApp — {CONFIG['name']}, {CONFIG['city']}.",
    scripts=["products.js"],
    body=page_hero("Motorcycle spare parts", "Filter by category or your bike. Prices change with stock, so tap <strong>Ask price</strong> for today's price — or add parts to your list and send them all at once.", "Spare Parts") + f"""
<section class="section">
  <div class="container">
    <div class="filters">
      <div class="field filter-search"><label for="p-search">Search parts</label><input id="p-search" type="search" placeholder="e.g. clutch plates, battery, CG 125" data-filter-search></div>
      <div class="field"><label for="p-cat">Category</label><select id="p-cat" data-filter-cat></select></div>
      <div class="field"><label for="p-bike">Your bike</label><select id="p-bike" data-filter-bike></select></div>
    </div>
    <ul class="cat-tabs" data-cat-tabs aria-label="Categories"></ul>
    <div class="grid grid--3" data-products></div>
    <div class="card" style="margin-top:32px;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">
      <div><h3 style="margin:0">Can't find your part?</h3><p>We stock many more parts than we list here. Send a photo of the old part on WhatsApp.</p></div>
      <div class="btn-row"><a class="btn btn--wa" href="{wa('Hi Al-Bais Motors, I am looking for a part (photo attached). My bike: ')}" target="_blank" rel="noopener">{i('whatsapp')} Send photo</a><a class="btn btn--ghost" href="enquiry.html">{i('list')} View my list</a></div>
    </div>
  </div>
</section>
{cta_band()}
""")

PAGES["enquiry.html"] = dict(
    title="My Parts List",
    description="Send your list of motorcycle parts to Al-Bais Motors and get prices and availability.",
    scripts=["products.js"],
    noindex=True,
    body=page_hero("My parts list", "Review your list, then send it on WhatsApp or by email. We'll reply with prices and availability.", "My Parts List") + f"""
<section class="section">
  <div class="container split split--wide">
    <div>
      <h2>Your parts</h2>
      <ul class="enquiry-items" data-enquiry-list></ul>
      <div class="btn-row">
        <a class="btn btn--wa" data-enquiry-wa href="{CONFIG['wa_link']}" target="_blank" rel="noopener">{i('whatsapp')} Send list on WhatsApp</a>
        <a class="btn btn--ghost" href="products.html">{i('plus')} Add more parts</a>
      </div>
    </div>
    <div class="form-panel">
      <h2>Or send by email</h2>
      <form class="form" data-form data-subject="Parts list enquiry" novalidate>
        {contact_fields()}
        <div class="field"><label for="e-bike">Bike model <span class="req">*</span></label><select id="e-bike" name="Bike" required><option value="">Select…</option>{BIKE_OPTIONS}</select></div>
        <input type="hidden" name="Parts list" data-enquiry-field>
        <div class="field"><label for="e-msg">Anything else?</label><textarea id="e-msg" name="Message" placeholder="Year of the bike, colour, collection or delivery…"></textarea></div>
        {submit_block('Send my list')}
      </form>
    </div>
  </div>
</section>
""")

PAGES["services.html"] = dict(
    title=f"Motorcycle Repair & Service in {CONFIG['city']}",
    description=f"Engine repair, tune-ups, brakes, clutch, electrical and tyre work for all popular motorcycles in {CONFIG['city']}. Book your service with {CONFIG['name']}.",
    body=page_hero("Repair &amp; service", "Our mechanics fix the problems riders see every day — and fit the parts you buy from us while you wait.", "Repair &amp; Service") + f"""
<section class="section">
  <div class="container">
    <div class="grid grid--4">
      {''.join(f'<div class="card"><span class="card-icon">{i(ic)}</span><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in SERVICES)}
    </div>
  </div>
</section>
<section class="section section--soft">
  <div class="container split">
    <div>
      <span class="eyebrow">Before you come</span>
      <h2>Make your visit quick</h2>
      <ul class="list-check">
        <li>Tell us the problem on WhatsApp — a short video of the noise or fault really helps</li>
        <li>We'll tell you the likely fix and the parts needed</li>
        <li>Book a time so the mechanic is ready for you</li>
        <li>We explain the work and agree the price before we start</li>
      </ul>
      <a class="btn btn--wa" href="{wa('Hi Al-Bais Motors, my bike has a problem: ')}" target="_blank" rel="noopener">{i('whatsapp')} Describe the problem</a>
    </div>
    <div class="form-panel" id="book">
      <h2>Book a service</h2>
      <form class="form" data-form data-subject="Service booking" novalidate>
        {contact_fields()}
        <div class="form-row">
          <div class="field"><label for="s-bike">Bike model <span class="req">*</span></label><select id="s-bike" name="Bike" required><option value="">Select…</option>{BIKE_OPTIONS}</select></div>
          <div class="field"><label for="s-service">Service needed <span class="req">*</span></label><select id="s-service" name="Service" required><option value="">Select…</option>{service_options()}</select></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="s-date">Preferred day</label><input id="s-date" name="Preferred day" type="date"></div>
          <div class="field"><label for="s-time">Preferred time</label><select id="s-time" name="Preferred time"><option value="">Any time</option><option>Morning</option><option>Afternoon</option><option>Evening (before 8 PM)</option></select></div>
        </div>
        <div class="field"><label for="s-msg">What's the problem?</label><textarea id="s-msg" name="Problem" placeholder="e.g. bike won't start in the morning, clutch slipping…"></textarea></div>
        {submit_block('Request booking')}
      </form>
    </div>
  </div>
</section>
{cta_band('Bike broken down?', 'Call us — we can usually tell you over the phone what to check first.')}
""")

PAGES["get-a-quote.html"] = dict(
    title=f"Get a Motorcycle Parts Quote — {CONFIG['name']}",
    description=f"Tell us your bike and the part you need. {CONFIG['name']} in {CONFIG['city']} replies with price and stock, usually the same day.",
    body=f"""
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow">Free, no-obligation quote</span>
      <h1>Get the right part's <span>price today</span></h1>
      <p class="lead">Tell us your bike and the part you need. We check stock and send you a clear price — usually the same day.</p>
      <ul class="list-check" style="color:#e7e9ee">
        <li>Parts for Honda, Yamaha, Suzuki &amp; all local bikes</li>
        <li>We confirm the correct part for your model</li>
        <li>Collect from the shop or get it fitted</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--wa" href="{wa('Hi Al-Bais Motors, please quote me for: ')}" target="_blank" rel="noopener">{i('whatsapp')} Faster on WhatsApp</a>
        <a class="btn btn--ghost" href="tel:{CONFIG['phone_intl']}">{i('phone')} {CONFIG['phone_display']}</a>
      </div>
    </div>
    <div class="form-panel">
      <h2>Request a quote</h2>
      <form class="form" data-form data-subject="Parts quote request" novalidate>
        {contact_fields()}
        <div class="form-row">
          <div class="field"><label for="q-bike">Bike model <span class="req">*</span></label><select id="q-bike" name="Bike" required><option value="">Select…</option>{BIKE_OPTIONS}</select></div>
          <div class="field"><label for="q-year">Year</label><input id="q-year" name="Year" inputmode="numeric" placeholder="e.g. 2021"></div>
        </div>
        <div class="field"><label for="q-part">Part(s) needed <span class="req">*</span></label><textarea id="q-part" name="Parts needed" required placeholder="e.g. clutch plates and gasket set"></textarea><p class="hint">Have a photo of the old part? Send it on WhatsApp after submitting.</p></div>
        <div class="field"><label for="q-how">How do you want it?</label><select id="q-how" name="Collection"><option>I'll collect from the shop</option><option>Collect and fit it for me</option><option>Please deliver (ask about delivery)</option></select></div>
        {submit_block('Get my quote')}
      </form>
    </div>
  </div>
</section>
<section class="section">
  <div class="container grid grid--3">
    <div class="card"><span class="card-icon">{i('tag')}</span><h3>Clear prices</h3><p>You get the price before you travel. No surprises at the counter.</p></div>
    <div class="card"><span class="card-icon">{i('check')}</span><h3>The right part</h3><p>Tell us the model and year — we double-check the part fits.</p></div>
    <div class="card"><span class="card-icon">{i('wrench')}</span><h3>Fitting available</h3><p>Our mechanic can fit the part on the same visit.</p></div>
  </div>
</section>
""")

PAGES["book-service.html"] = dict(
    title=f"Book a Motorcycle Service in {CONFIG['city']}",
    description=f"Book your motorcycle service or repair at {CONFIG['name']}, {CONFIG['city']}. Choose a day and time and we'll confirm on WhatsApp.",
    body=f"""
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow">Workshop booking</span>
      <h1>Book your bike in — <span>skip the wait</span></h1>
      <p class="lead">Choose the service and a time that suits you. We'll confirm on WhatsApp and have the mechanic ready when you arrive.</p>
      <ul class="list-check" style="color:#e7e9ee">
        <li>Tune-ups, oil changes and full services</li>
        <li>Engine, clutch, brake and electrical repairs</li>
        <li>Price agreed before any work starts</li>
      </ul>
    </div>
    <div class="form-panel">
      <h2>Choose your service</h2>
      <form class="form" data-form data-subject="Service booking" novalidate>
        {contact_fields()}
        <div class="form-row">
          <div class="field"><label for="b-bike">Bike model <span class="req">*</span></label><select id="b-bike" name="Bike" required><option value="">Select…</option>{BIKE_OPTIONS}</select></div>
          <div class="field"><label for="b-service">Service <span class="req">*</span></label><select id="b-service" name="Service" required><option value="">Select…</option>{service_options()}</select></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="b-date">Preferred day <span class="req">*</span></label><input id="b-date" name="Preferred day" type="date" required></div>
          <div class="field"><label for="b-time">Preferred time</label><select id="b-time" name="Preferred time"><option value="">Any time</option><option>Morning</option><option>Afternoon</option><option>Evening (before 8 PM)</option></select></div>
        </div>
        <div class="field"><label for="b-msg">Notes</label><textarea id="b-msg" name="Notes" placeholder="Anything we should know?"></textarea></div>
        {submit_block('Book my service')}
      </form>
    </div>
  </div>
</section>
{cta_band('Prefer to talk?', 'Call or WhatsApp and we will book you in directly.')}
""")

PAGES["about.html"] = dict(
    title=f"About {CONFIG['name']}",
    description=f"{CONFIG['name']} is a motorcycle spare parts shop and workshop in {CONFIG['city']}, helping local riders keep their bikes running.",
    body=page_hero(f"About {CONFIG['name']}", f"A local motorcycle spare parts shop and workshop in {CONFIG['city']}.", "About") + f"""
<section class="section">
  <div class="container split">
    <div class="prose">
      <h2 style="margin-top:0">Keeping {CONFIG['city']} riding</h2>
      <p>For most families here, the motorcycle is how you get to work, school and the market. When it breaks down, you need the right part quickly — at a fair price — and someone who can fit it properly.</p>
      <p>That's what we do. {CONFIG['name']} stocks spare parts for the bikes people actually ride, from Honda CD 70s and CG 125s to Yamaha, Suzuki and local 70cc and 125cc models, with a workshop to fit them.</p>
      <h3>What we believe in</h3>
      <ul class="list-check">
        <li><strong>Honest advice</strong> — if a part can be repaired instead of replaced, we'll tell you.</li>
        <li><strong>The right part first time</strong> — we check your model before we sell.</li>
        <li><strong>Clear prices</strong> — you know the cost before we start.</li>
      </ul>
    </div>
    <div class="grid">
      <div class="card"><span class="card-icon">{i('tag')}</span><h3>Spare parts counter</h3><p>Engine, brake, clutch, electrical, tyres, oils and body parts.</p></div>
      <div class="card"><span class="card-icon">{i('wrench')}</span><h3>Workshop</h3><p>Servicing and repairs, with parts fitted the same visit.</p></div>
      <div class="card"><span class="card-icon">{i('chat')}</span><h3>Quick help on WhatsApp</h3><p>Ask about prices, stock or a problem with your bike.</p></div>
    </div>
  </div>
</section>
<section class="section section--soft"><div class="container">{share_block()}</div></section>
{cta_band()}
""")

PAGES["contact.html"] = dict(
    title=f"Contact {CONFIG['name']} — {CONFIG['city']}",
    description=f"Call or WhatsApp {CONFIG['phone_display']}, email us or visit {CONFIG['name']} in {CONFIG['city']}. {CONFIG['hours']}.",
    body=page_hero("Contact us", "The quickest way to reach us is WhatsApp. You can also call, email or use the form below.", "Contact") + f"""
<section class="section">
  <div class="container split">
    <div>
      <ul class="contact-list">
        <li>{i('phone')}<div><strong>Phone</strong><a href="tel:{CONFIG['phone_intl']}">{CONFIG['phone_display']}</a></div></li>
        <li>{i('whatsapp')}<div><strong>WhatsApp</strong><a href="{CONFIG['wa_link']}" target="_blank" rel="noopener">Chat with us</a></div></li>
        <li>{i('mail')}<div><strong>Email</strong><a href="mailto:{CONFIG['email']}">{CONFIG['email']}</a></div></li>
        <li>{i('pin')}<div><strong>Address</strong>{CONFIG['address']}<br><a href="{CONFIG['map_link']}" target="_blank" rel="noopener">Get directions →</a></div></li>
        <li>{i('clock')}<div><strong>Hours</strong>{CONFIG['hours']}</div></li>
      </ul>
      <iframe class="map" src="{CONFIG['map_embed']}" title="Map showing {CONFIG['name']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
    <div class="form-panel">
      <h2>Send a message</h2>
      <form class="form" data-form data-subject="Contact form" novalidate>
        {contact_fields()}
        <div class="field"><label for="c-topic">Topic</label><select id="c-topic" name="Topic"><option>Spare part price / stock</option><option>Repair or service</option><option>Order or delivery</option><option>Return or warranty</option><option>Something else</option></select></div>
        <div class="field"><label for="c-msg">Message <span class="req">*</span></label><textarea id="c-msg" name="Message" required></textarea></div>
        {submit_block('Send message')}
      </form>
    </div>
  </div>
</section>
""")

FAQS = [
    ("Do you have parts for my bike?", "We stock parts for Honda CD 70, CG 125, Pridor, CB 150F, Yamaha YBR 125, Suzuki GD 110, GS 150, GR 150 and most local 70cc and 125cc bikes (United, Road Prince, Unique and others). If you don't see your bike, send us the model on WhatsApp."),
    ("How do I know the price?", "Prices change with stock and supplier rates, so we don't list them online. Tap <strong>Ask price</strong> on any part, or send your list on WhatsApp, and we'll reply with today's price."),
    ("Are your parts genuine?", "We sell both original (genuine company) parts and good-quality replacement parts. We always tell you which one you're buying and the price of each, so you can choose."),
    ("Can you fit the part for me?", "Yes. Our workshop can fit most parts on the same visit. Fitting is charged separately depending on the job — ask us for the price first."),
    ("Do you deliver?", "We may be able to arrange delivery within the city for some orders. Ask on WhatsApp and we'll confirm the cost and timing. See our <a href=\"delivery-policy.html\">delivery policy</a>."),
    ("Can I return a part?", "Unused parts in their original packing can usually be exchanged if they don't fit your bike. Electrical parts and parts that have been fitted can't be returned. Read our <a href=\"returns-warranty.html\">returns &amp; warranty policy</a>."),
    ("How do I pay?", "Pay at the shop. Ask us on WhatsApp if you'd like to pay another way."),
    ("What are your opening hours?", CONFIG["hours"] + ". Call before you come if you need a specific part, so we can keep it ready."),
]

PAGES["faq.html"] = dict(
    title="Frequently Asked Questions",
    description=f"Answers about parts, prices, fitting, delivery, returns and payment at {CONFIG['name']}, {CONFIG['city']}.",
    body=page_hero("Frequently asked questions", "Quick answers to what riders ask us most.", "FAQ") + f"""
<section class="section">
  <div class="container" style="max-width:860px">
    <div class="faq">
      {''.join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in FAQS)}
    </div>
    <div class="card" style="margin-top:32px;text-align:center">
      <h3>Still have a question?</h3>
      <p>Ask us directly — we usually reply the same day.</p>
      <div class="btn-row" style="justify-content:center;margin-top:16px">
        <a class="btn btn--wa" href="{CONFIG['wa_link']}" target="_blank" rel="noopener">{i('whatsapp')} WhatsApp</a>
        <a class="btn btn--ghost" href="contact.html">Contact page</a>
      </div>
    </div>
  </div>
</section>
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]})}</script>
""")

TIPS = [
    ("oil", "Change your engine oil on time", "Old, thin oil is the number-one cause of engine wear. Follow the interval in your bike's owner manual — and change it sooner if you ride in heavy traffic, dust or heat. Check the level on the dipstick every week."),
    ("chain", "Keep the chain clean, oiled and adjusted", "A dry or loose chain wears out sprockets fast and can jump off. Clean and lubricate it regularly, especially after rain or dusty roads, and keep the slack as shown in your manual."),
    ("filter", "Clean the air filter", "A dusty filter makes the engine work harder and drink more petrol. Check it often in dusty weather and clean or replace it when it's dirty."),
    ("brake", "Check your brakes every week", "If the lever or pedal goes further than usual, or you hear squealing or grinding, have the shoes or pads checked. Brakes are not something to put off."),
    ("tyre", "Ride on the right tyre pressure", "Low pressure wears tyres quickly, hurts mileage and makes steering heavy. Check pressure when tyres are cold, and look for cuts, cracks and worn tread."),
    ("electric", "Look after the battery and lights", "Dim lights or a weak horn usually mean a weak battery or loose connection. Keep terminals clean and tight, and check all lights before riding at night."),
    ("engine", "Listen to your bike", "New noises, smoke, poor pickup or hard starting are early warnings. A quick check now is almost always cheaper than a big repair later."),
]

PAGES["bike-care-tips.html"] = dict(
    title="Motorcycle Care Tips",
    description="Simple motorcycle maintenance tips: oil changes, chain care, air filter, brakes, tyre pressure and battery — from the mechanics at Al-Bais Motors.",
    body=page_hero("Bike care tips", "Simple habits that keep your motorcycle running longer and save you money on repairs.", "Bike Care Tips") + f"""
<section class="section">
  <div class="container split split--wide">
    <article class="prose">
      {''.join(f'<div class="tip"><h3>{i(ic)} {t}</h3><p>{d}</p></div>' for ic, t, d in TIPS)}
      <p><em>Always follow your motorcycle's owner manual for service intervals and specifications. These tips are general advice.</em></p>
      {share_block()}
    </article>
    <aside>
      <div class="form-panel">
        <h2>Due for a service?</h2>
        <p class="form-note" style="margin-bottom:16px">Book a tune-up and we'll check everything on this list.</p>
        <a class="btn btn--primary btn--block" href="book-service.html">{i('calendar')} Book a service</a>
        <a class="btn btn--wa btn--block" style="margin-top:10px" href="{wa('Hi Al-Bais Motors, I have a question about my bike: ')}" target="_blank" rel="noopener">{i('whatsapp')} Ask a mechanic</a>
      </div>
    </aside>
  </div>
</section>
""")

PAGES["feedback.html"] = dict(
    title="Your Feedback",
    description=f"Tell {CONFIG['name']} how we did. Your feedback helps us serve riders in {CONFIG['city']} better.",
    body=page_hero("How did we do?", "Your feedback goes straight to the owner. Happy with us? A Google review helps other riders find us.", "Feedback") + f"""
<section class="section">
  <div class="container split">
    <div>
      <h2>Loved the service?</h2>
      <p class="lead">Please leave a review on Google — it takes a minute and really helps a local business.</p>
      <a class="btn btn--primary" href="{CONFIG['google_listing']}" target="_blank" rel="noopener">{i('star')} Review us on Google</a>
      <div style="margin-top:28px">{share_block()}</div>
    </div>
    <div class="form-panel">
      <h2>Private feedback</h2>
      <form class="form" data-form data-subject="Customer feedback" novalidate>
        <fieldset class="field">
          <legend>Your rating <span class="req">*</span></legend>
          <div class="rating">
            {''.join(f'<input type="radio" id="r{n}" name="Rating" value="{n} / 5" required><label for="r{n}" aria-label="{n} star{"s" if n > 1 else ""}">★</label>' for n in range(5, 0, -1))}
          </div>
        </fieldset>
        <div class="form-row">
          <div class="field"><label for="fb-name">Name</label><input id="fb-name" name="Name" autocomplete="name"></div>
          <div class="field"><label for="fb-phone">Phone (if you'd like a reply)</label><input id="fb-phone" name="Phone" type="tel" inputmode="tel" pattern="[0-9+ ()-]{{10,16}}"></div>
        </div>
        <div class="field"><label for="fb-msg">Your feedback <span class="req">*</span></label><textarea id="fb-msg" name="Feedback" required></textarea></div>
        {honeypot()}
        <div class="form-status" role="status" aria-live="polite"></div>
        <button class="btn btn--primary btn--block" type="submit">Send feedback</button>
      </form>
    </div>
  </div>
</section>
""")

# ---------- Policies ----------
def policy(slug, title, description, sections):
    body = page_hero(title, description, title) + f"""
<section class="section"><div class="container"><article class="prose">
<p class="updated">Last updated: {CONFIG['policy_updated']}</p>
{sections}
<h2>Contact us</h2>
<p>Questions about this policy? Call or WhatsApp <a href="tel:{CONFIG['phone_intl']}">{CONFIG['phone_display']}</a>, email <a href="mailto:{CONFIG['email']}">{CONFIG['email']}</a>, or visit us in {CONFIG['city']}.</p>
</article></div></section>"""
    PAGES[slug] = dict(title=title, description=description, body=body)


policy("privacy-policy.html", "Privacy Policy",
       f"How {CONFIG['name']} collects, uses and protects your information.", f"""
<h2>Who we are</h2>
<p>{CONFIG['name']} is a motorcycle spare parts shop and workshop in {CONFIG['address']}. This policy explains what information we collect through this website and how we use it.</p>
<h2>What we collect</h2>
<ul>
  <li><strong>Information you send us</strong> through our forms: your name, phone/WhatsApp number, email (if you give it), bike model, and your message or parts list.</li>
  <li><strong>Messages</strong> you send us on WhatsApp, by phone or email.</li>
  <li><strong>Your parts list</strong> is saved only in your own browser until you send it to us.</li>
  <li><strong>Basic technical data</strong> such as pages visited, collected by website analytics tools if we use them.</li>
</ul>
<h2>How we use it</h2>
<ul>
  <li>To reply to your enquiry, quote prices, confirm stock and arrange service bookings.</li>
  <li>To send offers on WhatsApp — only if you signed up and agreed. Reply "STOP" any time to leave.</li>
  <li>To improve our website and service.</li>
</ul>
<p>We do <strong>not</strong> sell or rent your personal information.</p>
<h2>Services we use</h2>
<ul>
  <li><strong>FormSubmit</strong> delivers form messages to our email inbox.</li>
  <li><strong>WhatsApp</strong> (Meta) when you choose to message us there.</li>
  <li><strong>Google Maps</strong> to show our location, and <strong>Google Fonts</strong> for the website's text style.</li>
  <li>Analytics or advertising tools such as Google Analytics or Meta Pixel, if we add them, which may use cookies.</li>
</ul>
<p>These services handle data under their own privacy policies.</p>
<h2>How long we keep it</h2>
<p>We keep enquiry messages only as long as needed to help you and for our normal business records.</p>
<h2>Your choices</h2>
<p>You can ask us to show you, correct or delete the information we hold about you. Contact us using the details below.</p>""")

policy("terms.html", "Terms & Conditions",
       f"The terms for using the {CONFIG['name']} website and buying from us.", f"""
<h2>Using this website</h2>
<p>This website gives information about our parts and services and lets you contact us. By using it, you agree to these terms.</p>
<h2>Products, prices and stock</h2>
<ul>
  <li>Product pictures and descriptions are for general guidance. Parts can vary by model and year.</li>
  <li>Prices are not listed online because they change with stock and supplier rates. The price we confirm to you (in the shop, by phone or WhatsApp) is the price that applies.</li>
  <li>An enquiry or quote request is not an order. A sale is complete when you pay for the part.</li>
  <li>We tell you whether a part is original (genuine company part) or a replacement part. Please ask if you are not sure.</li>
</ul>
<h2>Workshop services</h2>
<ul>
  <li>We agree the work and an estimated price with you before starting. If we find more work is needed, we ask you first.</li>
  <li>Please collect your bike once the work is done. We are not responsible for loss or damage to bikes left for a long time after we've asked you to collect.</li>
  <li>Remove valuables from your bike before leaving it with us.</li>
</ul>
<h2>Returns and warranty</h2>
<p>See our <a href="returns-warranty.html">Returns &amp; Warranty Policy</a>.</p>
<h2>Liability</h2>
<p>We fit parts with care. We are not responsible for problems caused by misuse, accidents, poor maintenance, or parts fitted by someone else.</p>
<h2>Changes</h2>
<p>We may update these terms. The version on this page is the one that applies.</p>""")

policy("returns-warranty.html", "Returns & Warranty Policy",
       "When you can exchange or return a part, and how warranty claims work.", f"""
<h2>Exchanges for unused parts</h2>
<p>If a part doesn't fit your bike, bring it back <strong>unused, undamaged and in its original packing</strong>, with your receipt, within <strong>7 days</strong>. We'll exchange it for the correct part, or give a refund or store credit at our discretion.</p>
<h2>Parts that can't be returned</h2>
<ul>
  <li>Parts that have been fitted or used</li>
  <li>Electrical parts (CDI, coils, bulbs, wiring, batteries) once taken out of the packing</li>
  <li>Oils, lubricants and chemicals once opened</li>
  <li>Parts specially ordered for you</li>
  <li>Parts damaged by wrong fitting, accident or misuse</li>
</ul>
<h2>Warranty</h2>
<p>Some parts — for example batteries and certain branded parts — come with a manufacturer's warranty. We'll tell you at the time of sale if a part has a warranty and for how long. Keep your receipt and the warranty card.</p>
<p>Warranty covers manufacturing faults. It does not cover normal wear, accidents, misuse, or fitting by another workshop.</p>
<h2>Workshop work</h2>
<p>If a problem we repaired comes back soon after the repair, bring the bike back and we'll check our work. If the fault is from our workmanship, we'll put it right.</p>
<h2>How to make a claim</h2>
<p>Bring the part (or bike) and your receipt to the shop, or WhatsApp us a photo and description first so we can advise you.</p>""")

policy("delivery-policy.html", "Delivery Policy",
       "Shop collection and local delivery of motorcycle parts.", f"""
<h2>Collect from the shop</h2>
<p>Most customers collect from our shop in {CONFIG['city']}. Call or WhatsApp first and we'll keep your part ready.</p>
<h2>Local delivery</h2>
<p>For some orders we may be able to arrange delivery within {CONFIG['city']} and nearby areas. The delivery charge and timing depend on the order and location, and we'll confirm them with you before sending anything.</p>
<h2>Outside the city</h2>
<p>For customers outside {CONFIG['city']}, ask us on WhatsApp — we may be able to send parts by courier. Courier charges are paid by the customer.</p>
<h2>Checking your parts</h2>
<p>Please check the part when it arrives. If it's wrong or damaged, contact us within 24 hours with a photo. See our <a href="returns-warranty.html">Returns &amp; Warranty Policy</a>.</p>""")

PAGES["thank-you.html"] = dict(
    title="Thank You",
    description="We've received your message.",
    noindex=True,
    body=f"""
<section class="section center-page">
  <div class="container" style="max-width:640px">
    <svg class="icon big-icon" aria-hidden="true"><use href="#i-check"></use></svg>
    <h1>Thank you!</h1>
    <p class="lead">We've received your message and will reply by phone or WhatsApp, usually the same day.</p>
    <p>Need it faster? Send us a WhatsApp — and attach a photo of the part if you have one.</p>
    <div class="btn-row" style="justify-content:center;margin-top:20px">
      <a class="btn btn--wa" href="{CONFIG['wa_link']}" target="_blank" rel="noopener">{i('whatsapp')} WhatsApp us</a>
      <a class="btn btn--ghost" href="products.html">Keep browsing parts</a>
    </div>
  </div>
</section>
""")

PAGES["404.html"] = dict(
    title="Page Not Found",
    description="This page doesn't exist.",
    noindex=True,
    body=f"""
<section class="section center-page">
  <div class="container" style="max-width:640px">
    <svg class="icon big-icon" aria-hidden="true"><use href="#i-wrench"></use></svg>
    <h1>This page took a wrong turn</h1>
    <p class="lead">The page you're looking for isn't here. Try one of these instead:</p>
    <div class="btn-row" style="justify-content:center;margin-top:20px">
      <a class="btn btn--primary" href="index.html">Home</a>
      <a class="btn btn--ghost" href="products.html">Spare parts</a>
      <a class="btn btn--wa" href="{CONFIG['wa_link']}" target="_blank" rel="noopener">{i('whatsapp')} WhatsApp</a>
    </div>
  </div>
</section>
""")


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(SRC / "assets", DIST / "assets")

    (DIST / "assets/img").mkdir(parents=True, exist_ok=True)
    (DIST / "assets/img/favicon.svg").write_text(LOGO.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))

    for slug, p in PAGES.items():
        html = page(slug, p["title"], p["description"], p["body"], p.get("scripts", ()), p.get("noindex", False))
        (DIST / slug).write_text(html, encoding="utf-8")

    indexable = [s for s, p in PAGES.items() if not p.get("noindex")]
    urls = "".join(
        f"<url><loc>{CONFIG['site_url']}/{'' if s == 'index.html' else s}</loc></url>" for s in indexable)
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {CONFIG['site_url']}/sitemap.xml\n")
    (DIST / "site.webmanifest").write_text(json.dumps({
        "name": CONFIG["name"], "short_name": "Al-Bais", "start_url": "index.html",
        "display": "standalone", "background_color": "#121419", "theme_color": "#e8491d",
        "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
    }, indent=2))
    print(f"Built {len(PAGES)} pages into {DIST}")


if __name__ == "__main__":
    main()
