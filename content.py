# -*- coding: utf-8 -*-
"""
All website text in three languages: Sindhi (sd), Urdu (ur), English (en).

To change any wording: find the key below and edit the text for that
language, then run  python3 build.py.
Placeholders in {curly braces} are filled in automatically
(city, address, phone, hours, name).
"""

S = {}


def s(key, sd, ur, en):
    S[key] = {"sd": sd, "ur": ur, "en": en}


# ---------------------------------------------------------------------------
# Shop details shown in text
# ---------------------------------------------------------------------------
s("city", "سکر", "سکھر", "Sukkur")
s("address", "سکر، سنڌ، پاڪستان", "سکھر، سندھ، پاکستان", "Sukkur, Sindh, Pakistan")
s("hours", "اڄ رات 8 وڳي تائين کليل", "آج رات 8 بجے تک کھلا ہے", "Open today until 8:00 PM")
s("hours_short", "رات 8 وڳي تائين", "رات 8 بجے تک", "Closes 8:00 PM")
s("tagline", "موٽر سائيڪل اسپيئر پارٽس ۽ مرمت", "موٹر سائیکل اسپیئر پارٹس اور مرمت", "Motorcycle Spare Parts & Repair")
s("lang_name", "سنڌي", "اردو", "English")
s("language", "ٻولي", "زبان", "Language")

# ---------------------------------------------------------------------------
# Header, navigation, footer
# ---------------------------------------------------------------------------
s("skip", "مواد ڏانهن وڃو", "مواد پر جائیں", "Skip to content")
s("nav_home", "مکيه صفحو", "ہوم", "Home")
s("nav_parts", "اسپيئر پارٽس", "اسپیئر پارٹس", "Spare Parts")
s("nav_services", "مرمت ۽ سروس", "مرمت اور سروس", "Repair & Service")
s("nav_tips", "بائيڪ جي سنڀال", "بائیک کی دیکھ بھال", "Bike Care Tips")
s("nav_about", "اسان بابت", "ہمارے بارے میں", "About")
s("nav_faq", "عام سوال", "عام سوالات", "FAQ")
s("nav_contact", "رابطو", "رابطہ", "Contact")
s("menu", "مينيو", "مینو", "Menu")
s("whatsapp_us", "واٽس ايپ ڪريو", "واٹس ایپ کریں", "WhatsApp us")
s("whatsapp", "واٽس ايپ", "واٹس ایپ", "WhatsApp")
s("call", "ڪال", "کال", "Call")
s("call_now", "هاڻي ڪال ڪريو", "ابھی کال کریں", "Call now")
s("email", "اي ميل", "ای میل", "Email")
s("chat_wa", "واٽس ايپ تي ڳالهايو", "واٹس ایپ پر بات کریں", "Chat on WhatsApp")
s("get_quote", "قيمت معلوم ڪريو", "قیمت معلوم کریں", "Get a quote")
s("get_quote_long", "پارٽس جي قيمت معلوم ڪريو", "پارٹس کی قیمت معلوم کریں", "Get a parts quote")
s("my_list", "منهنجي پارٽس لسٽ", "میری پارٹس لسٹ", "My parts list")
s("home_aria", "مکيه صفحو", "ہوم پیج", "home")
s("footer_about", "سڀني مشهور موٽر سائيڪلن جا اسپيئر پارٽس، ۽ انهن کي لڳائڻ لاءِ ورڪشاپ — {city} ۾.",
  "تمام مشہور موٹر سائیکلوں کے اسپیئر پارٹس، اور انہیں لگانے کے لیے ورکشاپ — {city} میں۔",
  "Spare parts for all popular motorcycles, and a workshop to fit them — in {city}.")
s("f_shop", "دڪان", "دکان", "Shop")
s("f_help", "مدد", "مدد", "Help")
s("f_visit", "اچو يا ڪال ڪريو", "تشریف لائیں یا کال کریں", "Visit or call")
s("all_parts_link", "سڀ اسپيئر پارٽس", "تمام اسپیئر پارٹس", "All spare parts")
s("book_service", "سروس بُڪ ڪريو", "سروس بک کریں", "Book a service")
s("give_feedback", "پنهنجي راءِ ڏيو", "اپنی رائے دیں", "Give feedback")
s("directions", "رستو ڏسو ←", "راستہ دیکھیں ←", "Get directions →")
s("rights", "سڀ حق محفوظ آهن.", "جملہ حقوق محفوظ ہیں۔", "All rights reserved.")
s("privacy_short", "رازداري", "پرائیویسی", "Privacy")
s("terms_short", "شرطون", "شرائط", "Terms")
s("returns_short", "واپسي ۽ وارنٽي", "واپسی اور وارنٹی", "Returns & warranty")
s("delivery_short", "ڊليوري", "ڈیلیوری", "Delivery")
s("share", "شيئر ڪريو:", "شیئر کریں:", "Share:")
s("share_wa", "واٽس ايپ تي شيئر ڪريو", "واٹس ایپ پر شیئر کریں", "Share on WhatsApp")
s("share_fb", "فيس بڪ تي شيئر ڪريو", "فیس بک پر شیئر کریں", "Share on Facebook")
s("share_x", "X تي شيئر ڪريو", "X پر شیئر کریں", "Share on X")
s("share_copy", "لنڪ ڪاپي ڪريو", "لنک کاپی کریں", "Copy link")
s("share_more", "ٻيا طريقا", "مزید طریقے", "More sharing options")
s("share_text", "{city} ۾ موٽر سائيڪل پارٽس ۽ مرمت — Al-Bais Motors",
  "{city} میں موٹر سائیکل پارٹس اور مرمت — Al-Bais Motors",
  "Motorcycle spare parts & repair in {city} — Al-Bais Motors")

# ---------------------------------------------------------------------------
# Categories & services
# ---------------------------------------------------------------------------
s("cat_engine", "انجڻ جا پارٽس", "انجن پارٹس", "Engine Parts")
s("cat_brakes", "بريڪون", "بریکیں", "Brakes")
s("cat_clutch", "ڪلچ ۽ گيئر باڪس", "کلچ اور گیئر باکس", "Clutch & Gearbox")
s("cat_chain", "زنجير ۽ اسپراڪيٽ", "چین اور اسپراکٹ", "Chain & Sprockets")
s("cat_electrical", "اليڪٽريڪل ۽ لائٽون", "الیکٹریکل اور لائٹس", "Electrical & Lights")
s("cat_tyres", "ٽائر ۽ ٽيوب", "ٹائر اور ٹیوب", "Tyres & Tubes")
s("cat_oils", "آئل ۽ لُبريڪنٽ", "آئل اور لبریکنٹس", "Oils & Lubricants")
s("cat_body", "باڊي ۽ ايڪسيسريز", "باڈی اور ایکسیسریز", "Body & Accessories")
s("view_parts", "پارٽس ڏسو", "پارٹس دیکھیں", "View parts")

s("svc1_t", "جنرل سروس ۽ ٽيون اپ", "جنرل سروس اور ٹیون اپ", "General service & tune-up")
s("svc1_d", "آئل بدلائڻ، ايئر فلٽر جي صفائي، اسپارڪ پلگ چيڪ، زنجير سيٽ ڪرڻ ۽ مڪمل حفاظتي چيڪ.",
  "آئل کی تبدیلی، ایئر فلٹر کی صفائی، اسپارک پلگ چیک، چین کی ایڈجسٹمنٹ اور مکمل حفاظتی چیک۔",
  "Oil change, air filter clean, spark plug check, chain adjust and a full safety check.")
s("svc2_t", "انجڻ جي مرمت ۽ اوور هال", "انجن کی مرمت اور اوور ہال", "Engine repair & overhaul")
s("svc2_d", "ڪمزور پڪ اپ، دونهون، آواز يا آئل ليڪ — اسين خرابي ڳولي مرمت ڪريون ٿا، ٽاپ اوور هال کان مڪمل انجڻ تائين.",
  "کمزور پک اپ، دھواں، شور یا آئل لیک — ہم خرابی تلاش کر کے مرمت کرتے ہیں، ٹاپ اوور ہال سے مکمل انجن تک۔",
  "Low pickup, smoke, noise or oil leaks — we diagnose and repair, from top overhaul to full rebuild.")
s("svc3_t", "بريڪون", "بریکیں", "Brakes")
s("svc3_d", "بريڪ شوز، ڊسڪ پيڊز، ڪيبل ۽ سيٽنگ ته جيئن بائيڪ محفوظ طريقي سان رڪجي.",
  "بریک شوز، ڈسک پیڈز، کیبلز اور ایڈجسٹمنٹ تاکہ بائیک محفوظ طریقے سے رکے۔",
  "Brake shoes, disc pads, cables and adjustment so your bike stops safely.")
s("svc4_t", "ڪلچ ۽ گيئر باڪس", "کلچ اور گیئر باکس", "Clutch & gearbox")
s("svc4_d", "ڪلچ سلپ، گيئر سخت لڳڻ يا گيئر نڪري وڃڻ — پليٽون، اسپرنگ ۽ ڪيبل لڳايون ٿا.",
  "کلچ سلپ، گیئر سخت لگنا یا گیئر نکل جانا — پلیٹیں، اسپرنگ اور کیبلز لگاتے ہیں۔",
  "Clutch slip, hard gear shifts or jumping gears — plates, springs and cables fitted.")
s("svc5_t", "اليڪٽريڪل ۽ سيلف اسٽارٽ", "الیکٹریکل اور سیلف اسٹارٹ", "Electrical & self-start")
s("svc5_d", "بيٽري، وائرنگ، لائٽون، انڊيڪيٽر، هارن، CDI ۽ سيلف اسٽارٽ جا مسئلا.",
  "بیٹری، وائرنگ، لائٹس، انڈیکیٹرز، ہارن، CDI اور سیلف اسٹارٹ کے مسائل۔",
  "Battery, wiring, lights, indicators, horn, CDI and self-start problems.")
s("svc6_t", "زنجير ۽ اسپراڪيٽ", "چین اور اسپراکٹ", "Chain & sprocket")
s("svc6_d", "زنجير جي صفائي، سيٽنگ ۽ ڪٽ بدلائڻ — آرام سان ۽ خاموش سواري لاءِ.",
  "چین کی صفائی، ایڈجسٹمنٹ اور کٹ کی تبدیلی — ہموار اور خاموش سواری کے لیے۔",
  "Chain cleaning, adjustment and kit replacement for a smooth, quiet ride.")
