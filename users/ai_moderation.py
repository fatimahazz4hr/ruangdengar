"""
AI Content Moderation Module
Menggunakan Google Gemini (GRATIS) untuk analisis konten laporan
"""

import google.generativeai as genai
import os
import logging

logger = logging.getLogger(__name__)

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')

def get_model():
    """Initialize Gemini model"""
    try:
        if GEMINI_API_KEY:
            genai.configure(api_key=GEMINI_API_KEY)
            model = genai.GenerativeModel('gemini-pro')
            logger.info("Gemini model initialized successfully")
            return model
        else:
            logger.warning("GEMINI_API_KEY not found, AI moderation disabled")
            return None
    except Exception as e:
        logger.error(f"Failed to initialize Gemini model: {e}")
        return None


# Keyword-based classification
KATEGORI_KEYWORDS = {
    'Kekerasan Seksual': [
        'perkosa', 'cabul', 'alat kelamin', 'memaksa berhubungan',
        'sentuh pribadi', 'raba pribadi', 'pegang pribadi', 'diremas pribadi', 
        'dicium paksa', 'sexual assault', 'rape', 'molest', 'harass sexually'
    ],
    'Kekerasan Fisik dan Psikis': [
        'pukul', 'tampar', 'tendang', 'dorong', 'cekik', 'dicekik', 'tonjok', 'jambak',
        'lempar', 'injak', 'gigit', 'assault', 'physical abuse', 'kekerasan fisik',
        'dipukul', 'ditampar', 'ditendang', 'didorong', 'ditonjok', 'dijambak',
        'dilempar', 'diinjak', 'digigit', 'ditarik', 'dilecehkan', 'leceh', 'lecehkan'
    ],
    'Pelecehan Verbal': [
        'ancam', 'intimidasi', 'maksa', 'memaki', 'menghina', 'kata kasar',
        'verbal abuse', 'threat', 'blackmail', 'mengancam', 'teror', 'diancam',
        'diintimidasi', 'dimaki', 'dihinakan'
    ],
    'Pelecehan Psikologis': [
        'manipulasi', 'gaslighting', 'kontrol', 'isolasi', 'mengekang',
        'merendahkan', 'emotional abuse', 'mental torture', 'trauma', 'depresi',
        'cemas', 'takut', 'ketakutan'
    ],
    'Perundungan (Bullying)': [
        'bullying', 'bully', 'dibully', 'usir', 'kucilkan', 'kucilan', 'gosip',
        'fitnah', 'ejek', 'hina', 'mengolok', 'sindiran', 'olok'
    ],
    'Cyberbullying': [
        'chat', 'dm', 'wa', 'foto', 'video', 'sosmed', 'online', 'instagram',
        'facebook', 'twitter', 'tiktok', 'cyberbully', 'revenge porn', 'screenshot'
    ],
    'Stalking': [
        'mengikuti', 'menguntit', 'stalking', 'terus menerus', 'memata-matai',
        'slalu ada', 'pantau terus', 'diikuti', 'diuntit'
    ]
}


def classify_kategori(teks):
    """
    Klasifikasi kategori berdasarkan keyword matching
    Returns: nama kategori atau 'Lainnya'
    """
    teks_lower = teks.lower()
    
    # Count matches per kategori
    kategori_scores = {}
    for kategori, keywords in KATEGORI_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in teks_lower)
        if score > 0:
            kategori_scores[kategori] = score
    
    # Return kategori dengan score tertinggi
    if kategori_scores:
        return max(kategori_scores, key=kategori_scores.get)
    return 'Lainnya'


def determine_urgency(toxicity_scores, teks):
    """
    Tentukan tingkat urgensi berdasarkan toxicity scores dan keywords
    """
    # Keywords untuk urgency DARURAT (situasi kritis)
    darurat_keywords = [
        'bunuh diri', 'suicide', 'mati', 'ingin mati', 'mengakhiri hidup',
        'hamil', 'pregnant', 'tidak bisa keluar', 'disekap', 'dikurung',
        'masih berlangsung', 'sedang terjadi', 'tolong', 'help'
    ]
    
    # Keywords untuk urgency TINGGI (kekerasan serius)
    tinggi_keywords = [
        'cekik', 'dicekik', 'pukul', 'dipukul', 'luka', 'darah', 'patah',
        'dirawat', 'rumah sakit', 'darurat medis', 'jatuh'
    ]
    
    teks_lower = teks.lower()
    
    # Check darurat keywords
    if any(keyword in teks_lower for keyword in darurat_keywords):
        return 'darurat'
    
    # Check tinggi keywords
    if any(keyword in teks_lower for keyword in tinggi_keywords):
        return 'tinggi'
    
    # Check toxicity scores
    if toxicity_scores.get('severe_toxicity', 0) > 0.7 or toxicity_scores.get('threat', 0) > 0.6:
        return 'darurat'
    elif toxicity_scores.get('toxicity', 0) > 0.7:
        return 'tinggi'
    elif toxicity_scores.get('toxicity', 0) > 0.4:
        return 'sedang'
    else:
        return 'rendah'


