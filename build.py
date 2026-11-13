#!/usr/bin/env python3
"""
Al-Bais Motors — static site builder (Sindhi, Urdu, English).

  /        Sindhi (main language)
  /ur/     Urdu
  /en/     English

Edit CONFIG below for shop details, content.py for page text,
policies.py for policy pages and src/assets/js/products.js for parts.
Then run:   python3 build.py
The finished website is written to  dist/  (Netlify publishes it).
"""
import json
import shutil
from pathlib import Path
from urllib.parse import quote

from content import S, FAQ_KEYS, JS_KEYS
from policies import POLICIES, LABELS
from svg_blocks import SPRITE, LOGO, HERO_ART

ROOT = Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"

# ---------------------------------------------------------------------------
# CONFIG — change these and rebuild
# ---------------------------------------------------------------------------
CONFIG = {
    "name": "Al-Bais Motors",
    "phone_display": "0300 3100751",
    "phone_intl": "+923003100751",
    "whatsapp": "923003100751",            # digits only, with country code
    "email": "aliasad@gmail.com",           # form submissions arrive here
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
    "policy_updated": "12-11-2026",
}
CONFIG["form_endpoint"] = "https://formsubmit.co/ajax/" + CONFIG["email"]
CONFIG["map_embed"] = "https://www.google.com/maps?q=" + quote(CONFIG["map_query"]) + "&output=embed"
CONFIG["map_link"] = "https://www.google.com/maps/search/?api=1&query=" + quote(CONFIG["map_query"])

# Languages: the first one is the main language and lives at the site root.
LANGS = {
    "sd": {"folder": "", "dir": "rtl", "og": "sd_PK"},
    "ur": {"folder": "ur/", "dir": "rtl", "og": "ur_PK"},
    "en": {"folder": "en/", "dir": "ltr", "og": "en_PK"},
}
L = "sd"  # language currently being built


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def fill(text):
    return (text.replace("{city}", S["city"][L])
                .replace("{address}", S["address"][L])
                .replace("{hours}", S["hours"][L])
                .replace("{phone}", CONFIG["phone_display"]))


def t(key, **extra):
    text = fill(S[key][L])
    for k, v in extra.items():
        text = text.replace("{" + k + "}", v)
    return text


def wa(key_or_text):
    text = t(key_or_text) if key_or_text in S else key_or_text
    return "https://wa.me/" + CONFIG["whatsapp"] + "?text=" + quote(text)


def i(name):
    cls = "icon icon--dir" if name == "arrow" else "icon"
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"></use></svg>'


def up():
    """Path from the current language folder back to the site root."""
    return "../" if LANGS[L]["folder"] else ""


def phone_html():
    return f'<span class="ltr">{CONFIG["phone_display"]}</span>'


def url_for(lang, slug):
    page = "" if slug == "index.html" else slug
    return CONFIG["site_url"] + "/" + LANGS[lang]["folder"] + page


def link_to_lang(lang, slug):
    return up() + LANGS[lang]["folder"] + slug


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def nav_items():
    return [
        ("index.html", t("nav_home")),
        ("products.html", t("nav_parts")),
        ("services.html", t("nav_services")),
        ("bike-care-tips.html", t("nav_tips")),
        ("about.html", t("nav_about")),
        ("faq.html", t("nav_faq")),
        ("contact.html", t("nav_contact")),
    ]


def lang_switch(slug):
    links = []
    for lang in LANGS:
        cur = ' aria-current="true"' if lang == L else ""
        links.append(f'<a href="{link_to_lang(lang, slug)}" lang="{lang}" hreflang="{lang}"{cur}>{S["lang_name"][lang]}</a>')
    return f'<nav class="lang-switch" aria-label="{t("language")}">{"".join(links)}</nav>'


def socials_html():
    wa_default = wa("wa_default")
    links = [
        (wa_default, "whatsapp", t("whatsapp")),
        ("tel:" + CONFIG["phone_intl"], "phone", t("call")),
        ("mailto:" + CONFIG["email"], "mail", t("email")),
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
    current = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{href}"{current if href == slug else ""}>{label}</a></li>'
        for href, label in nav_items())
    return f"""
<a class="skip-link" href="#main">{t('skip')}</a>
<div class="topbar">
  <div class="container">
    <span class="hide-sm">{i('pin')} {t('address')}</span>
    <span class="hide-sm">{i('clock')} {t('hours')}</span>
    <a href="tel:{CONFIG['phone_intl']}">{i('phone')} {phone_html()}</a>
    {lang_switch(slug)}
  </div>
</div>
<header class="header">
  <div class="container">
    <a class="logo" href="index.html" aria-label="{CONFIG['name']} — {t('home_aria')}">
      {LOGO}
      <span><strong>{CONFIG['name']}</strong><small>{t('tagline')}</small></span>
    </a>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>{items}</ul>
      <div class="nav-cta">
        <a class="btn btn--wa" href="{wa('wa_default')}" target="_blank" rel="noopener">{i('whatsapp')} {t('whatsapp_us')}</a>
        <a class="btn btn--primary" href="get-a-quote.html">{t('get_quote_long')}</a>
      </div>
    </nav>
    <div class="header-actions">
      <a class="enquiry-link" href="enquiry.html" aria-label="{t('my_list')}">{i('list')}<span class="enquiry-count" data-enquiry-count hidden>0</span></a>
      <a class="btn btn--primary btn--sm" href="get-a-quote.html">{t('get_quote')}</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">{i('menu')}<span class="sr-only">{t('menu')}</span></button>
    </div>
  </div>
</header>"""


