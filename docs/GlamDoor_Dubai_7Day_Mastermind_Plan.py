from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

doc = SimpleDocTemplate("GlamDoor_Dubai_7Day_Mastermind_Plan.pdf", pagesize=A4,
                        leftMargin=0.5*inch, rightMargin=0.5*inch,
                        topMargin=0.5*inch, bottomMargin=0.5*inch)

styles = getSampleStyleSheet()
story = []

title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=24,
    textColor=colors.HexColor('#8B4513'), spaceAfter=12, alignment=TA_CENTER, fontName='Helvetica-Bold')
heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=14,
    textColor=colors.HexColor('#8B4513'), spaceAfter=8, spaceBefore=10, fontName='Helvetica-Bold')
subheading_style = ParagraphStyle('SubHeading', parent=styles['Heading3'], fontSize=11,
    textColor=colors.HexColor('#D4A574'), spaceAfter=6, fontName='Helvetica-Bold')
body_style = ParagraphStyle('BodyText', parent=styles['Normal'], fontSize=9,
    alignment=TA_LEFT, spaceAfter=6, leading=12)
bot_style = ParagraphStyle('BotStyle', parent=styles['Normal'], fontSize=9,
    alignment=TA_LEFT, spaceAfter=6, leading=12, textColor=colors.HexColor('#2E7D32'))

story.append(Paragraph("GlamDoor Dubai 7-Day Mastermind", title_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Week 1: Get First Clients &amp; Build Momentum", subheading_style))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph("Updated: AI Chatbot + Bilingual EN/AR Support", subheading_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))
summary_text = """
<b>Goal:</b> 50+ leads, 10+ partner sign-ups, 3+ confirmed bookings in 7 days<br/>
<b>Focus:</b> Dubai only (hyper-local: Marina, Downtown, JVC)<br/>
<b>Strategy:</b> Parallel outreach + daily content + zone-based targeting + AI chatbot<br/>
<b>Cost:</b> AED 1,500-2,500 (ads + tools) + AED 500 chatbot dev<br/>
<b>Win Metric:</b> First booking confirmed by Day 5<br/>
<b>NEW:</b> AI Chatbot live by Day 4 (EN/AR) handling bookings &amp; support 24/7
"""
story.append(Paragraph(summary_text, body_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("DUBAI ZONES - PRIORITY TIERS", heading_style))
zones_data = [
    ['TIER 1 (High Priority)', 'TIER 2 (Medium)', 'TIER 3 (Week 2+)'],
    ['Marina | Downtown | Jumeirah', 'Deira | Al Barsha | Mirdif | Al Wasl', 'Sharjah | Abu Dhabi'],
    ['Affluent, expats, online-savvy, high spend', 'Growing income, strong communities', 'Scale after Dubai dominance']
]
zones_table = Table(zones_data, colWidths=[2.2*inch, 2.2*inch, 2.2*inch])
zones_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#8B4513')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 9),
    ('BOTTOMPADDING', (0,0), (-1,0), 10),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('FONTSIZE', (0,1), (-1,-1), 8),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 6),
]))
story.append(zones_table)
story.append(Spacer(1, 0.3*inch))
story.append(PageBreak())

