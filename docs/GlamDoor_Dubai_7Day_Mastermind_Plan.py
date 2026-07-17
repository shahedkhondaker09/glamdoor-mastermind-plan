# GlamDoor Dubai 7-Day Mastermind Plan - PDF Generator
# Run: python3 GlamDoor_Dubai_7Day_Mastermind_Plan.py
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

story.append(Paragraph("GlamDoor Dubai 7-Day Mastermind", title_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Week 1: Get First Clients & Build Momentum", subheading_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))
story.append(Paragraph("""
<b>Goal:</b> 50+ leads, 10+ partner sign-ups, 3+ confirmed bookings in 7 days<br/>
<b>Focus:</b> Dubai only (hyper-local: Marina, Downtown, JVC)<br/>
<b>Strategy:</b> Parallel outreach + daily content + zone-based targeting<br/>
<b>Cost:</b> AED 1,500-2,500 (ads + tools)<br/>
<b>Win Metric:</b> First booking confirmed by Day 5
""", body_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("DUBAI ZONES - PRIORITY TIERS", heading_style))
zones_data = [
    ['TIER 1 (High Priority)', 'TIER 2 (Medium)', 'TIER 3 (Week 2+)'],
    ['Marina | Downtown | Jumeirah', 'Deira | Al Barsha | Mirdif | Al Wasl', 'Sharjah | Abu Dhabi'],
    ['Affluent, expats, online-savvy, high spend', 'Growing income, strong communities', 'Scale after Dubai dominance']
]
zones_table = Table(zones_data, colWidths=[2.2*inch, 2.2*inch, 2.2*inch])
zones_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B4513')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
]))
story.append(zones_table)
story.append(Spacer(1, 0.3*inch))
story.append(PageBreak())

story.append(Paragraph("7-DAY ACTION BREAKDOWN", heading_style))
days = [
    ('DAY 1 (MONDAY) - SETUP & LAUNCH', [
        'Scrape 50 salons + 30 home stylists (Google Business, Instagram #dubaistylists)',
        'Create WhatsApp Business account + template message',
        'Deploy landing page (Carrd/Framer) EN/AR, WhatsApp CTA, partner form',
        'Prep 7 Reels (before/after, partner spotlights, tips)',
        'Meta Ads: AED 200 budget, women 22-50, beauty/salons interests, pixel installed',
    ]),
    ('DAY 2 (TUESDAY) - PARTNER BLITZ', [
        'Message 50 salons: "Hi [Name], we connect customers with salons. Free 60 days. Chat?"',
        'Visit 5 salons in Marina in person (30-min pitch, offer founding partner badge)',
        'Post Reel 1 (team intro) + Carousel (3 salon spotlights)',
        'Email 20 salons with Loom demo video + landing page link',
        'Log all replies in Airtable (name, contact, interest, follow-up date)',
    ]),
    ('DAY 3 (WEDNESDAY) - CUSTOMER ACQUISITION', [
        'DM 10 micro-influencers (5K-50K followers, Dubai beauty/lifestyle)',
        'Join 5 Facebook groups: Dubai Moms, Expats, Beauty. Post value (no hard sell)',
        'WhatsApp broadcast: "Book now & get AED 20. Refer friend, both get AED 20"',
        'Post Reel 2 (before/after testimonial) + 5 Stories (salon highlights, Q&A)',
        '2nd touch: Message 30 non-responders "Interested in free customer leads?"',
    ]),
    ('DAY 4 (THURSDAY) - CONTENT + CONVERSION', [
        'Write 300-word SEO blog: "Top Salons in Dubai Marina for Nails/Hair/Skin"',
        'Create GlamDoor Google Business Profile, add partner listings',
        'Onboard 1st partner: profile, photos, WhatsApp chat, booking availability',
        'Post Reel 3 (meet the partner) + Carousel (5 partner photos + service tags)',
        'Email welcome to 20 sign-ups: video tour, FAQ, booking link',
    ]),
    ('DAY 5 (FRIDAY) - FIRST BOOKING TARGET', [
        'WhatsApp broadcast (warm + email leads): "Book this weekend. AED 20 discount inside"',
        'Call 5 waitlist salons: confirm participation, offer free featured listing',
        'Meta Ads: pause underperformers, double budget on winners (best CPC leads)',
        'Post Reel 4 (customer success) + Story takeover (influencer books)',
        'TARGET: 1st confirmed booking end of day. Offer free service for testimonial',
    ]),
    ('DAY 6 (SATURDAY) - WEEKEND PUSH', [
        'Post in 3 Facebook groups: "Weekend vibes! Whos booking? Tag your salon"',
        'Email 5 co-working spaces (Nasab, AstroLabs): "Offer team 20% off. Partnership?"',
        'Capture video testimonial (30s) from first customer, publish same day',
        'Post Reel 5 (weekend glow-up) + Carousel (5 trending looks) + Stories',
        'Increase Meta budget 50% (AED 300 total), retarget landing page visitors',
    ]),
    ('DAY 7 (SUNDAY) - WEEK 1 SUMMARY', [
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
        story.append(Paragraph(f"- {action}", body_style))
    story.append(Spacer(1, 0.1*inch))
story.append(PageBreak())

story.append(Paragraph("AI AGENTS FOR SCALE (SOCIAL + SEO)", heading_style))
story.append(Paragraph("""
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
Output: 10 ready-to-send DMs (send manually for best open rates)
""", body_style))
story.append(PageBreak())

story.append(Paragraph("7-DAY SOCIAL MEDIA CALENDAR", heading_style))
cal_data = [
    ['Day', 'Format', 'Theme', 'Time (GST)'],
    ['Monday', 'Carousel', 'Welcome + Salon Intro', '10 AM'],
    ['Tuesday', 'Reel', 'Partner Spotlight', '7 PM'],
    ['Wednesday', 'Carousel', 'Before/After (UGC)', '5 PM'],
    ['Thursday', 'Reel', 'Booking Process 30s', '8 PM'],
    ['Friday', 'Carousel', 'Weekend Specials', '6 PM'],
    ['Saturday', 'Reel', 'Customer Success Story', '5 PM'],
    ['Sunday', 'Carousel', 'Week Recap + Referral', '9 AM'],
]
cal_table = Table(cal_data, colWidths=[1*inch, 1.2*inch, 2.2*inch, 1.3*inch])
cal_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B4513')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
]))
story.append(cal_table)
story.append(Spacer(1, 0.15*inch))
story.append(Paragraph("<b>Pro Tip:</b> Post each Reel/Carousel at scheduled time + reshare in Stories 4 hours later. Repost partner content 1x daily (tag them).", body_style))
story.append(PageBreak())