s("svc7_t", "ٽائر ۽ پنڪچر", "ٹائر اور پنکچر", "Tyres & puncture")
s("svc7_d", "ٽائر ۽ ٽيوب بدلائڻ، پنڪچر جي مرمت ۽ ڦيٿي جي چڪاس.",
  "ٹائر اور ٹیوب کی تبدیلی، پنکچر کی مرمت اور پہیے کی جانچ۔",
  "Tyre and tube change, puncture repair and wheel checks.")
s("svc8_t", "ڪاربوريٽر ۽ فيول", "کاربوریٹر اور فیول", "Carburetor & fuel")
s("svc8_d", "ڪاربوريٽر جي صفائي ۽ ٽيوننگ — سٺي آئيڊلنگ ۽ بهتر ايوريج لاءِ.",
  "کاربوریٹر کی صفائی اور ٹیوننگ — بہتر آئیڈلنگ اور اوسط کے لیے۔",
  "Carburetor cleaning and tuning for steady idle and better mileage.")
s("svc_not_sure", "پڪ ناهي — منهنجي بائيڪ چيڪ ڪريو", "یقین نہیں — میری بائیک چیک کریں", "Not sure — please check my bike")

# ---------------------------------------------------------------------------
# Forms (shared)
# ---------------------------------------------------------------------------
s("f_name", "توهان جو نالو", "آپ کا نام", "Your name")
s("f_name_short", "نالو", "نام", "Name")
s("f_phone", "فون / واٽس ايپ", "فون / واٹس ایپ", "Phone / WhatsApp")
s("f_wa_number", "واٽس ايپ نمبر", "واٹس ایپ نمبر", "WhatsApp number")
s("f_email", "اي ميل", "ای میل", "Email")
s("optional", "(اختياري)", "(اختیاری)", "(optional)")
s("f_bike", "بائيڪ ماڊل", "بائیک ماڈل", "Bike model")
s("f_your_bike", "توهان جي بائيڪ", "آپ کی بائیک", "Your bike")
s("select", "چونڊيو…", "منتخب کریں…", "Select…")
s("other", "ٻي", "دیگر", "Other")
s("f_message", "پيغام", "پیغام", "Message")
s("f_topic", "موضوع", "موضوع", "Topic")
s("f_service", "ڪهڙي سروس گهرجي", "کون سی سروس چاہیے", "Service needed")
s("f_day", "پسنديده ڏينهن", "پسندیدہ دن", "Preferred day")
s("f_time", "پسنديده وقت", "پسندیدہ وقت", "Preferred time")
s("any_time", "ڪنهن به وقت", "کسی بھی وقت", "Any time")
s("morning", "صبح", "صبح", "Morning")
s("afternoon", "منجهند", "دوپہر", "Afternoon")
s("evening", "شام (رات 8 کان اڳ)", "شام (رات 8 سے پہلے)", "Evening (before 8 PM)")
s("f_problem", "ڪهڙو مسئلو آهي؟", "کیا مسئلہ ہے؟", "What's the problem?")
s("f_problem_ph", "مثال: صبح جو بائيڪ اسٽارٽ نٿي ٿئي، ڪلچ سلپ ٿو ڪري…", "مثلاً: صبح بائیک اسٹارٹ نہیں ہوتی، کلچ سلپ کرتا ہے…",
  "e.g. bike won't start in the morning, clutch slipping…")
s("f_notes", "نوٽس", "نوٹس", "Notes")
s("f_notes_ph", "ڪا ٻي ڳالهه جيڪا اسان کي ڄاڻڻ گهرجي؟", "کوئی اور بات جو ہمیں معلوم ہونی چاہیے؟", "Anything we should know?")
s("f_year", "سال", "سال", "Year")
s("f_year_ph", "مثال: 2021", "مثلاً 2021", "e.g. 2021")
s("f_parts", "گهربل پارٽ / پارٽس", "مطلوبہ پارٹ / پارٹس", "Part(s) needed")
s("f_parts_ph", "مثال: ڪلچ پليٽون ۽ گيسڪيٽ سيٽ", "مثلاً کلچ پلیٹیں اور گیسکٹ سیٹ", "e.g. clutch plates and gasket set")
s("f_parts_hint", "پراڻي پارٽ جي تصوير آهي؟ فارم موڪلڻ کان پوءِ واٽس ايپ تي موڪليو.",
  "پرانے پارٹ کی تصویر ہے؟ فارم بھیجنے کے بعد واٹس ایپ پر بھیج دیں۔",
  "Have a photo of the old part? Send it on WhatsApp after submitting.")
s("f_how", "پارٽ ڪيئن گهرجي؟", "پارٹ کیسے چاہیے؟", "How do you want it?")
s("how_collect", "دڪان تان پاڻ وٺندس", "دکان سے خود لوں گا", "I'll collect from the shop")
s("how_fit", "وٺي بائيڪ ۾ لڳائي ڏيو", "لے کر بائیک میں لگا دیں", "Collect and fit it for me")
s("how_deliver", "ڊليوري ڪريو (ڊليوري بابت پڇو)", "ڈیلیوری کریں (ڈیلیوری کے بارے میں پوچھیں)", "Please deliver (ask about delivery)")
s("f_anything", "ٻيو ڪجهه؟", "کچھ اور؟", "Anything else?")
s("f_anything_ph", "بائيڪ جو سال، رنگ، پاڻ وٺڻ يا ڊليوري…", "بائیک کا سال، رنگ، خود لینا یا ڈیلیوری…", "Year of the bike, colour, collection or delivery…")
s("f_parts_list", "پارٽس جي لسٽ", "پارٹس کی لسٹ", "Parts list")
s("f_language", "ٻولي", "زبان", "Language")
s("f_sent_from", "صفحو", "صفحہ", "Sent from page")
s("f_note", "اسين فون يا واٽس ايپ تي جواب ڏيون ٿا، اڪثر ساڳئي ڏينهن. ڏسو اسان جي <a href=\"privacy-policy.html\">رازداري پاليسي</a>.",
  "ہم فون یا واٹس ایپ پر جواب دیتے ہیں، عموماً اسی دن۔ ہماری <a href=\"privacy-policy.html\">پرائیویسی پالیسی</a> دیکھیں۔",
  "We reply by phone or WhatsApp, usually the same day. See our <a href=\"privacy-policy.html\">privacy policy</a>.")
s("phone_ph", "03XX XXXXXXX", "03XX XXXXXXX", "03XX XXXXXXX")
s("topic_part", "اسپيئر پارٽ جي قيمت / اسٽاڪ", "اسپیئر پارٹ کی قیمت / اسٹاک", "Spare part price / stock")
s("topic_repair", "مرمت يا سروس", "مرمت یا سروس", "Repair or service")
s("topic_order", "آرڊر يا ڊليوري", "آرڈر یا ڈیلیوری", "Order or delivery")
s("topic_return", "واپسي يا وارنٽي", "واپسی یا وارنٹی", "Return or warranty")
s("topic_other", "ٻيو ڪجهه", "کچھ اور", "Something else")

# Form subjects (email subject line)
s("subj_offers", "آفرز لاءِ سائن اپ", "آفرز کے لیے سائن اپ", "Offers sign-up")
s("subj_list", "پارٽس لسٽ جي پڇا", "پارٹس لسٹ کی انکوائری", "Parts list enquiry")
s("subj_booking", "سروس بُڪنگ", "سروس بکنگ", "Service booking")
s("subj_quote", "پارٽس جي قيمت جي درخواست", "پارٹس کوٹ کی درخواست", "Parts quote request")
s("subj_contact", "رابطي جو فارم", "رابطہ فارم", "Contact form")
s("subj_feedback", "گراهڪ جي راءِ", "کسٹمر کی رائے", "Customer feedback")

# ---------------------------------------------------------------------------
# Shared blocks
# ---------------------------------------------------------------------------
s("cta_title", "اڄ ئي پارٽ گهرجي؟", "آج ہی پارٹ چاہیے؟", "Need a part today?")
s("cta_text", "پنهنجي بائيڪ جو ماڊل ۽ گهربل پارٽ موڪليو — اسين واٽس ايپ تي قيمت ۽ اسٽاڪ ٻڌائينداسين.",
  "اپنی بائیک کا ماڈل اور مطلوبہ پارٹ بھیجیں — ہم واٹس ایپ پر قیمت اور اسٹاک بتائیں گے۔",
  "Send your bike model and the part you need — we'll confirm price and stock on WhatsApp.")

# WhatsApp prefilled messages
s("wa_default", "السلام عليڪم Al-Bais Motors، مون کي پنهنجي بائيڪ لاءِ مدد گهرجي.",
  "السلام علیکم Al-Bais Motors، مجھے اپنی بائیک کے لیے مدد چاہیے۔",
  "Hi Al-Bais Motors, I need help with my bike.")
s("wa_need_part", "السلام عليڪم Al-Bais Motors، مون کي اسپيئر پارٽ گهرجي. منهنجي بائيڪ: ",
  "السلام علیکم Al-Bais Motors، مجھے اسپیئر پارٹ چاہیے۔ میری بائیک: ",
  "Hi Al-Bais Motors, I need a spare part. My bike: ")
s("wa_bike_q", "السلام عليڪم Al-Bais Motors، ڇا توهان وٽ منهنجي بائيڪ جا پارٽس آهن؟ ماڊل: ",
  "السلام علیکم Al-Bais Motors، کیا آپ کے پاس میری بائیک کے پارٹس ہیں؟ ماڈل: ",
  "Hi Al-Bais Motors, do you have parts for my bike? Model: ")
s("wa_photo", "السلام عليڪم Al-Bais Motors، مان هي پارٽ ڳولي رهيو آهيان (تصوير گڏ آهي). منهنجي بائيڪ: ",
  "السلام علیکم Al-Bais Motors، میں یہ پارٹ تلاش کر رہا ہوں (تصویر ساتھ ہے)۔ میری بائیک: ",
  "Hi Al-Bais Motors, I am looking for a part (photo attached). My bike: ")
s("wa_problem", "السلام عليڪم Al-Bais Motors، منهنجي بائيڪ ۾ هي مسئلو آهي: ",
  "السلام علیکم Al-Bais Motors، میری بائیک میں یہ مسئلہ ہے: ",
  "Hi Al-Bais Motors, my bike has a problem: ")
s("wa_quote", "السلام عليڪم Al-Bais Motors، مهرباني ڪري هن جي قيمت ٻڌايو: ",
  "السلام علیکم Al-Bais Motors، براہ کرم اس کی قیمت بتائیں: ",
  "Hi Al-Bais Motors, please quote me for: ")
s("wa_question", "السلام عليڪم Al-Bais Motors، منهنجو بائيڪ بابت سوال آهي: ",
  "السلام علیکم Al-Bais Motors، میرا بائیک کے بارے میں سوال ہے: ",
  "Hi Al-Bais Motors, I have a question about my bike: ")

# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------
s("home_title", "Al-Bais Motors — {city} ۾ موٽر سائيڪل اسپيئر پارٽس ۽ مرمت",
  "Al-Bais Motors — {city} میں موٹر سائیکل اسپیئر پارٹس اور مرمت",
  "Al-Bais Motors — Motorcycle Spare Parts & Repair in {city}")
s("home_desc", "{city} ۾ معياري موٽر سائيڪل اسپيئر پارٽس ۽ ماهر مرمت. هونڊا، ياماها، سوزوڪي ۽ سڀني 70cc/125cc بائيڪن جا پارٽس. ڪال يا واٽس ايپ {phone}.",
  "{city} میں معیاری موٹر سائیکل اسپیئر پارٹس اور ماہر مرمت۔ ہونڈا، یاماہا، سوزوکی اور تمام 70cc/125cc بائیکس کے پارٹس۔ کال یا واٹس ایپ {phone}۔",
  "Quality motorcycle spare parts and expert repair in {city}. Parts for Honda, Yamaha, Suzuki and all 70cc/125cc bikes. Call or WhatsApp {phone}.")
s("hero_eyebrow", "{city} · اسپيئر پارٽس ۽ ورڪشاپ", "{city} · اسپیئر پارٹس اور ورکشاپ", "{city} · Spare parts & workshop")
s("hero_h1", "موٽر سائيڪل پارٽس ۽ مرمت، <span>صحيح نموني.</span>", "موٹر سائیکل پارٹس اور مرمت، <span>بالکل درست۔</span>",
  "Motorcycle parts &amp; repair, <span>done right.</span>")
s("hero_lead", "نئين اسپارڪ پلگ کان وٺي مڪمل انجڻ اوور هال تائين — پنهنجي بائيڪ لاءِ صحيح پارٽ وٺو ۽ ساڳئي هنڌ مستري کان لڳرايو.",
  "نئے اسپارک پلگ سے لے کر مکمل انجن اوور ہال تک — اپنی بائیک کے لیے درست پارٹ لیں اور ایک ہی جگہ مستری سے لگوائیں۔",
  "From a new spark plug to a full engine overhaul — get the right part for your bike and a mechanic to fit it, all in one place.")
s("badge_parts", "سڀني مشهور بائيڪن جا پارٽس", "تمام مشہور بائیکس کے پارٹس", "Parts for all popular bikes")
s("badge_mech", "دڪان تي مستري موجود", "دکان پر مستری موجود", "Mechanic on site")
s("ask_wa", "واٽس ايپ تي پڇو", "واٹس ایپ پر پوچھیں", "Ask on WhatsApp")
s("browse_parts", "پارٽس ڏسو", "پارٹس دیکھیں", "Browse parts")
s("info_call", "ڪال يا واٽس ايپ", "کال یا واٹس ایپ", "Call or WhatsApp")
s("info_visit", "دڪان تي اچو", "دکان پر آئیں", "Visit the shop")
s("info_hours", "کلڻ جو وقت", "اوقاتِ کار", "Opening hours")
s("hero_art_label", "موٽر سائيڪل ۽ اسپيئر پارٽس جي تصوير", "موٹر سائیکل اور اسپیئر پارٹس کی تصویر", "Illustration of a motorcycle with spare parts")
s("cats_eyebrow", "قسم مطابق ڏسو", "قسم کے مطابق دیکھیں", "Shop by category")
s("cats_h2", "توهان جي بائيڪ جو هر پارٽ", "آپ کی بائیک کا ہر پارٹ", "Every part your bike needs")
s("cats_lead", "ڪو قسم چونڊيو ۽ عام پارٽس ڏسو — يا رڳو پنهنجي بائيڪ جو ماڊل موڪليو. اسان وٽ لسٽ کان گهڻا وڌيڪ پارٽس آهن.",
  "کوئی قسم منتخب کریں اور عام پارٹس دیکھیں — یا صرف اپنی بائیک کا ماڈل بھیجیں۔ ہمارے پاس فہرست سے کہیں زیادہ پارٹس موجود ہیں۔",
  "Pick a category to see common parts, or just send us your bike model — we stock far more than we can list.")
s("popular_eyebrow", "مشهور پارٽس", "مقبول پارٹس", "Popular parts")
s("popular_h2", "سڀ کان وڌيڪ گهرجندڙ پارٽس", "سب سے زیادہ مانگے جانے والے پارٹس", "Most-asked-for parts")
s("popular_lead", "<strong>قيمت پڇو</strong> دٻايو ۽ واٽس ايپ تي اڄ جي قيمت معلوم ڪريو — يا پارٽس لسٽ ۾ شامل ڪري سڀ گڏ موڪليو.",
  "<strong>قیمت پوچھیں</strong> دبائیں اور واٹس ایپ پر آج کی قیمت معلوم کریں — یا پارٹس لسٹ میں شامل کر کے سب ایک ساتھ بھیجیں۔",
  "Tap <strong>Ask price</strong> to get today's price on WhatsApp, or add parts to your list and send them all at once.")
s("see_all_parts", "سڀ پارٽس ڏسو", "تمام پارٹس دیکھیں", "See all parts")
s("ws_eyebrow", "ورڪشاپ", "ورکشاپ", "Workshop")
s("ws_h2", "تجربيڪار مستري کان مرمت ۽ سروس", "تجربہ کار مستریوں سے مرمت اور سروس", "Repair & service by experienced mechanics")
s("ws_lead", "پارٽ وٺو ۽ ساڳئي وقت لڳرايو — دڪان دڪان ڊوڙڻ جي ضرورت ناهي.",
  "پارٹ خریدیں اور اسی وقت لگوائیں — دکان دکان بھاگنے کی ضرورت نہیں۔",
  "Buy the part and get it fitted the same visit — no running between shops.")
s("all_services", "سڀ سروسز", "تمام سروسز", "All services")
s("how_eyebrow", "ڪيئن ٿو ٿئي", "طریقہ کار", "How it works")
s("how_h2", "3 آسان قدمن ۾ پارٽ", "3 آسان مراحل میں پارٹ", "Your part in 3 easy steps")
s("step1_t", "پنهنجي بائيڪ ٻڌايو", "اپنی بائیک بتائیں", "Tell us your bike")
s("step1_d", "واٽس ايپ يا ڪال ڪري بائيڪ ماڊل ۽ گهربل پارٽ ٻڌايو. پراڻي پارٽ جي تصوير مدد ڪري ٿي.",
  "واٹس ایپ یا کال کر کے بائیک ماڈل اور مطلوبہ پارٹ بتائیں۔ پرانے پارٹ کی تصویر مددگار ہوتی ہے۔",
  "WhatsApp or call with your bike model and the part you need. A photo of the old part helps.")
s("step2_t", "قيمت ۽ اسٽاڪ معلوم ڪريو", "قیمت اور اسٹاک معلوم کریں", "Get price & stock")
s("step2_d", "اسين صحيح پارٽ، قيمت ۽ اسٽاڪ جي تصديق ڪريون ٿا — توهان جي اچڻ کان اڳ.",
  "ہم درست پارٹ، قیمت اور اسٹاک کی تصدیق کرتے ہیں — آپ کے آنے سے پہلے۔",
  "We confirm the right part, the price and whether it's in stock — before you travel.")
s("step3_t", "وٺو يا لڳرايو", "لے جائیں یا لگوائیں", "Collect or get it fitted")
s("step3_d", "دڪان تان پارٽ وٺو، يا اسان جو مستري توهان جي سامهون لڳائي ڏيندو.",
  "دکان سے پارٹ لے جائیں، یا ہمارا مستری آپ کے سامنے لگا دے گا۔",
  "Pick it up at the shop, or let our mechanic fit it while you wait.")
s("why_eyebrow", "سوار اسان کي ڇو چونڊين ٿا", "سوار ہمیں کیوں چنتے ہیں", "Why riders choose us")
s("why_h2", "سڌو جواب، صحيح پارٽ", "سیدھا جواب، درست پارٹ", "Straight answers, the right part")
s("why1", "هونڊا، ياماها، سوزوڪي ۽ سڀني مقامي 70cc ۽ 125cc بائيڪن جا پارٽس",
  "ہونڈا، یاماہا، سوزوکی اور تمام مقامی 70cc اور 125cc بائیکس کے پارٹس",
  "Parts for Honda, Yamaha, Suzuki and all local 70cc &amp; 125cc bikes")
s("why2", "صاف قيمتون — خريد کان اڳ پڇو، ڪو سرپرائز ناهي", "واضح قیمتیں — خریدنے سے پہلے پوچھیں، کوئی سرپرائز نہیں",
  "Clear prices — ask before you buy, no surprises")
s("why3", "خريد ڪيل پارٽ لڳائڻ لاءِ دڪان تي مستري", "خریدا گیا پارٹ لگانے کے لیے دکان پر مستری", "Mechanic on site to fit what you buy")
s("why4", "واٽس ايپ تي جلدي جواب", "واٹس ایپ پر فوری جواب", "Quick replies on WhatsApp")
s("why5", "ايماندار صلاح — پارٽ بدلائڻو آهي يا رڳو مرمت", "ایماندارانہ مشورہ — پارٹ بدلنا ہے یا صرف مرمت",
  "Honest advice on whether a part needs replacing or just repair")
s("free_quote", "مفت قيمت معلوم ڪريو", "مفت قیمت معلوم کریں", "Get a free parts quote")
s("bikes_eyebrow", "اسان جون بائيڪون", "ہم کن بائیکس کے پارٹس رکھتے ہیں", "Bikes we cover")
s("bikes_h2", "توهان جي بائيڪ جا پارٽس", "آپ کی بائیک کے پارٹس", "Parts for your bike")
s("bikes_other", "ٻي 70cc / 125cc", "دیگر 70cc / 125cc", "Other 70cc / 125cc")
s("bikes_missing", "توهان جي بائيڪ نه آهي؟ <a href=\"{wa}\" target=\"_blank\" rel=\"noopener\">واٽس ايپ تي پڇو</a>.",
  "آپ کی بائیک نظر نہیں آئی؟ <a href=\"{wa}\" target=\"_blank\" rel=\"noopener\">واٹس ایپ پر پوچھیں</a>۔",
  "Don't see your bike? <a href=\"{wa}\" target=\"_blank\" rel=\"noopener\">Ask us on WhatsApp</a>.")