# AI CHATBOT SECTION
story.append(Paragraph("AI CHATBOT - GLAMDOOR ASSISTANT (EN/AR)", heading_style))
bot_text = """
<b>OVERVIEW</b><br/>
GlamDoor AI Chatbot handles customer bookings, salon inquiries, and support 24/7 in Arabic &amp; English.<br/>
Reduces manual WhatsApp replies by 70%, captures leads even at 3 AM, books appointments directly.<br/><br/>
<b>CORE FEATURES</b><br/>
1. <b>Bilingual Support (EN/AR):</b> Auto-detects user language, switches instantly. All responses, menus, and booking flows in both languages.<br/>
2. <b>Smart Booking Engine:</b> Customer says "I want a manicure in Marina tomorrow 4pm" - bot checks availability, confirms, sends calendar invite.<br/>
3. <b>Salon Directory Search:</b> "Show me salons near Downtown for hair" - returns top 3 matches with ratings, prices, and instant book button.<br/>
4. <b>Real-Time Support:</b> FAQs (pricing, cancellation, reschedule, refunds), live agent handoff for complex cases.<br/>
5. <b>Lead Capture:</b> Collects name, phone, email, preferred zone &amp; service before booking attempt. Logs to tracking sheet.<br/>
6. <b>Partner Dashboard Sync:</b> Bookings appear in partner's dashboard instantly. Auto-confirm or manual approve option.<br/>
7. <b>WhatsApp + Web Widget:</b> Deploys on WhatsApp Business (primary) and as a web widget on the landing page.<br/>
8. <b>Post-Booking Follow-Up:</b> Auto-sends reminder 2 hrs before, asks for review 2 hrs after. Collects testimonials automatically.<br/><br/>
<b>TECH STACK</b><br/>
- <b>AI Engine:</b> OpenAI GPT-4o-mini (cost-efficient, fast, multilingual)<br/>
- <b>Platform:</b> WhatsApp Business API (Twilio) + web widget (React/JS embed)<br/>
- <b>NLU:</b> GPT-4o-mini with Arabic + English prompts (no separate NLU needed)<br/>
- <b>Booking:</b> Cal.com API integration for real-time availability<br/>
- <b>Database:</b> Base44 entities (Bookings, Customers, Partners, Conversations)<br/>
- <b>Hosting:</b> Backend function (Base44 serverless) - no server maintenance<br/>
- <b>Cost:</b> ~AED 500/mo (API calls + Twilio) for up to 1,000 conversations<br/><br/>
<b>ARABIC SUPPORT SPECIFICS</b><br/>
- RTL text rendering in chat UI<br/>
- Arabic salon service terms (manicure = manakir, haircut = qisat shaar, etc.)<br/>
- Local dialect awareness (Khaleeji / Gulf Arabic phrases)<br/>
- Arabic + English mixed input handling ("I want manakir in Marina")<br/>
- Currency always AED, dates in Hijri + Gregorian option<br/><br/>
<b>BOOKING FLOW (Customer Side)</b><br/>
Step 1: Customer sends message (EN or AR) -> bot greets in detected language<br/>
Step 2: Bot asks: What service? Which area? When?<br/>
Step 3: Bot searches partner database, shows 3 options with prices &amp; ratings<br/>
Step 4: Customer selects -> bot checks Cal.com availability -> confirms or offers alternatives<br/>
Step 5: Bot asks for name + phone (if new) -> creates booking -> sends confirmation + calendar invite<br/>
Step 6: 2 hrs before: reminder message. 2 hrs after: review request<br/><br/>
<b>BOOKING FLOW (Partner Side)</b><br/>
- New booking notification on WhatsApp + dashboard<br/>
- Auto-confirm (default) or manual approve toggle<br/>
- Daily summary: tomorrow's bookings at 8 PM<br/>
- Block unavailable slots via WhatsApp command: "Block tomorrow 2-4pm"<br/><br/>
<b>SUPPORT FLOW</b><br/>
- FAQs auto-handled: pricing, hours, location, cancellation policy, reschedule<br/>
- Complex queries -> bot says "Let me connect you with our team" -> notifies admin<br/>
- All conversations logged for quality + training<br/>
- Sentiment tracking: if user seems frustrated -> auto-escalate to human<br/><br/>
<b>DEPLOYMENT TIMELINE</b><br/>
- Day 1: Build chatbot backend function (Base44) + WhatsApp Business setup<br/>
- Day 2: Train on GlamDoor FAQ + partner data + Arabic prompts<br/>
- Day 3: Beta test with 5 friends (EN + AR) -> fix bugs -> go live<br/>
- Day 4+: Monitor, collect conversation logs, improve responses weekly<br/><br/>
<b>SUCCESS METRICS</b><br/>
- Bot conversation response time: < 3 seconds<br/>
- Booking conversion rate: > 15% (of bot conversations -> confirmed bookings)<br/>
- Language auto-detect accuracy: > 95%<br/>
- Customer satisfaction (post-chat rating): > 4/5<br/>
- Human handoff rate: < 20% (most queries resolved by bot)
"""
story.append(Paragraph(bot_text, body_style))
story.append(PageBreak())

# CHATBOT CONVERSATION EXAMPLES
story.append(Paragraph("CHATBOT CONVERSATION EXAMPLES (EN/AR)", heading_style))