def footer():
    cats = "".join(f'<li><a href="products.html?cat={c}">{t("cat_" + c)}</a></li>' for c in ("engine", "brakes", "electrical", "tyres"))
    return f"""
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo" href="index.html">{LOGO}<span><strong>{CONFIG['name']}</strong><small>{t('tagline')}</small></span></a>
        <p>{t('footer_about')}</p>
        {socials_html()}
      </div>
      <div>
        <h4>{t('f_shop')}</h4>
        <ul>
          <li><a href="products.html">{t('all_parts_link')}</a></li>
          {cats}
          <li><a href="enquiry.html">{t('my_list')}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t('f_help')}</h4>
        <ul>
          <li><a href="services.html">{t('nav_services')}</a></li>
          <li><a href="book-service.html">{t('book_service')}</a></li>
          <li><a href="get-a-quote.html">{t('get_quote_long')}</a></li>
          <li><a href="faq.html">{t('nav_faq')}</a></li>
          <li><a href="bike-care-tips.html">{t('nav_tips')}</a></li>
          <li><a href="feedback.html">{t('give_feedback')}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t('f_visit')}</h4>
        <ul>
          <li>{t('address')}</li>
          <li>{t('hours')}</li>
          <li><a href="tel:{CONFIG['phone_intl']}">{phone_html()}</a></li>
          <li><a href="mailto:{CONFIG['email']}" class="ltr">{CONFIG['email']}</a></li>
          <li><a href="{CONFIG['map_link']}" target="_blank" rel="noopener">{t('directions')}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> {CONFIG['name']}. {t('rights')}</span>
      <span><a href="privacy-policy.html">{t('privacy_short')}</a> · <a href="terms.html">{t('terms_short')}</a> · <a href="returns-warranty.html">{t('returns_short')}</a> · <a href="delivery-policy.html">{t('delivery_short')}</a></span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{wa('wa_default')}" target="_blank" rel="noopener" aria-label="{t('chat_wa')}">{i('whatsapp')}<span>{t('chat_wa')}</span></a>
<div class="callbar">
  <a class="btn btn--primary" href="tel:{CONFIG['phone_intl']}">{i('phone')} {t('call_now')}</a>
  <a class="btn btn--wa" href="{wa('wa_default')}" target="_blank" rel="noopener">{i('whatsapp')} {t('whatsapp')}</a>
</div>"""


def schema():
    data = {
        "@context": "https://schema.org",
        "@type": ["AutoPartsStore", "MotorcycleRepair"],
        "name": CONFIG["name"],
        "description": t("home_desc"),
        "url": url_for(L, "index.html"),
        "telephone": CONFIG["phone_intl"],
        "email": CONFIG["email"],
        "address": {"@type": "PostalAddress", "addressLocality": "Sukkur",
                    "addressRegion": "Sindh", "addressCountry": "PK"},
        "areaServed": "Sukkur",
        "availableLanguage": ["sd", "ur", "en"],
        "priceRange": "$",
    }
    same = [CONFIG[k] for k in ("facebook", "instagram", "tiktok", "youtube") if CONFIG[k]]
    if same:
        data["sameAs"] = same
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def i18n_js():
    data = {k: fill(v[L]) for k, v in JS_KEYS.items()}
    data["fLanguage"] = t("f_language")
    data["fSentFrom"] = t("f_sent_from")
    data["langName"] = S["lang_name"][L]
    return json.dumps(data, ensure_ascii=False)


FONTS = ("https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700"
         "&family=Inter:wght@400;500;600;700"
         "&family=Noto+Naskh+Arabic:wght@400;600;700"
         "{nastaliq}&display=swap")


def page(slug, title, description, body, scripts=(), noindex=False):
    site_js = json.dumps({
        "whatsapp": CONFIG["whatsapp"],
        "phoneIntl": CONFIG["phone_intl"],
        "phoneDisplay": CONFIG["phone_display"],
        "formEndpoint": CONFIG["form_endpoint"],
    })
    full_title = title if CONFIG["name"] in title else f"{title} | {CONFIG['name']}"
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    alternates = "".join(f'<link rel="alternate" hreflang="{lang}" href="{url_for(lang, slug)}">\n' for lang in LANGS)
    alternates += f'<link rel="alternate" hreflang="x-default" href="{url_for("sd", slug)}">\n'
    fonts = FONTS.replace("{nastaliq}", "&family=Noto+Nastaliq+Urdu:wght@400;600;700" if L == "ur" else "")
    extra = "".join(f'<script src="{up()}assets/js/{s}" defer></script>' for s in scripts)
    return f"""<!doctype html>
<html lang="{L}" dir="{LANGS[L]['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
{robots}<link rel="canonical" href="{url_for(L, slug)}">
{alternates}<meta property="og:type" content="website">
<meta property="og:site_name" content="{CONFIG['name']}">
<meta property="og:locale" content="{LANGS[L]['og']}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url_for(L, slug)}">
<meta name="theme-color" content="#121419">
<link rel="icon" href="{up()}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{up()}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">
<link rel="stylesheet" href="{up()}assets/css/style.css">
{schema() if slug in ('index.html', 'contact.html') else ''}
<script>window.SITE = {site_js}; window.I18N = {i18n_js()};</script>
<!-- Analytics: paste Google Analytics / Meta Pixel code here -->
</head>
<body>
{SPRITE}
{header(slug)}
<main id="main">
{body}
</main>
{footer()}
{extra}<script src="{up()}assets/js/main.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Building blocks
# ---------------------------------------------------------------------------
def page_hero(title, text, crumb):
    return f"""