s("review_eyebrow", "اسان کان خوش آهيو؟", "ہم سے خوش ہیں؟", "Happy with us?")
s("review_h2", "ٻين سوارن کي ٻڌايو", "دوسرے سواروں کو بتائیں", "Tell other riders")
s("review_lead", "گوگل تي هڪ ننڍو ريويو {city} جي ٻين سوارن کي ڀروسي وارو دڪان ڳولڻ ۾ مدد ڪري ٿو.",
  "گوگل پر ایک مختصر ریویو {city} کے دوسرے سواروں کو قابلِ اعتماد دکان تلاش کرنے میں مدد دیتا ہے۔",
  "A quick Google review helps other riders in {city} find a shop they can trust.")
s("review_google", "گوگل تي ريويو ڏيو", "گوگل پر ریویو دیں", "Review us on Google")
s("private_feedback", "پنهنجي راءِ موڪليو", "اپنی رائے بھیجیں", "Send private feedback")
s("offers_h2", "واٽس ايپ تي آفرز حاصل ڪريو", "واٹس ایپ پر آفرز حاصل کریں", "Get offers on WhatsApp")
s("offers_text", "نئين اسٽاڪ ۽ موسمي آفرز بابت سڀ کان پهرين ڄاڻو. ڪو اسپام ناهي — جڏهن چاهيو بند ڪريو.",
  "نئے اسٹاک اور موسمی آفرز کے بارے میں سب سے پہلے جانیں۔ کوئی اسپام نہیں — جب چاہیں بند کریں۔",
  "Be first to hear about new stock and seasonal offers. No spam — leave any time.")
s("offers_consent", "مان واٽس ايپ تي آفرز وٺڻ لاءِ راضي آهيان.", "میں واٹس ایپ پر آفرز وصول کرنے پر راضی ہوں۔",
  "I agree to receive offers on WhatsApp.")
s("offers_consent_value", "ها، واٽس ايپ تي آفرز موڪليو", "جی ہاں، واٹس ایپ پر آفرز بھیجیں", "Yes, send me offers on WhatsApp")
s("offers_btn", "سائن اپ ڪريو", "سائن اپ کریں", "Sign me up")
s("consent", "اجازت", "اجازت", "Consent")

# ---------------------------------------------------------------------------
# Products & enquiry pages
# ---------------------------------------------------------------------------
s("products_title", "{city} ۾ موٽر سائيڪل اسپيئر پارٽس", "{city} میں موٹر سائیکل اسپیئر پارٹس", "Motorcycle Spare Parts in {city}")
s("products_desc", "انجڻ پارٽس، بريڪون، ڪلچ، زنجير ڪٽ، اليڪٽريڪل، ٽائر ۽ آئل — هونڊا، ياماها، سوزوڪي ۽ مقامي بائيڪن لاءِ. واٽس ايپ تي اڄ جي قيمت پڇو.",
  "انجن پارٹس، بریکیں، کلچ، چین کٹس، الیکٹریکل، ٹائر اور آئل — ہونڈا، یاماہا، سوزوکی اور مقامی بائیکس کے لیے۔ واٹس ایپ پر آج کی قیمت پوچھیں۔",
  "Engine parts, brakes, clutch, chain kits, electrical, tyres and oils for Honda, Yamaha, Suzuki and local bikes. Ask today's price on WhatsApp.")
s("products_h1", "موٽر سائيڪل اسپيئر پارٽس", "موٹر سائیکل اسپیئر پارٹس", "Motorcycle spare parts")
s("products_lead", "قسم يا بائيڪ مطابق ڳوليو. قيمتون اسٽاڪ مطابق بدلجن ٿيون، تنهنڪري اڄ جي قيمت لاءِ <strong>قيمت پڇو</strong> دٻايو — يا پارٽس لسٽ ۾ شامل ڪري سڀ گڏ موڪليو.",
  "قسم یا بائیک کے مطابق تلاش کریں۔ قیمتیں اسٹاک کے ساتھ بدلتی ہیں، اس لیے آج کی قیمت کے لیے <strong>قیمت پوچھیں</strong> دبائیں — یا پارٹس لسٹ میں شامل کر کے سب ایک ساتھ بھیجیں۔",
  "Filter by category or your bike. Prices change with stock, so tap <strong>Ask price</strong> for today's price — or add parts to your list and send them all at once.")
s("search_parts", "پارٽس ڳوليو", "پارٹس تلاش کریں", "Search parts")
s("search_ph", "مثال: ڪلچ پليٽ، بيٽري، CG 125", "مثلاً کلچ پلیٹ، بیٹری، CG 125", "e.g. clutch plates, battery, CG 125")
s("category", "قسم", "قسم", "Category")
s("categories", "قسم", "اقسام", "Categories")
s("cant_find_h", "پارٽ نٿو ملي؟", "پارٹ نہیں مل رہا؟", "Can't find your part?")
s("cant_find_p", "اسان وٽ هتي لسٽ کان گهڻا وڌيڪ پارٽس آهن. پراڻي پارٽ جي تصوير واٽس ايپ تي موڪليو.",
  "ہمارے پاس یہاں کی فہرست سے کہیں زیادہ پارٹس ہیں۔ پرانے پارٹ کی تصویر واٹس ایپ پر بھیجیں۔",
  "We stock many more parts than we list here. Send a photo of the old part on WhatsApp.")
s("send_photo", "تصوير موڪليو", "تصویر بھیجیں", "Send photo")
s("view_list", "منهنجي لسٽ ڏسو", "میری لسٹ دیکھیں", "View my list")
s("enquiry_title", "منهنجي پارٽس لسٽ", "میری پارٹس لسٹ", "My Parts List")
s("enquiry_desc", "پنهنجي موٽر سائيڪل پارٽس جي لسٽ Al-Bais Motors ڏانهن موڪليو ۽ قيمت ۽ اسٽاڪ معلوم ڪريو.",
  "اپنی موٹر سائیکل پارٹس کی لسٹ Al-Bais Motors کو بھیجیں اور قیمت اور اسٹاک معلوم کریں۔",
  "Send your list of motorcycle parts to Al-Bais Motors and get prices and availability.")
s("enquiry_lead", "لسٽ چيڪ ڪريو، پوءِ واٽس ايپ يا اي ميل ذريعي موڪليو. اسين قيمت ۽ اسٽاڪ سان جواب ڏينداسين.",
  "لسٹ چیک کریں، پھر واٹس ایپ یا ای میل سے بھیجیں۔ ہم قیمت اور اسٹاک کے ساتھ جواب دیں گے۔",
  "Review your list, then send it on WhatsApp or by email. We'll reply with prices and availability.")
s("your_parts", "توهان جا پارٽس", "آپ کے پارٹس", "Your parts")
s("send_list_wa", "لسٽ واٽس ايپ تي موڪليو", "لسٹ واٹس ایپ پر بھیجیں", "Send list on WhatsApp")
s("add_more_parts", "وڌيڪ پارٽس شامل ڪريو", "مزید پارٹس شامل کریں", "Add more parts")
s("or_email", "يا اي ميل ذريعي موڪليو", "یا ای میل سے بھیجیں", "Or send by email")
s("send_my_list", "منهنجي لسٽ موڪليو", "میری لسٹ بھیجیں", "Send my list")

# ---------------------------------------------------------------------------
# Services & landing pages
# ---------------------------------------------------------------------------
s("services_title", "{city} ۾ موٽر سائيڪل مرمت ۽ سروس", "{city} میں موٹر سائیکل مرمت اور سروس", "Motorcycle Repair & Service in {city}")
s("services_desc", "{city} ۾ سڀني مشهور موٽر سائيڪلن لاءِ انجڻ مرمت، ٽيون اپ، بريڪون، ڪلچ، اليڪٽريڪل ۽ ٽائر جو ڪم. Al-Bais Motors تي سروس بُڪ ڪريو.",
  "{city} میں تمام مشہور موٹر سائیکلوں کے لیے انجن مرمت، ٹیون اپ، بریکیں، کلچ، الیکٹریکل اور ٹائر کا کام۔ Al-Bais Motors پر سروس بک کریں۔",
  "Engine repair, tune-ups, brakes, clutch, electrical and tyre work for all popular motorcycles in {city}. Book your service with Al-Bais Motors.")
s("services_h1", "مرمت ۽ سروس", "مرمت اور سروس", "Repair &amp; service")
s("services_lead", "اسان جا مستري روزانه جا مسئلا حل ڪن ٿا — ۽ اسان کان خريد ڪيل پارٽ توهان جي سامهون لڳائي ڏين ٿا.",
  "ہمارے مستری روزمرہ کے مسائل حل کرتے ہیں — اور ہم سے خریدا گیا پارٹ آپ کے سامنے لگا دیتے ہیں۔",
  "Our mechanics fix the problems riders see every day — and fit the parts you buy from us while you wait.")
s("before_eyebrow", "اچڻ کان اڳ", "آنے سے پہلے", "Before you come")
s("before_h2", "پنهنجو وقت بچايو", "اپنا وقت بچائیں", "Make your visit quick")
s("before1", "مسئلو واٽس ايپ تي ٻڌايو — آواز يا خرابي جي ننڍي وڊيو تمام گهڻي مدد ڪري ٿي",
  "مسئلہ واٹس ایپ پر بتائیں — آواز یا خرابی کی مختصر ویڈیو بہت مدد کرتی ہے",
  "Tell us the problem on WhatsApp — a short video of the noise or fault really helps")
s("before2", "اسين ممڪن حل ۽ گهربل پارٽس ٻڌائينداسين", "ہم ممکنہ حل اور مطلوبہ پارٹس بتائیں گے", "We'll tell you the likely fix and the parts needed")
s("before3", "وقت بُڪ ڪريو ته جيئن مستري توهان لاءِ تيار هجي", "وقت بک کریں تاکہ مستری آپ کے لیے تیار ہو", "Book a time so the mechanic is ready for you")
s("before4", "ڪم شروع ڪرڻ کان اڳ ڪم ۽ قيمت طئي ڪريون ٿا", "کام شروع کرنے سے پہلے کام اور قیمت طے کرتے ہیں", "We explain the work and agree the price before we start")
s("describe_problem", "مسئلو ٻڌايو", "مسئلہ بتائیں", "Describe the problem")
s("request_booking", "بُڪنگ جي درخواست موڪليو", "بکنگ کی درخواست بھیجیں", "Request booking")
s("breakdown_title", "بائيڪ خراب ٿي وئي؟", "بائیک خراب ہو گئی؟", "Bike broken down?")
s("breakdown_text", "اسان کي ڪال ڪريو — اڪثر فون تي ئي ٻڌائي سگهون ٿا ته پهرين ڇا چيڪ ڪجي.",
  "ہمیں کال کریں — اکثر فون پر ہی بتا سکتے ہیں کہ پہلے کیا چیک کریں۔",
  "Call us — we can usually tell you over the phone what to check first.")

