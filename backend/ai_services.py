import os
import time
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HF_API_KEY   = os.getenv("HF_API_KEY")
IBM_MODEL    = os.getenv("IBM_MODEL", "ibm-granite/granite-4.0-h-350m")
GROQ_MODEL   = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bizforge")

# ── IBM GRANITE LOCAL MODEL ────────────────────────────────
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

granite_tokenizer = None
granite_model     = None
device = "cpu"

try:
    print("◆ Loading IBM Granite 4.0-h-350m...")
    granite_tokenizer = AutoTokenizer.from_pretrained(
        IBM_MODEL, trust_remote_code=True
    )
    granite_model = AutoModelForCausalLM.from_pretrained(
        IBM_MODEL,
        torch_dtype=torch.float32,
        trust_remote_code=True
    ).to(device)
    granite_model.eval()
    print("✅ IBM Granite loaded!")
except Exception as e:
    granite_model = None
    granite_tokenizer = None
    print(f"⚠  Granite failed (Groq fallback active): {e}")

# ── GROQ CLIENT ────────────────────────────────────────────
from groq import Groq

groq_client = None
if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)
    print("✅ Groq client ready!")
else:
    print("⚠  GROQ_API_KEY missing in .env!")

# ── BASE GROQ FUNCTION ─────────────────────────────────────
async def generate_with_groq(
    prompt: str,
    system_prompt: str = "You are BizForge, an expert AI branding assistant.",
    max_tokens: int = 1500,
    temperature: float = 0.7
) -> str:
    if not groq_client:
        return "Error: Groq API key not configured."
    try:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        response = groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=0.95
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Groq error: {e}")
        return f"Generation error: {str(e)}"

# ── FEATURE 1: BRAND NAME GENERATION ──────────────────────
async def generate_brand_names(
    industry: str, keywords: str,
    tone: str = "Professional", language: str = "en"
) -> str:
    system = (
        "You are BizForge, a world-class brand naming strategist "
        "who has named Fortune 500 companies. You understand linguistics, "
        "memorability, trademark safety, and global brand appeal."
    )
    prompt = f"""Generate 10 creative, unique, memorable brand names for a {industry} company.

Keywords to inspire: {keywords}
Brand Personality: {tone}
Output Language: {language}

For EACH of the 10 names provide:
**[Name]**
- Tagline: [one punchy tagline under 8 words]
- Why it works: [one specific reason]
- Name type: [Invented / Compound / Metaphorical / Descriptive]

Cover these categories across the 10 names:
• 2-3 invented/portmanteau words (like Spotify, Kodak)
• 2-3 compound words (like Facebook, YouTube)
• 2-3 metaphorical (like Amazon, Apple)
• 2-3 short and punchy (max 2 syllables)

AVOID: generic names, overused suffixes like -ify, -ly, -io"""

    return await generate_with_groq(prompt, system, max_tokens=1800)

# ── FEATURE 2: MARKETING CONTENT ──────────────────────────
async def generate_marketing_content(
    brand_description: str, tone: str = "Professional",
    content_type: str = "product_description", language: str = "en"
) -> str:
    system = (
        "You are an award-winning copywriter who has written campaigns "
        "for Nike, Apple, and Airbnb. Every word you write converts customers."
    )
    instructions = {
        "product_description": (
            "Write a compelling product description with: "
            "opening hook, 3 key features, emotional benefit, CTA."
        ),
        "social_media_post": (
            "Write 3 posts: one for Instagram (visual, emojis, hashtags), "
            "one for Twitter/X (punchy, under 280 chars), "
            "one for LinkedIn (professional, value-focused)."
        ),
        "email_campaign": (
            "Write a complete email: Subject line, Preview text, "
            "Greeting, Body (3 paragraphs), CTA button text, Sign-off."
        ),
        "tagline": (
            "Create 5 tagline variations. Max 8 words each. "
            "Label each: Bold / Emotional / Clever / Simple / Question."
        ),
        "ad_copy": (
            "Write ad copy with: Headline (6 words max), "
            "Subheadline, Body (2 sentences), CTA, Urgency line."
        ),
        "brand_story": (
            "Write a brand origin story covering: "
            "The problem we saw, Our mission, How we're different, "
            "Our promise to customers. 3-4 paragraphs."
        ),
    }
    instruction = instructions.get(content_type, instructions["product_description"])
    prompt = f"""Brand: {brand_description}
Tone: {tone}
Language: {language}

Task: {instruction}

Write high-quality, on-brand content:"""
    return await generate_with_groq(prompt, system, max_tokens=1200)