story.append(Paragraph("EXAMPLE 1: English Booking", subheading_style))
story.append(Paragraph("Customer: Hi, I want to book a manicure in Dubai Marina for tomorrow afternoon", body_style))
story.append(Paragraph("Bot: Hi! I'd love to help you book a manicure in Marina. Do you have a preferred time? (e.g., 2 PM, 4 PM)", bot_style))
story.append(Paragraph("Customer: Around 4 PM", body_style))
story.append(Paragraph("Bot: I found 3 salons in Marina with manicure availability at 4 PM tomorrow:", bot_style))
story.append(Paragraph("1. Glow Beauty Lounge - AED 120 - 4.8 stars - Available 4:00 PM", bot_style))
story.append(Paragraph("2. Marina Nails Spa - AED 95 - 4.6 stars - Available 4:30 PM", bot_style))
story.append(Paragraph("3. The Nail Bar - AED 150 - 4.9 stars - Available 3:45 PM", bot_style))
story.append(Paragraph("Which one would you like? (Reply 1, 2, or 3)", bot_style))
story.append(Paragraph("Customer: 1", body_style))
story.append(Paragraph("Bot: Great choice! Glow Beauty Lounge at 4:00 PM tomorrow. What's your name and phone number?", bot_style))
story.append(Paragraph("Customer: Sara, 0501234567", body_style))
story.append(Paragraph("Bot: Booking confirmed! Glow Beauty Lounge, tomorrow 4:00 PM, Manicure - AED 120. You'll get a reminder 2 hours before. See you then! :)", bot_style))

story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("EXAMPLE 2: Arabic Booking", subheading_style))
story.append(Paragraph("Customer: Salam, abi ahjaz manakir fi Marina bacher alasr", body_style))
story.append(Paragraph("Bot: Ahlan wasahlan! haba asa3dik tihazeen manakir fi Marina. 3indik waqt mu'ayan? (masalan 4 alasr)", bot_style))
story.append(Paragraph("Customer: hawali 4 alasr", body_style))
story.append(Paragraph("Bot: laqayt 3 saloonat fi Marina 3indahum mawa3id l-manakir alsaa 4 alasr bacher:", bot_style))
story.append(Paragraph("1. Glow Beauty Lounge - 120 dirham - 4.8 stars - mutah 4:00", bot_style))
story.append(Paragraph("2. Marina Nails Spa - 95 dirham - 4.6 stars - mutah 4:30", bot_style))
story.append(Paragraph("3. The Nail Bar - 150 dirham - 4.9 stars - mutah 3:45", bot_style))
story.append(Paragraph("ay wahid takhtareen? (jawi 1, 2, aw 3)", bot_style))
story.append(Paragraph("Customer: 1", body_style))
story.append(Paragraph("Bot: mumtaz! Glow Beauty Lounge alsaa 4:00 alasr bacher, manakir b-120 dirham. shno ismik w raqmik?", bot_style))
story.append(Paragraph("Customer: Noura, 0567654321", body_style))
story.append(Paragraph("Bot: tam al-hajz! Glow Beauty Lounge, bacher 4:00 alasr, manakir - 120 dirham. binirsil lik tadhkir qabl sa'atayn. nilqakum! :)", bot_style))

story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("EXAMPLE 3: Support Inquiry (Mixed Language)", subheading_style))
story.append(Paragraph("Customer: Can I cancel my booking? abghi alghi al-hajz", body_style))
story.append(Paragraph("Bot: Sure! I can help with cancellation. What's your booking reference or phone number?", bot_style))
story.append(Paragraph("Customer: 0501234567", body_style))
story.append(Paragraph("Bot: Found your booking: Glow Beauty Lounge, tomorrow 4 PM, Manicure AED 120.", bot_style))
story.append(Paragraph("Bot: Would you like to cancel or reschedule? (Reply 'cancel' or 'reschedule')", bot_style))
story.append(Paragraph("Customer: reschedule", body_style))
story.append(Paragraph("Bot: No problem! What day and time works better for you?", bot_style))
story.append(Paragraph("Customer: Saturday 6 PM", body_style))
story.append(Paragraph("Bot: Done! Your booking is moved to Saturday 6:00 PM at Glow Beauty Lounge. New confirmation sent! :)", bot_style))

story.append(PageBreak())