s("quote_title", "موٽر سائيڪل پارٽس جي قيمت معلوم ڪريو — Al-Bais Motors", "موٹر سائیکل پارٹس کی قیمت معلوم کریں — Al-Bais Motors",
  "Get a Motorcycle Parts Quote — Al-Bais Motors")
s("quote_desc", "پنهنجي بائيڪ ۽ گهربل پارٽ ٻڌايو. {city} ۾ Al-Bais Motors اڪثر ساڳئي ڏينهن قيمت ۽ اسٽاڪ سان جواب ڏئي ٿو.",
  "اپنی بائیک اور مطلوبہ پارٹ بتائیں۔ {city} میں Al-Bais Motors عموماً اسی دن قیمت اور اسٹاک کے ساتھ جواب دیتا ہے۔",
  "Tell us your bike and the part you need. Al-Bais Motors in {city} replies with price and stock, usually the same day.")
s("quote_eyebrow", "مفت قيمت، ڪا پابندي ناهي", "مفت قیمت، کوئی پابندی نہیں", "Free, no-obligation quote")
s("quote_h1", "صحيح پارٽ جي قيمت <span>اڄ ئي</span>", "درست پارٹ کی قیمت <span>آج ہی</span>", "Get the right part's <span>price today</span>")
s("quote_lead", "پنهنجي بائيڪ ۽ گهربل پارٽ ٻڌايو. اسين اسٽاڪ چيڪ ڪري صاف قيمت موڪليون ٿا — اڪثر ساڳئي ڏينهن.",
  "اپنی بائیک اور مطلوبہ پارٹ بتائیں۔ ہم اسٹاک چیک کر کے واضح قیمت بھیجتے ہیں — عموماً اسی دن۔",
  "Tell us your bike and the part you need. We check stock and send you a clear price — usually the same day.")
s("quote_b1", "هونڊا، ياماها، سوزوڪي ۽ سڀني مقامي بائيڪن جا پارٽس", "ہونڈا، یاماہا، سوزوکی اور تمام مقامی بائیکس کے پارٹس", "Parts for Honda, Yamaha, Suzuki &amp; all local bikes")
s("quote_b2", "توهان جي ماڊل لاءِ صحيح پارٽ جي تصديق", "آپ کے ماڈل کے لیے درست پارٹ کی تصدیق", "We confirm the correct part for your model")
s("quote_b3", "دڪان تان وٺو يا لڳرايو", "دکان سے لیں یا لگوائیں", "Collect from the shop or get it fitted")
s("faster_wa", "واٽس ايپ تي جلدي", "واٹس ایپ پر جلدی", "Faster on WhatsApp")
s("request_quote", "قيمت جي درخواست", "قیمت کی درخواست", "Request a quote")
s("get_my_quote", "منهنجي قيمت موڪليو", "میری قیمت بھیجیں", "Get my quote")
s("clear_prices", "صاف قيمتون", "واضح قیمتیں", "Clear prices")
s("clear_prices_d", "سفر کان اڳ قيمت معلوم — ڪائونٽر تي ڪو سرپرائز ناهي.", "آنے سے پہلے قیمت معلوم — کاؤنٹر پر کوئی سرپرائز نہیں۔",
  "You get the price before you travel. No surprises at the counter.")
s("right_part", "صحيح پارٽ", "درست پارٹ", "The right part")
s("right_part_d", "ماڊل ۽ سال ٻڌايو — اسين ٻيهر چيڪ ڪريون ٿا ته پارٽ فٽ ٿئي.", "ماڈل اور سال بتائیں — ہم دوبارہ چیک کرتے ہیں کہ پارٹ فٹ ہو۔",
  "Tell us the model and year — we double-check the part fits.")
s("fitting_avail", "لڳائڻ جي سهولت", "لگانے کی سہولت", "Fitting available")
s("fitting_avail_d", "اسان جو مستري ساڳئي وقت پارٽ لڳائي سگهي ٿو.", "ہمارا مستری اسی وقت پارٹ لگا سکتا ہے۔", "Our mechanic can fit the part on the same visit.")

s("book_title", "{city} ۾ موٽر سائيڪل سروس بُڪ ڪريو", "{city} میں موٹر سائیکل سروس بک کریں", "Book a Motorcycle Service in {city}")
s("book_desc", "{city} ۾ Al-Bais Motors تي پنهنجي موٽر سائيڪل جي سروس يا مرمت بُڪ ڪريو. ڏينهن ۽ وقت چونڊيو، اسين واٽس ايپ تي تصديق ڪنداسين.",
  "{city} میں Al-Bais Motors پر اپنی موٹر سائیکل کی سروس یا مرمت بک کریں۔ دن اور وقت منتخب کریں، ہم واٹس ایپ پر تصدیق کریں گے۔",
  "Book your motorcycle service or repair at Al-Bais Motors, {city}. Choose a day and time and we'll confirm on WhatsApp.")
s("book_eyebrow", "ورڪشاپ بُڪنگ", "ورکشاپ بکنگ", "Workshop booking")
s("book_h1", "بائيڪ بُڪ ڪريو — <span>انتظار کان بچو</span>", "بائیک بک کریں — <span>انتظار سے بچیں</span>", "Book your bike in — <span>skip the wait</span>")
s("book_lead", "سروس ۽ پنهنجي مرضي جو وقت چونڊيو. اسين واٽس ايپ تي تصديق ڪنداسين ۽ مستري توهان جي اچڻ تي تيار هوندو.",
  "سروس اور اپنی مرضی کا وقت منتخب کریں۔ ہم واٹس ایپ پر تصدیق کریں گے اور مستری آپ کے آنے پر تیار ہوگا۔",
  "Choose the service and a time that suits you. We'll confirm on WhatsApp and have the mechanic ready when you arrive.")
s("book_b1", "ٽيون اپ، آئل چينج ۽ مڪمل سروس", "ٹیون اپ، آئل چینج اور مکمل سروس", "Tune-ups, oil changes and full services")
s("book_b2", "انجڻ، ڪلچ، بريڪ ۽ اليڪٽريڪل مرمت", "انجن، کلچ، بریک اور الیکٹریکل مرمت", "Engine, clutch, brake and electrical repairs")
s("book_b3", "ڪم شروع ٿيڻ کان اڳ قيمت طئي", "کام شروع ہونے سے پہلے قیمت طے", "Price agreed before any work starts")
s("choose_service", "سروس چونڊيو", "سروس منتخب کریں", "Choose your service")
s("service", "سروس", "سروس", "Service")
s("book_my_service", "منهنجي سروس بُڪ ڪريو", "میری سروس بک کریں", "Book my service")
s("prefer_talk", "ڳالهائڻ پسند ڪندا؟", "بات کرنا پسند کریں گے؟", "Prefer to talk?")
s("prefer_talk_t", "ڪال يا واٽس ايپ ڪريو، اسين سڌو بُڪ ڪنداسين.", "کال یا واٹس ایپ کریں، ہم براہِ راست بک کر دیں گے۔", "Call or WhatsApp and we will book you in directly.")

# ---------------------------------------------------------------------------
# About, contact, FAQ, tips, feedback
# ---------------------------------------------------------------------------
s("about_title", "Al-Bais Motors بابت", "Al-Bais Motors کے بارے میں", "About Al-Bais Motors")
s("about_desc", "Al-Bais Motors {city} ۾ موٽر سائيڪل اسپيئر پارٽس جو دڪان ۽ ورڪشاپ آهي، جيڪو مقامي سوارن جون بائيڪون هلندڙ رکي ٿو.",
  "Al-Bais Motors {city} میں موٹر سائیکل اسپیئر پارٹس کی دکان اور ورکشاپ ہے، جو مقامی سواروں کی بائیکس چلتی رکھتی ہے۔",
  "Al-Bais Motors is a motorcycle spare parts shop and workshop in {city}, helping local riders keep their bikes running.")
s("about_lead", "{city} ۾ موٽر سائيڪل اسپيئر پارٽس جو مقامي دڪان ۽ ورڪشاپ.", "{city} میں موٹر سائیکل اسپیئر پارٹس کی مقامی دکان اور ورکشاپ۔",
  "A local motorcycle spare parts shop and workshop in {city}.")
s("about_h2", "{city} کي هلندڙ رکڻ", "{city} کو رواں دواں رکھنا", "Keeping {city} riding")
s("about_p1", "هتي گهڻن خاندانن لاءِ موٽر سائيڪل ڪم، اسڪول ۽ بازار وڃڻ جو ذريعو آهي. جڏهن اها خراب ٿئي ٿي، توهان کي جلدي صحيح پارٽ گهرجي — مناسب قيمت تي — ۽ اهڙو ماڻهو جيڪو ان کي صحيح نموني لڳائي.",
  "یہاں زیادہ تر خاندانوں کے لیے موٹر سائیکل ہی کام، اسکول اور بازار جانے کا ذریعہ ہے۔ جب یہ خراب ہو تو آپ کو جلدی درست پارٹ چاہیے — مناسب قیمت پر — اور کوئی ایسا جو اسے صحیح طریقے سے لگائے۔",
  "For most families here, the motorcycle is how you get to work, school and the market. When it breaks down, you need the right part quickly — at a fair price — and someone who can fit it properly.")
s("about_p2", "اسين اهو ئي ڪريون ٿا. Al-Bais Motors انهن بائيڪن جا اسپيئر پارٽس رکي ٿو جيڪي ماڻهو واقعي هلائين ٿا — هونڊا CD 70 ۽ CG 125 کان وٺي ياماها، سوزوڪي ۽ مقامي 70cc ۽ 125cc ماڊلن تائين — ۽ انهن کي لڳائڻ لاءِ ورڪشاپ به.",
  "ہم یہی کرتے ہیں۔ Al-Bais Motors ان بائیکس کے اسپیئر پارٹس رکھتا ہے جو لوگ واقعی چلاتے ہیں — ہونڈا CD 70 اور CG 125 سے لے کر یاماہا، سوزوکی اور مقامی 70cc اور 125cc ماڈلز تک — اور انہیں لگانے کے لیے ورکشاپ بھی۔",
  "That's what we do. Al-Bais Motors stocks spare parts for the bikes people actually ride, from Honda CD 70s and CG 125s to Yamaha, Suzuki and local 70cc and 125cc models, with a workshop to fit them.")