# ── FEATURE 3: SENTIMENT ANALYSIS ─────────────────────────
async def analyze_sentiment(
    text: str, brand_tone: str = "Professional"
) -> str:
    system = (
        "You are a brand analyst specializing in NLP sentiment analysis "
        "and brand communication strategy."
    )
    prompt = f"""Analyze this text for brand sentiment:

TEXT: "{text}"
BRAND TONE: {brand_tone}

Provide this EXACT structure:

**1. Overall Sentiment:** Positive / Neutral / Negative
**2. Confidence Score:** X/10
**3. Emotional Tone:** [what emotions are present]
**4. Key Points Mentioned:**
• [point 1]
• [point 2]
**5. Brand-Tone Alignment:** X/10 — [brief explanation]
**6. Professional Rewrite:**
[Rewrite the text in a professional {brand_tone} brand voice]
**7. Actionable Insights:**
• [insight 1]
• [insight 2]
• [insight 3]"""
    return await generate_with_groq(prompt, system, max_tokens=1000)

# ── FEATURE 4: COLOR PALETTE ───────────────────────────────
async def get_color_palette(tone: str, industry: str) -> str:
    system = (
        "You are a senior brand designer and color theorist "
        "with 20 years of visual identity experience."
    )
    prompt = f"""Create a complete visual identity system for a {tone} {industry} brand.

**COLOR PALETTE (5 colors):**
1. Primary:    #HEXCODE | Name | Usage | Psychology
2. Secondary:  #HEXCODE | Name | Usage | Psychology
3. Accent:     #HEXCODE | Name | Usage | Psychology
4. Background: #HEXCODE | Name | Usage | Psychology
5. Text:       #HEXCODE | Name | Usage | Psychology

**TYPOGRAPHY:**
- Heading Font: [name] — why it fits
- Body Font: [name] — why it pairs well
- Pairing rationale: [one sentence]

**MOOD BOARD KEYWORDS:** [5 words]

**WHY THESE WORK FOR {industry.upper()}:** [2 sentences]"""
    return await generate_with_groq(prompt, system, max_tokens=900)

# ── FEATURE 5: AI CHATBOT (GRANITE + GROQ FALLBACK) ───────
async def chat_with_ai(message: str) -> str:
    # Try IBM Granite first
    if granite_model and granite_tokenizer:
        try:
            system_ctx = (
                "You are BizForge AI, an expert brand strategist. "
                "Help with naming, logos, marketing, brand strategy. "
                "Be concise and actionable."
            )
            full_prompt = f"{system_ctx}\n\nUser: {message}\nBizForge:"
            inputs = granite_tokenizer(
                full_prompt,
                return_tensors="pt",
                max_length=512,
                truncation=True
            ).to(device)
            with torch.no_grad():
                outputs = granite_model.generate(
                    **inputs,
                    max_new_tokens=300,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=granite_tokenizer.eos_token_id
                )
            response = granite_tokenizer.decode(
                outputs[0][inputs["input_ids"].shape[1]:],
                skip_special_tokens=True
            ).strip()
            if response and len(response) > 10:
                logger.info("IBM Granite responded")
                return response
        except Exception as e:
            logger.warning(f"Granite inference failed: {e}")

    # Groq fallback
    logger.info("Using Groq fallback for chat")
    system = (
        "You are BizForge AI, an expert brand strategist with 20 years experience. "
        "Help with naming, logos, marketing, brand positioning. "
        "Be specific, reference real brand examples, and give actionable advice."
    )
    return await generate_with_groq(message, system, max_tokens=600)

# ── FEATURE 6: LOGO PROMPT ────────────────────────────────
async def generate_logo_prompt(
    brand_name: str, industry: str, keywords: str
) -> str:
    system = "You are a senior graphic designer specializing in brand identity."
    prompt = f"""Create a logo design brief for:
Brand: {brand_name} | Industry: {industry} | Style: {keywords}

Include:
1. Visual Concept (what it symbolizes)
2. Shape Language (specific geometric forms)
3. Color Recommendations (with HEX codes)
4. Typography Style (font category and weight)
5. Composition (how elements are arranged)
6. SDXL Generation Prompt (optimized for Stable Diffusion)"""
    return await generate_with_groq(prompt, system, max_tokens=700)