story.append(Paragraph("WEEK 1 LEAD GENERATION ROADMAP", heading_style))
story.append(Paragraph("""
<b>Meta Ads (Instagram/Facebook):</b> AED 500 budget | Target: 25-30 leads | CPL target: AED 20-40 | Retarget landing page viewers 3x<br/><br/>
<b>Partner Outreach (WhatsApp/DM/Email):</b> 10 msgs/day | Target: 10-15 partner sign-ups | Offer: free listing + featured badge<br/><br/>
<b>Community Groups (Facebook):</b> Post 1-2x daily | Target: 10-15 leads | Join: Dubai Moms, Expats, Beauty groups | Share testimonials, not ads<br/><br/>
<b>Influencers (5K-50K followers):</b> DM 2-3 new ones daily | Target: 8-12 leads + brand buzz | Free bookings for 3-5 top influencers<br/><br/>
<b>Organic Social (Reels/Stories):</b> 1 Reel + 5 Stories daily | Target: 5-10 leads | Use trending audio + partner UGC<br/><br/>
<b>Email/SMS (Warm List):</b> 2 emails + 1 broadcast daily | Target: 3-5 leads | Segment: new visitors vs. repeat viewers<br/><br/>
<b>Google Business (Local SEO):</b> 1 daily post + reviews | Target: 2-5 local searches | Link from landing page to GBP profile<br/><br/>
<b>WEEK 1 TARGETS: 50-80 leads | 10-15 partners onboarded | 3-5 confirmed bookings | CPL < AED 40</b>
""", body_style))
story.append(PageBreak())

story.append(Paragraph("METRICS TO TRACK DAILY", heading_style))
story.append(Paragraph("""
<b>LEAD FUNNEL:</b> Landing page visitors | WhatsApp inquiries | Email sign-ups | Booking page clicks | Confirmed bookings<br/><br/>
<b>PARTNER FUNNEL:</b> Salons contacted | Response rate % | Onboarded (live) | Posted first availability<br/><br/>
<b>SOCIAL METRICS:</b> Reel reach/impressions (target: 5K+ per Reel by Day 5) | Engagement rate | Link clicks to landing page | Follower growth<br/><br/>
<b>AD METRICS (Meta):</b> Cost per lead (target: AED 20-40) | CPC | CTR % | Conversion rate | ROAS from bookings<br/><br/>
<b>SUCCESS CHECKLIST:</b> 50+ leads | 10+ partners | 3+ bookings | CPL < AED 40 | Social reach > 50K
""", body_style))
story.append(PageBreak())