s("about_values", "اسان جا اصول", "ہمارے اصول", "What we believe in")
s("about_v1", "<strong>ايماندار صلاح</strong> — جيڪڏهن پارٽ مرمت ٿي سگهي ٿو ته اسين ٻڌائينداسين.",
  "<strong>ایماندارانہ مشورہ</strong> — اگر پارٹ مرمت ہو سکتا ہے تو ہم بتائیں گے۔",
  "<strong>Honest advice</strong> — if a part can be repaired instead of replaced, we'll tell you.")
s("about_v2", "<strong>پهرين ڀيري صحيح پارٽ</strong> — وڪڻڻ کان اڳ توهان جو ماڊل چيڪ ڪريون ٿا.",
  "<strong>پہلی بار ہی درست پارٹ</strong> — بیچنے سے پہلے آپ کا ماڈل چیک کرتے ہیں۔",
  "<strong>The right part first time</strong> — we check your model before we sell.")
s("about_v3", "<strong>صاف قيمتون</strong> — ڪم شروع ٿيڻ کان اڳ توهان کي خرچ معلوم هوندو.",
  "<strong>واضح قیمتیں</strong> — کام شروع ہونے سے پہلے آپ کو خرچ معلوم ہوگا۔",
  "<strong>Clear prices</strong> — you know the cost before we start.")
s("about_c1_t", "اسپيئر پارٽس ڪائونٽر", "اسپیئر پارٹس کاؤنٹر", "Spare parts counter")
s("about_c1_d", "انجڻ، بريڪ، ڪلچ، اليڪٽريڪل، ٽائر، آئل ۽ باڊي پارٽس.", "انجن، بریک، کلچ، الیکٹریکل، ٹائر، آئل اور باڈی پارٹس۔",
  "Engine, brake, clutch, electrical, tyres, oils and body parts.")
s("about_c2_t", "ورڪشاپ", "ورکشاپ", "Workshop")
s("about_c2_d", "سروس ۽ مرمت، ساڳئي وقت پارٽ لڳائڻ سان.", "سروس اور مرمت، اسی وقت پارٹ لگانے کے ساتھ۔", "Servicing and repairs, with parts fitted the same visit.")
s("about_c3_t", "واٽس ايپ تي جلدي مدد", "واٹس ایپ پر فوری مدد", "Quick help on WhatsApp")
s("about_c3_d", "قيمت، اسٽاڪ يا بائيڪ جي مسئلي بابت پڇو.", "قیمت، اسٹاک یا بائیک کے مسئلے کے بارے میں پوچھیں۔", "Ask about prices, stock or a problem with your bike.")

s("contact_title", "Al-Bais Motors سان رابطو — {city}", "Al-Bais Motors سے رابطہ — {city}", "Contact Al-Bais Motors — {city}")
s("contact_desc", "ڪال يا واٽس ايپ {phone}، اي ميل ڪريو يا {city} ۾ Al-Bais Motors تي اچو. {hours}.",
  "کال یا واٹس ایپ {phone}، ای میل کریں یا {city} میں Al-Bais Motors پر آئیں۔ {hours}۔",
  "Call or WhatsApp {phone}, email us or visit Al-Bais Motors in {city}. {hours}.")
s("contact_h1", "اسان سان رابطو ڪريو", "ہم سے رابطہ کریں", "Contact us")
s("contact_lead", "اسان تائين پهچڻ جو سڀ کان تيز طريقو واٽس ايپ آهي. توهان ڪال، اي ميل يا هيٺيون فارم به استعمال ڪري سگهو ٿا.",
  "ہم تک پہنچنے کا سب سے تیز طریقہ واٹس ایپ ہے۔ آپ کال، ای میل یا نیچے دیا گیا فارم بھی استعمال کر سکتے ہیں۔",
  "The quickest way to reach us is WhatsApp. You can also call, email or use the form below.")
s("phone", "فون", "فون", "Phone")
s("chat_with_us", "اسان سان ڳالهايو", "ہم سے بات کریں", "Chat with us")
s("address_label", "پتو", "پتہ", "Address")
s("hours_label", "وقت", "اوقات", "Hours")
s("map_title", "Al-Bais Motors جو نقشو", "Al-Bais Motors کا نقشہ", "Map showing Al-Bais Motors")
s("send_message", "پيغام موڪليو", "پیغام بھیجیں", "Send a message")
s("send_message_btn", "پيغام موڪليو", "پیغام بھیجیں", "Send message")

s("faq_title", "عام سوال", "عام سوالات", "Frequently Asked Questions")
s("faq_desc", "{city} ۾ Al-Bais Motors تي پارٽس، قيمتن، لڳائڻ، ڊليوري، واپسي ۽ ادائگي بابت جواب.",
  "{city} میں Al-Bais Motors پر پارٹس، قیمتوں، لگانے، ڈیلیوری، واپسی اور ادائیگی کے بارے میں جوابات۔",
  "Answers about parts, prices, fitting, delivery, returns and payment at Al-Bais Motors, {city}.")
s("faq_h1", "عام سوال", "عام سوالات", "Frequently asked questions")
s("faq_lead", "سوارن جي سڀ کان وڌيڪ پڇيل سوالن جا مختصر جواب.", "سواروں کے سب سے زیادہ پوچھے گئے سوالات کے مختصر جوابات۔",
  "Quick answers to what riders ask us most.")
s("still_q", "اڃا ڪو سوال آهي؟", "اب بھی کوئی سوال ہے؟", "Still have a question?")
s("still_q_t", "سڌو پڇو — اسين اڪثر ساڳئي ڏينهن جواب ڏيون ٿا.", "براہِ راست پوچھیں — ہم عموماً اسی دن جواب دیتے ہیں۔",
  "Ask us directly — we usually reply the same day.")
s("contact_page", "رابطي جو صفحو", "رابطہ صفحہ", "Contact page")
FAQ_KEYS = []
for n, (sd_q, ur_q, en_q, sd_a, ur_a, en_a) in enumerate([
    ("ڇا توهان وٽ منهنجي بائيڪ جا پارٽس آهن؟", "کیا آپ کے پاس میری بائیک کے پارٹس ہیں؟", "Do you have parts for my bike?",
     "اسان وٽ هونڊا CD 70، CG 125، پرائيڊر، CB 150F، ياماها YBR 125، سوزوڪي GD 110، GS 150، GR 150 ۽ اڪثر مقامي 70cc ۽ 125cc بائيڪن (يونائيٽڊ، روڊ پرنس، يونيڪ ۽ ٻين) جا پارٽس آهن. توهان جي بائيڪ نه ڏسو ته ماڊل واٽس ايپ تي موڪليو.",
     "ہمارے پاس ہونڈا CD 70، CG 125، پرائیڈر، CB 150F، یاماہا YBR 125، سوزوکی GD 110، GS 150، GR 150 اور زیادہ تر مقامی 70cc اور 125cc بائیکس (یونائیٹڈ، روڈ پرنس، یونیک وغیرہ) کے پارٹس ہیں۔ اپنی بائیک نظر نہ آئے تو ماڈل واٹس ایپ پر بھیجیں۔",
     "We stock parts for Honda CD 70, CG 125, Pridor, CB 150F, Yamaha YBR 125, Suzuki GD 110, GS 150, GR 150 and most local 70cc and 125cc bikes (United, Road Prince, Unique and others). If you don't see your bike, send us the model on WhatsApp."),
    ("قيمت ڪيئن معلوم ٿيندي؟", "قیمت کیسے معلوم ہوگی؟", "How do I know the price?",
     "قيمتون اسٽاڪ ۽ سپلائر ريٽ مطابق بدلجن ٿيون، تنهنڪري آنلائن نه ٿا لکون. ڪنهن به پارٽ تي <strong>قيمت پڇو</strong> دٻايو، يا لسٽ واٽس ايپ تي موڪليو — اسين اڄ جي قيمت ٻڌائينداسين.",
     "قیمتیں اسٹاک اور سپلائر ریٹ کے ساتھ بدلتی ہیں، اس لیے ہم آن لائن نہیں لکھتے۔ کسی بھی پارٹ پر <strong>قیمت پوچھیں</strong> دبائیں، یا لسٹ واٹس ایپ پر بھیجیں — ہم آج کی قیمت بتائیں گے۔",
     "Prices change with stock and supplier rates, so we don't list them online. Tap <strong>Ask price</strong> on any part, or send your list on WhatsApp, and we'll reply with today's price."),
    ("ڇا توهان جا پارٽس اصلي آهن؟", "کیا آپ کے پارٹس اصلی ہیں؟", "Are your parts genuine?",
     "اسين اصلي (ڪمپني جا) پارٽس ۽ سٺي معيار جا متبادل پارٽس ٻئي وڪڻون ٿا. اسين هميشه ٻڌايون ٿا ته توهان ڪهڙو خريد ڪري رهيا آهيو ۽ ٻنهي جي قيمت ڪيتري آهي، ته جيئن توهان پاڻ چونڊيو.",
     "ہم اصلی (کمپنی کے) پارٹس اور اچھے معیار کے متبادل پارٹس دونوں بیچتے ہیں۔ ہم ہمیشہ بتاتے ہیں کہ آپ کون سا خرید رہے ہیں اور دونوں کی قیمت کیا ہے، تاکہ آپ خود انتخاب کریں۔",
     "We sell both original (genuine company) parts and good-quality replacement parts. We always tell you which one you're buying and the price of each, so you can choose."),
    ("ڇا توهان پارٽ لڳائي ڏيندا؟", "کیا آپ پارٹ لگا دیں گے؟", "Can you fit the part for me?",
     "ها. اسان جي ورڪشاپ اڪثر پارٽس ساڳئي وقت لڳائي سگهي ٿي. لڳائڻ جو خرچ ڪم مطابق الڳ آهي — پهرين قيمت پڇو.",
     "جی ہاں۔ ہماری ورکشاپ زیادہ تر پارٹس اسی وقت لگا سکتی ہے۔ لگانے کا خرچ کام کے مطابق الگ ہوتا ہے — پہلے قیمت پوچھ لیں۔",
     "Yes. Our workshop can fit most parts on the same visit. Fitting is charged separately depending on the job — ask us for the price first."),
    ("ڇا توهان ڊليوري ڪريو ٿا؟", "کیا آپ ڈیلیوری کرتے ہیں؟", "Do you deliver?",
     "ڪجهه آرڊرن لاءِ شهر اندر ڊليوري جو بندوبست ٿي سگهي ٿو. واٽس ايپ تي پڇو، اسين خرچ ۽ وقت ٻڌائينداسين. ڏسو اسان جي <a href=\"delivery-policy.html\">ڊليوري پاليسي</a>.",
     "کچھ آرڈرز کے لیے شہر کے اندر ڈیلیوری کا انتظام ہو سکتا ہے۔ واٹس ایپ پر پوچھیں، ہم خرچ اور وقت بتائیں گے۔ ہماری <a href=\"delivery-policy.html\">ڈیلیوری پالیسی</a> دیکھیں۔",
     "We may be able to arrange delivery within the city for some orders. Ask on WhatsApp and we'll confirm the cost and timing. See our <a href=\"delivery-policy.html\">delivery policy</a>."),
    ("ڇا پارٽ واپس ٿي سگهي ٿو؟", "کیا پارٹ واپس ہو سکتا ہے؟", "Can I return a part?",
     "اڻ استعمال ٿيل پارٽ، اصلي پيڪنگ ۾، جيڪڏهن توهان جي بائيڪ ۾ فٽ نه ٿئي ته عام طور تي بدلائي سگهجي ٿو. اليڪٽريڪل پارٽس ۽ لڳايل پارٽس واپس نه ٿيندا. پڙهو اسان جي <a href=\"returns-warranty.html\">واپسي ۽ وارنٽي پاليسي</a>.",
     "غیر استعمال شدہ پارٹ، اصل پیکنگ میں، اگر آپ کی بائیک میں فٹ نہ ہو تو عموماً تبدیل ہو سکتا ہے۔ الیکٹریکل پارٹس اور لگے ہوئے پارٹس واپس نہیں ہوں گے۔ ہماری <a href=\"returns-warranty.html\">واپسی اور وارنٹی پالیسی</a> پڑھیں۔",
     "Unused parts in their original packing can usually be exchanged if they don't fit your bike. Electrical parts and parts that have been fitted can't be returned. Read our <a href=\"returns-warranty.html\">returns &amp; warranty policy</a>."),
    ("ادائگي ڪيئن ڪريان؟", "ادائیگی کیسے کروں؟", "How do I pay?",
     "دڪان تي ادائگي ڪريو. ٻئي طريقي سان ادائگي ڪرڻ چاهيو ته واٽس ايپ تي پڇو.",
     "دکان پر ادائیگی کریں۔ کسی اور طریقے سے ادائیگی کرنا چاہیں تو واٹس ایپ پر پوچھیں۔",
     "Pay at the shop. Ask us on WhatsApp if you'd like to pay another way."),
    ("توهان جو وقت ڪهڙو آهي؟", "آپ کے اوقات کیا ہیں؟", "What are your opening hours?",
     "{hours}. جيڪڏهن ڪو خاص پارٽ گهرجي ته اچڻ کان اڳ ڪال ڪريو، ته جيئن اسين تيار رکون.",
     "{hours}۔ اگر کوئی خاص پارٹ چاہیے تو آنے سے پہلے کال کریں، تاکہ ہم تیار رکھیں۔",
     "{hours}. Call before you come if you need a specific part, so we can keep it ready."),
], 1):
    s(f"faq{n}_q", sd_q, ur_q, en_q)
    s(f"faq{n}_a", sd_a, ur_a, en_a)
    FAQ_KEYS.append(n)