<section class="page-hero">
  <div class="container">
    <ol class="breadcrumb"><li><a href="index.html">{t('nav_home')}</a></li><li>{crumb}</li></ol>
    <h1>{title}</h1>
    <p>{text}</p>
  </div>
</section>"""


def honeypot():
    return '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'


BIKES = ["Honda CD 70", "Honda CG 125", "Honda Pridor", "Honda CB 150F", "Yamaha YBR 125",
         "Suzuki GD 110", "Suzuki GS 150", "Suzuki GR 150", "70cc (United, Road Prince, Unique…)",
         "125cc (local brands)"]


def bike_options():
    return "".join(f"<option>{b}</option>" for b in BIKES) + f"<option>{t('other')}</option>"


def select_bike(fid, required=True, label_key="f_bike"):
    req = " required" if required else ""
    star = ' <span class="req">*</span>' if required else ""
    return (f'<div class="field"><label for="{fid}">{t(label_key)}{star}</label>'
            f'<select id="{fid}" name="{t("f_bike")}"{req}><option value="">{t("select")}</option>{bike_options()}</select></div>')


def contact_fields(prefix="f"):
    return f"""
      <div class="form-row">
        <div class="field"><label for="{prefix}-name">{t('f_name')} <span class="req">*</span></label><input id="{prefix}-name" name="{t('f_name_short')}" autocomplete="name" required></div>
        <div class="field"><label for="{prefix}-phone">{t('f_phone')} <span class="req">*</span></label><input id="{prefix}-phone" name="{t('phone')}" type="tel" inputmode="tel" autocomplete="tel" placeholder="{t('phone_ph')}" pattern="[0-9+ ()-]{{10,16}}" required></div>
      </div>
      <div class="field"><label for="{prefix}-email">{t('f_email')} {t('optional')}</label><input id="{prefix}-email" name="{t('f_email')}" type="email" autocomplete="email"></div>"""


def submit_block(label):
    return f"""
      {honeypot()}
      <div class="form-status" role="status" aria-live="polite"></div>
      <button class="btn btn--primary btn--block" type="submit">{label}</button>
      <p class="form-note">{t('f_note')}</p>"""


def share_block():
    url = quote(url_for(L, "index.html"))
    text = quote(t("share_text") + " ")
    return f"""
<div class="share">
  <strong>{t('share')}</strong>
  <a href="https://wa.me/?text={text}{url}" target="_blank" rel="noopener" aria-label="{t('share_wa')}">{i('whatsapp')}</a>
  <a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener" aria-label="{t('share_fb')}">{i('facebook')}</a>
  <a href="https://twitter.com/intent/tweet?url={url}&text={quote(t('share_text'))}" target="_blank" rel="noopener" aria-label="{t('share_x')}">{i('x')}</a>
  <button type="button" data-share-copy aria-label="{t('share_copy')}">{i('link')}</button>
  <button type="button" data-share-native aria-label="{t('share_more')}">{i('share')}</button>
</div>"""


def cta_band(title_key="cta_title", text_key="cta_text"):
    return f"""
<section class="section">
  <div class="container">
    <div class="cta-band">
      <div><h2>{t(title_key)}</h2><p>{t(text_key)}</p></div>
      <div class="btn-row">
        <a class="btn btn--light" href="{wa('wa_default')}" target="_blank" rel="noopener">{i('whatsapp')} {t('whatsapp_us')}</a>
        <a class="btn btn--ghost" href="tel:{CONFIG['phone_intl']}">{i('phone')} {phone_html()}</a>
      </div>
    </div>
  </div>
