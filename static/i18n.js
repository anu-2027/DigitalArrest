/**
 * DigitalArmour — i18n (English · हिंदी · ಕನ್ನಡ · தமிழ் · తెలుగు)
 * Usage: add data-i18n="key" to any element whose textContent should be translated.
 *        For placeholders: data-i18n-ph="key"
 * The active language is stored in localStorage under 'da_lang'.
 */
const DA_TRANSLATIONS = {
  en: {
    /* ── HEADER ── */
    'nav.helpline':        '📞 1930',
    'nav.lang-toggle':     'हिं',

    /* ── INDEX — HERO ── */
    'hero.eyebrow':        '🇮🇳 India Cybercrime Prevention',
    'hero.title-line1':    'Got a suspicious call?',
    'hero.title-line2':    "Report it. We'll detect it.",
    'hero.subtitle':       "Fill in what happened on the call — who called, what they claimed, what they wanted. Our engine analyses it and tells you if it's a scam.",

    /* ── INDEX — SCANNER CARD ── */
    'scan.card-title':     'Paste Message or Describe the Call',
    'scan.field-hint':     'Paste the exact SMS / WhatsApp message you received, or type what the caller said in your own words.',
    'scan.placeholder':    "e.g. 'Dear Customer, your SBI KYC has expired…'\n\nOr: 'A person called claiming to be an ED officer…'",
    'scan.btn':            '🔍 Scan Now',
    'scan.bar':            'Analysing your report across 5 scam categories…',

    /* ── INDEX — DEMO ── */
    'demo.title':          '🧪 Demo Test Cases',

    /* ── INDEX — HISTORY ── */
    'hist.title':          '🕓 Your Previous Scans',
    'hist.clear':          'Clear',
    'hist.empty':          'No scans yet — your results will appear here.',

    /* ── INDEX — ANALYTICS ── */
    'analytics.title':     '📊 Live Analytics',
    'analytics.badge':     'TODAY',
    'kpi.detected':        'Scams Detected',
    'kpi.money':           'Money Protected',
    'kpi.users':           'Users Warned',
    'kpi.top':             'Most: Digital Arrest',
    'bd.title':            'Scam Type Breakdown',
    'lf.title':            'Recent Detections',

    /* ── INDEX — HELPLINE CARD ── */
    'hl.title':            '🆘 Need Help Now?',
    'hl.call-main':        'Call 1930',
    'hl.call-sub':         'Cyber Crime Helpline · Free · 24×7',
    'hl.web-main':         'Report at cybercrime.gov.in',
    'hl.web-sub':          'Official National Cyber Crime Portal',
    'hl.cert-main':        'CERT-In Portal',
    'hl.cert-sub':         'cert-in.org.in · Cyber Security Incidents',
    'hl.note':             'Free official government services. Never pay anyone claiming to be from a helpline.',

    /* ── INDEX — FOOTER ── */
    'footer.text':         'Built for Hackathon 2025 · Helpline:',

    /* ── SCAM DETAIL — HEADER ── */
    'detail.back':         '← Back to Scanner',
    'detail.breadcrumb1':  'DigitalArmour',
    'detail.breadcrumb2':  'Scam Guide',

    /* ── SCAM DETAIL — FACTS ── */
    'detail.fact-threat':  'Threat Level',
    'detail.fact-kw':      'Detection Keywords',
    'detail.fact-steps':   'Protective Steps',
    'detail.fact-phrases': 'phrases',
    'detail.fact-actions': 'actions',

    /* ── SCAM DETAIL — CTA ── */
    'detail.cta-strong':   'Got a suspicious message related to this?',
    'detail.cta-span':     'Paste it in the scanner — our engine analyses it in seconds.',
    'detail.cta-btn':      '🔍 Scan a Message',

    /* ── SCAM DETAIL — SECTIONS ── */
    'detail.kw-lbl':       'Warning Signals',
    'detail.kw-ttl':       'Trigger Phrases & Threat Weights',
    'detail.kw-hint':      'Each phrase is weighted <strong>1–10</strong> based on how exclusively it appears in scam messages. Weight 10 = almost never used in legitimate communication.',
    'detail.eg-lbl':       'Real Scam Example',
    'detail.eg-msg-lbl':   'Typical scam message',
    'detail.eg-warn':      '⚠ This is an example for awareness only — do not respond to messages like this.',
    'detail.act-lbl':      'Immediate Actions',
    'detail.act-ttl':      'What You Must Do Right Now',
    'detail.rpt-lbl':      'Official Government Channels',
    'detail.rpt-ttl':      "Report This Scam — It's Free",
    'detail.hl-call-main': 'Call 1930',
    'detail.hl-call-sub':  'National Cyber Crime Helpline · Free · 24×7',
    'detail.hl-web-main':  'cybercrime.gov.in',
    'detail.hl-web-sub':   'Official National Cyber Crime Reporting Portal',
    'detail.hl-cert-main': 'CERT-In Portal',
    'detail.hl-cert-sub':  'cert-in.org.in · Cyber Security Incident Response',
    'detail.hl-note':      'All services are free and operated by the Government of India. Never pay anyone claiming to be from a helpline.',
    'detail.sev-suffix':   'SEVERITY',
    'detail.country-tag':  'India Cyber Crime — Active Scam Type',

    /* ── SHARED FOOTER ── */
    'footer.back':         '← Back to DigitalArmour Scanner',
    'footer.helpline':     'Helpline:',
  },

  hi: {
    /* ── HEADER ── */
    'nav.helpline':        '📞 1930',

    /* ── INDEX — HERO ── */
    'hero.eyebrow':        '🇮🇳 भारत साइबर अपराध रोकथाम',
    'hero.title-line1':    'संदिग्ध कॉल आई?',
    'hero.title-line2':    'रिपोर्ट करें। हम पहचानेंगे।',
    'hero.subtitle':       'कॉल में क्या हुआ — किसने फोन किया, क्या कहा, क्या माँगा — सब लिखें। हमारा इंजन विश्लेषण करके बताएगा कि यह धोखाधड़ी है या नहीं।',

    /* ── INDEX — SCANNER CARD ── */
    'scan.card-title':     'संदेश पेस्ट करें या कॉल का विवरण लिखें',
    'scan.field-hint':     'प्राप्त SMS / WhatsApp संदेश सीधे पेस्ट करें, या जो कॉलर ने कहा वो अपने शब्दों में लिखें।',
    'scan.placeholder':    "उदा. 'प्रिय ग्राहक, आपका SBI KYC समाप्त हो गया है…'\n\नया: 'एक व्यक्ति ने ED अधिकारी बनकर फोन किया…'",
    'scan.btn':            '🔍 अभी स्कैन करें',
    'scan.bar':            '5 श्रेणियों में आपकी रिपोर्ट का विश्लेषण हो रहा है…',

    /* ── INDEX — DEMO ── */
    'demo.title':          '🧪 डेमो टेस्ट केस',

    /* ── INDEX — HISTORY ── */
    'hist.title':          '🕓 आपके पिछले स्कैन',
    'hist.clear':          'मिटाएं',
    'hist.empty':          'अभी कोई स्कैन नहीं — परिणाम यहाँ दिखेंगे।',

    /* ── INDEX — ANALYTICS ── */
    'analytics.title':     '📊 लाइव आँकड़े',
    'analytics.badge':     'आज',
    'kpi.detected':        'धोखाधड़ी पकड़ी गई',
    'kpi.money':           'धन सुरक्षित',
    'kpi.users':           'उपयोगकर्ता सतर्क',
    'kpi.top':             'सबसे अधिक: डिजिटल गिरफ्तारी',
    'bd.title':            'धोखाधड़ी प्रकार विवरण',
    'lf.title':            'हालिया पहचान',

    /* ── INDEX — HELPLINE CARD ── */
    'hl.title':            '🆘 अभी मदद चाहिए?',
    'hl.call-main':        '1930 पर कॉल करें',
    'hl.call-sub':         'साइबर क्राइम हेल्पलाइन · निःशुल्क · 24×7',
    'hl.web-main':         'cybercrime.gov.in पर रिपोर्ट करें',
    'hl.web-sub':          'राष्ट्रीय साइबर क्राइम रिपोर्टिंग पोर्टल',
    'hl.cert-main':        'CERT-In पोर्टल',
    'hl.cert-sub':         'cert-in.org.in · साइबर सुरक्षा घटनाएं',
    'hl.note':             'सभी सेवाएं निःशुल्क और सरकारी हैं। कोई भी हेल्पलाइन के नाम पर पैसे माँगे तो न दें।',

    /* ── INDEX — FOOTER ── */
    'footer.text':         'Hackathon 2025 के लिए निर्मित · हेल्पलाइन:',

    /* ── SCAM DETAIL — HEADER ── */
    'detail.back':         '← स्कैनर पर वापस जाएं',
    'detail.breadcrumb1':  'DigitalArmour',
    'detail.breadcrumb2':  'धोखाधड़ी मार्गदर्शिका',

    /* ── SCAM DETAIL — FACTS ── */
    'detail.fact-threat':  'खतरे का स्तर',
    'detail.fact-kw':      'पहचान कीवर्ड',
    'detail.fact-steps':   'सुरक्षात्मक कदम',
    'detail.fact-phrases': 'वाक्यांश',
    'detail.fact-actions': 'कार्य',

    /* ── SCAM DETAIL — CTA ── */
    'detail.cta-strong':   'इससे संबंधित कोई संदिग्ध संदेश मिला?',
    'detail.cta-span':     'स्कैनर में पेस्ट करें — हमारा इंजन कुछ ही सेकंड में जाँच करेगा।',
    'detail.cta-btn':      '🔍 संदेश स्कैन करें',

    /* ── SCAM DETAIL — SECTIONS ── */
    'detail.kw-lbl':       'चेतावनी संकेत',
    'detail.kw-ttl':       'ट्रिगर वाक्यांश और खतरे का भार',
    'detail.kw-hint':      'प्रत्येक वाक्यांश को <strong>1–10</strong> भार दिया गया है। भार 10 = वैध संचार में लगभग कभी उपयोग नहीं होता।',
    'detail.eg-lbl':       'असली धोखाधड़ी का उदाहरण',
    'detail.eg-msg-lbl':   'सामान्य धोखाधड़ी संदेश',
    'detail.eg-warn':      '⚠ यह केवल जागरूकता के लिए है — ऐसे संदेशों का जवाब न दें।',
    'detail.act-lbl':      'तत्काल कार्रवाई',
    'detail.act-ttl':      'अभी यह करें',
    'detail.rpt-lbl':      'आधिकारिक सरकारी चैनल',
    'detail.rpt-ttl':      'यह धोखाधड़ी रिपोर्ट करें — निःशुल्क',
    'detail.hl-call-main': '1930 पर कॉल करें',
    'detail.hl-call-sub':  'राष्ट्रीय साइबर क्राइम हेल्पलाइन · निःशुल्क · 24×7',
    'detail.hl-web-main':  'cybercrime.gov.in',
    'detail.hl-web-sub':   'राष्ट्रीय साइबर क्राइम रिपोर्टिंग पोर्टल',
    'detail.hl-cert-main': 'CERT-In पोर्टल',
    'detail.hl-cert-sub':  'cert-in.org.in · साइबर सुरक्षा घटना प्रतिक्रिया',
    'detail.hl-note':      'सभी सेवाएं भारत सरकार द्वारा निःशुल्क संचालित हैं। हेल्पलाइन के नाम पर कोई भी पैसे माँगे तो न दें।',
    'detail.sev-suffix':   'गंभीरता',
    'detail.country-tag':  'भारत साइबर क्राइम — सक्रिय धोखाधड़ी प्रकार',

    /* ── SHARED FOOTER ── */
    'footer.back':         '← DigitalArmour स्कैनर पर वापस',
    'footer.helpline':     'हेल्पलाइन:',
  },

  /* ════════════════════════════════════════════
     KANNADA
  ════════════════════════════════════════════ */
  kn: {
    'nav.helpline':        '📞 1930',
    'hero.eyebrow':        '🇮🇳 ಭಾರತ ಸೈಬರ್ ಅಪರಾಧ ತಡೆಗಟ್ಟುವಿಕೆ',
    'hero.title-line1':    'ಅನುಮಾನಾಸ್ಪದ ಕರೆ ಬಂತೇ?',
    'hero.title-line2':    'ವರದಿ ಮಾಡಿ. ನಾವು ಪತ್ತೆ ಮಾಡುತ್ತೇವೆ.',
    'hero.subtitle':       'ಕರೆಯಲ್ಲಿ ಏನಾಯಿತು — ಯಾರು ಕರೆದರು, ಏನು ಹೇಳಿದರು, ಏನು ಕೇಳಿದರು ಎಂದು ಬರೆಯಿರಿ. ನಮ್ಮ ಎಂಜಿನ್ ವಿಶ್ಲೇಷಿಸಿ ಮೋಸ ಎಂದು ತಿಳಿಸುತ್ತದೆ.',
    'scan.card-title':     'ಸಂದೇಶ ಅಂಟಿಸಿ ಅಥವಾ ಕರೆ ವಿವರಿಸಿ',
    'scan.field-hint':     'ನೀವು ಸ್ವೀಕರಿಸಿದ SMS / WhatsApp ಸಂದೇಶ ಅಂಟಿಸಿ, ಅಥವಾ ಕರೆ ಮಾಡಿದವರು ಹೇಳಿದ್ದನ್ನು ಬರೆಯಿರಿ.',
    'scan.placeholder':    "ಉದಾ. 'ಪ್ರಿಯ ಗ್ರಾಹಕ, ನಿಮ್ಮ SBI KYC ಅವಧಿ ಮೀರಿದೆ…'\n\nಅಥವಾ: 'ಒಬ್ಬ ವ್ಯಕ್ತಿ ED ಅಧಿಕಾರಿ ಎಂದು ಹೇಳಿ ಕರೆ ಮಾಡಿದ…'",
    'scan.btn':            '🔍 ಈಗ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ',
    'scan.bar':            '5 ವರ್ಗಗಳಲ್ಲಿ ನಿಮ್ಮ ವರದಿ ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ…',
    'demo.title':          '🧪 ಡೆಮೊ ಪರೀಕ್ಷಾ ಪ್ರಕರಣಗಳು',
    'hist.title':          '🕓 ನಿಮ್ಮ ಹಿಂದಿನ ಸ್ಕ್ಯಾನ್‌ಗಳು',
    'hist.clear':          'ತೆರವುಗೊಳಿಸಿ',
    'hist.empty':          'ಇನ್ನೂ ಯಾವುದೇ ಸ್ಕ್ಯಾನ್ ಇಲ್ಲ — ಫಲಿತಾಂಶಗಳು ಇಲ್ಲಿ ಕಾಣಿಸುತ್ತವೆ.',
    'analytics.title':     '📊 ನೇರ ಅಂಕಿಅಂಶಗಳು',
    'analytics.badge':     'ಇಂದು',
    'kpi.detected':        'ಮೋಸ ಪತ್ತೆ',
    'kpi.money':           'ಹಣ ರಕ್ಷಣೆ',
    'kpi.users':           'ಬಳಕೆದಾರರಿಗೆ ಎಚ್ಚರಿಕೆ',
    'kpi.top':             'ಹೆಚ್ಚು: ಡಿಜಿಟಲ್ ಬಂಧನ',
    'bd.title':            'ಮೋಸ ಪ್ರಕಾರ ವಿಭಾಗ',
    'lf.title':            'ಇತ್ತೀಚಿನ ಪತ್ತೆಗಳು',
    'hl.title':            '🆘 ಈಗ ಸಹಾಯ ಬೇಕೇ?',
    'hl.call-main':        '1930 ಕರೆ ಮಾಡಿ',
    'hl.call-sub':         'ಸೈಬರ್ ಅಪರಾಧ ಸಹಾಯವಾಣಿ · ಉಚಿತ · 24×7',
    'hl.web-main':         'cybercrime.gov.in ನಲ್ಲಿ ವರದಿ ಮಾಡಿ',
    'hl.web-sub':          'ಅಧಿಕೃತ ರಾಷ್ಟ್ರೀಯ ಸೈಬರ್ ಅಪರಾಧ ಪೋರ್ಟಲ್',
    'hl.cert-main':        'CERT-In ಪೋರ್ಟಲ್',
    'hl.cert-sub':         'cert-in.org.in · ಸೈಬರ್ ಭದ್ರತಾ ಘಟನೆಗಳು',
    'hl.note':             'ಎಲ್ಲಾ ಸೇವೆಗಳು ಉಚಿತ ಮತ್ತು ಸರ್ಕಾರಿ. ಸಹಾಯವಾಣಿ ಹೆಸರಿನಲ್ಲಿ ಹಣ ಕೇಳಿದರೆ ನೀಡಬೇಡಿ.',
    'footer.text':         'Hackathon 2025 ಗಾಗಿ ನಿರ್ಮಿಸಲಾಗಿದೆ · ಸಹಾಯವಾಣಿ:',
    'detail.back':         '← ಸ್ಕ್ಯಾನರ್‌ಗೆ ಹಿಂತಿರುಗಿ',
    'detail.breadcrumb1':  'DigitalArmour',
    'detail.breadcrumb2':  'ಮೋಸ ಮಾರ್ಗದರ್ಶಿ',
    'detail.fact-threat':  'ಅಪಾಯದ ಮಟ್ಟ',
    'detail.fact-kw':      'ಪತ್ತೆ ಕೀವರ್ಡ್‌ಗಳು',
    'detail.fact-steps':   'ರಕ್ಷಣಾ ಕ್ರಮಗಳು',
    'detail.fact-phrases': 'ಪದಗುಚ್ಛಗಳು',
    'detail.fact-actions': 'ಕ್ರಮಗಳು',
    'detail.cta-strong':   'ಇದಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಅನುಮಾನಾಸ್ಪದ ಸಂದೇಶ ಬಂದಿದೆಯೇ?',
    'detail.cta-span':     'ಸ್ಕ್ಯಾನರ್‌ನಲ್ಲಿ ಅಂಟಿಸಿ — ನಮ್ಮ ಎಂಜಿನ್ ಕ್ಷಣಗಳಲ್ಲಿ ಪರಿಶೀಲಿಸುತ್ತದೆ.',
    'detail.cta-btn':      '🔍 ಸಂದೇಶ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ',
    'detail.kw-lbl':       'ಎಚ್ಚರಿಕೆ ಸಂಕೇತಗಳು',
    'detail.kw-ttl':       'ಟ್ರಿಗರ್ ಪದಗುಚ್ಛಗಳು & ಅಪಾಯ ತೂಕ',
    'detail.kw-hint':      'ಪ್ರತಿ ಪದಗುಚ್ಛಕ್ಕೆ <strong>1–10</strong> ತೂಕ ನೀಡಲಾಗಿದೆ. ತೂಕ 10 = ವೈಧ ಸಂದೇಶದಲ್ಲಿ ಬಹುತೇಕ ಕಾಣಿಸುವುದಿಲ್ಲ.',
    'detail.eg-lbl':       'ನೈಜ ಮೋಸದ ಉದಾಹರಣೆ',
    'detail.eg-msg-lbl':   'ವಿಶಿಷ್ಟ ಮೋಸ ಸಂದೇಶ',
    'detail.eg-warn':      '⚠ ಇದು ಜಾಗೃತಿಗಾಗಿ ಮಾತ್ರ — ಇಂತಹ ಸಂದೇಶಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯಿಸಬೇಡಿ.',
    'detail.act-lbl':      'ತಕ್ಷಣದ ಕ್ರಮಗಳು',
    'detail.act-ttl':      'ಈಗ ಇದನ್ನು ಮಾಡಿ',
    'detail.rpt-lbl':      'ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಚಾನಲ್‌ಗಳು',
    'detail.rpt-ttl':      'ಈ ಮೋಸ ವರದಿ ಮಾಡಿ — ಉಚಿತ',
    'detail.hl-call-main': '1930 ಕರೆ ಮಾಡಿ',
    'detail.hl-call-sub':  'ರಾಷ್ಟ್ರೀಯ ಸೈಬರ್ ಅಪರಾಧ ಸಹಾಯವಾಣಿ · ಉಚಿತ · 24×7',
    'detail.hl-web-main':  'cybercrime.gov.in',
    'detail.hl-web-sub':   'ರಾಷ್ಟ್ರೀಯ ಸೈಬರ್ ಅಪರಾಧ ವರದಿ ಪೋರ್ಟಲ್',
    'detail.hl-cert-main': 'CERT-In ಪೋರ್ಟಲ್',
    'detail.hl-cert-sub':  'cert-in.org.in · ಸೈಬರ್ ಭದ್ರತಾ ಘಟನೆ ಪ್ರತಿಕ್ರಿಯೆ',
    'detail.hl-note':      'ಎಲ್ಲಾ ಸೇವೆಗಳು ಭಾರತ ಸರ್ಕಾರದಿಂದ ಉಚಿತವಾಗಿ ನಡೆಸಲ್ಪಡುತ್ತವೆ.',
    'detail.sev-suffix':   'ತೀವ್ರತೆ',
    'detail.country-tag':  'ಭಾರತ ಸೈಬರ್ ಅಪರಾಧ — ಸಕ್ರಿಯ ಮೋಸ ಪ್ರಕಾರ',
    'footer.back':         '← DigitalArmour ಸ್ಕ್ಯಾನರ್‌ಗೆ ಹಿಂತಿರುಗಿ',
    'footer.helpline':     'ಸಹಾಯವಾಣಿ:',
  },

  /* ════════════════════════════════════════════
     TAMIL
  ════════════════════════════════════════════ */
  ta: {
    'nav.helpline':        '📞 1930',
    'hero.eyebrow':        '🇮🇳 இந்தியா இணையவழி குற்ற தடுப்பு',
    'hero.title-line1':    'சந்தேகமான அழைப்பு வந்ததா?',
    'hero.title-line2':    'புகாரளியுங்கள். நாங்கள் கண்டறிவோம்.',
    'hero.subtitle':       'அழைப்பில் என்ன நடந்தது — யார் அழைத்தார்கள், என்ன சொன்னார்கள், என்ன கேட்டார்கள் என எழுதுங்கள். நம் இயந்திரம் பகுப்பாய்வு செய்து மோசடி என்று தெரிவிக்கும்.',
    'scan.card-title':     'செய்தியை ஒட்டவும் அல்லது அழைப்பை விவரிக்கவும்',
    'scan.field-hint':     'பெற்ற SMS / WhatsApp செய்தியை நேரடியாக ஒட்டவும், அல்லது அழைப்பாளர் சொன்னதை உங்கள் வார்த்தைகளில் எழுதவும்.',
    'scan.placeholder':    "எ.கா. 'அன்புள்ள வாடிக்கையாளர், உங்கள் SBI KYC காலாவதியாகிவிட்டது…'\n\nஅல்லது: 'ஒருவர் ED அதிகாரி என்று சொல்லி அழைத்தார்…'",
    'scan.btn':            '🔍 இப்போது ஸ்கேன் செய்',
    'scan.bar':            '5 வகைகளில் உங்கள் அறிக்கை பகுப்பாய்வு செய்யப்படுகிறது…',
    'demo.title':          '🧪 டெமோ சோதனை வழக்குகள்',
    'hist.title':          '🕓 உங்கள் முந்தைய ஸ்கேன்கள்',
    'hist.clear':          'அழி',
    'hist.empty':          'இன்னும் ஸ்கேன் இல்லை — முடிவுகள் இங்கே தோன்றும்.',
    'analytics.title':     '📊 நேரடி புள்ளிவிவரங்கள்',
    'analytics.badge':     'இன்று',
    'kpi.detected':        'மோசடிகள் கண்டறியப்பட்டவை',
    'kpi.money':           'பணம் பாதுகாக்கப்பட்டது',
    'kpi.users':           'பயனர்கள் எச்சரிக்கப்பட்டனர்',
    'kpi.top':             'அதிகம்: டிஜிட்டல் கைது',
    'bd.title':            'மோசடி வகை பிரிவு',
    'lf.title':            'சமீபத்திய கண்டுபிடிப்புகள்',
    'hl.title':            '🆘 இப்போது உதவி வேண்டுமா?',
    'hl.call-main':        '1930 அழையுங்கள்',
    'hl.call-sub':         'இணையவழி குற்ற உதவி எண் · இலவசம் · 24×7',
    'hl.web-main':         'cybercrime.gov.in இல் புகாரளியுங்கள்',
    'hl.web-sub':          'அதிகாரப்பூர்வ தேசிய இணையவழி குற்ற போர்டல்',
    'hl.cert-main':        'CERT-In போர்டல்',
    'hl.cert-sub':         'cert-in.org.in · இணையவழி பாதுகாப்பு சம்பவங்கள்',
    'hl.note':             'அனைத்து சேவைகளும் இலவசம் மற்றும் அரசாங்க நடத்தல். உதவி எண்ணின் பெயரில் பணம் கேட்பவர்களுக்கு கொடுக்காதீர்கள்.',
    'footer.text':         'Hackathon 2025 க்காக உருவாக்கப்பட்டது · உதவி எண்:',
    'detail.back':         '← ஸ்கேனருக்கு திரும்பு',
    'detail.breadcrumb1':  'DigitalArmour',
    'detail.breadcrumb2':  'மோசடி வழிகாட்டி',
    'detail.fact-threat':  'அச்சுறுத்தல் நிலை',
    'detail.fact-kw':      'கண்டறிதல் முக்கிய வார்த்தைகள்',
    'detail.fact-steps':   'பாதுகாப்பு நடவடிக்கைகள்',
    'detail.fact-phrases': 'சொற்றொடர்கள்',
    'detail.fact-actions': 'செயல்கள்',
    'detail.cta-strong':   'இதனோடு தொடர்புடைய சந்தேகமான செய்தி வந்ததா?',
    'detail.cta-span':     'ஸ்கேனரில் ஒட்டுங்கள் — நம் இயந்திரம் சில நொடிகளில் ஆய்வு செய்யும்.',
    'detail.cta-btn':      '🔍 செய்தியை ஸ்கேன் செய்',
    'detail.kw-lbl':       'எச்சரிக்கை சமிக்ஞைகள்',
    'detail.kw-ttl':       'தூண்டுதல் சொற்றொடர்கள் & அச்சுறுத்தல் எடை',
    'detail.kw-hint':      'ஒவ்வொரு சொற்றொடருக்கும் <strong>1–10</strong> எடை கொடுக்கப்பட்டுள்ளது. எடை 10 = சட்டப்பூர்வ தகவல்தொடர்பில் இது ஏறக்குறைய தோன்றாது.',
    'detail.eg-lbl':       'உண்மையான மோசடி உதாரணம்',
    'detail.eg-msg-lbl':   'வழக்கமான மோசடி செய்தி',
    'detail.eg-warn':      '⚠ இது விழிப்புணர்வுக்காக மட்டுமே — இது போன்ற செய்திகளுக்கு பதில் சொல்லாதீர்கள்.',
    'detail.act-lbl':      'உடனடி நடவடிக்கைகள்',
    'detail.act-ttl':      'இப்போது இதை செய்யுங்கள்',
    'detail.rpt-lbl':      'அதிகாரப்பூர்வ அரசாங்க சேனல்கள்',
    'detail.rpt-ttl':      'இந்த மோசடியை புகாரளியுங்கள் — இலவசம்',
    'detail.hl-call-main': '1930 அழையுங்கள்',
    'detail.hl-call-sub':  'தேசிய இணையவழி குற்ற உதவி எண் · இலவசம் · 24×7',
    'detail.hl-web-main':  'cybercrime.gov.in',
    'detail.hl-web-sub':   'தேசிய இணையவழி குற்ற புகாரளிப்பு போர்டல்',
    'detail.hl-cert-main': 'CERT-In போர்டல்',
    'detail.hl-cert-sub':  'cert-in.org.in · இணையவழி பாதுகாப்பு சம்பவ மறுமொழி',
    'detail.hl-note':      'அனைத்து சேவைகளும் இந்திய அரசாங்கத்தால் இலவசமாக நடத்தப்படுகின்றன.',
    'detail.sev-suffix':   'தீவிரம்',
    'detail.country-tag':  'இந்தியா இணையவழி குற்றம் — செயலில் உள்ள மோசடி வகை',
    'footer.back':         '← DigitalArmour ஸ்கேனருக்கு திரும்பு',
    'footer.helpline':     'உதவி எண்:',
  },

  /* ════════════════════════════════════════════
     TELUGU
  ════════════════════════════════════════════ */
  te: {
    'nav.helpline':        '📞 1930',
    'hero.eyebrow':        '🇮🇳 భారత సైబర్ నేర నివారణ',
    'hero.title-line1':    'అనుమానాస్పద కాల్ వచ్చిందా?',
    'hero.title-line2':    'నివేదించండి. మేము గుర్తిస్తాం.',
    'hero.subtitle':       'కాల్‌లో ఏం జరిగింది — ఎవరు చేశారు, ఏం చెప్పారు, ఏం అడిగారు అని రాయండి. మా ఇంజిన్ విశ్లేషించి మోసం అని చెప్తుంది.',
    'scan.card-title':     'సందేశాన్ని అతికించండి లేదా కాల్ వివరించండి',
    'scan.field-hint':     'మీరు అందుకున్న SMS / WhatsApp సందేశాన్ని నేరుగా అతికించండి, లేదా కాలర్ చెప్పింది మీ మాటల్లో రాయండి.',
    'scan.placeholder':    "ఉదా. 'ప్రియమైన కస్టమర్, మీ SBI KYC గడువు తీరిపోయింది…'\n\nలేదా: 'ఒక వ్యక్తి ED అధికారి అని చెప్పి కాల్ చేశాడు…'",
    'scan.btn':            '🔍 ఇప్పుడు స్కాన్ చేయి',
    'scan.bar':            '5 వర్గాలలో మీ నివేదిక విశ్లేషిస్తోంది…',
    'demo.title':          '🧪 డెమో పరీక్ష కేసులు',
    'hist.title':          '🕓 మీ మునుపటి స్కాన్‌లు',
    'hist.clear':          'తొలగించు',
    'hist.empty':          'ఇంకా స్కాన్‌లు లేవు — ఫలితాలు ఇక్కడ కనిపిస్తాయి.',
    'analytics.title':     '📊 లైవ్ అనలిటిక్స్',
    'analytics.badge':     'ఈరోజు',
    'kpi.detected':        'మోసాలు గుర్తించబడ్డాయి',
    'kpi.money':           'డబ్బు సురక్షితం',
    'kpi.users':           'వినియోగదారులకు హెచ్చరిక',
    'kpi.top':             'అత్యధికం: డిజిటల్ అరెస్ట్',
    'bd.title':            'మోసం రకం విభజన',
    'lf.title':            'ఇటీవలి గుర్తింపులు',
    'hl.title':            '🆘 ఇప్పుడు సహాయం కావాలా?',
    'hl.call-main':        '1930 కి కాల్ చేయండి',
    'hl.call-sub':         'సైబర్ నేర హెల్ప్‌లైన్ · ఉచితం · 24×7',
    'hl.web-main':         'cybercrime.gov.in లో నివేదించండి',
    'hl.web-sub':          'అధికారిక జాతీయ సైబర్ నేర పోర్టల్',
    'hl.cert-main':        'CERT-In పోర్టల్',
    'hl.cert-sub':         'cert-in.org.in · సైబర్ భద్రతా సంఘటనలు',
    'hl.note':             'అన్ని సేవలు ఉచితం మరియు ప్రభుత్వ నిర్వహణలో ఉన్నాయి. హెల్ప్‌లైన్ పేరిట డబ్బు అడిగేవారికి ఇవ్వకండి.',
    'footer.text':         'Hackathon 2025 కోసం నిర్మించబడింది · హెల్ప్‌లైన్:',
    'detail.back':         '← స్కానర్‌కు తిరిగి వెళ్ళు',
    'detail.breadcrumb1':  'DigitalArmour',
    'detail.breadcrumb2':  'మోసం గైడ్',
    'detail.fact-threat':  'ముప్పు స్థాయి',
    'detail.fact-kw':      'గుర్తింపు కీవర్డ్‌లు',
    'detail.fact-steps':   'రక్షణ చర్యలు',
    'detail.fact-phrases': 'పదబంధాలు',
    'detail.fact-actions': 'చర్యలు',
    'detail.cta-strong':   'దీనికి సంబంధించిన అనుమానాస్పద సందేశం వచ్చిందా?',
    'detail.cta-span':     'స్కానర్‌లో అతికించండి — మా ఇంజిన్ క్షణాల్లో విశ్లేషిస్తుంది.',
    'detail.cta-btn':      '🔍 సందేశం స్కాన్ చేయి',
    'detail.kw-lbl':       'హెచ్చరిక సంకేతాలు',
    'detail.kw-ttl':       'ట్రిగర్ పదబంధాలు & ముప్పు బరువు',
    'detail.kw-hint':      'ప్రతి పదబంధానికి <strong>1–10</strong> బరువు ఇవ్వబడింది. బరువు 10 = చట్టబద్ధమైన సందేశంలో దాదాపు వాడబడదు.',
    'detail.eg-lbl':       'నిజమైన మోసం ఉదాహరణ',
    'detail.eg-msg-lbl':   'విలక్షణమైన మోసం సందేశం',
    'detail.eg-warn':      '⚠ ఇది అవగాహన కోసం మాత్రమే — ఇలాంటి సందేశాలకు స్పందించకండి.',
    'detail.act-lbl':      'తక్షణ చర్యలు',
    'detail.act-ttl':      'ఇప్పుడే ఇది చేయండి',
    'detail.rpt-lbl':      'అధికారిక ప్రభుత్వ ఛానెళ్ళు',
    'detail.rpt-ttl':      'ఈ మోసాన్ని నివేదించండి — ఉచితం',
    'detail.hl-call-main': '1930 కి కాల్ చేయండి',
    'detail.hl-call-sub':  'జాతీయ సైబర్ నేర హెల్ప్‌లైన్ · ఉచితం · 24×7',
    'detail.hl-web-main':  'cybercrime.gov.in',
    'detail.hl-web-sub':   'జాతీయ సైబర్ నేర నివేదన పోర్టల్',
    'detail.hl-cert-main': 'CERT-In పోర్టల్',
    'detail.hl-cert-sub':  'cert-in.org.in · సైబర్ భద్రతా సంఘటన ప్రతిస్పందన',
    'detail.hl-note':      'అన్ని సేవలు భారత ప్రభుత్వంచే ఉచితంగా నిర్వహించబడతాయి.',
    'detail.sev-suffix':   'తీవ్రత',
    'detail.country-tag':  'భారత సైబర్ నేరం — క్రియాశీల మోసం రకం',
    'footer.back':         '← DigitalArmour స్కానర్‌కు తిరిగి వెళ్ళు',
    'footer.helpline':     'హెల్ప్‌లైన్:',
  },
};

const DA_I18N_LANG_KEY = 'da_lang';
const DA_LANGS = ['en', 'hi', 'kn', 'ta', 'te'];

function daGetLang() {
  const saved = localStorage.getItem(DA_I18N_LANG_KEY);
  return DA_LANGS.includes(saved) ? saved : 'en';
}

function daApplyLang(lang) {
  if (!DA_LANGS.includes(lang)) lang = 'en';
  const T = DA_TRANSLATIONS[lang] || DA_TRANSLATIONS.en;
  document.documentElement.lang = lang;

  // Text content
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    if (T[key] !== undefined) el.innerHTML = T[key];
  });

  // Placeholders
  document.querySelectorAll('[data-i18n-ph]').forEach(el => {
    const key = el.dataset.i18nPh;
    if (T[key] !== undefined) el.placeholder = T[key];
  });

  // Sync all language dropdowns on the page
  document.querySelectorAll('.lang-select').forEach(sel => { sel.value = lang; });

  localStorage.setItem(DA_I18N_LANG_KEY, lang);
}

function daSetLang(lang) {
  daApplyLang(lang);
}

// Auto-apply on load
document.addEventListener('DOMContentLoaded', () => daApplyLang(daGetLang()));
