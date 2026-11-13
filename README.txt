AL-BAIS MOTORS WEBSITE — Sindhi, Urdu, English
==============================================

Languages
  /        Sindhi (main language)
  /ur/     Urdu
  /en/     English
Every page has a language switch at the top.

Files
  build.py        Shop details: phone, email, map, social links, domain (CONFIG at the top)
  content.py      All page text in Sindhi, Urdu and English
  policies.py     Privacy, Terms, Returns & Warranty, Delivery pages in all three languages
  svg_blocks.py   Icons, logo and the hero picture
  src/            Styles, scripts and the parts catalogue (src/assets/js/products.js)
  dist/           The finished website (built automatically — do not edit)
  netlify.toml    Tells Netlify to run build.py and publish dist/

Change something
  1. Edit the file (e.g. a sentence in content.py, a part in products.js).
  2. Commit and push from VS Code. Netlify rebuilds the site in 1–2 minutes.
     (To check on your own computer first:  python3 build.py  then open dist/index.html)

Forms
  Forms email aliasad@gmail.com through FormSubmit. The first time a form is sent
  from the live site, FormSubmit emails an activation link — click it once.
  Form emails use the visitor's language for field names and show which language
  they used.
