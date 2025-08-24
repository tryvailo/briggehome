# CLAUDE PROMPT: HomeBridge Family Member Registration Interface

Create a complete, production-ready HTML page for HomeBridge family member registration. This is a 6-step wizard for adult children setting up AI health monitoring for their elderly parents.

## OVERALL DESIGN REQUIREMENTS

**Brand Identity:**
- Product name: HomeBridge
- Tagline: "AI Health Companion for Your Parents"
- Primary color: #4f46e5 (medical blue)
- Secondary color: #10b981 (success green)
- Error color: #ef4444
- Font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif

**Layout Philosophy:**
- Clean, professional medical-grade interface
- Warm, trustworthy design that reduces anxiety
- Progressive 6-step wizard with clear progress indication
- Mobile-first responsive design
- Touch targets minimum 44px
- Form validation with helpful, encouraging messages

## STEP-BY-STEP SPECIFICATIONS

### STEP 1: FAMILY REGISTRATION
**Header Section:**
- Large H1: "Welcome to HomeBridge"
- Subtitle: "Set up AI health monitoring for your parents in under 5 minutes"
- Progress indicator: Step 1 of 6

**Trust Indicators (top right):**
- "NHS-compliant security" badge
- "GDPR protected" badge
- "Used by 10,000+ families" social proof

**Main Form:**
- Email address field (with real-time validation)
- Full name field
- Phone number field (international format with country selector)
- Relationship dropdown: "Son", "Daughter", "Spouse", "Other family member"

**GDPR Consent Section:**
- Checkbox: "I consent to processing health data for family care monitoring"
- Checkbox: "I understand my data rights and privacy protections"  
- Links: "Privacy Policy" and "Terms of Service" (open in new tab)
- Small text: "You can withdraw consent anytime from your dashboard"

**Action Button:**
- Large button: "Create Family Account"
- Loading state: "Creating your account..."
- Below button: "Already have an account? Sign in"

### STEP 2: PARENT PROFILE SETUP
**Header:**
- H1: "Tell us about [Parent Name]" (use name from previous step)
- Progress indicator: Step 2 of 6
- Back button to previous step

**Required Fields:**
- Parent's full name (large input field)
- Age (visual slider from 60-100 with number display)
- Phone number (with validation for UK/international numbers)
- Preferred language dropdown: "English", "Welsh", "Other"

**Optional Details (Collapsible Section - "More details (optional)"):**
- Medical conditions (searchable multi-select dropdown with common conditions)
- Current medications (free text area with placeholder: "e.g., Blood pressure medication, vitamins...")
- Emergency contact name and phone
- Best time for daily check-ins (time picker)

**Tech Skills Assessment:**
- Header: "How comfortable is [Parent Name] with technology?"
- Four large visual cards (radio button selection):
  1. "Uses smartphone daily" (smartphone icon, green border)
  2. "Occasionally uses smartphone" (phone icon, yellow border)  
  3. "Prefers phone calls" (landline icon, orange border)
  4. "Needs help with technology" (helping hands icon, red border)

**Action Buttons:**
- "Continue to Platform Selection" (primary)
- "Back" (secondary)

### STEP 3: TECHNOLOGY SELECTION
**Header:**
- H1: "How should HomeBridge connect with [Parent Name]?"
- Subtitle: "Based on their tech comfort level, we recommend:"
- Progress indicator: Step 3 of 6

**Platform Cards (show recommendation badges based on step 2 selection):**

**Card 1: WhatsApp Bot**
- Icon: WhatsApp logo
- Badge: "Recommended" (if smartphone user)
- Header: "WhatsApp Messages"
- Difficulty: 2/5 stars
- Setup time: "5 minutes"
- Description: "Daily health conversations through familiar WhatsApp chat"
- Best for: "Parents who already use WhatsApp"
- Preview: Mock WhatsApp conversation screenshot

**Card 2: Website Link**
- Icon: Globe/computer
- Header: "Simple Website"  
- Difficulty: 2/5 stars
- Setup time: "3 minutes"
- Description: "Click a link to start talking with AI health companion"
- Best for: "Parents who browse the internet occasionally"
- Preview: Mock website interface

**Card 3: Email Links**
- Icon: Email envelope
- Badge: "Easiest" 
- Header: "Magic Email Links"
- Difficulty: 1/5 stars
- Setup time: "2 minutes"
- Description: "Daily email with button to start health conversation"
- Best for: "Parents who check email regularly"
- Preview: Mock email with large button

**Card 4: Phone Calls**
- Icon: Traditional phone
- Badge: "Most familiar"
- Header: "AI Phone Calls"
- Difficulty: 1/5 stars
- Setup time: "1 minute"
- Description: "HomeBridge calls your parent directly for health check-ins"
- Best for: "Parents who prefer traditional phone conversations"
- Cost note: "Higher monthly cost due to phone charges"

**Smart Recommendation:**
- Toggle switch: "Let HomeBridge choose automatically" (enabled by default)
- Explanation text based on tech skills assessment
- Override option: "I know what's best for my parent"

**Action Buttons:**
- "Continue to Security Setup" (primary)
- "Back to Parent Profile" (secondary)

### STEP 4: AUTHENTICATION METHOD
**Header:**
- H1: "How will [Parent Name] sign in securely?"
- Subtitle: "We'll set this up together to keep their health data safe"
- Progress indicator: Step 4 of 6

**Authentication Cards (show only compatible methods based on platform selection):**