</section>"""


SERVICE_ICONS = ["wrench", "engine", "brake", "clutch", "electric", "chain", "tyre", "filter"]


def services(n=8):
    return [(SERVICE_ICONS[k], t(f"svc{k + 1}_t"), t(f"svc{k + 1}_d")) for k in range(n)]


def service_options():
    return "".join(f"<option>{title}</option>" for _, title, _ in services()) + f"<option>{t('svc_not_sure')}</option>"


def service_cards(n=8):
    return "".join(f'<div class="card"><span class="card-icon">{i(ic)}</span><h3>{ti}</h3><p>{d}</p></div>' for ic, ti, d in services(n))


def time_select(fid):
    return (f'<div class="field"><label for="{fid}">{t("f_time")}</label><select id="{fid}" name="{t("f_time")}">'
            f'<option value="">{t("any_time")}</option><option>{t("morning")}</option><option>{t("afternoon")}</option><option>{t("evening")}</option></select></div>')


def list_check(keys, style=""):
    st = f' style="{style}"' if style else ""
    return f'<ul class="list-check"{st}>' + "".join(f"<li>{t(k)}</li>" for k in keys) + "</ul>"


# ---------------------------------------------------------------------------
# Pages — each function returns (title, description, body, scripts, noindex)
# ---------------------------------------------------------------------------
def p_index():
    cats = [("engine", "engine"), ("brakes", "brake"), ("clutch", "clutch"), ("chain", "chain"),
            ("electrical", "electric"), ("tyres", "tyre"), ("oils", "oil"), ("body", "accessory")]
    cat_cards = "".join(
        f'<a class="card card--link" href="products.html?cat={c}"><span class="card-icon">{i(ic)}</span><h3>{t("cat_" + c)}</h3><span class="more">{t("view_parts")} {i("arrow")}</span></a>'
        for c, ic in cats)
    chips = "".join(f"<li>{b}</li>" for b in ["Honda CD 70", "Honda CG 125", "Honda Pridor", "Honda CB 150F", "Yamaha YBR 125",
                                              "Suzuki GD 110", "Suzuki GS 150", "Suzuki GR 150", "United", "Road Prince", "Unique", "Super Power"])
    chips += f"<li>{t('bikes_other')}</li>"
    body = f"""
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow">{t('hero_eyebrow')}</span>
      <h1>{t('hero_h1')}</h1>
      <p class="lead">{t('hero_lead')}</p>
      <ul class="hero-badges">
        <li>{i('check')} {t('badge_parts')}</li>
        <li>{i('wrench')} {t('badge_mech')}</li>
        <li>{i('clock')} {t('hours_short')}</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--wa" href="{wa('wa_need_part')}" target="_blank" rel="noopener">{i('whatsapp')} {t('ask_wa')}</a>
        <a class="btn btn--primary" href="products.html">{t('browse_parts')} {i('arrow')}</a>
        <a class="btn btn--ghost" href="tel:{CONFIG['phone_intl']}">{i('phone')} {t('call')}</a>
      </div>
    </div>
    <div class="hero-art">{HERO_ART.replace('{label}', t('hero_art_label'))}</div>
  </div>
</section>

<div class="info-strip">
  <div class="container">
    <div class="grid">
      <div class="info-item">{i('phone')}<div><strong>{t('info_call')}</strong><a href="tel:{CONFIG['phone_intl']}">{phone_html()}</a></div></div>
      <div class="info-item">{i('pin')}<div><strong>{t('info_visit')}</strong><a href="{CONFIG['map_link']}" target="_blank" rel="noopener">{t('address')}</a></div></div>
      <div class="info-item">{i('clock')}<div><strong>{t('info_hours')}</strong><span>{t('hours')}</span></div></div>
    </div>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{t('cats_eyebrow')}</span>
      <h2>{t('cats_h2')}</h2>
      <p class="lead">{t('cats_lead')}</p>
    </div>
    <div class="grid grid--4">{cat_cards}</div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{t('popular_eyebrow')}</span>
      <h2>{t('popular_h2')}</h2>
      <p class="lead">{t('popular_lead')}</p>
    </div>
    <div class="grid grid--3" data-products data-limit="6"></div>
    <p style="margin-top:28px"><a class="btn btn--ghost" href="products.html">{t('see_all_parts')} {i('arrow')}</a></p>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{t('ws_eyebrow')}</span>
      <h2>{t('ws_h2')}</h2>
      <p class="lead">{t('ws_lead')}</p>
    </div>
    <div class="grid grid--4">{service_cards(4)}</div>
    <div class="btn-row" style="margin-top:28px">
      <a class="btn btn--primary" href="book-service.html">{i('calendar')} {t('book_service')}</a>
      <a class="btn btn--ghost" href="services.html">{t('all_services')} {i('arrow')}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">{t('how_eyebrow')}</span>
      <h2>{t('how_h2')}</h2>
    </div>
    <div class="grid grid--3 steps">
      <div class="card step"><h3>{t('step1_t')}</h3><p>{t('step1_d')}</p></div>
      <div class="card step"><h3>{t('step2_t')}</h3><p>{t('step2_d')}</p></div>
      <div class="card step"><h3>{t('step3_t')}</h3><p>{t('step3_d')}</p></div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container split">
    <div>
      <span class="eyebrow">{t('why_eyebrow')}</span>
      <h2>{t('why_h2')}</h2>
      {list_check(['why1', 'why2', 'why3', 'why4', 'why5'])}
      <a class="btn btn--primary" href="get-a-quote.html">{t('free_quote')}</a>
    </div>
    <div>
      <span class="eyebrow">{t('bikes_eyebrow')}</span>
      <h2>{t('bikes_h2')}</h2>
      <ul class="chips" dir="ltr">{chips}</ul>
      <p style="margin-top:18px;color:var(--muted)">{t('bikes_missing', wa=wa('wa_bike_q'))}</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">{t('review_eyebrow')}</span>
      <h2>{t('review_h2')}</h2>
      <p class="lead">{t('review_lead')}</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="{CONFIG['google_listing']}" target="_blank" rel="noopener">{i('star')} {t('review_google')}</a>
        <a class="btn btn--ghost" href="feedback.html">{t('private_feedback')}</a>
      </div>
    </div>
    <div class="form-panel">
      <h2>{t('offers_h2')}</h2>
      <p class="form-note" style="margin-bottom:16px">{t('offers_text')}</p>
      <form class="form" data-form data-subject="{t('subj_offers')}" novalidate>
        <div class="form-row">
          <div class="field"><label for="o-name">{t('f_name_short')} <span class="req">*</span></label><input id="o-name" name="{t('f_name_short')}" autocomplete="name" required></div>
          <div class="field"><label for="o-phone">{t('f_wa_number')} <span class="req">*</span></label><input id="o-phone" name="{t('f_wa_number')}" type="tel" inputmode="tel" placeholder="{t('phone_ph')}" pattern="[0-9+ ()-]{{10,16}}" required></div>
        </div>
        {select_bike('o-bike', required=False, label_key='f_your_bike')}
        <label class="check"><input type="checkbox" name="{t('consent')}" value="{t('offers_consent_value')}" required> {t('offers_consent')}</label>
        {submit_block(t('offers_btn'))}
      </form>
    </div>
  </div>