s("tips_title", "موٽر سائيڪل جي سنڀال جا طريقا", "موٹر سائیکل کی دیکھ بھال کے طریقے", "Motorcycle Care Tips")
s("tips_desc", "موٽر سائيڪل جي سنڀال جا آسان طريقا: آئل، زنجير، ايئر فلٽر، بريڪون، ٽائر پريشر ۽ بيٽري — Al-Bais Motors جي مستري کان.",
  "موٹر سائیکل کی دیکھ بھال کے آسان طریقے: آئل، چین، ایئر فلٹر، بریکیں، ٹائر پریشر اور بیٹری — Al-Bais Motors کے مستریوں سے۔",
  "Simple motorcycle maintenance tips: oil changes, chain care, air filter, brakes, tyre pressure and battery — from the mechanics at Al-Bais Motors.")
s("tips_h1", "بائيڪ جي سنڀال", "بائیک کی دیکھ بھال", "Bike care tips")
s("tips_lead", "سادا عادتون جيڪي توهان جي موٽر سائيڪل کي ڊگهو هلائين ٿيون ۽ مرمت جو خرچ بچائين ٿيون.",
  "سادہ عادتیں جو آپ کی موٹر سائیکل کو زیادہ دیر چلاتی ہیں اور مرمت کا خرچ بچاتی ہیں۔",
  "Simple habits that keep your motorcycle running longer and save you money on repairs.")
for n, (sd_t, ur_t, en_t, sd_d, ur_d, en_d) in enumerate([
    ("وقت تي انجڻ آئل بدلايو", "وقت پر انجن آئل تبدیل کریں", "Change your engine oil on time",
     "پراڻو ۽ پتلو آئل انجڻ جي خرابي جو سڀ کان وڏو سبب آهي. پنهنجي بائيڪ جي مالڪ ڪتابچي مطابق آئل بدلايو — ۽ ٽريفڪ، مٽي يا گرمي ۾ هلائيندا هجو ته جلدي بدلايو. هر هفتي ڊپ اسٽڪ تي آئل جي سطح چيڪ ڪريو.",
     "پرانا اور پتلا آئل انجن کی خرابی کی سب سے بڑی وجہ ہے۔ اپنی بائیک کی اونر مینوئل کے مطابق آئل تبدیل کریں — اور ٹریفک، مٹی یا گرمی میں چلاتے ہوں تو جلدی تبدیل کریں۔ ہر ہفتے ڈپ اسٹک پر آئل کی سطح چیک کریں۔",
     "Old, thin oil is the number-one cause of engine wear. Follow the interval in your bike's owner manual — and change it sooner if you ride in heavy traffic, dust or heat. Check the level on the dipstick every week."),
    ("زنجير صاف، آئل ٿيل ۽ سيٽ رکو", "چین صاف، آئل شدہ اور ایڈجسٹ رکھیں", "Keep the chain clean, oiled and adjusted",
     "سڪل يا ڍري زنجير اسپراڪيٽ کي جلدي گهاري ٿي ۽ لهي به سگهي ٿي. ان کي باقاعدي صاف ۽ آئل ڪريو، خاص ڪري مينهن يا مٽي واري رستي کان پوءِ.",
     "خشک یا ڈھیلی چین اسپراکٹ کو جلدی گھسا دیتی ہے اور اتر بھی سکتی ہے۔ اسے باقاعدگی سے صاف اور آئل کریں، خاص طور پر بارش یا مٹی والی سڑکوں کے بعد۔",
     "A dry or loose chain wears out sprockets fast and can jump off. Clean and lubricate it regularly, especially after rain or dusty roads, and keep the slack as shown in your manual."),
    ("ايئر فلٽر صاف ڪريو", "ایئر فلٹر صاف کریں", "Clean the air filter",
     "مٽي ڀريل فلٽر انجڻ تي زور وجهي ٿو ۽ پيٽرول وڌيڪ کائي ٿو. مٽي واري موسم ۾ گهڻو چيڪ ڪريو ۽ گندو هجي ته صاف ڪريو يا بدلايو.",
     "گرد آلود فلٹر انجن پر زور ڈالتا ہے اور پیٹرول زیادہ کھاتا ہے۔ گرد والے موسم میں اکثر چیک کریں اور گندا ہو تو صاف کریں یا بدلیں۔",
     "A dusty filter makes the engine work harder and drink more petrol. Check it often in dusty weather and clean or replace it when it's dirty."),
    ("هر هفتي بريڪون چيڪ ڪريو", "ہر ہفتے بریکیں چیک کریں", "Check your brakes every week",
     "جيڪڏهن ليور يا پيڊل معمول کان وڌيڪ هيٺ وڃي، يا چيڀاٽ يا گهرڙ جو آواز اچي، ته شوز يا پيڊز چيڪ ڪرايو. بريڪن ۾ دير نه ڪريو.",
     "اگر لیور یا پیڈل معمول سے زیادہ نیچے جائے، یا چیخنے یا رگڑنے کی آواز آئے، تو شوز یا پیڈز چیک کروائیں۔ بریکوں میں تاخیر نہ کریں۔",
     "If the lever or pedal goes further than usual, or you hear squealing or grinding, have the shoes or pads checked. Brakes are not something to put off."),
    ("صحيح ٽائر پريشر تي هلايو", "درست ٹائر پریشر پر چلائیں", "Ride on the right tyre pressure",
     "گهٽ هوا ٽائر جلدي گهاري ٿي، ايوريج گهٽائي ٿي ۽ اسٽيئرنگ ڳرو ڪري ٿي. ٿڌي ٽائر تي پريشر چيڪ ڪريو، ۽ ڪٽ، ڦاٽ ۽ گهريل ٽريڊ ڏسو.",
     "کم ہوا ٹائر جلدی گھساتی ہے، اوسط کم کرتی ہے اور اسٹیئرنگ بھاری کرتی ہے۔ ٹھنڈے ٹائر پر پریشر چیک کریں، اور کٹ، دراڑیں اور گھسا ہوا ٹریڈ دیکھیں۔",
     "Low pressure wears tyres quickly, hurts mileage and makes steering heavy. Check pressure when tyres are cold, and look for cuts, cracks and worn tread."),
    ("بيٽري ۽ لائٽن جو خيال رکو", "بیٹری اور لائٹس کا خیال رکھیں", "Look after the battery and lights",
     "مدهم لائٽ يا ڪمزور هارن جو مطلب عام طور تي ڪمزور بيٽري يا ڍرو ڪنيڪشن آهي. ٽرمينل صاف ۽ ٽائيٽ رکو، ۽ رات جو هلائڻ کان اڳ سڀ لائٽون چيڪ ڪريو.",
     "مدھم لائٹس یا کمزور ہارن کا مطلب عموماً کمزور بیٹری یا ڈھیلا کنکشن ہوتا ہے۔ ٹرمینل صاف اور ٹائٹ رکھیں، اور رات کو چلانے سے پہلے تمام لائٹس چیک کریں۔",
     "Dim lights or a weak horn usually mean a weak battery or loose connection. Keep terminals clean and tight, and check all lights before riding at night."),
    ("پنهنجي بائيڪ جي ٻڌو", "اپنی بائیک کی سنیں", "Listen to your bike",
     "نئون آواز، دونهون، ڪمزور پڪ اپ يا مشڪل سان اسٽارٽ ٿيڻ شروعاتي خبرداري آهن. هاڻي ننڍو چيڪ اڪثر بعد جي وڏي مرمت کان سستو پوي ٿو.",
     "نئی آواز، دھواں، کمزور پک اپ یا مشکل سے اسٹارٹ ہونا ابتدائی تنبیہ ہیں۔ ابھی ایک چھوٹا سا چیک اکثر بعد کی بڑی مرمت سے سستا پڑتا ہے۔",
     "New noises, smoke, poor pickup or hard starting are early warnings. A quick check now is almost always cheaper than a big repair later."),
], 1):
    s(f"tip{n}_t", sd_t, ur_t, en_t)
    s(f"tip{n}_d", sd_d, ur_d, en_d)