# ── FEATURE 7: LOGO IMAGE (STABLE DIFFUSION XL) ───────────
async def generate_logo_image(
    brand_name: str, industry: str, keywords: str
) -> dict:
    try:
        from huggingface_hub import InferenceClient
        from PIL import Image

        logo_concept = await generate_logo_prompt(brand_name, industry, keywords)

        enhanced_prompt = (
            f"Professional minimalist logo design for '{brand_name}', "
            f"{industry} brand, style: {keywords}. "
            f"Clean vector art, white background, geometric shapes, "
            f"modern typography, scalable icon, flat design, "
            f"high contrast, print-ready, award-winning logo design."
        )
        negative_prompt = (
            "blurry, low quality, distorted, watermark, photorealistic, "
            "3d render, complex background, cluttered, amateur"
        )

        client = InferenceClient(api_key=HF_API_KEY)
        print(f"🎨 Calling Stable Diffusion XL for {brand_name}...")

        image = client.text_to_image(
            enhanced_prompt,
            model="stabilityai/stable-diffusion-xl-base-1.0",
            negative_prompt=negative_prompt,
            width=1024,
            height=1024
        )

        # Save with absolute path
        base_dir = Path(__file__).parent.parent
        logos_dir = base_dir / "frontend" / "static" / "generated_logos"
        logos_dir.mkdir(parents=True, exist_ok=True)

        timestamp = int(time.time())
        filename  = f"logo_{brand_name.replace(' ','_')}_{timestamp}.png"
        save_path = logos_dir / filename
        image.save(str(save_path))
        print(f"✅ Logo saved: {save_path}")

        return {
            "image_url":    f"/static/generated_logos/{filename}",
            "logo_concept": logo_concept,
            "prompt_used":  enhanced_prompt,
            "success":      True,
            "error":        None
        }
    except Exception as e:
        logger.error(f"Logo image error: {e}")
        return {
            "image_url":    None,
            "logo_concept": await generate_logo_prompt(brand_name, industry, keywords),
            "prompt_used":  "",
            "success":      False,
            "error":        str(e)
        }

# ── FEATURE 8: VOICE TRANSCRIPTION ────────────────────────
async def transcribe_voice(audio_content: bytes) -> str:
    try:
        import speech_recognition as sr
        temp = "temp_audio.wav"
        with open(temp, "wb") as f:
            f.write(audio_content)
        r = sr.Recognizer()
        with sr.AudioFile(temp) as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        try: os.remove(temp)
        except: pass
        return text
    except sr.UnknownValueError:
        return "Could not understand audio. Please speak clearly."
    except sr.RequestError as e:
        return f"Speech service error: {e}"
    except Exception as e:
        return f"Transcription failed: {str(e)}"

# ── FEATURE 9: LONG-TEXT SUMMARIZATION ────────────────────
async def summarize_text(text: str) -> str:
    system = (
        "You are an expert editor who creates clear, concise, "
        "professional summaries capturing all critical information."
    )
    prompt = f"""Summarize this text professionally:

TEXT:
{text}

Provide:
**Summary** (3-5 sentences, captures all main points)

**Key Takeaways:**
• [point 1]
• [point 2]
• [point 3]

**Action Items** (if implied in text):
• [action 1]"""
    return await generate_with_groq(prompt, system, max_tokens=800)