</section>
{cta_band()}
"""
    return t("home_title"), t("home_desc"), body, ["products.js"], False


def p_products():
    body = page_hero(t("products_h1"), t("products_lead"), t("nav_parts")) + f"""
<section class="section">
  <div class="container">
    <div class="filters">
      <div class="field filter-search"><label for="p-search">{t('search_parts')}</label><input id="p-search" type="search" placeholder="{t('search_ph')}" data-filter-search></div>
      <div class="field"><label for="p-cat">{t('category')}</label><select id="p-cat" data-filter-cat></select></div>
      <div class="field"><label for="p-bike">{t('f_your_bike')}</label><select id="p-bike" data-filter-bike></select></div>
    </div>
    <ul class="cat-tabs" data-cat-tabs aria-label="{t('categories')}"></ul>
    <div class="grid grid--3" data-products></div>
    <div class="card" style="margin-top:32px;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">
      <div><h3 style="margin:0">{t('cant_find_h')}</h3><p>{t('cant_find_p')}</p></div>
      <div class="btn-row"><a class="btn btn--wa" href="{wa('wa_photo')}" target="_blank" rel="noopener">{i('whatsapp')} {t('send_photo')}</a><a class="btn btn--ghost" href="enquiry.html">{i('list')} {t('view_list')}</a></div>
    </div>
  </div>
</section>
{cta_band()}
"""
    return t("products_title"), t("products_desc"), body, ["products.js"], False


def p_enquiry():
    body = page_hero(t("my_list"), t("enquiry_lead"), t("my_list")) + f"""
<section class="section">
  <div class="container split split--wide">
    <div>
      <h2>{t('your_parts')}</h2>
      <ul class="enquiry-items" data-enquiry-list></ul>
      <div class="btn-row">
        <a class="btn btn--wa" data-enquiry-wa href="{wa('wa_default')}" target="_blank" rel="noopener">{i('whatsapp')} {t('send_list_wa')}</a>
        <a class="btn btn--ghost" href="products.html">{i('plus')} {t('add_more_parts')}</a>
      </div>
    </div>
    <div class="form-panel">
      <h2>{t('or_email')}</h2>
      <form class="form" data-form data-subject="{t('subj_list')}" novalidate>
        {contact_fields()}
        {select_bike('e-bike')}
        <input type="hidden" name="{t('f_parts_list')}" data-enquiry-field>
        <div class="field"><label for="e-msg">{t('f_anything')}</label><textarea id="e-msg" name="{t('f_message')}" placeholder="{t('f_anything_ph')}"></textarea></div>
        {submit_block(t('send_my_list'))}
      </form>
    </div>
  </div>
</section>
"""
    return t("enquiry_title"), t("enquiry_desc"), body, ["products.js"], True


def booking_form(prefix, subject_key, btn_key, date_required=False):
    dreq = " required" if date_required else ""
    dstar = ' <span class="req">*</span>' if date_required else ""
    return f"""
      <form class="form" data-form data-subject="{t(subject_key)}" novalidate>
        {contact_fields()}
        <div class="form-row">
          {select_bike(prefix + '-bike')}
          <div class="field"><label for="{prefix}-service">{t('f_service')} <span class="req">*</span></label><select id="{prefix}-service" name="{t('service')}" required><option value="">{t('select')}</option>{service_options()}</select></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="{prefix}-date">{t('f_day')}{dstar}</label><input id="{prefix}-date" name="{t('f_day')}" type="date"{dreq}></div>
          {time_select(prefix + '-time')}
        </div>
        <div class="field"><label for="{prefix}-msg">{t('f_problem')}</label><textarea id="{prefix}-msg" name="{t('f_problem')}" placeholder="{t('f_problem_ph')}"></textarea></div>
        {submit_block(t(btn_key))}
      </form>"""


def p_services():
    body = page_hero(t("services_h1"), t("services_lead"), t("nav_services")) + f"""
<section class="section">
  <div class="container">
    <div class="grid grid--4">{service_cards()}</div>
  </div>