def moderate_laporan(deskripsi, jenis=None):
    """
    Analisis laporan dengan AI Content Moderation
    
    Args:
        deskripsi (str): Teks deskripsi laporan
        jenis (str): Jenis laporan (opsional, untuk tambahan konteks)
    
    Returns:
        dict: {
            'kategori': str,
            'urgency': str,
            'toxicity_score': float,
            'needs_blur': bool,
            'scores': dict (detail semua scores),
            'analyzed': bool
        }
    """
    result = {
        'kategori': 'Lainnya',
        'urgency': 'sedang',
        'toxicity_score': 0.0,
        'needs_blur': False,
        'scores': {},
        'analyzed': False
    }
    
    try:
        # Gabungkan jenis dan deskripsi untuk analisis lebih baik
        full_text = f"{jenis or ''} {deskripsi}".strip()
        
        # 1. Keyword-based Classification (SELALU jalan)
        result['kategori'] = classify_kategori(full_text)
        
        # 2. Gemini AI Analysis (jika API key tersedia)
        model = get_model()
        if model and GEMINI_API_KEY:
            try:
                prompt = f"""Analisis laporan PPKPT berikut dan berikan dalam format JSON:
Deskripsi: {full_text}

Berikan output JSON dengan key berikut:
- urgency: "rendah"/"sedang"/"tinggi"/"darurat"
- toxicity_score: angka 0.0-1.0
- needs_blur: true/false (jika konten ekstrem)
- reasoning: penjelasan singkat

Contoh output:
{{"urgency": "tinggi", "toxicity_score": 0.8, "needs_blur": true, "reasoning": "Konten mengandung ancaman serius"}}"""

                response = model.generate_content(prompt)
                # Parse JSON dari response
                import json
                ai_result = json.loads(response.text.strip().replace('```json', '').replace('```', ''))
                
                result['urgency'] = ai_result.get('urgency', 'sedang')
                result['toxicity_score'] = ai_result.get('toxicity_score', 0.5)
                result['needs_blur'] = ai_result.get('needs_blur', False)
                result['analyzed'] = True
                result['scores'] = {'ai_reasoning': ai_result.get('reasoning', '')}
                
                logger.info(f"Gemini AI analysis: {ai_result.get('reasoning', '')}")
            except Exception as e:
                logger.error(f"Gemini API error: {e}, using fallback")
                # Fallback ke keyword-based
                result['urgency'] = determine_urgency({}, full_text)
                result['toxicity_score'] = 0.5
        else:
            # Fallback jika tidak ada API key: skor heuristik berdasarkan keyword
            logger.info("Gemini API not configured, using keyword-based fallback")
            # Hitung skor toksisitas sederhana
            teks_lower = full_text.lower()
            # Kelompok kata berat
            severe_terms = ['cekik', 'dicekik', 'perkosa', 'rape', 'suicide', 'bunuh diri', 'ancam', 'diancam']
            medium_terms = ['pukul', 'tampar', 'tendang', 'dorong', 'jambak', 'harass', 'intimidasi', 'gaslighting', 'leceh', 'dilecehkan']
            severe_hits = sum(1 for k in severe_terms if k in teks_lower)
            medium_hits = sum(1 for k in medium_terms if k in teks_lower)
            base = 0.3
            score = min(1.0, base + severe_hits * 0.25 + medium_hits * 0.1)
            result['toxicity_score'] = round(score, 2)
            result['urgency'] = determine_urgency({'toxicity': score}, full_text)
        
        logger.info(f"AI Moderation completed: kategori={result['kategori']}, urgency={result['urgency']}, toxicity={result['toxicity_score']:.2f}")
        
    except Exception as e:
        logger.error(f"Error in AI moderation: {e}")
        # Return safe defaults on error
        result['analyzed'] = False
    
    return result


def batch_moderate(laporan_list):
    """
    Moderate multiple laporan sekaligus (untuk existing data)
    
    Args:
        laporan_list: List of Laporan objects
    
    Returns:
        dict: {laporan_id: moderation_result}
    """
    results = {}
    for laporan in laporan_list:
        try:
            result = moderate_laporan(laporan.deskripsi, laporan.jenis)
            results[laporan.id] = result
        except Exception as e:
            logger.error(f"Error moderating laporan {laporan.id}: {e}")
            results[laporan.id] = None
    
    return results
