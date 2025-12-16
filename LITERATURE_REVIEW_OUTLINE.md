# Literature Review Outline: Ruang Dengar Platform

**Subtitle**: A Comprehensive Framework for Violence Reporting, AI-Driven Moderation, and Trauma-Informed Counseling in Higher Education

**Date**: December 2025  
**Project**: Ruang Dengar - Safe Reporting Platform for Campus Violence

---

## Table of Contents

1. [Introduction](#introduction)
2. [Part I: Violence in Higher Education](#part-i-violence-in-higher-education)
3. [Part II: Trauma & Counseling Frameworks](#part-ii-trauma--counseling-frameworks)
4. [Part III: Reporting Systems & Case Management](#part-iii-reporting-systems--case-management)
5. [Part IV: Artificial Intelligence & Content Moderation](#part-iv-artificial-intelligence--content-moderation)
6. [Part V: Privacy, Trust & Confidentiality](#part-v-privacy-trust--confidentiality)
7. [Part VI: Safe Campus Environment & Prevention](#part-vi-safe-campus-environment--prevention)
8. [Integration & Synthesis](#integration--synthesis)
9. [Bibliography](#bibliography)

---

## Introduction

### Context
Violence in higher education institutions represents a significant public health and human rights issue. The World Health Organization (WHO) recognizes campus-based violence as a barrier to safe learning environments and student development.

### Problem Statement
Many higher education institutions in Indonesia lack integrated, confidential, and trauma-informed reporting mechanisms for students and staff experiencing violence. Ruang Dengar addresses this gap by creating a platform that:
- Enables anonymous and identity-based reporting
- Implements AI-assisted content moderation
- Integrates professional counseling and case management
- Ensures data privacy and confidentiality

### Objectives
This literature review examines the theoretical foundations supporting the design and implementation of Ruang Dengar:
1. Understanding violence dynamics in educational settings
2. Applying trauma-informed care and counseling best practices
3. Designing effective reporting and case management systems
4. Leveraging AI/ML for content analysis and urgency assessment
5. Ensuring privacy, trust, and institutional change

---

## Part I: Violence in Higher Education

### 1.1 Ecological Theory of Human Development
**Key Author**: Urie Bronfenbrenner (1979, 1994)

**Core Concepts**:
- Five nested systems: microsystem (individual), mesosystem (family/school), exosystem (community), macrosystem (culture/policy), chronosystem (time/change)
- Violence is shaped by multi-level interactions, not just individual behavior
- Institutional context matters for prevention and response

**Relevance to Ruang Dengar**:
- Helps understand violence at multiple levels: peer relationships (microsystem), institution policies (mesosystem), societal norms (macrosystem)
- Informs design of multi-stakeholder platform (students, counselors, admins, PPKPT)
- Guides institutional change strategies

**Key Citation**: Bronfenbrenner, U. (1994). "Ecological models of human development." *International Encyclopedia of Education*, Vol. 3, pp. 1643–1647.

---

### 1.2 Social Learning Theory
**Key Author**: Albert Bandura (1977, 1986)

**Core Concepts**:
- Violence is learned through observation, imitation, and reinforcement
- Modeling of aggression in family, media, and peer groups perpetuates cycles
- Self-efficacy and perceived outcomes influence behavior

**Relevance to Ruang Dengar**:
- Explains why comprehensive reporting mechanisms are needed (to break normalization of violence)
- Justifies educational content about non-violence and healthy relationships
- Supports counseling interventions aimed at behavior change

**Key Citation**: Bandura, A. (1977). *Social Learning Theory*. Prentice-Hall.

---

### 1.3 Types of Violence in Educational Settings
**Key Framework**: WHO Classification & PPKPT Taxonomy

**Categorization**:
- **Physical violence**: assault, beatings, sexual assault
- **Psychological violence**: threats, intimidation, humiliation, gaslighting
- **Verbal harassment**: insults, mockery, hateful speech
- **Sexual violence**: unwanted touching, coercion, rape, sexual harassment
- **Cyberbullying & Digital violence**: harassment via social media, revenge porn, online threats
- **Stalking & Harassment**: persistent unwanted contact, surveillance
- **Discrimination & Intolerance**: bias-based harassment

**Relevance to Ruang Dengar**:
- Defines the scope of reportable incidents in the platform
- Maps to the `JENIS_KEKERASAN_CHOICES` field in `Laporan` model
- Informs AI categorization keywords and urgency assessment

**Key References**:
- WHO (2002). *World Report on Violence and Health*
- Kementerian PPPA & Kemenristekdikti (2020). *Panduan Penanganan Kekerasan di Perguruan Tinggi*

---

### 1.4 Cycle of Violence Theory
**Key Authors**: Lenore Walker (1979); Evan Stark (2007)

**Core Concepts**:
- Violence follows a pattern: tension → incident → reconciliation → calm → repeat
- Victims often do not leave due to psychological, economic, or institutional factors
- Institutional response can interrupt or perpetuate the cycle

**Relevance to Ruang Dengar**:
- Justifies the tracking system (`Progress` model) to monitor cases through stages
- Supports the need for timely intervention and follow-up (booking system for counseling)
- Emphasizes the role of institutional accountability in breaking cycles

**Key Citation**: Walker, L. E. (1979). *The Battered Woman*. Harper & Row.

---

## Part II: Trauma & Counseling Frameworks

### 2.1 Trauma-Informed Care Framework
**Key Organizations**: National Child Traumatic Stress Network (NCTSN), Substance Abuse and Mental Health Services Administration (SAMHSA)

**Core Principles**:
1. **Safety**: Physical and emotional safety is paramount
2. **Trustworthiness**: Transparency in all communications and decisions
3. **Choice & Control**: Survivors have agency in their healing
4. **Collaboration**: Shared decision-making between helper and survivor
5. **Empowerment**: Building on strengths and resilience

**Relevance to Ruang Dengar**:
- **Anonymous reporting** ensures safety and reduces fear of retaliation
- **Clear communication** about process and timeline builds trust
- **User control** over report visibility and counseling preferences
- **Collaborative case management** between PPKPT, counselors, and pelapor
- **Progress updates** and empowerment through information transparency

**Implementation in Platform**:
- `is_anonim` field allows identity protection
- `PelaporResponse` model enables two-way communication
- `RekamMedisKonseling` tracks recovery progress
- Notification system keeps pelapor informed

**Key Citation**: SAMHSA (2014). *Trauma-Informed Care and Practice (TIP)*, TIP 57.

---

### 2.2 Cognitive Behavioral Therapy (CBT)
**Key Authors**: Albert Ellis (1962); Aaron Beck (1976); David Clark (1986)

**Core Concepts**:
- Thoughts → Feelings → Behaviors are interconnected
- Maladaptive thought patterns perpetuate distress
- Behavioral experiments and cognitive restructuring promote change
- Collaborative, goal-oriented approach

**Relevance to Ruang Dengar**:
- Informs counseling modalities offered through the platform
- `RekamMedisKonseling.intervensi_diberikan` tracks CBT techniques used
- Supports mental health assessment via mood scale (`mood_klien`) and risk assessment (`risiko_bunuh_diri`, `risiko_self_harm`)

**Key Citation**: Beck, A. T. (1976). *Cognitive Therapy and the Emotional Disorders*. International Universities Press.

---

### 2.3 Person-Centered Therapy
**Key Author**: Carl Rogers (1951, 1980)

**Core Concepts**:
- Unconditional positive regard, genuineness, and empathy are curative
- Clients have innate capacity for growth and self-healing
- Non-directive, client-led therapeutic alliance

**Relevance to Ruang Dengar**:
- Supports counselor training and ethical guidelines
- Emphasizes counselor's role in validating and supporting survivors
- Informs platform design to center user voice (e.g., feedback mechanism, user-controlled report updates)

**Key Citation**: Rogers, C. R. (1951). *Client-Centered Therapy*. Houghton Mifflin.

---

### 2.4 Attachment Theory
**Key Author**: John Bowlby (1969, 1988); Mary Ainsworth (1978)

**Core Concepts**:
- Early attachment relationships shape capacity for trust and intimacy
- Secure attachment enables resilience; insecure attachment increases vulnerability
- Support systems (counselors, peers, family) serve as "secure bases"

**Relevance to Ruang Dengar**:
- Explains why institutional support and validated relationships are protective
- Justifies comprehensive support system: counseling, peer support, administrative advocacy
- Informs risk assessment for suicide/self-harm (attachment disruption as risk factor)

**Key Citation**: Bowlby, J. (1988). *A Secure Base: Parent-Child Attachment and Healthy Human Development*. Basic Books.

---

### 2.5 Crisis Intervention Theory
**Key Authors**: William Larson (1974); Gerald Caplan (1964); Karl Slaikeu (1990)

**Core Concepts**:
- Crisis is a temporary state of disequilibrium with danger and opportunity
- Immediate intervention can prevent deterioration and facilitate growth
- Multi-stage response: first-order (hotline/triage) → second-order (short-term counseling) → third-order (longer-term support)

**Relevance to Ruang Dengar**:
- Justifies **urgency assessment** in AI moderation (`ai_urgency` field)
- Supports **emergency contact protocol** for high-risk reports (darurat = emergency)
- Enables **rapid triage** via `Booking` system for urgent counseling
- Informs escalation procedures for dangerous situations

**Implementation**: Darurat-level cases trigger immediate admin review and counselor contact

**Key Citation**: Slaikeu, K. A. (1990). *Crisis Intervention: A Handbook for Practice and Research* (2nd ed.). Allyn & Bacon.

---

## Part III: Reporting Systems & Case Management

### 3.1 Systems Theory in Organizations
**Key Authors**: Ludwig von Bertalanffy (1968); W. Edwards Deming (1994)

**Core Concepts**:
- Organizations are systems with interacting components and feedback loops
- Effectiveness requires alignment of structure, process, and culture
- Change in one part affects the whole system

**Relevance to Ruang Dengar**:
- Models the reporting platform as a system with interdependent actors:
  - **Pelapor** (reporter) → inputs report
  - **AI Moderation** → filters/categorizes
  - **Admin** → reviews and assigns
  - **Counselor** → provides support
  - **PPKPT** → conducts formal investigation
  - **Feedback loops** → progress updates, responses
- Justifies the `Laporan` state machine with defined status transitions
- Supports multi-stakeholder design and governance

**Key Citation**: Bertalanffy, L. von (1968). *General System Theory: Foundations, Development, Applications*. George Braziller.

---

### 3.2 Case Management Theory
**Key Authors**: Katharine Briar-Lawson (1995); Nora Gustavsson (2007)

**Core Concepts**:
- Integrated, person-centered approach to service coordination
- Assessment → Planning → Implementation → Monitoring → Evaluation
- Accountability and outcomes measurement
- Cultural competency and advocacy

**Relevance to Ruang Dengar**:
- The `Laporan` model represents a case file with complete lifecycle
- `Progress` entries track case movement through 5 PPKPT tahapan (stages)
- `RekamMedisKonseling` documents clinical intervention and outcomes
- `Booking` system coordinates multi-disciplinary team (counselor, admin, PPKPT)

**Implementation**:
```
Tahapan Mapping:
1. Pelaporan → diterima, verifikasi_awal
2. Tindak Lanjut Awal → wawancara_pelapor, pengumpulan_bukti
3. Pemeriksaan → wawancara_terlapor, analisis_kronologi, rapat_pemutusan
4. Penanganan → rekomendasi
5. Tindak Lanjut → pelaksanaan, ditutup
```

**Key Citation**: Briar-Lawson, K. (1995). "Capacity building for integrated family-centered services." *Families in Society*, 76(10), 605–614.

---

### 3.3 Institutional Change & Organizational Learning
**Key Authors**: Kotter & Cohen (2002); Schein (1992)

**Core Concepts**:
- Institutional change requires aligned leadership, culture, and systems
- Learning organizations adapt to feedback and improve continuously
- Change management is gradual and requires stakeholder buy-in

**Relevance to Ruang Dengar**:
- Platform is a change agent within the institution
- Requires training and support for admin, counselors, and PPKPT members
- Generates data for institutional reflection (analytics dashboard planned)
- Supports continuous improvement via feedback loops

**Key Citation**: Kotter, J. P., & Cohen, D. S. (2002). *The Heart of Change: Real-Life Stories of How People Change Their Organizations*. Harvard Business Press.

---

## Part IV: Artificial Intelligence & Content Moderation

### 4.1 Natural Language Processing (NLP)
**Key Concepts**:
- **Tokenization**: Breaking text into words/phrases
- **Semantic analysis**: Understanding meaning and intent
- **Entity recognition**: Identifying names, dates, locations
- **Sentiment analysis**: Detecting emotional tone and toxicity
- **Text classification**: Assigning documents to categories

**Relevance to Ruang Dengar**:
- Platform uses **keyword-based classification** for fallback categorization (6 violence types)
- Supports **initial triage** and routing to appropriate responders
- Enables **search and filtering** of reports by category
- Informs **anonymization** of sensitive identifying information

**Implementation in Code**:
```python
# users/ai_moderation.py - keyword-based classification
KATEGORI_KEYWORDS = {
    'Kekerasan Seksual': ['perkosa', 'cabul', 'memaksa', ...],
    'Pelecehan Fisik': ['pukul', 'tampar', 'tendang', ...],
    # ... etc
}
```

**Key References**:
- Jurafsky, D., & Martin, J. H. (2021). *Speech and Language Processing* (3rd ed. draft). Stanford University Press.
- Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python*. O'Reilly Media.

---

### 4.2 Large Language Models (LLMs) & Generative AI
**Key Models**: Transformer architecture (Vaswani et al., 2017); BERT (Devlin et al., 2018); GPT series (OpenAI); Gemini (Google)

**Core Concepts**:
- **Transformers**: Attention mechanisms enabling context-aware understanding at scale
- **Pre-training**: Models trained on massive text corpora capture general language knowledge
- **Fine-tuning/Prompting**: Adapting pre-trained models for specific tasks via instruction or few-shot examples
- **Instruction-tuning**: Training models to follow natural language instructions

**Relevance to Ruang Dengar**:
- **Gemini API** (Google's generative model) is used for:
  - Analyzing report descriptions for urgency level
  - Estimating toxicity scores
  - Generating structured JSON output (category, urgency, toxicity)
  - Providing reasoning/explanations

**Implementation in Code**:
```python
# users/ai_moderation.py - Gemini-based moderation
model = genai.GenerativeModel('gemini-pro')
prompt = """Analisis laporan PPKPT dan berikan dalam format JSON:
Deskripsi: {full_text}
"""
response = model.generate_content(prompt)
ai_result = json.loads(response.text)
```

**Advantages**:
- Zero-shot capability: Works without task-specific training data
- Reasoning transparency: Can explain decisions
- Multi-modal understanding: Contextual awareness of violence types
- Cost-effective: No GPU/fine-tuning required

**Limitations**:
- API dependency: Requires network and API key
- Fallback needed: Keyword-based system provides robustness
- Privacy consideration: Text sent to external API (mitigated by anonymization)

**Key References**:
- Vaswani, A., et al. (2017). "Attention is all you need." *NIPS 2017*.
- Devlin, J., et al. (2018). "BERT: Pre-training of deep bidirectional transformers..." *arXiv:1810.04805*.
- Brown, T. M., et al. (2020). "Language models are few-shot learners." *arXiv:2005.14165*.
- Google AI (2024). "Gemini API Documentation". https://ai.google.dev/

---

### 4.3 Content Moderation & Toxicity Detection
**Key Frameworks**: Perspective API (Jigsaw/Google); Content policy frameworks

**Core Concepts**:
- **Toxicity**: Rude, disrespectful, or hurtful language
- **Severe toxicity**: Extremely aggressive, profane, or hateful speech
- **Threat detection**: Identification of implicit/explicit threats
- **Context matters**: Same words have different meaning in different contexts

**Relevance to Ruang Dengar**:
- **Urgency assessment** depends on detected toxicity and threat level:
  - `ai_urgency` ∈ {darurat, tinggi, sedang, rendah}
  - `ai_toxicity_score` ∈ [0.0, 1.0]
- **Escalation protocol**: High-urgency cases (`darurat`) trigger immediate admin notification
- **Blur/redaction**: Extremely violent content flagged for potential redaction

**Implementation**:
```python
def determine_urgency(toxicity_scores, teks):
    # Darurat keywords: bunuh diri, hamil, disekap, dll
    # Severe toxicity > 0.7 → darurat
    # Toxicity > 0.7 → tinggi
    # Toxicity > 0.4 → sedang
    # Else → rendah
```

**Ethical Considerations**:
- **Human-in-the-loop**: AI recommendations, not autonomous decisions
- **False positives/negatives**: Some harmful content may be missed; some benign content may be flagged
- **Bias**: Models may exhibit demographic biases from training data
- **Transparency**: Explanation of AI decisions important for user trust

**Key References**:
- Perspective API (Jigsaw Project, Google). https://www.perspectiveapi.com/
- Wulczyn, E., et al. (2017). "Ex machina: Personal attacks seen at scale." *WWW 2017*.

---

### 4.4 Ensemble Learning & Model Combination
**Key Techniques**: Voting, stacking, bagging (Random Forests), boosting (Gradient Boosting), blending

**Core Concepts**:
- **Ensemble**: Combining multiple models to improve robustness and accuracy
- **Diversity**: Different models capture different patterns
- **Voting/Averaging**: Simple combination strategies
- **Stacking**: Training a meta-learner to combine base learner predictions

**Relevance to Ruang Dengar**:
- The `ensemble_mental_health.py` script demonstrates ensemble ML for mental health classification
- Could be extended to:
  - Predict risk levels (suicide, self-harm) from mental health data
  - Classify trauma severity from narrative reports
  - Estimate counselor load and schedule optimization
- **Hybrid approach**:
  - **AI-based**: Gemini for semantic understanding
  - **Rule-based**: Keywords for structured data
  - **Statistical**: Ensemble models for risk prediction

**Ensemble Models Used** (from code):
- Random Forests (300-400 trees)
- Extra Trees (400-500 trees)
- Histogram Gradient Boosting
- Gradient Boosting
- AdaBoost
- Stacking (meta-learner: LogisticRegression or LinearRegression)

**Implementation Potential**:
```python
# Future: Predict counseling session outcomes or suicide risk
# from mental health datasets + report content features
```

**Key References**:
- Breiman, L. (1996). "Bagging predictors." *Machine Learning*, 24(2), 123–140.
- Freund, Y., & Schapire, R. E. (1997). "A decision-theoretic generalization of online learning..." *Journal of Computer and System Sciences*, 55(1), 119–139.
- Wolpert, D. H. (1992). "Stacked generalization." *Neural Networks*, 5(2), 241–259.
- Scikit-learn (2024). "Ensemble Methods Documentation". https://scikit-learn.org/stable/modules/ensemble.html

---

### 4.5 AI Ethics & Responsible Deployment
**Key Frameworks**: EU AI Act; Google AI Principles; Fairness, Accountability, Transparency (FAT)

**Core Principles**:
1. **Fairness**: System treats all users equitably; detects and mitigates bias
2. **Accountability**: Clear responsibility for AI decisions and outcomes
3. **Transparency**: Users understand how AI works and why decisions are made
4. **Privacy**: User data is protected and used appropriately
5. **Safety**: System is robust to adversarial inputs; has safeguards

**Relevance to Ruang Dengar**:
- **Bias mitigation**: Ensure AI categorization works across gender, sexuality, ethnicity
- **Transparency**: Explain to users why reports are marked "darurat" or require follow-up
- **Accountability**: Admin reviews all AI recommendations; AI is advisory, not final arbiter
- **Privacy**: Reports are anonymized before API calls; sensitive data is protected
- **Safety**: Fallback to rule-based system if API fails; no report is lost

**Implementation Safeguards**:
```python
# Fallback mechanism ensures robustness
if model is None or GEMINI_API_KEY is None:
    logger.info("Using keyword-based fallback")
    result['urgency'] = determine_urgency({}, full_text)
```

**Key References**:
- Mittelstadt, B. D., et al. (2016). "The ethics of algorithms..." *Science and Engineering Ethics*, 22(3), 505–527.
- Google AI Principles (2018). https://ai.google/principles/
- European Commission (2021). "Proposal for a Regulation on Artificial Intelligence". *AI Act*.

---

## Part V: Privacy, Trust & Confidentiality

### 5.1 Privacy Theory & Data Protection
**Key Frameworks**: GDPR (EU), Personal Data Protection Law (Indonesia), Privacy-by-Design (Cavoukian, 2009)

**Core Concepts**:
- Privacy is a fundamental human right
- Informational self-determination: individuals control their data
- Data minimization: collect only necessary data
- Purpose limitation: use data only for stated purposes
- Transparency: inform users about data practices

**Relevance to Ruang Dengar**:
- **Anonymity option**: `is_anonim=True` protects reporter identity from terlapor
- **Data minimization**: Collect only essential profile fields
- **Transparency**: Clear data policy and privacy terms
- **Access control**: Only authorized users (counselors, admin) see sensitive records
- **RekamMedisKonseling**: Medical confidentiality; inaccessible to pelapor

**Implementation**:
```python
# CustomUser model: Optional fields for those choosing anonymity
# Laporan model: is_anonim flag; identity hidden in investigations
# RekamMedisKonseling: Access restricted via Django permissions
```

**Key References**:
- Cavoukian, A. (2009). "Privacy by Design: The 7 Foundational Principles". Information & Privacy Commissioner of Ontario.
- GDPR (2018). "General Data Protection Regulation". European Commission.
- UU PDP Indonesia (2022). "Undang-Undang Perlindungan Data Pribadi No. 27 Tahun 2022".

---

### 5.2 Trust in Institutional Systems
**Key Authors**: Onora O'Neill (2002); Fukuyama (1995)

**Core Concepts**:
- Trust requires transparency, competence, and benevolence
- Institutional credibility depends on consistent, ethical behavior
- Broken trust is hard to rebuild; prevention is key

**Relevance to Ruang Dengar**:
- **Transparency**: Users see status updates and progress on their reports
- **Competence**: PPKPT & counselors are trained, credentialed professionals
- **Benevolence**: System is designed to help, not punish; confidentiality protected
- **Anonymity**: Allows vulnerable users to report without fear of retaliation

**Implementation**:
- `PelaporResponse` model enables dialogue between pelapor and admin
- `Progress` tracking shows case movement and commitment
- Clear communication about process reduces uncertainty
- Emergency hotline and contacts visible on landing page

**Key Citation**: O'Neill, O. (2002). *A Question of Trust: The BBC Reith Lectures 2002*. Cambridge University Press.

---

### 5.3 Whistleblowing & Protected Disclosure
**Key Frameworks**: SOX (Sarbanes-Oxley); Protected Disclosure Laws; Institutional Ombudsman

**Core Concepts**:
- Whistleblowers face retaliation risk; protections are essential
- Confidentiality must be absolute; anonymity enables disclosure
- Institutional acceptance of criticism is sign of healthy culture
- Independent investigation required to ensure impartiality

**Relevance to Ruang Dengar**:
- Platform enables **protected disclosure** of campus violations
- **Anonymity option** reduces retaliation risk
- **Independent PPKPT** conducts investigation (not just campus admin)
- **Documented process** ensures accountability and transparency

**Key References**:
- Near, J. P., & Miceli, M. P. (2002). "Organizational dissidence: The case of whistleblowing." *Journal of Business Ethics*, 4(1), 1–16.
- Sarbanes-Oxley Act (2002). Section 806: Whistleblower Protection. U.S. Congress.

---

## Part VI: Safe Campus Environment & Prevention

### 6.1 Safe Learning Environment Theory
**Key Framework**: WHO; UNESCO; Whole-School Approach

**Core Concepts**:
- Safety is prerequisite for learning
- Multiple dimensions: physical, emotional, social, digital
- Involves entire school community: students, staff, parents, leadership
- Prevention through awareness, capacity-building, and accountability

**Relevance to Ruang Dengar**:
- Platform contributes to **emotional safety** through confidential reporting
- **Educational content** (articles, modules) promotes awareness
- **Counseling services** help healing and resilience
- **Accountability** (tracking cases, following up) deters future harm

**Implementation**:
- Landing page with PPKPT information and violence categories
- Educational modules on violence types and resources
- Counseling booking system
- Admin dashboard for incident tracking

**Key References**:
- WHO (2009). "Violence Prevention: The Evidence". World Health Organization.
- UNESCO (2019). "Behind the Numbers: Ending School Violence and Bullying". UNESCO Report.

---

### 6.2 Institutional Prevention & Zero-Tolerance Framework
**Key Concepts**:
- Prevention > reaction; early intervention > crisis management
- Clear consequences for violations; consistent enforcement
- Multiple interventions: education, bystander intervention, policy enforcement
- Trauma-informed approach even in discipline (avoid retraumatization)

**Relevance to Ruang Dengar**:
- Reporting mechanism is **early detection** tool
- **AI urgency assessment** enables rapid response
- **Case management** tracks institutional follow-through
- **Analytics** (planned) reveal patterns and inform prevention strategies

**Key References**:
- Berkowitz, A. D. (2002). "Fostering Men's Responsibility for Preventing Sexual Assault". *Handbook of College Sexual Assault Prevention*. Jossey-Bass.
- RAINN (2020). "Campus Sexual Assault". https://www.rainn.org/articles/sexual-assault-campus

---

### 6.3 Community of Care & Collective Responsibility
**Key Concepts**:
- Violence prevention is shared responsibility, not just victims'
- Bystander intervention and upstander behavior critical
- Institutional culture shapes whether violence is tolerated or resisted
- Collectivity > isolation; connection > shame

**Relevance to Ruang Dengar**:
- Platform is **hub for collective action**: students, counselors, admin, PPKPT
- **Community knowledge**: Aggregated reports reveal patterns
- **Peer support**: Booking system + counselor matching
- **Institutional acknowledgment**: Admin response validates survivors

**Key References**:
- Banyard, V. L., et al. (2007). "The impact of social influences on perpetration of unwanted coercion..." *Journal of Interpersonal Violence*, 22(8), 1061–1078.

---

## Integration & Synthesis

### 6.4 Integrated Model: Ruang Dengar as Socio-Technical System

**Model Architecture**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    RUANG DENGAR PLATFORM                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  USER LAYER (Trauma-Informed, Trauma-Sensitive)               │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ Pelapor (Anonymous/Identified) → Report Submission      │  │
│  │ Counselor → Booking + RekamMedisKonseling              │  │
│  │ Admin/PPKPT → Case Management + Progress Tracking      │  │
│  └─────────────────────────────────────────────────────────┘  │
│                            ↓                                    │
│  MODERATION LAYER (AI + Rule-Based)                            │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ Keyword Classification (Rule-Based Fallback)            │  │
│  │ ↓                                                        │  │
│  │ Gemini AI Analysis (NLP + Toxicity + Urgency)          │  │
│  │ ↓                                                        │  │
│  │ Categorization: {Kekerasan Seksual, Fisik, ...}        │  │
│  │ Urgency: {Darurat, Tinggi, Sedang, Rendah}            │  │
│  │ Toxicity Score: [0.0, 1.0]                             │  │
│  └─────────────────────────────────────────────────────────┘  │
│                            ↓                                    │
│  CASE MANAGEMENT LAYER (Systems Theory + Case Management)     │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ 5-Stage PPKPT Process:                                 │  │
│  │ 1. Pelaporan (diterima, verifikasi_awal)               │  │
│  │ 2. Tindak Lanjut Awal (wawancara_pelapor, bukti)       │  │
│  │ 3. Pemeriksaan (wawancara_terlapor, analisis)          │  │
│  │ 4. Penanganan (rekomendasi)                            │  │
│  │ 5. Tindak Lanjut (pelaksanaan, ditutup)                │  │
│  │                                                        │  │
│  │ Progress tracking, Documentation (Evidence model)      │  │
│  │ Pelapor Communication (PelaporResponse model)         │  │
│  └─────────────────────────────────────────────────────────┘  │
│                            ↓                                    │
│  COUNSELING LAYER (Trauma-Informed Care + CBT + Attachment)   │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ Booking System → Schedule Counselor Sessions            │  │
│  │ ↓                                                        │  │
│  │ RekamMedisKonseling → Clinical Assessment:             │  │
│  │   - Mood (1-10 scale)                                  │  │
│  │   - Suicide Risk / Self-Harm Risk                      │  │
│  │   - Interventions (CBT, mindfulness, etc.)             │  │
│  │   - Progress Notes                                     │  │
│  │   - Next Session Planning                              │  │
│  │                                                        │  │
│  │ Access: Counselor + Admin only (Privacy)               │  │
│  └─────────────────────────────────────────────────────────┘  │
│                            ↓                                    │
│  INSTITUTIONAL CHANGE LAYER (Org Theory + Prevention)         │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ Analytics & Reporting (Trends, Patterns)                │  │
│  │ Leadership Dashboard (for PPKPT + Admin leadership)     │  │
│  │ Institutional Learning (Feedback loops)                 │  │
│  │ Prevention Strategies (Informed by data)                │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│              UNDERLYING PRINCIPLES (All Layers)                │
│  • Privacy & Confidentiality (Data Protection)                │
│  • Transparency & Trust (Institutional)                        │
│  • Multi-Stakeholder Coordination (Systems Theory)             │
│  • AI Ethics & Human Oversight (Responsible AI)               │
│  • Trauma-Informed Care (Psychology)                          │
└─────────────────────────────────────────────────────────────────┘
```

---

### Synthesis: Why These Theories Matter

| Theory | Problem It Solves | Ruang Dengar Implementation |
|--------|------------------|---------------------------|
| Ecological Theory | Violence is multi-level | Multi-stakeholder design (students, counselors, admin, PPKPT) |
| Social Learning | Violence is learned & normalized | Educational modules + reporting changes norms |
| Trauma-Informed Care | Survivors need safety & voice | Anonymous reporting + user control + progress updates |
| Systems Theory | Organizations are interconnected | Laporan model coordinates multiple actors |
| Case Management | Cases need holistic coordination | Progress tracking + Evidence collection + Booking system |
| NLP & LLMs | Reports need intelligent analysis | AI moderation for categorization & urgency |
| Content Moderation | Harmful content must be flagged | Toxicity scoring + threshold-based escalation |
| Privacy Theory | Data must be protected | Anonymity option + access controls + encryption ready |
| Trust Theory | Institutions must be credible | Transparency (progress updates) + accountability (case tracking) |
| Safe Campus Theory | Prevention is possible | Educational content + early detection + rapid response |

---

## Bibliography

### Foundational Theories

1. Bronfenbrenner, U. (1994). "Ecological models of human development." *International Encyclopedia of Education*, Vol. 3, pp. 1643–1647.

2. Bandura, A. (1977). *Social Learning Theory*. Prentice-Hall.

3. Bertalanffy, L. von (1968). *General System Theory: Foundations, Development, Applications*. George Braziller.

4. Bowlby, J. (1988). *A Secure Base: Parent-Child Attachment and Healthy Human Development*. Basic Books.

5. Beck, A. T. (1976). *Cognitive Therapy and the Emotional Disorders*. International Universities Press.

6. Rogers, C. R. (1951). *Client-Centered Therapy*. Houghton Mifflin.

7. Walker, L. E. (1979). *The Battered Woman*. Harper & Row.

### Violence & Campus Safety

8. WHO (2002). *World Report on Violence and Health*. World Health Organization. https://www.who.int/publications/i/item/9241545615

9. Kementerian PPPA & Kemenristekdikti (2020). *Panduan Penanganan Kekerasan di Perguruan Tinggi*. Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi.

10. UNESCO (2019). *Behind the Numbers: Ending School Violence and Bullying*. UNESCO Report. https://www.unesco.org/

11. RAINN (2020). *Campus Sexual Assault*. https://www.rainn.org/articles/sexual-assault-campus

12. Berkowitz, A. D. (2002). "Fostering Men's Responsibility for Preventing Sexual Assault." *Handbook of College Sexual Assault Prevention*. Jossey-Bass.

### Trauma & Mental Health

13. SAMHSA (2014). *Trauma-Informed Care and Practice (TIP 57)*, Substance Abuse and Mental Health Services Administration. https://store.samhsa.gov/product/TIP-57-Trauma-Informed-Care-and-Practice

14. National Child Traumatic Stress Network (NCTSN). *Resources on Trauma-Informed Care*. https://www.nctsn.org/

15. Slaikeu, K. A. (1990). *Crisis Intervention: A Handbook for Practice and Research* (2nd ed.). Allyn & Bacon.

### Case Management & Organizational Change

16. Briar-Lawson, K. (1995). "Capacity building for integrated family-centered services." *Families in Society*, 76(10), 605–614.

17. Kotter, J. P., & Cohen, D. S. (2002). *The Heart of Change: Real-Life Stories of How People Change Their Organizations*. Harvard Business Press.

18. Schein, E. H. (1992). *Organizational Culture and Leadership* (2nd ed.). Jossey-Bass.

### Privacy & Trust

19. Cavoukian, A. (2009). *Privacy by Design: The 7 Foundational Principles*. Information & Privacy Commissioner of Ontario. https://www.ipc.on.ca/wp-content/uploads/resources/7foundationalprinciples.pdf

20. European Commission (2018). *General Data Protection Regulation (GDPR)*. Official Journal of the European Union. https://eur-lex.europa.eu/eli/reg/2016/679/oj

21. UU PDP Indonesia (2022). *Undang-Undang Perlindungan Data Pribadi No. 27 Tahun 2022*. Kementerian Hukum dan HAM. https://www.kemenkumham.go.id/

22. O'Neill, O. (2002). *A Question of Trust: The BBC Reith Lectures 2002*. Cambridge University Press.

23. Near, J. P., & Miceli, M. P. (2002). "Organizational dissidence: The case of whistleblowing." *Journal of Business Ethics*, 4(1), 1–16.

### Natural Language Processing & AI

24. Jurafsky, D., & Martin, J. H. (2021). *Speech and Language Processing* (3rd ed. draft). Stanford University Press. https://web.stanford.edu/~jurafsky/slp3/

25. Bird, S., Klein, E., & Loper, E. (2009). *Natural Language Processing with Python: Analyzing Text with the Natural Language Toolkit*. O'Reilly Media.

26. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). "Attention is all you need." In *Advances in Neural Information Processing Systems 30 (NIPS 2017)*, pp. 5998–6008.

27. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). "BERT: Pre-training of deep bidirectional transformers for language understanding." *arXiv preprint arXiv:1810.04805*.

28. Brown, T. M., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., ... & Amodei, D. (2020). "Language models are few-shot learners." *arXiv preprint arXiv:2005.14165*.

### Content Moderation & Toxicity Detection

29. Wulczyn, E., Thain, N., & Dixon, L. (2017). "Ex machina: Personal attacks seen at scale." In *Proceedings of the 26th International Conference on World Wide Web* (WWW '17), pp. 1391–1399.

30. Perspective API (Jigsaw Project, Google). *Toxicity & Bias Detection for Online Comments*. https://www.perspectiveapi.com/

31. Mittelstadt, B. D., Allo, P., Taddeo, M., Watcher, S., & Floridi, L. (2016). "The ethics of algorithms: Mapping the debate." *Science and Engineering Ethics*, 22(3), 505–527.

### Machine Learning & Ensemble Methods

32. Breiman, L. (1996). "Bagging predictors." *Machine Learning*, 24(2), 123–140.

33. Freund, Y., & Schapire, R. E. (1997). "A decision-theoretic generalization of online learning and an application to boosting." *Journal of Computer and System Sciences*, 55(1), 119–139.

34. Wolpert, D. H. (1992). "Stacked generalization." *Neural Networks*, 5(2), 241–259.

35. Scikit-learn Developers (2024). *Ensemble Methods: RandomForestClassifier, GradientBoostingClassifier, StackingClassifier*. https://scikit-learn.org/stable/modules/ensemble.html

### Large Language Models & Generative AI

36. Google AI (2024). *Gemini API Documentation*. https://ai.google.dev/

37. OpenAI (2023). *GPT-4 Technical Report*. https://arxiv.org/abs/2303.08774

38. Google Research (2024). *Responsible AI Practices*. https://ai.google/responsibility/

### Institutional AI Governance

39. European Commission (2021). *Proposal for a Regulation on Artificial Intelligence (AI Act)*. https://ec.europa.eu/info/publications/proposal-regulation-artificial-intelligence_en

40. Google (2018). *AI Principles*. https://ai.google/principles/

---

## Appendix: Ruang Dengar Model Mapping

### How Models Embody Theoretical Principles

| Django Model | Theories Embodied | Key Fields |
|--------------|------------------|-----------|
| `CustomUser` | Privacy, Identity, Trust | email, is_profile_complete, is_active |
| `Laporan` | Case Management, Systems Theory, Violence Theory | status, kode, ai_kategori, ai_urgency, is_anonim |
| `Evidence` | Case Management, Accountability | file, uploaded_by, keterangan |
| `Progress` | Case Management, Institutional Accountability | status, catatan, oleh, tanggal |
| `PelaporResponse` | Trust, Communication, Feedback Loops | pesan, tanggal, laporan |
| `Booking` | Crisis Intervention, Trauma-Informed Care | tanggal, waktu, konselor_fk, status |
| `RekamMedisKonseling` | Trauma-Informed Care, CBT, Crisis Intervention | mood_klien, risiko_bunuh_diri, catatan_konselor, intervensi |
| `Counselor` | Trauma-Informed Care, Professional Support | name, title |

---

## Notes for Further Development

1. **Analytics & Institutional Learning**: Build dashboard to visualize trends (e.g., incidents by time, type, faculty) for leadership reflection and prevention strategy refinement.

2. **Ensemble ML for Risk Prediction**: Integrate ensemble models (as in `ensemble_mental_health.py`) to predict suicide/self-harm risk from mental health data + report features.

3. **Bias Audit**: Regularly test AI models for demographic bias in urgency/category assignments.

4. **User Research**: Conduct qualitative interviews with survivors, counselors, and admin to validate that platform design reflects lived experience and best practices.

5. **Policy Development**: Co-develop institutional policies on response timelines, confidentiality, and consequences for perpetrators.

6. **Training Programs**: Create curriculum for counselors, admin, and student leaders on trauma-informed care and violence prevention.

---

**Document Version**: 1.0  
**Last Updated**: December 15, 2025  
**Maintainer**: Ruang Dengar Development Team  
**License**: CC BY-NC-SA 4.0 (for academic use)

---