</section>
<section class="section section--soft">
  <div class="container split">
    <div>
      <span class="eyebrow">{t('before_eyebrow')}</span>
      <h2>{t('before_h2')}</h2>
      {list_check(['before1', 'before2', 'before3', 'before4'])}
      <a class="btn btn--wa" href="{wa('wa_problem')}" target="_blank" rel="noopener">{i('whatsapp')} {t('describe_problem')}</a>
    </div>
    <div class="form-panel" id="book">
      <h2>{t('book_service')}</h2>
      {booking_form('s', 'subj_booking', 'request_booking')}
    </div>
  </div>
</section>
{cta_band('breakdown_title', 'breakdown_text')}
"""
    return t("services_title"), t("services_desc"), body, [], False


def p_quote():
    body = f"""
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow">{t('quote_eyebrow')}</span>
      <h1>{t('quote_h1')}</h1>
      <p class="lead">{t('quote_lead')}</p>
      {list_check(['quote_b1', 'quote_b2', 'quote_b3'], 'color:#e7e9ee')}
      <div class="btn-row">
        <a class="btn btn--wa" href="{wa('wa_quote')}" target="_blank" rel="noopener">{i('whatsapp')} {t('faster_wa')}</a>
        <a class="btn btn--ghost" href="tel:{CONFIG['phone_intl']}">{i('phone')} {phone_html()}</a>
      </div>
    </div>
    <div class="form-panel">
      <h2>{t('request_quote')}</h2>
      <form class="form" data-form data-subject="{t('subj_quote')}" novalidate>
        {contact_fields()}
        <div class="form-row">
          {select_bike('q-bike')}
          <div class="field"><label for="q-year">{t('f_year')}</label><input id="q-year" name="{t('f_year')}" inputmode="numeric" placeholder="{t('f_year_ph')}"></div>
        </div>
        <div class="field"><label for="q-part">{t('f_parts')} <span class="req">*</span></label><textarea id="q-part" name="{t('f_parts')}" required placeholder="{t('f_parts_ph')}"></textarea><p class="hint">{t('f_parts_hint')}</p></div>
        <div class="field"><label for="q-how">{t('f_how')}</label><select id="q-how" name="{t('f_how')}"><option>{t('how_collect')}</option><option>{t('how_fit')}</option><option>{t('how_deliver')}</option></select></div>
        {submit_block(t('get_my_quote'))}
      </form>
    </div>
  </div>
</section>
<section class="section">
  <div class="container grid grid--3">
    <div class="card"><span class="card-icon">{i('tag')}</span><h3>{t('clear_prices')}</h3><p>{t('clear_prices_d')}</p></div>
    <div class="card"><span class="card-icon">{i('check')}</span><h3>{t('right_part')}</h3><p>{t('right_part_d')}</p></div>
    <div class="card"><span class="card-icon">{i('wrench')}</span><h3>{t('fitting_avail')}</h3><p>{t('fitting_avail_d')}</p></div>
  </div>
</section>
"""
    return t("quote_title"), t("quote_desc"), body, [], False


def p_book():
    body = f"""
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow">{t('book_eyebrow')}</span>
      <h1>{t('book_h1')}</h1>
      <p class="lead">{t('book_lead')}</p>
      {list_check(['book_b1', 'book_b2', 'book_b3'], 'color:#e7e9ee')}
    </div>
    <div class="form-panel">
      <h2>{t('choose_service')}</h2>
      {booking_form('b', 'subj_booking', 'book_my_service', date_required=True)}
    </div>
  </div>
</section>
{cta_band('prefer_talk', 'prefer_talk_t')}
"""
    return t("book_title"), t("book_desc"), body, [], False


def p_about():
    body = page_hero(t("about_title"), t("about_lead"), t("nav_about")) + f"""
<section class="section">
  <div class="container split">
    <div class="prose">
      <h2 style="margin-top:0">{t('about_h2')}</h2>
      <p>{t('about_p1')}</p>
      <p>{t('about_p2')}</p>
      <h3>{t('about_values')}</h3>
      {list_check(['about_v1', 'about_v2', 'about_v3'])}
    </div>
    <div class="grid">
      <div class="card"><span class="card-icon">{i('tag')}</span><h3>{t('about_c1_t')}</h3><p>{t('about_c1_d')}</p></div>
      <div class="card"><span class="card-icon">{i('wrench')}</span><h3>{t('about_c2_t')}</h3><p>{t('about_c2_d')}</p></div>
      <div class="card"><span class="card-icon">{i('chat')}</span><h3>{t('about_c3_t')}</h3><p>{t('about_c3_d')}</p></div>
    </div>
  </div>
</section>
<section class="section section--soft"><div class="container">{share_block()}</div></section>
{cta_band()}
"""
    return t("about_title"), t("about_desc"), body, [], False


def p_contact():
    topics = "".join(f"<option>{t(k)}</option>" for k in ("topic_part", "topic_repair", "topic_order", "topic_return", "topic_other"))
    body = page_hero(t("contact_h1"), t("contact_lead"), t("nav_contact")) + f"""