# UPDATED PROJECT TIMELINE
story.append(Paragraph("UPDATED PROJECT TIMELINE (WITH AI CHATBOT)", heading_style))
timeline_data = [
    ['Phase', 'Week', 'Focus', 'Key Deliverable'],
    ['1. Launch', 'Week 1', 'First clients + momentum', '3+ bookings, 10+ partners, 50+ leads'],
    ['2. Chatbot', 'Week 1 (Day 3-4)', 'AI chatbot EN/AR live', 'Bot handling bookings + support 24/7'],
    ['3. Scale', 'Week 2', 'Expand zones + optimize', '20 partners, 15+ bookings, 2 new zones'],
    ['4. Automate', 'Week 3', 'Hire + automate', '50+ partners, partner manager hired'],
    ['5. Dominate', 'Week 4', 'Scale ad budget + referral', '200+ partners, referral automation'],
    ['6. Revenue', 'Month 2', 'Monetize + expand', 'AED 15K-25K/mo, Abu Dhabi launch'],
]
timeline_table = Table(timeline_data, colWidths=[1.2*inch, 1.3*inch, 1.8*inch, 2.3*inch])
timeline_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#8B4513')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 9),
    ('BOTTOMPADDING', (0,0), (-1,0), 10),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('FONTSIZE', (0,1), (-1,-1), 8),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BACKGROUND', (0,2), (-1,2), colors.HexColor('#E8F5E9')),
]))
story.append(timeline_table)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("CHATBOT DEVELOPMENT MILESTONES", subheading_style))
milestones_text = """
<b>Day 1 (Mon):</b> Build backend function (Base44) + Twilio WhatsApp setup + Cal.com integration<br/>
<b>Day 2 (Tue):</b> Write EN/AR prompt system, FAQ knowledge base, partner data sync<br/>
<b>Day 3 (Wed):</b> Beta test with 5 users (EN + AR), fix language detection bugs, optimize flow<br/>
<b>Day 4 (Thu):</b> Go live on WhatsApp Business + web widget on landing page<br/>
<b>Day 5 (Fri):</b> First bot-driven booking, monitor conversation logs, tune responses<br/>
<b>Day 7 (Sun):</b> Review bot metrics: conversion rate, response time, satisfaction, iterate
"""
story.append(Paragraph(milestones_text, body_style))
story.append(PageBreak())

# DAY-BY-DAY UPDATED
story.append(Paragraph("7-DAY ACTION BREAKDOWN (UPDATED WITH CHATBOT)", heading_style))
days = [
    ('DAY 1 (MONDAY) - SETUP & LAUNCH + CHATBOT BUILD', [
        'Scrape 50 salons + 30 home stylists (Google Business, Instagram #dubaistylists)',
        'Create WhatsApp Business account + template message',
        'Deploy landing page (Carrd/Framer) EN/AR, WhatsApp CTA, partner form',
        'NEW: Build chatbot backend function (Base44) + Twilio WhatsApp setup',
        'NEW: Connect Cal.com API for real-time booking availability',
        'Prep 7 Reels (before/after, partner spotlights, tips)',
        'Meta Ads: AED 200 budget, women 22-50, beauty/salons interests, pixel installed',
    ]),
    ('DAY 2 (TUESDAY) - PARTNER BLITZ + CHATBOT TRAINING', [
        'Message 50 salons: "Hi [Name], we connect customers with salons. Free 60 days. Chat?"',
        'Visit 5 salons in Marina in person (30-min pitch, offer founding partner badge)',
        'Post Reel 1 (team intro) + Carousel (3 salon spotlights)',
        'NEW: Write EN/AR chatbot prompts - FAQ, booking flow, support queries',
        'NEW: Sync partner database (salons, services, prices) to chatbot knowledge base',
        'Email 20 salons with Loom demo video + landing page link',
        'Log all replies in Airtable (name, contact, interest, follow-up date)',
    ]),
    ('DAY 3 (WEDNESDAY) - CUSTOMER ACQUISITION + CHATBOT BETA', [
        'NEW: Beta test chatbot with 5 friends (3 English, 2 Arabic) - test all flows',
        'NEW: Fix language detection bugs, optimize response speed < 3 sec',
        'DM 10 micro-influencers (5K-50K followers, Dubai beauty/lifestyle)',
        'Join 5 Facebook groups: Dubai Moms, Expats, Beauty. Post value (no hard sell)',
        'WhatsApp broadcast: "Book now & get AED 20. Refer friend, both get AED 20"',
        'Post Reel 2 (before/after testimonial) + 5 Stories (salon highlights, Q&A)',
        '2nd touch: Message 30 non-responders "Interested in free customer leads?"',
    ]),
    ('DAY 4 (THURSDAY) - CONTENT + CONVERSION + CHATBOT LIVE', [
        'NEW: Chatbot goes LIVE on WhatsApp Business + web widget on landing page',
        'NEW: Add chatbot CTA on landing page: "Chat with our AI assistant 24/7 EN/AR"',
        'Write 300-word SEO blog: "Top Salons in Dubai Marina for Nails/Hair/Skin"',
        'Create GlamDoor Google Business Profile, add partner listings',
        'Onboard 1st partner: profile, photos, WhatsApp chat, booking availability',
        'Post Reel 3 (meet the partner) + Carousel (5 partner photos + service tags)',
        'Email welcome to 20 sign-ups: video tour, FAQ, booking link',
    ]),
    ('DAY 5 (FRIDAY) - FIRST BOOKING TARGET + CHATBOT MONITORING', [
        'NEW: Monitor chatbot conversations - check conversion rate, fix dead-end flows',
        'NEW: First bot-driven booking target (bot handles entire flow end-to-end)',
        'WhatsApp broadcast (warm + email leads): "Book this weekend. AED 20 discount inside"',
        'Call 5 waitlist salons: confirm participation, offer free featured listing',
        'Meta Ads: pause underperformers, double budget on winners (best CPC leads)',
        'Post Reel 4 (customer success) + Story takeover (influencer books)',
        'TARGET: 1st confirmed booking end of day. Offer free service for testimonial',
    ]),
    ('DAY 6 (SATURDAY) - WEEKEND PUSH + CHATBOT OPTIMIZATION', [
        'NEW: Review bot conversation logs - identify top questions, add to FAQ',
        'NEW: Tune Arabic responses for local dialect (Khaleeji) accuracy',
        'Post in 3 Facebook groups: "Weekend vibes! Chat with our AI to book instantly"',
        'Email 5 co-working spaces (Nasab, AstroLabs): "Offer team 20% off. Partnership?"',
        'Capture video testimonial (30s) from first customer, publish same day',
        'Post Reel 5 (weekend glow-up) + Carousel (5 trending looks) + Stories',
        'Increase Meta budget 50% (AED 300 total), retarget landing page visitors',
    ]),
    ('DAY 7 (SUNDAY) - WEEK 1 SUMMARY + CHATBOT METRICS', [
        'NEW: Chatbot metrics review: conversations, booking conversion, language split, satisfaction',
        'NEW: Plan Week 2 bot upgrades: voice messages, Arabic dialect expansion, upsell flow',
        'Metrics review: count leads, partners, bookings, CPL, social reach',
        'Confirm 3-5 partners live with photos, pricing, bookings enabled',
        'Collect 2-3 video testimonials, publish as Reels',
        'Week 2 plan: double down on highest-ROI channel from this week',
        'Post Reel 6 (week recap) + thank you (tag influencers, partners, customers)',
    ]),
]
for day, actions in days:
    story.append(Paragraph(day, subheading_style))
    for action in actions:
        if action.startswith('NEW'):
            story.append(Paragraph(f"- {action}", bot_style))
        else:
            story.append(Paragraph(f"- {action}", body_style))
    story.append(Spacer(1, 0.1*inch))