# ── FEATURE 10: COMPETITOR & MARKET ANALYSIS ──────────────
async def analyze_competitors(
    brand_name: str,
    industry: str,
    target_audience: str,
    unique_value: str
) -> str:
    system = (
        "You are a senior brand strategist and competitive intelligence "
        "analyst. You specialize in helping brands find their unique market "
        "positioning and Blue Ocean strategies."
    )
    prompt = f"""Conduct a complete competitive brand analysis for:

Brand Name:    {brand_name}
Industry:      {industry}
Target Market: {target_audience}
Their Edge:    {unique_value}

Deliver ALL 6 sections with depth and specificity:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — COMPETITIVE LANDSCAPE (4-5 likely competitors)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For each competitor write:

🏢 [COMPETITOR NAME]
  Category Position:   [How they position themselves in {industry}]
  Core Strength:       [What they do better than anyone]
  Visible Weakness:    [Where they are vulnerable or missing]
  Brand Personality:   [3 adjectives that describe their brand]
  Target Customer:     [Who they primarily serve]
  Their Tagline/Claim: [Real or estimated tagline/positioning]
  Threat Level to {brand_name}: [High / Medium / Low — and why]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — MARKET GAPS & OPPORTUNITIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gap 1: [Specific unmet need that no competitor addresses well]
  Evidence: [Why this gap exists]
  Opportunity Size: [Who wants this / how big]

Gap 2: [Underserved customer segment or use case]
  Evidence: [Why competitors miss this segment]
  Opportunity Size: [Potential]

Gap 3: [Messaging or positioning territory that's unclaimed]
  Evidence: [What everyone is saying — and what no one is]
  Opportunity Size: [Brand equity potential]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — {brand_name.upper()} DIFFERENTIATION STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Blue Ocean Opportunity:
  [The specific space where {brand_name} can operate alone —
   away from direct competition. Be specific, not generic.]

Unique Angle:
  [What claim can {brand_name} make that NO competitor is making?
   What truth about the market can {brand_name} own?]

Positioning Statement:
  "For [specific target audience], {brand_name} is the only [category]
  that [unique benefit] because [credible reason to believe]."

Category to Own:
  [Can {brand_name} CREATE a new category rather than compete in an existing one?
   What would that category be called?]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — BRAND PERSONALITY GAP ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
What competitors collectively sound like:
  [Describe the collective personality/tone of the competitive set.
   What words do they all use? What feeling do their brands create?]

What {brand_name} should sound like INSTEAD:
  [The contrasting personality that creates differentiation.
   Be specific — what exact adjectives and tone?]

The Personality Vacuum {brand_name} can fill:
  [What kind of brand does this market desperately need but doesn't have yet?]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — MESSAGING STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
What all competitors say (the category clichés to avoid):
  → [Overused phrase 1 in {industry}]
  → [Overused phrase 2]
  → [Overused claim 3]

What {brand_name} should say instead:
  → [Contrarian or fresh angle 1]
  → [Unique message 2]
  → [Third distinct message]

3 Message Pillars {brand_name} can own:
  Pillar 1: [Topic/territory] — [Why this is ownable]
  Pillar 2: [Topic/territory] — [Why this is ownable]
  Pillar 3: [Topic/territory] — [Why this is ownable]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — 30-60-90 DAY QUICK WIN PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Month 1 (Establish Foundation):
  → [Specific brand action to take immediately]
  → [Second immediate action]

Month 2 (Build Differentiation):
  → [Action to amplify unique position]
  → [Content or marketing action]

Month 3 (Claim Territory):
  → [Action to own the chosen positioning]
  → [Longer-term brand building move]"""
    return await generate_with_groq(prompt, system, max_tokens=2000, temperature=0.6)


