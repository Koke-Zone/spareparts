AL-BAIS MOTORS WEBSITE
======================

dist/      The finished website. Upload everything inside this folder to your hosting.
src/       Styles, scripts and the parts catalogue (src/assets/js/products.js).
build.py   Shop details (phone, email, address, social links, domain) and page text.

CHANGE DETAILS
1. Open build.py and edit the CONFIG section at the top.
2. Run:  python3 build.py
3. Upload the new dist/ folder.

ADD OR EDIT PARTS
Edit src/assets/js/products.js (copy a line, change it), run build.py, upload dist/.

FORMS
Forms email aliasad@gmail.com through FormSubmit (free, no account).
The FIRST time someone submits a form on the live site, FormSubmit emails
aliasad@gmail.com an activation link. Click it once — after that, every form
arrives by email. Forms only work on the live website (not when opening files
directly from your computer). If sending fails, visitors are offered WhatsApp instead.