story.append(PageBreak())

# AI AGENTS UPDATED
story.append(Paragraph("AI AGENTS FOR SCALE (SOCIAL + SEO + CHATBOT)", heading_style))
agents_text = """
<b>Agent 1: Content Creator Bot</b><br/>
Generate 3 Reel scripts daily. Tool: ChatGPT API (batch) + Canva auto-design + Make/Zapier auto-post<br/>
Output: 21 scripted Reels for Week 1<br/><br/>
<b>Agent 2: Zone-Based Outreach Bot</b><br/>
Write 5 WhatsApp messages per zone (personalized). Tool: ChatGPT<br/>
Output: 50+ copy-paste variations across Marina/Downtown/JVC<br/><br/>
<b>Agent 3: SEO Blog + Google Business Optimizer</b><br/>
Generate 300-word SEO posts: "Best Salons in [Zone] for [Service]". Tool: ChatGPT batch + WordPress auto-publish<br/>
Output: 20+ posts (4 zones x 5 services). Each links to partner profiles.<br/><br/>
<b>Agent 4: Email Drip Automation</b><br/>
Auto 5-email sequence to landing page visitors. Tool: Zapier + HubSpot/Mailchimp<br/>
Day 0: Welcome + demo | Day 2: Social proof | Day 4: Limited offer | Day 6: Referral | Day 8: Last chance<br/><br/>
<b>Agent 5: Influencer Manager</b><br/>
Generate personalized DM outreach (10 influencers). Tool: ChatGPT<br/>
Include: @ handle, specific post reference, offer (free service + AED 50 credit)<br/>
Output: 10 ready-to-send DMs (send manually for best open rates)<br/><br/>
<b>Agent 6: NEW - GlamDoor AI Chatbot (Booking + Support EN/AR)</b><br/>
24/7 WhatsApp + web widget chatbot handling bookings, support, lead capture<br/>
Tool: GPT-4o-mini + Twilio WhatsApp API + Cal.com + Base44 backend function<br/>
Features: Bilingual EN/AR auto-detect, smart booking, salon search, live agent handoff<br/>
Target: 70% reduction in manual replies, 15%+ booking conversion from bot conversations<br/>
Cost: ~AED 500/mo for up to 1,000 conversations
"""
story.append(Paragraph(agents_text, body_style))
story.append(PageBreak())