<section class="section">
  <div class="container split">
    <div>
      <ul class="contact-list">
        <li>{i('phone')}<div><strong>{t('phone')}</strong><a href="tel:{CONFIG['phone_intl']}">{phone_html()}</a></div></li>
        <li>{i('whatsapp')}<div><strong>{t('whatsapp')}</strong><a href="{wa('wa_default')}" target="_blank" rel="noopener">{t('chat_with_us')}</a></div></li>
        <li>{i('mail')}<div><strong>{t('email')}</strong><a href="mailto:{CONFIG['email']}" class="ltr">{CONFIG['email']}</a></div></li>
        <li>{i('pin')}<div><strong>{t('address_label')}</strong>{t('address')}<br><a href="{CONFIG['map_link']}" target="_blank" rel="noopener">{t('directions')}</a></div></li>
        <li>{i('clock')}<div><strong>{t('hours_label')}</strong>{t('hours')}</div></li>
      </ul>
      <iframe class="map" src="{CONFIG['map_embed']}" title="{t('map_title')}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
    <div class="form-panel">
      <h2>{t('send_message')}</h2>
      <form class="form" data-form data-subject="{t('subj_contact')}" novalidate>
        {contact_fields()}
        <div class="field"><label for="c-topic">{t('f_topic')}</label><select id="c-topic" name="{t('f_topic')}">{topics}</select></div>
        <div class="field"><label for="c-msg">{t('f_message')} <span class="req">*</span></label><textarea id="c-msg" name="{t('f_message')}" required></textarea></div>
        {submit_block(t('send_message_btn'))}
      </form>
    </div>
  </div>
</section>
"""
    return t("contact_title"), t("contact_desc"), body, [], False


def p_faq():
    items = "".join(f'<details><summary>{t(f"faq{n}_q")}</summary><div><p>{t(f"faq{n}_a")}</p></div></details>' for n in FAQ_KEYS)
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": L,
          "mainEntity": [{"@type": "Question", "name": t(f"faq{n}_q"),
                          "acceptedAnswer": {"@type": "Answer", "text": t(f"faq{n}_a")}} for n in FAQ_KEYS]}
    body = page_hero(t("faq_h1"), t("faq_lead"), t("nav_faq")) + f"""
<section class="section">
  <div class="container" style="max-width:860px">
    <div class="faq">{items}</div>
    <div class="card" style="margin-top:32px;text-align:center">
      <h3>{t('still_q')}</h3>
      <p>{t('still_q_t')}</p>
      <div class="btn-row" style="justify-content:center;margin-top:16px">
        <a class="btn btn--wa" href="{wa('wa_default')}" target="_blank" rel="noopener">{i('whatsapp')} {t('whatsapp')}</a>
        <a class="btn btn--ghost" href="contact.html">{t('contact_page')}</a>
      </div>
    </div>
  </div>
</section>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
"""
    return t("faq_title"), t("faq_desc"), body, [], False


def p_tips():
    icons = ["oil", "chain", "filter", "brake", "tyre", "electric", "engine"]
    tips = "".join(f'<div class="tip"><h3>{i(ic)} {t(f"tip{n}_t")}</h3><p>{t(f"tip{n}_d")}</p></div>' for n, ic in enumerate(icons, 1))
    body = page_hero(t("tips_h1"), t("tips_lead"), t("nav_tips")) + f"""
<section class="section">
  <div class="container split split--wide">
    <article class="prose">
      {tips}
      <p><em>{t('tips_note')}</em></p>
      {share_block()}
    </article>
    <aside>
      <div class="form-panel">
        <h2>{t('due_service')}</h2>
        <p class="form-note" style="margin-bottom:16px">{t('due_service_t')}</p>
        <a class="btn btn--primary btn--block" href="book-service.html">{i('calendar')} {t('book_service')}</a>
        <a class="btn btn--wa btn--block" style="margin-top:10px" href="{wa('wa_question')}" target="_blank" rel="noopener">{i('whatsapp')} {t('ask_mechanic')}</a>
      </div>
    </aside>
  </div>
</section>
"""
    return t("tips_title"), t("tips_desc"), body, [], False


def p_feedback():
    stars = "".join(
        f'<input type="radio" id="r{n}" name="{t("rating")}" value="{n} / 5" required><label for="r{n}" aria-label="{n} {t("stars")}">★</label>'
        for n in range(5, 0, -1))
    body = page_hero(t("feedback_h1"), t("feedback_lead"), t("give_feedback")) + f"""
<section class="section">
  <div class="container split">
    <div>
      <h2>{t('loved_it')}</h2>
      <p class="lead">{t('loved_it_t')}</p>
      <a class="btn btn--primary" href="{CONFIG['google_listing']}" target="_blank" rel="noopener">{i('star')} {t('review_google')}</a>
      <div style="margin-top:28px">{share_block()}</div>
    </div>
    <div class="form-panel">
      <h2>{t('private_fb_h')}</h2>
      <form class="form" data-form data-subject="{t('subj_feedback')}" novalidate>
        <fieldset class="field">
          <legend>{t('rating')} <span class="req">*</span></legend>
          <div class="rating">{stars}</div>
        </fieldset>
        <div class="form-row">
          <div class="field"><label for="fb-name">{t('f_name_short')}</label><input id="fb-name" name="{t('f_name_short')}" autocomplete="name"></div>
          <div class="field"><label for="fb-phone">{t('fb_phone')}</label><input id="fb-phone" name="{t('phone')}" type="tel" inputmode="tel" pattern="[0-9+ ()-]{{10,16}}"></div>
        </div>
        <div class="field"><label for="fb-msg">{t('fb_text')} <span class="req">*</span></label><textarea id="fb-msg" name="{t('fb_text')}" required></textarea></div>
        {honeypot()}
        <div class="form-status" role="status" aria-live="polite"></div>
        <button class="btn btn--primary btn--block" type="submit">{t('send_feedback')}</button>
      </form>
    </div>
  </div>