# ── FEATURE 11: BRAND VOICE & MESSAGING GUIDE ─────────────
async def generate_brand_voice(
    brand_name: str,
    industry: str,
    values: str,
    audience: str,
    tone: str = "Professional"
) -> str:
    system = (
        "You are the head of brand strategy and content at a top creative "
        "agency. You know exactly how to translate brand values into "
        "living, breathing communication guidelines."
    )
    prompt = f"""Create a complete Brand Voice & Messaging Guide for:

Brand Name:   {brand_name}
Industry:     {industry}
Core Values:  {values}
Audience:     {audience}
Tone:         {tone}

Deliver ALL 8 sections completely:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — BRAND PERSONALITY (The Human Behind The Brand)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
If {brand_name} were a person at a dinner party, they would be:

The 3-Word Brand Personality:
  Word 1: [Adjective]
    In practice this means: [How this quality shows up in real copy]
    Example phrase: "[A line that sounds like this quality]"

  Word 2: [Adjective]
    In practice this means: [Specific communication behavior]
    Example phrase: "[A line that sounds like this quality]"

  Word 3: [Adjective]
    In practice this means: [How this shapes writing choices]
    Example phrase: "[A line that sounds like this quality]"

The Celebrity / Character Reference:
  "{brand_name} sounds like [famous person or fictional character]
   combined with [another reference] — but unique because [what makes
   {brand_name} different from both]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — VOICE CHARACTERISTICS (The Rules)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Write 4 characteristic pairs. Each row = one rule.

WE ARE:              WE ARE NOT:         WHY THIS MATTERS:
[Quality]            [Its opposite]      [Impact on reader]
[Quality]            [Its opposite]      [Impact on reader]
[Quality]            [Its opposite]      [Impact on reader]
[Quality]            [Its opposite]      [Impact on reader]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — TONE ACROSS CHANNELS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Note: Core personality stays constant. TONE shifts by context.

Website / Homepage:
  Tone: [Specific description]
  Goal: [What should the visitor feel?]
  Example opening line: "[Write an example]"

Social Media (Instagram/TikTok):
  Tone: [Specific description]
  Goal: [What reaction are we driving?]
  Example caption opener: "[Write an example]"

Email Marketing:
  Tone: [Specific description]
  Goal: [Open rate / conversion goal]
  Example subject line: "[Write an example]"

Customer Support:
  Tone: [Specific description]
  Goal: [Feeling after interaction]
  Example response to complaint: "[Write an example]"

Advertising & Paid Media:
  Tone: [Specific description]
  Goal: [Action we want]
  Example headline: "[Write an example]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — MESSAGING ARCHITECTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Brand Promise (one sentence, the core commitment to every customer):
  "[The single most important promise {brand_name} makes]"

Mission Statement (why we exist beyond profit):
  "[1-2 sentences — internal north star]"

Vision Statement (the future we're building):
  "[1-2 sentences — the world if we succeed]"

Elevator Pitch (30 seconds at a networking event):
  "[Complete pitch someone could say — natural, specific, compelling]"

Value Proposition (what we offer + why it's unique):
  "We help [target audience] achieve [desired outcome]
   through [unique method/approach], unlike [alternatives]
   which [limitation they have]."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — VOCABULARY GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WORDS & PHRASES WE OWN (use freely — they reinforce our identity):
  1. [Word/phrase] — why it's on-brand
  2. [Word/phrase] — why it's on-brand
  3. [Word/phrase] — why it's on-brand
  4. [Word/phrase] — why it's on-brand
  5. [Word/phrase] — why it's on-brand

WORDS TO AVOID (overused or off-brand):
  1. "[Word]" → Use instead: "[Better alternative]"
  2. "[Word]" → Use instead: "[Better alternative]"
  3. "[Word]" → Use instead: "[Better alternative]"
  4. "[Word]" → Use instead: "[Better alternative]"
  5. "[Phrase]" → Use instead: "[Better alternative]"

INDUSTRY JARGON POLICY:
  [Use freely / Explain when used / Avoid entirely — with rationale]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — ON-BRAND vs OFF-BRAND EXAMPLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
These examples show writers EXACTLY what the voice sounds like:

WEBSITE HEADLINE:
  ✅ ON-BRAND:  "[Example that perfectly captures the voice]"
  ❌ OFF-BRAND: "[What it would sound like if written wrong]"
  Why the difference: [1 sentence explaining the gap]

SOCIAL MEDIA POST:
  ✅ ON-BRAND:  "[Full example post in perfect brand voice]"
  ❌ OFF-BRAND: "[How competitors or generic brands would write it]"
  Why the difference: [1 sentence]

ERROR MESSAGE (even errors should sound on-brand):
  ✅ ON-BRAND:  "[A {brand_name} error message — shows personality in a frustrating moment]"
  ❌ OFF-BRAND: "[Generic corporate error message]"
  Why the difference: [1 sentence]

RESPONDING TO A COMPLAINT:
  ✅ ON-BRAND:  "[How {brand_name} responds to a negative review]"
  ❌ OFF-BRAND: "[The robotic PR response to avoid]"
  Why the difference: [1 sentence]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7 — CONTENT PILLARS (What We Talk About)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
These are the 4 topics {brand_name} leads conversations about.
All content maps to at least one pillar.

Pillar 1: [Topic Name]
  Why we own this: [Our authority or unique perspective]
  Content types: [Blog / Video / Social / Podcast / etc.]
  Example content idea: "[Specific title or concept]"

Pillar 2: [Topic Name]
  Why we own this: [Our authority]
  Content types: [Formats]
  Example content idea: "[Specific example]"

Pillar 3: [Topic Name]
  Why we own this: [Our authority]
  Content types: [Formats]
  Example content idea: "[Specific example]"

Pillar 4: [Topic Name]
  Why we own this: [Our authority]
  Content types: [Formats]
  Example content idea: "[Specific example]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 8 — DEEP AUDIENCE CONNECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
What our audience fears (their 3am thought):
  "[The deep fear, written in their exact internal voice]"

What they secretly want (their dream they rarely say out loud):
  "[The aspiration — specific and emotionally resonant]"

What they're tired of hearing (from competitors and the industry):
  "[The clichés and broken promises they've heard too many times]"

What they need to hear from {brand_name}:
  "[The message that breaks through — what no one else is saying to them]"

The sentence that makes them feel truly understood:
  "[Write the one line that makes them think 'finally, someone gets it']"

How {brand_name} bridges the gap:
  "[Specific connection between their pain/aspiration and what we offer]" """
    return await generate_with_groq(prompt, system, max_tokens=2500, temperature=0.72)