# SOCIAL CALENDAR UPDATED
story.append(Paragraph("7-DAY SOCIAL MEDIA CALENDAR", heading_style))
cal_data = [
    ['Day', 'Format', 'Theme', 'Time (GST)'],
    ['Monday', 'Carousel', 'Welcome + Salon Intro', '10 AM'],
    ['Tuesday', 'Reel', 'Partner Spotlight', '7 PM'],
    ['Wednesday', 'Carousel', 'Before/After (UGC)', '5 PM'],
    ['Thursday', 'Reel', 'Meet Our AI Assistant EN/AR', '8 PM'],
    ['Friday', 'Carousel', 'Weekend Specials', '6 PM'],
    ['Saturday', 'Reel', 'Customer Success Story', '5 PM'],
    ['Sunday', 'Carousel', 'Week Recap + Referral', '9 AM'],
]
cal_table = Table(cal_data, colWidths=[1*inch, 1.2*inch, 2.2*inch, 1.3*inch])
cal_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#8B4513')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 9),
    ('BOTTOMPADDING', (0,0), (-1,0), 10),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('FONTSIZE', (0,1), (-1,-1), 8),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BACKGROUND', (0,4), (-1,4), colors.HexColor('#E8F5E9')),
]))
story.append(cal_table)
story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("<b>Pro Tip:</b> Post each Reel/Carousel at scheduled time + reshare in Stories 4 hours later. Repost partner content 1x daily (tag them). <b>NEW:</b> Thursday Reel promotes the AI chatbot - 'Book any salon in 30 seconds, in Arabic or English!'", body_style))
story.append(PageBreak())

# LEAD GEN UPDATED
story.append(Paragraph("WEEK 1 LEAD GENERATION ROADMAP", heading_style))
channels_text = """
<b>Meta Ads (Instagram/Facebook):</b> AED 500 budget | Target: 25-30 leads | CPL target: AED 20-40 | Retarget landing page viewers 3x<br/><br/>
<b>NEW - AI Chatbot (WhatsApp + Web):</b> 24/7 availability | Target: 15-25 leads + 3-5 bookings | Auto-detects EN/AR | Books directly via Cal.com<br/><br/>
<b>Partner Outreach (WhatsApp/DM/Email):</b> 10 msgs/day | Target: 10-15 partner sign-ups | Offer: free listing + featured badge<br/><br/>
<b>Community Groups (Facebook):</b> Post 1-2x daily | Target: 10-15 leads | Join: Dubai Moms, Expats, Beauty groups | Share testimonials, not ads<br/><br/>
<b>Influencers (5K-50K followers):</b> DM 2-3 new ones daily | Target: 8-12 leads + brand buzz | Free bookings for 3-5 top influencers<br/><br/>
<b>Organic Social (Reels/Stories):</b> 1 Reel + 5 Stories daily | Target: 5-10 leads | Use trending audio + partner UGC<br/><br/>
<b>Email/SMS (Warm List):</b> 2 emails + 1 broadcast daily | Target: 3-5 leads | Segment: new visitors vs. repeat viewers<br/><br/>
<b>Google Business (Local SEO):</b> 1 daily post + reviews | Target: 2-5 local searches | Link from landing page to GBP profile<br/><br/>
<b>WEEK 1 TARGETS: 50-80 leads | 10-15 partners onboarded | 3-5 confirmed bookings (incl. bot-driven) | CPL < AED 40</b>
"""
story.append(Paragraph(channels_text, body_style))
story.append(PageBreak())

# METRICS UPDATED
story.append(Paragraph("METRICS TO TRACK DAILY", heading_style))
metrics_text = """
<b>LEAD FUNNEL:</b> Landing page visitors | WhatsApp inquiries | Email sign-ups | Booking page clicks | Confirmed bookings<br/><br/>
<b>NEW - CHATBOT METRICS:</b> Total conversations | Bot booking conversion rate (target > 15%) | EN vs AR split | Avg response time (target < 3 sec) | Satisfaction rating (target > 4/5) | Human handoff rate (target < 20%)<br/><br/>
<b>PARTNER FUNNEL:</b> Salons contacted | Response rate % | Onboarded (live) | Posted first availability<br/><br/>
<b>SOCIAL METRICS:</b> Reel reach/impressions (target: 5K+ per Reel by Day 5) | Engagement rate | Link clicks to landing page | Follower growth<br/><br/>
<b>AD METRICS (Meta):</b> Cost per lead (target: AED 20-40) | CPC | CTR % | Conversion rate | ROAS from bookings<br/><br/>
<b>SUCCESS CHECKLIST:</b><br/>
50+ leads | 10+ partners | 3+ bookings (1+ bot-driven) | CPL < AED 40 | Social reach > 50K | Chatbot live EN/AR by Day 4
"""
story.append(Paragraph(metrics_text, body_style))
story.append(PageBreak())