**PIN Code Method:**
- Icon: Keypad
- Header: "4-Digit PIN Code"
- Security level: 3/5 shields
- Description: "You create a simple 4-digit code that [Parent Name] enters"
- Setup process: "1. You choose PIN → 2. We teach them → 3. Daily sign-in takes 10 seconds"
- Family control: "You can reset the PIN anytime from your dashboard"
- Preview: Mock PIN entry screen

**Voice Recognition Method:**
- Icon: Microphone  
- Header: "Voice Recognition"
- Security level: 4/5 shields
- Description: "AI learns [Parent Name]'s voice for automatic sign-in"
- Setup process: "1. Record voice samples → 2. AI learns patterns → 3. Just say 'Hello HomeBridge'"
- Backup: "PIN code backup if voice not recognized"
- Preview: Mock voice setup screen

**Magic Links Method:**
- Icon: Magic wand + link
- Header: "Magic Email Links"
- Security level: 5/5 shields  
- Description: "Secure links that work for 4 hours, no passwords needed"
- Setup process: "1. We email secure link → 2. [Parent Name] clicks → 3. Automatic sign-in"
- Family control: "You get notified when links are used"
- Preview: Mock secure email

**Backup Methods Section:**
- Header: "What if the main method doesn't work?"
- Checkbox options for backup methods
- "Family emergency access" - explanation of how family can help remotely

**Action Buttons:**
- "Continue to Send Invitation" (primary)
- "Back to Platform Selection" (secondary)

### STEP 5: SEND INVITATION
**Header:**
- H1: "Ready to invite [Parent Name]!"
- Subtitle: "Preview what they'll experience, then send the invitation"
- Progress indicator: Step 5 of 6

**Setup Summary Card:**
- Platform: [Selected platform with icon]
- Authentication: [Selected method with security level]
- Daily check-in time: [Selected time]
- Emergency contact: [Family member contact]
- "Change any of these" link

**Parent Experience Preview:**
- Header: "Here's what [Parent Name] will see:"
- Mock-up of their first experience based on selections
- For WhatsApp: Mock conversation flow
- For Email: Mock email and website interface
- For Phone: Mock call flow description

**Personalized Invitation Message (Editable Text Area):**
Default message:
"Hi [Parent Name],

I've set up HomeBridge to help keep track of your health and make sure you're doing well. It's like having a caring nurse check in with you daily.

HomeBridge will [description based on platform selection]. It only takes a few minutes each day, and it helps me worry less about you while keeping you independent.

I'll help you get started when you're ready.

Love,
[Family member name]"

**Delivery Method Selection:**
- Multiple checkboxes (can select multiple):
  - WhatsApp message (if parent has WhatsApp)
  - SMS text message  
  - Email
  - Printed instructions (generates PDF)
- Phone number/email fields auto-filled from previous steps
- "Send a test to myself first" checkbox

**Delivery Timing:**
- Radio buttons: "Send now", "Send later" (with date/time picker)
- "I'll deliver this myself in person" option

**Action Buttons:**
- "Send Invitation" (primary, with loading state)
- "Back to Authentication" (secondary)

### STEP 6: SETUP COMPLETE
**Success Celebration:**
- Large checkmark icon
- H1: "Setup Complete! 🎉"
- Subtitle: "HomeBridge is ready to care for [Parent Name]"

**What Happens Next Timeline:**
1. "[Parent Name] receives invitation within 5 minutes"
2. "You help them with first sign-in (we'll guide you)"  
3. "Daily health conversations begin"
4. "You receive weekly health insights"
5. "Emergency alerts if needed"

**Immediate Actions:**
- Large card: "Help [Parent Name] Get Started"
  - "Download setup guide" (PDF with screenshots)
  - "Schedule video call for setup help"
  - "Call our family support line: 0800-HOMEBRIDGE"

**Family Dashboard Preview:**
- "Your Family Dashboard is ready" 
- Screenshot of dashboard interface
- "Manage settings, view reports, get support"
- "Access Dashboard" button

**Support Information:**
- "Questions? We're here to help"
- Email: support@homebridge.health
- Phone: 0800-HOMEBRIDGE (free from UK)
- "Average response time: 2 hours"
- "Family setup success rate: 94%"

**Final Actions:**
- "Go to Family Dashboard" (primary button)
- "Send another invitation" (secondary)
- "Download mobile app" (optional)

## TECHNICAL IMPLEMENTATION REQUIREMENTS

**HTML Structure:**
- Semantic HTML5 with proper ARIA labels
- Form elements with proper validation attributes
- Progressive enhancement (works without JavaScript)
- Clean, readable code structure

**CSS Requirements:**
- Mobile-first responsive design
- CSS Grid/Flexbox for layouts
- Smooth transitions between steps (0.3s ease)
- Focus indicators for keyboard navigation
- High contrast mode support
- Print-friendly styles for PDF generation

**JavaScript Functionality:**
- Form validation with real-time feedback
- Progress saving to localStorage
- Smooth step transitions
- Auto-save form data every 30 seconds
- Client-side validation before submission
- Loading states for all async operations
- Error handling with user-friendly messages

**Accessibility Requirements:**
- WCAG 2.1 AA compliance
- Screen reader optimization
- Keyboard navigation support
- High contrast ratios (4.5:1 minimum)
- Focus management between steps
- Alternative text for all images
- Form labels and descriptions

**Performance Considerations:**
- Minimal external dependencies
- Optimized images and icons
- Fast loading on 3G connections
- Offline capability for form completion
- Error recovery from network issues

**Browser Support:**
- Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- Mobile browsers: iOS Safari, Android Chrome
- Graceful degradation for older browsers

Please implement this as a complete, single HTML file with embedded CSS and JavaScript. Include placeholder API calls for form submission and add detailed comments explaining the implementation approach for each section.