s("tips_note", "هميشه پنهنجي موٽر سائيڪل جي مالڪ ڪتابچي مطابق سروس جو وقت ۽ هدايتون مڃيو. هي عام صلاحون آهن.",
  "ہمیشہ اپنی موٹر سائیکل کی اونر مینوئل کے مطابق سروس کے وقفے اور ہدایات پر عمل کریں۔ یہ عمومی مشورے ہیں۔",
  "Always follow your motorcycle's owner manual for service intervals and specifications. These tips are general advice.")
s("due_service", "سروس جو وقت آهي؟", "سروس کا وقت ہے؟", "Due for a service?")
s("due_service_t", "ٽيون اپ بُڪ ڪريو، اسين هن لسٽ جي هر شيءِ چيڪ ڪنداسين.", "ٹیون اپ بک کریں، ہم اس فہرست کی ہر چیز چیک کریں گے۔",
  "Book a tune-up and we'll check everything on this list.")
s("ask_mechanic", "مستري کان پڇو", "مستری سے پوچھیں", "Ask a mechanic")

s("feedback_title", "توهان جي راءِ", "آپ کی رائے", "Your Feedback")
s("feedback_desc", "Al-Bais Motors کي ٻڌايو ته اسان جو ڪم ڪيئن هو. توهان جي راءِ اسان کي {city} جي سوارن جي بهتر خدمت ۾ مدد ڪري ٿي.",
  "Al-Bais Motors کو بتائیں کہ ہمارا کام کیسا رہا۔ آپ کی رائے ہمیں {city} کے سواروں کی بہتر خدمت میں مدد دیتی ہے۔",
  "Tell Al-Bais Motors how we did. Your feedback helps us serve riders in {city} better.")
s("feedback_h1", "اسان جو ڪم ڪيئن هو؟", "ہمارا کام کیسا رہا؟", "How did we do?")
s("feedback_lead", "توهان جي راءِ سڌي مالڪ تائين پهچي ٿي. خوش آهيو؟ گوگل ريويو ٻين سوارن کي اسان کي ڳولڻ ۾ مدد ڪري ٿو.",
  "آپ کی رائے براہِ راست مالک تک پہنچتی ہے۔ خوش ہیں؟ گوگل ریویو دوسرے سواروں کو ہمیں تلاش کرنے میں مدد دیتا ہے۔",
  "Your feedback goes straight to the owner. Happy with us? A Google review helps other riders find us.")
s("loved_it", "سروس پسند آئي؟", "سروس پسند آئی؟", "Loved the service?")
s("loved_it_t", "مهرباني ڪري گوگل تي ريويو ڏيو — هڪ منٽ لڳندو ۽ مقامي ڪاروبار جي وڏي مدد ٿيندي.",
  "براہ کرم گوگل پر ریویو دیں — ایک منٹ لگے گا اور مقامی کاروبار کی بڑی مدد ہوگی۔",
  "Please leave a review on Google — it takes a minute and really helps a local business.")
s("private_fb_h", "ذاتي راءِ", "نجی رائے", "Private feedback")
s("rating", "توهان جي ريٽنگ", "آپ کی ریٹنگ", "Your rating")
s("stars", "اسٽار", "اسٹار", "stars")
s("fb_phone", "فون (جيڪڏهن جواب گهرجي)", "فون (اگر جواب چاہیے)", "Phone (if you'd like a reply)")
s("fb_text", "توهان جي راءِ", "آپ کی رائے", "Your feedback")
s("send_feedback", "راءِ موڪليو", "رائے بھیجیں", "Send feedback")

# ---------------------------------------------------------------------------
# Thank you & 404
# ---------------------------------------------------------------------------
s("thanks_title", "مهرباني", "شکریہ", "Thank You")
s("thanks_desc", "اسان کي توهان جو پيغام ملي ويو آهي.", "ہمیں آپ کا پیغام موصول ہو گیا ہے۔", "We've received your message.")
s("thanks_h1", "توهان جي مهرباني!", "آپ کا شکریہ!", "Thank you!")
s("thanks_lead", "اسان کي توهان جو پيغام ملي ويو آهي. اسين فون يا واٽس ايپ تي جواب ڏينداسين، اڪثر ساڳئي ڏينهن.",
  "ہمیں آپ کا پیغام موصول ہو گیا ہے۔ ہم فون یا واٹس ایپ پر جواب دیں گے، عموماً اسی دن۔",
  "We've received your message and will reply by phone or WhatsApp, usually the same day.")
s("thanks_more", "جلدي گهرجي؟ واٽس ايپ ڪريو — ۽ جيڪڏهن پارٽ جي تصوير آهي ته موڪليو.",
  "جلدی چاہیے؟ واٹس ایپ کریں — اور اگر پارٹ کی تصویر ہے تو بھیجیں۔",
  "Need it faster? Send us a WhatsApp — and attach a photo of the part if you have one.")
s("keep_browsing", "وڌيڪ پارٽس ڏسو", "مزید پارٹس دیکھیں", "Keep browsing parts")
s("nf_title", "صفحو نه مليو", "صفحہ نہیں ملا", "Page Not Found")
s("nf_desc", "هي صفحو موجود ناهي.", "یہ صفحہ موجود نہیں۔", "This page doesn't exist.")
s("nf_h1", "هي صفحو غلط رستي تي هليو ويو", "یہ صفحہ غلط راستے پر چلا گیا", "This page took a wrong turn")
s("nf_lead", "جيڪو صفحو توهان ڳولي رهيا آهيو اهو هتي ناهي. هي ڪوشش ڪريو:", "جو صفحہ آپ تلاش کر رہے ہیں وہ یہاں نہیں۔ یہ آزمائیں:",
  "The page you're looking for isn't here. Try one of these instead:")

# ---------------------------------------------------------------------------
# Strings used by the website script (main.js)
# ---------------------------------------------------------------------------
JS_KEYS = {}


def js(key, sd, ur, en):
    JS_KEYS[key] = {"sd": sd, "ur": ur, "en": en}


js("askPrice", "قيمت پڇو", "قیمت پوچھیں", "Ask price")
js("addToList", "لسٽ ۾ شامل ڪريو", "لسٹ میں شامل کریں", "Add to list")
js("added", "شامل ٿي ويو", "شامل ہو گیا", "Added")
js("addMore", "وڌيڪ شامل ڪريو", "مزید شامل کریں", "Add more")
js("fits", "فٽ ٿئي:", "فٹ ہوتا ہے:", "Fits:")
js("allBikes", "سڀ بائيڪون", "تمام بائیکس", "All bikes")
js("allParts", "سڀ پارٽس", "تمام پارٹس", "All parts")
js("allCategories", "سڀ قسم", "تمام اقسام", "All categories")
js("noResultsTitle", "هتي اسان جا عام پارٽس لکيل آهن — اسان وٽ گهڻا وڌيڪ آهن.",
   "یہاں ہمارے عام پارٹس درج ہیں — ہمارے پاس اور بھی بہت ہیں۔",
   "We list our most common parts here — we stock many more.")
js("noResultsText", "پنهنجي بائيڪ جو ماڊل ۽ گهربل پارٽ موڪليو، اسين قيمت ۽ اسٽاڪ ٻڌائينداسين.",
   "اپنی بائیک کا ماڈل اور مطلوبہ پارٹ بھیجیں، ہم قیمت اور اسٹاک بتائیں گے۔",
   "Send us your bike model and the part you need, and we'll confirm price and stock.")
js("askOnWa", "واٽس ايپ تي پڇو", "واٹس ایپ پر پوچھیں", "Ask on WhatsApp")
js("msgLookingFor", "السلام عليڪم Al-Bais Motors، مون کي هي گهرجي: ", "السلام علیکم Al-Bais Motors، مجھے یہ چاہیے: ",
   "Hi Al-Bais Motors, I am looking for: ")
js("msgPrice", "السلام عليڪم Al-Bais Motors، مهرباني ڪري هن جي قيمت ۽ اسٽاڪ ٻڌايو: ",
   "السلام علیکم Al-Bais Motors، براہ کرم اس کی قیمت اور اسٹاک بتائیں: ",
   "Hi Al-Bais Motors, please tell me the price and availability of: ")
js("msgMyBike", "منهنجي بائيڪ: ", "میری بائیک: ", "My bike: ")
js("msgListIntro", "السلام عليڪم Al-Bais Motors، مهرباني ڪري هنن جي قيمت ۽ اسٽاڪ ٻڌايو:",
   "السلام علیکم Al-Bais Motors، براہ کرم ان کی قیمت اور اسٹاک بتائیں:",
   "Hi Al-Bais Motors, please send prices and availability for:")
js("myPartsList", "(منهنجي پارٽس لسٽ)", "(میری پارٹس لسٹ)", "(my parts list)")
js("emptyList", "توهان جي لسٽ خالي آهي. <a href=\"products.html\">پارٽس ڏسو</a> ۽ <strong>لسٽ ۾ شامل ڪريو</strong> دٻايو.",
   "آپ کی لسٹ خالی ہے۔ <a href=\"products.html\">پارٹس دیکھیں</a> اور <strong>لسٹ میں شامل کریں</strong> دبائیں۔",
   "Your list is empty. <a href=\"products.html\">Browse parts</a> and tap <strong>Add to list</strong>.")
js("fewer", "گهٽ", "کم", "Fewer")
js("more", "وڌيڪ", "زیادہ", "More")
js("remove", "هٽايو", "ہٹائیں", "Remove")
js("sending", "موڪلي رهيا آهيون…", "بھیجا جا رہا ہے…", "Sending…")
js("sendError", "معاف ڪجو، توهان جو پيغام هن وقت نه وڃي سگهيو.", "معذرت، آپ کا پیغام اس وقت نہیں بھیجا جا سکا۔",
   "Sorry, your message could not be sent right now.")
js("sendOnWa", "ان جي بدران واٽس ايپ تي موڪليو", "اس کے بجائے واٹس ایپ پر بھیجیں", "Send it on WhatsApp instead")
js("orCall", "يا ڪال ڪريو", "یا کال کریں", "or call")
js("linkCopied", "لنڪ ڪاپي ٿي وئي", "لنک کاپی ہو گیا", "Link copied")
js("websiteEnquiry", "ويب سائيٽ تان پڇا", "ویب سائٹ سے انکوائری", "Website enquiry")
js("menu", "مينيو", "مینو", "Menu")