# TEMPLATES UPDATED
story.append(Paragraph("COPY-PASTE TEMPLATES", heading_style))
templates_text = """
<b>PARTNER OUTREACH - WhatsApp</b><br/>
"Hi [Salon Name] We're launching GlamDoor - connects customers with Dubai salons. FREE for 60 days (zero commission). Profile, bookings, WhatsApp chat, AI assistant, reviews all in one place. 5 min call? [Link]"<br/><br/>
<b>CUSTOMER EMAIL</b><br/>
"Subject: Book your first Dubai salon in 60 seconds<br/>
Hey [First Name], tired of calling, waiting, WhatsApp chats? GlamDoor = all salons in one app. Book, pay, rate instantly. Our AI assistant helps you book in Arabic or English - 24/7. First booking = AED 20 off (WELCOME20). [Link]"<br/><br/>
<b>INFLUENCER DM</b><br/>
"Hi [Name]! Obsessed with your post about [specific topic]. We just launched GlamDoor - easier way to book salons in Dubai. Our AI chatbot books you in 30 seconds, in Arabic or English! Would love to send you a free booking (your choice). If you like it, a quick Reel from you would be amazing. No payment, just content. LMK!"<br/><br/>
<b>REFERRAL BROADCAST</b><br/>
"NEW: Refer a friend to GlamDoor, get AED 20 credit each! Your friend books - You get AED 20 - They get AED 20 off first booking. Spread the glow. [Referral Link]"<br/><br/>
<b>NEW - CHATBOT PROMOTION (Instagram Story)</b><br/>
"Meet your new beauty concierge! Chat with our AI assistant 24/7 - book any salon in Dubai in 30 seconds. Arabic or English, we've got you. Try it now: [WhatsApp Link]"<br/>
"""
story.append(Paragraph(templates_text, body_style))
story.append(PageBreak())

# PITFALLS UPDATED
story.append(Paragraph("PITFALLS + QUICK WINS", heading_style))
pitfalls_text = """
<b>AVOID:</b><br/>
- Building a full app Week 1 (web + WhatsApp + chatbot is enough)<br/>
- Contacting all 100 salons at once (prioritize 50, nail it first)<br/>
- Posting generic content (use partner photos - authenticity wins)<br/>
- Tracking follower count over bookings<br/>
- Giving up after one "no" (follow up 2-3x minimum)<br/>
- Slow DM replies (bot handles 24/7, humans handle complex cases)<br/>
- NEW: Launching chatbot without testing (always beta test with 5 users first)<br/>
- NEW: Forgetting Arabic (50%+ of Dubai market speaks Arabic - bot must support it)<br/><br/>
<b>QUICK WINS:</b><br/>
- NEW: Chatbot live by Day 4 = 24/7 lead capture while you sleep<br/>
- NEW: Bot auto-collects reviews post-booking = free testimonials on autopilot<br/>
- Corporate Partnerships: Email 2-3 co-working spaces "Offer team 15% off beauty" = 10-20 bookings/month<br/>
- Partner Videos: Record 5x 30-sec salon videos (phone OK) as Reels = authentic, high engagement<br/>
- Review Capture: Collect 3-5 testimonials from first customers, screenshot + post<br/>
- WhatsApp List: Build 500+ broadcast list by Day 5 = owned channel (no algorithm)<br/>
- GBP Posts: Daily 1-liner update (free) = local search boost
"""
story.append(Paragraph(pitfalls_text, body_style))
story.append(Spacer(1, 0.2*inch))

# WEEK 2+ UPDATED
story.append(Paragraph("WEEK 2+ SCALE PREVIEW (WITH CHATBOT EVOLUTION)", heading_style))
week2_text = """
<b>Week 2:</b> 20 partners | 15+ bookings (5+ bot-driven) | Expand JVC + Al Barsha | Chatbot voice message support<br/>
<b>Week 3:</b> Hire 1 part-time partner manager (AED 3K/mo) | 50+ partners | 50+ bookings | Bot handles 80% of inquiries<br/>
<b>Week 4:</b> AED 5K/mo ad budget | Referral automation live | Expand Abu Dhabi | Bot upsell flow (add-ons during booking)<br/><br/>
<b>Month 2:</b> Bot feature: Arabic dialect expansion (Egyptian, Levantine) | Loyalty program integration | Partner analytics dashboard<br/><br/>
<b>Month 2 Revenue Target: AED 15K-25K/mo (10-20% commission + premium listings | 200+ partners | 300+ bookings | Chatbot handles 1,000+ conversations/mo</b>
"""
story.append(Paragraph(week2_text, body_style))
story.append(PageBreak())