story.append(Paragraph("COPY-PASTE TEMPLATES", heading_style))
story.append(Paragraph("""
<b>PARTNER OUTREACH - WhatsApp</b><br/>
"Hi [Salon Name] We're launching GlamDoor - connects customers with Dubai salons. FREE for 60 days (zero commission). Profile, bookings, WhatsApp chat, reviews all in one place. 5 min call? [Link]"<br/><br/>
<b>CUSTOMER EMAIL</b><br/>
"Subject: Book your first Dubai salon in 60 seconds. Hey [First Name], tired of calling, waiting, WhatsApp chats? GlamDoor = all salons in one app. Book, pay, rate instantly. First booking = AED 20 off (WELCOME20). [Link]"<br/><br/>
<b>INFLUENCER DM</b><br/>
"Hi [Name]! Obsessed with your post about [specific topic]. We just launched GlamDoor - easier way to book salons in Dubai. Would love to send you a free booking (your choice). If you like it, a quick Reel from you would be amazing. No payment, just content. LMK!"<br/><br/>
<b>REFERRAL BROADCAST</b><br/>
"NEW: Refer a friend to GlamDoor, get AED 20 credit each! Your friend books - You get AED 20 - They get AED 20 off first booking. Spread the glow. [Referral Link]"
""", body_style))
story.append(PageBreak())

story.append(Paragraph("PITFALLS + QUICK WINS", heading_style))
story.append(Paragraph("""
<b>AVOID:</b><br/>
- Building an app Week 1 (web + WhatsApp is enough)<br/>
- Contacting all 100 salons at once (prioritize 50, nail it first)<br/>
- Posting generic content (use partner photos - authenticity wins)<br/>
- Tracking follower count over bookings<br/>
- Giving up after one "no" (follow up 2-3x minimum)<br/>
- Slow DM replies (respond within 1 hour)<br/><br/>
<b>QUICK WINS:</b><br/>
- Corporate Partnerships: Email 2-3 co-working spaces "Offer team 15% off beauty" = 10-20 bookings/month<br/>
- Partner Videos: Record 5x 30-sec salon videos (phone OK) as Reels = authentic, high engagement<br/>
- Review Capture: Collect 3-5 testimonials from first customers, screenshot + post<br/>
- WhatsApp List: Build 500+ broadcast list by Day 5 = owned channel (no algorithm)<br/>
- GBP Posts: Daily 1-liner update (free) = local search boost
""", body_style))
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("WEEK 2+ SCALE PREVIEW", heading_style))
story.append(Paragraph("""
<b>Week 2:</b> 20 partners | 15+ bookings | Expand JVC + Al Barsha (2 new zones)<br/>
<b>Week 3:</b> Hire 1 part-time partner manager (AED 3K/mo) | 50+ partners | 50+ bookings<br/>
<b>Week 4:</b> AED 5K/mo ad budget | Referral automation live | Expand Abu Dhabi<br/><br/>
<b>Month 2 Revenue Target: AED 15K-25K/mo (10-20% commission + premium listings | 200+ partners | 300+ bookings</b>
""", body_style))
story.append(PageBreak())

story.append(Paragraph("WEEK 1 TOOLSTACK", heading_style))
story.append(Paragraph("""
<b>ESSENTIAL (Free/Cheap):</b><br/>
Landing Page: Carrd.co (AED 100/yr) or Framer free<br/>
Booking: Cal.com (free) | Email: Gmail/HubSpot free tier (500 contacts)<br/>
SMS/WhatsApp: Twilio (AED 0.50/msg) | Analytics: GA4 (free) + Sheets<br/>
Social: Buffer free tier (3 posts) | Design: Canva free + CapCut<br/><br/>
<b>NICE-TO-HAVE (AED 200-500/mo):</b><br/>
HubSpot Professional | Mailchimp (500+ contacts) | Adobe Creative Cloud<br/><br/>
<b>AI/AUTOMATION:</b><br/>
ChatGPT API (batch content) | Make.com or Zapier (automate posts/emails) | N8n (self-hosted, free)
""", body_style))
story.append(Spacer(1, 0.3*inch))

story.append(Paragraph("LAUNCH CHECKLIST (BEFORE MONDAY 9 AM)", heading_style))
story.append(Paragraph("""
[ ] Landing page (EN/AR) live + WhatsApp CTA button tested<br/>
[ ] Google Business Profile created for GlamDoor<br/>
[ ] WhatsApp Business account active<br/>
[ ] Airtable/Google Sheets dashboard for lead logging<br/>
[ ] Content calendar scripted (7 Reels + 7 Carousels)<br/>
[ ] Partner list (80 salons + stylists) with contact info<br/>
[ ] Email templates finalized (3+ variations)<br/>
[ ] Meta Ads account set up, pixel installed<br/>
[ ] Loom demo video recorded (2 min)<br/>
[ ] Influencer list (10 micro-influencers) ready<br/><br/>
<b>DAILY RITUAL (5 MIN/MORNING):</b><br/>
[ ] Post 1 Reel + 1 Carousel [ ] Log yesterday's metrics [ ] Send 5-10 partner outreach [ ] Reply to DMs (< 1 hr) [ ] Check Meta Ads performance<br/><br/>
<b>FINAL NOTE:</b> Week 1 is about momentum, not perfection. By Day 5, patterns emerge (best channels, partner types, conversion rates). Double winners, kill losers. <b>First booking + 3 partners + 50 leads = WIN.</b>
""", body_style))

doc.build(story)
print("PDF created successfully!")