</section>
"""
    return t("feedback_title"), t("feedback_desc"), body, [], False


def p_policy(slug):
    pol = POLICIES[slug]
    title = pol["title"][L]
    desc = pol["desc"][L]
    contact = (LABELS["contact_p"][L]
               .replace("{phone_link}", f'<a href="tel:{CONFIG["phone_intl"]}">{phone_html()}</a>')
               .replace("{email_link}", f'<a href="mailto:{CONFIG["email"]}" class="ltr">{CONFIG["email"]}</a>'))
    body = page_hero(title, desc, title) + f"""
<section class="section"><div class="container"><article class="prose">
<p class="updated">{LABELS['updated'][L]} <span class="ltr">{CONFIG['policy_updated']}</span></p>
{fill(pol['body'][L])}
<h2>{LABELS['contact_h'][L]}</h2>
<p>{fill(contact)}</p>
</article></div></section>"""
    return title, desc, body, [], False


def p_thanks():
    body = f"""
<section class="section center-page">
  <div class="container" style="max-width:640px">
    <svg class="icon big-icon" aria-hidden="true"><use href="#i-check"></use></svg>
    <h1>{t('thanks_h1')}</h1>
    <p class="lead">{t('thanks_lead')}</p>
    <p>{t('thanks_more')}</p>
    <div class="btn-row" style="justify-content:center;margin-top:20px">
      <a class="btn btn--wa" href="{wa('wa_default')}" target="_blank" rel="noopener">{i('whatsapp')} {t('whatsapp_us')}</a>
      <a class="btn btn--ghost" href="products.html">{t('keep_browsing')}</a>
    </div>
  </div>
</section>
"""
    return t("thanks_title"), t("thanks_desc"), body, [], True


def p_404():
    body = f"""
<section class="section center-page">
  <div class="container" style="max-width:640px">
    <svg class="icon big-icon" aria-hidden="true"><use href="#i-wrench"></use></svg>
    <h1>{t('nf_h1')}</h1>
    <p class="lead">{t('nf_lead')}</p>
    <div class="btn-row" style="justify-content:center;margin-top:20px">
      <a class="btn btn--primary" href="/{LANGS[L]['folder']}index.html">{t('nav_home')}</a>
      <a class="btn btn--ghost" href="/{LANGS[L]['folder']}products.html">{t('nav_parts')}</a>
      <a class="btn btn--wa" href="{wa('wa_default')}" target="_blank" rel="noopener">{i('whatsapp')} {t('whatsapp')}</a>
    </div>
  </div>
</section>
"""
    return t("nf_title"), t("nf_desc"), body, [], True


PAGES = {
    "index.html": p_index,
    "products.html": p_products,
    "enquiry.html": p_enquiry,
    "services.html": p_services,
    "get-a-quote.html": p_quote,
    "book-service.html": p_book,
    "about.html": p_about,
    "contact.html": p_contact,
    "faq.html": p_faq,
    "bike-care-tips.html": p_tips,
    "feedback.html": p_feedback,
    "thank-you.html": p_thanks,
    "404.html": p_404,
}
for _slug in POLICIES:
    PAGES[_slug] = (lambda s: (lambda: p_policy(s)))(_slug)


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def main():
    global L
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(SRC / "assets", DIST / "assets")
    (DIST / "assets/img").mkdir(parents=True, exist_ok=True)
    (DIST / "assets/img/favicon.svg").write_text(LOGO.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))

    indexable = []
    count = 0
    for L in LANGS:
        out_dir = DIST / LANGS[L]["folder"]
        out_dir.mkdir(parents=True, exist_ok=True)
        for slug, build in PAGES.items():
            title, desc, body, scripts, noindex = build()
            (out_dir / slug).write_text(page(slug, title, desc, body, scripts, noindex), encoding="utf-8")
            count += 1
            if not noindex and L == "sd":
                indexable.append(slug)

    # Sitemap with all three languages linked to each other
    urls = []
    for slug in indexable:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{lg}" href="{url_for(lg, slug)}"/>' for lg in LANGS)
        for lg in LANGS:
            urls.append(f"<url><loc>{url_for(lg, slug)}</loc>{alts}</url>")
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + "".join(urls) + "</urlset>\n")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {CONFIG['site_url']}/sitemap.xml\n")
    (DIST / "site.webmanifest").write_text(json.dumps({
        "name": CONFIG["name"], "short_name": "Al-Bais", "start_url": "/",
        "display": "standalone", "background_color": "#121419", "theme_color": "#e8491d",
        "icons": [{"src": "/assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
    }, indent=2))
    print(f"Built {count} pages ({len(PAGES)} pages x {len(LANGS)} languages) into {DIST}")


if __name__ == "__main__":
    main()