# TOOLSTACK UPDATED
story.append(Paragraph("WEEK 1 TOOLSTACK", heading_style))
tools_text = """
<b>ESSENTIAL (Free/Cheap):</b><br/>
Landing Page: Carrd.co (AED 100/yr) or Framer free<br/>
Booking: Cal.com (free) | Email: Gmail/HubSpot free tier (500 contacts)<br/>
SMS/WhatsApp: Twilio (AED 0.50/msg) | Analytics: GA4 (free) + Sheets<br/>
Social: Buffer free tier (3 posts) | Design: Canva free + CapCut<br/><br/>
<b>NEW - AI CHATBOT STACK:</b><br/>
AI Engine: OpenAI GPT-4o-mini (~AED 300/mo API costs)<br/>
WhatsApp: Twilio WhatsApp Business API (~AED 200/mo for 1,000 msgs)<br/>
Web Widget: React embed on landing page (one-time build)<br/>
Booking Integration: Cal.com API (free)<br/>
Backend: Base44 serverless function (no server cost)<br/>
Total chatbot cost: ~AED 500/mo<br/><br/>
<b>NICE-TO-HAVE (AED 200-500/mo):</b><br/>
HubSpot Professional | Mailchimp (500+ contacts) | Adobe Creative Cloud<br/><br/>
<b>AI/AUTOMATION:</b><br/>
ChatGPT API (batch content) | Make.com or Zapier (automate posts/emails) | N8n (self-hosted, free)
"""
story.append(Paragraph(tools_text, body_style))
story.append(Spacer(1, 0.3*inch))

# FINAL CHECKLIST UPDATED
story.append(Paragraph("LAUNCH CHECKLIST (BEFORE MONDAY 9 AM) - UPDATED", heading_style))
checklist_text = """
<b>SETUP:</b><br/>
[ ] Landing page (EN/AR) live + WhatsApp CTA button tested<br/>
[ ] Google Business Profile created for GlamDoor<br/>
[ ] WhatsApp Business account active<br/>
[ ] Airtable/Google Sheets dashboard for lead logging<br/>
[ ] Meta Ads account set up, pixel installed<br/><br/>
<b>NEW - CHATBOT:</b><br/>
[ ] OpenAI API key set up + GPT-4o-mini access confirmed<br/>
[ ] Twilio WhatsApp Business API configured<br/>
[ ] Cal.com account + API key for booking integration<br/>
[ ] Base44 backend function for chatbot written + tested<br/>
[ ] EN/AR prompt system drafted (FAQ, booking, support)<br/>
[ ] 5 beta testers identified (3 EN, 2 AR)<br/>
[ ] Web widget code ready for landing page embed<br/><br/>
<b>CONTENT:</b><br/>
[ ] Content calendar scripted (7 Reels + 7 Carousels)<br/>
[ ] Partner list (80 salons + stylists) with contact info<br/>
[ ] Email templates finalized (3+ variations)<br/>
[ ] Loom demo video recorded (2 min)<br/>
[ ] Influencer list (10 micro-influencers) ready<br/><br/>
<b>DAILY RITUAL (5 MIN/MORNING):</b><br/>
[ ] Post 1 Reel + 1 Carousel [ ] Log yesterday's metrics [ ] Send 5-10 partner outreach [ ] Reply to DMs (< 1 hr) [ ] Check Meta Ads performance<br/>
[ ] NEW: Review chatbot conversation logs [ ] NEW: Check bot booking conversion rate<br/><br/>
<b>FINAL NOTE:</b> Week 1 is about momentum + the chatbot working 24/7 while you sleep. By Day 5, patterns emerge (best channels, partner types, conversion rates). Double winners, kill losers. <b>First booking + 3 partners + 50 leads + chatbot live EN/AR = WIN.</b><br/><br/>
<b>You've got this - Let's go!</b>
"""
story.append(Paragraph(checklist_text, body_style))

doc.build(story)
print("PDF created successfully!")
print("File: GlamDoor_Dubai_7Day_Mastermind_Plan.pdf")
