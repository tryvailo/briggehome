# CLAUDE PROMPT: HomeBridge Elderly Daily Application Interface

Create a complete, production-ready HTML page for the HomeBridge elderly daily application. This is the primary interface elderly users (65+) interact with for daily health conversations and family communication.

## CRITICAL ELDERLY-FIRST DESIGN PRINCIPLES

**Simplicity Above All:**
- ONE primary action per screen maximum
- Extra large text: 28px minimum body, 48px+ headers, 56px+ critical buttons
- High contrast: Black text (#000000) on white (#ffffff) background
- Zero cognitive load - no decisions, just simple responses
- Warm, encouraging, patient tone in all interactions
- Family presence felt throughout the experience

**Accessibility Beyond Standards:**
- Touch targets: 80px minimum (elderly-optimized)
- High contrast ratios: 8:1 minimum (exceeds WCAG AAA)
- Voice-first interaction with visual backup
- Audio feedback for every action
- Simple, predictable navigation patterns
- Emergency help always one touch away

## SCREEN-BY-SCREEN SPECIFICATIONS

### SCREEN 1: DAILY WELCOME
**Layout: Single-column, centered content**

**Header Section:**
- Current date and time: "Tuesday, August 22, 2025, 2:40 PM" (32px font)
- Weather widget: Large weather icon + temperature + simple description
- Personal greeting: "Good afternoon, [Parent Name]!" (48px, bold)

**Family Context Panel:**
- Family member photo (150px × 150px, rounded)
- Message: "[Child Name] is thinking of you today" (28px)
- Secondary message: "Your AI health companion is ready to chat" (24px)
- Family contact: "Need help? Tap to call [Child Name]" (large button)

**Daily Health Check Invitation:**
- Large central message: "Ready for today's health chat?" (40px)
- Explanation: "Just like talking to a caring nurse - it only takes 5 minutes"
- Huge start button (300px width × 120px height):
  - Text: "🎤 Start Today's Chat" (36px font)
  - Background: #4f46e5 (HomeBridge blue)
  - Prominent border and shadow

**Status Indicators (bottom):**
- "Today: Not completed" or "Today: ✅ Completed at 10:30 AM"
- "Your family will receive a summary tomorrow morning"
- Battery level (if mobile) and connection status

**Emergency Section (always visible):**
- Large red button: "🚨 Emergency Help" (fixed position)
- Quick family call: "📞 Call [Child Name]" (always accessible)

### SCREEN 2: VOICE CONVERSATION INTERFACE
**Main Conversation Area:**

**AI Companion Section:**
- Large, friendly AI avatar (200px) with simple animated states:
  - Listening: Gentle pulsing animation
  - Thinking: Subtle processing animation  
  - Speaking: Sound wave animation
- AI name display: "HomeBridge" (40px, prominent)
- Status indicator: "Listening..." / "Thinking..." / "Speaking..." (32px)

**Conversation Display:**
- Large speech bubbles with generous padding
- AI messages (left side): Light blue background (#e6f3ff)
- User messages (right side): Light gray background (#f5f5f5)
- Font size: 28px for all conversation text
- Line height: 1.6 for easy reading
- Clear timestamps: "Just now", "2 minutes ago"

**User Response Interface:**
- Massive microphone button (400px diameter on desktop, 300px on mobile)
- Visual states:
  - Ready: Blue background with microphone icon
  - Listening: Red background with pulsing animation
  - Processing: Yellow background with loading spinner
- Button text: "🎤 Tap to Talk" (32px font)
- Audio level indicator: Simple volume bars when recording

**Conversation Support:**
- "🔄 Say that again" button (if AI didn't understand clearly)
- "⌨️ Type instead" option (large button, for users who prefer typing)
- "✅ I'm finished talking" button (to end conversation gracefully)
- "❓ I need help" button (connects to family or support)

**Progress Indicators:**
- Simple progress bar: "Question 2 of 5" (visual and text)
- Encouraging messages: "You're doing great!", "Almost done!"
- Time estimate: "About 3 more minutes"

### SCREEN 3: HEALTH CHECK-IN SPECIFICS
**Visual Health Scales:**

**Pain Assessment:**
- Large visual pain scale (1-10) with emoji faces
- Each number is 60px × 60px touch target
- Clear labels: "No pain" (1) to "Worst pain" (10)
- Voice instruction: "Tap the number or say how much pain you have"

**Mood Selection:**
- Large emoji mood scale with descriptive text:
  😢 Very sad / 😕 Sad / 😐 Okay / 😊 Good / 😄 Very happy
- Each emoji: 80px × 80px touch target
- Voice option: "Say how you're feeling today"

**Sleep Quality:**
- Simple 3-option selection:
  - 😴 "Slept well" (green background)
  - 😪 "Some trouble sleeping" (yellow background)
  - 😵 "Poor sleep" (orange background)
- Large buttons (200px width each)

**Energy Level:**
- Visual battery indicator (1-5 bars)
- Touch to select or voice: "How much energy do you have?"
- Clear labels: "Very tired" to "Full of energy"

**Medication Confirmation:**
- Simple yes/no questions with large buttons:
  - "Did you take your morning medications?" YES / NO (150px buttons)
  - Photo reminders of medication containers
  - "Set reminder for later" option if not taken

### SCREEN 4: FAMILY MESSAGES
**Family Communication Center:**

**Incoming Messages:**
- Family member photos with message previews
- Voice message support: Large play buttons (80px)
- Visual voice message indicator: audio waveform
- Auto-transcription of voice messages (large text)
- "Reply to [Child Name]" large button

**Quick Responses:**
- Pre-written response templates:
  - "I'm doing well, love you!"
  - "Thank you for thinking of me"
  - "Please call me when you can"
  - "Everything is fine here"
- Each template: Large button (250px width)
- Option to record custom voice reply

**Family Status Updates:**
- Recent family member activities
- Grandchildren photos and updates
- Upcoming family events or calls
- "Call family now" prominent button

**Photo Sharing:**
- Simple camera interface: "📷 Take photo for family"
- Gallery of recent family photos shared with user
- Large thumbnail views (150px × 150px)
- "Share with family" one-touch option

### SCREEN 5: EMERGENCY HELP
**Emergency Interface Design:**
- Large red background for urgency recognition
- Minimal options to prevent confusion during crisis

**Emergency Actions:**
- "🚨 Call Emergency Services" (huge button, red)
- "📞 Call [Primary Family Member]" (large button, blue)
- "📞 Call [Secondary Family Member]" (large button, blue)
- "📍 Share my location" (automatic with calls)
- "📋 Show my medical information" (displays on screen)

**Medical Information Display:**
- Large, clear text showing:
  - Current medications
  - Medical conditions
  - Allergies
  - Doctor contact information
  - Emergency contacts
- "Read this information aloud" voice button

**Quick Medical Questions:**
- "Are you hurt?" YES / NO (huge buttons)
- "Can you move?" YES / NO
- "Are you having chest pain?" YES / NO
- "Are you having trouble breathing?" YES / NO
- Responses automatically shared with emergency contacts

### SCREEN 6: SIMPLE SETTINGS
**Large Setting Controls:**

**Volume Controls:**
- Large volume slider with + and - buttons (80px each)
- Voice test: "🔊 Test volume level" button
- "Make everything louder" / "Make everything quieter" simple options

**Text Size Adjustment:**
- Three simple options with preview text:
  - "Large text" (current: 28px)
  - "Extra large text" (36px)
  - "Huge text" (44px)
- Live preview showing sample text at each size

**Family Contact Management:**
- "📞 Change main family contact" with photo selection
- "Add emergency contact" simple form
- "Test emergency call" button (calls family to verify)

**Platform Preferences:**
- Current connection method display: "WhatsApp" or "Website" etc.
- "Change how HomeBridge contacts me" button (requires family assistance)
- "Get help from family with settings" prominent button

### SCREEN 7: WEEKLY CELEBRATION & ENCOURAGEMENT
**Success Celebration Interface:**

**Achievement Display:**
- Large celebration graphics: 🎉 "Great Week!" 
- Health achievements: "7 days of health check-ins completed!"
- Positive progress highlights: "Your mood improved this week!"
- Family appreciation: "Your family is proud of you!"

**Simple Health Summary:**
- Visual progress indicators (green progress bars)
- "This week you..." achievements:
  - "Talked to HomeBridge 6 out of 7 days"
  - "Reported feeling good 4 days"
  - "Connected with family 3 times"
- Large "👍 Keep up the great work!" message

**Family Pride Messages:**
- Recorded messages from family members celebrating progress
- Photos from family with encouraging text
- "Your [grandson/granddaughter] is proud of you!"
- Audio recordings: "Play message from [Child Name]"

**Next Week Encouragement:**
- "Ready for another healthy week?" invitation
- Simple goal setting: "This week, try to chat every day"
- "Your family will see your progress" motivation
- "Continue your great health journey" button

## TECHNICAL IMPLEMENTATION REQUIREMENTS

### ELDERLY-OPTIMIZED TECHNICAL SPECIFICATIONS

**Font and Typography:**
- Base font size: 28px minimum (not 16px standard)
- Headers: 48px minimum, 56px for critical actions
- Line height: 1.8 for easier reading
- Letter spacing: 0.1em for character clarity
- Font weight: 600 (semi-bold) for better visibility
- No italic text (harder to read for elderly)

**Color and Contrast:**
- Primary text: #000000 (pure black for maximum contrast)
- Background: #ffffff (pure white)
- Accent color: #4f46e5 (HomeBridge blue) - only for buttons
- Success: #00aa00 (high contrast green)
- Warning: #ff6600 (high contrast orange)  
- Error: #cc0000 (high contrast red)
- All combinations must exceed 8:1 contrast ratio

**Touch and Interaction:**
- Minimum touch target: 80px × 80px (elderly-optimized)
- Ideal touch target: 100px × 100px for primary actions
- Button padding: 20px minimum all sides
- Clear spacing: 40px between interactive elements
- No hover states (confusing on touch devices)
- Clear pressed/active states with immediate visual feedback

**Voice Integration Requirements:**
- Web Speech API integration with fallbacks
- Large, clear visual feedback during voice recognition
- Auto-timeout after 10 seconds of silence
- Clear error messages: "I didn't hear you, please try again"
- Voice playback controls with large buttons (play/pause/stop)
- Volume controls easily accessible
- Background noise cancellation if possible

**Navigation Simplification:**
- Linear navigation only (no complex menus)
- Large "Back" button on every screen (except home)
- Breadcrumb trail with large text: "Home > Health Check"
- No hamburger menus or hidden navigation
- Clear "Home" button always visible
- Swipe gestures disabled (prevent accidental navigation)

**Error Handling for Elderly:**
- No technical error messages ever
- All errors explained in warm, simple language
- Multiple recovery options provided
- "Get help from family" option on every error
- Automatic retry mechanisms
- Clear "start over" options that don't lose progress

**Performance Optimizations:**
- Fast loading on older devices (iPhone 8+, Android 8+)
- Minimal animations (some elderly users find them distracting)
- Large image compression for family photos
- Offline functionality for core features
- Clear loading indicators with progress percentages
- Battery usage optimization

**Emergency Features:**
- One-touch emergency calling (no confirmation dialogs)
- GPS location sharing automatic with emergency calls
- Medical information immediately accessible
- Emergency contacts stored locally for offline access
- Panic button accessible from any screen
- Family notification system for all emergency activations

### FAMILY INTEGRATION FEATURES

**Seamless Family Connection:**
- Real-time family member activity indicators
- Shared photo galleries with automatic syncing
- Voice message exchange with easy playback
- Family calendar integration for appointments
- Celebration sharing (achievements sent to family)
- Emergency notification system to all family members

**Privacy Controls (Simple):**
- "Share health summary with family" YES/NO toggle
- "Allow family to see my conversations" YES/NO toggle
- "Emergency override" (family can access during emergencies)
- Clear explanations of what data is shared
- "Ask [Child Name] about privacy settings" help option

Please implement this as a complete HTML page optimized specifically for elderly users. Include realistic conversation examples, working voice interface mockups, and extensive accessibility features. Add detailed comments explaining all elderly-specific design decisions and accessibility implementations. Ensure emergency features are prominently accessible and family integration feels natural and supportive.