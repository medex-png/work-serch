# Examples

This directory contains sample files to help you understand how the CV Optimization AI Agent works.

## Files

### sample_cv.txt
A sample CV with common issues that job seekers make:
- ❌ Weak phrases ("responsible for", "worked on")
- ❌ Lack of quantification (no numbers or metrics)
- ❌ ATS-unfriendly formatting (special bullet points)
- ❌ Missing strong action verbs
- ❌ Too brief descriptions

### job_description.txt
An example job description for a Senior Software Engineer position. Used to demonstrate keyword matching and job-specific optimization.

## Try It Yourself

### Basic Analysis
```bash
python3 ../agent.py sample_cv.txt
```

### With Job Description Matching
```bash
python3 ../agent.py sample_cv.txt --job-description job_description.txt
```

### Full Analysis with Industry/Role
```bash
python3 ../agent.py sample_cv.txt \
  --job-description job_description.txt \
  --role "Senior Software Engineer" \
  --industry software
```

### Generate Optimized Version
```bash
python3 ../agent.py sample_cv.txt \
  --job-description job_description.txt \
  --role "Senior Software Engineer" \
  --industry software \
  --output optimized_cv.txt
```

## Before & After Examples

### Example 1: Weak Phrase → Strong Action Verb

**Before:**
```
• Responsible for developing web applications
```

**After:**
```
• Developed and deployed 5+ scalable web applications serving 10K+ users
```

**What Changed:**
- ❌ "Responsible for" → ✅ "Developed and deployed"
- Added quantification (5+ applications)
- Added impact metric (10K+ users)

---

### Example 2: Vague Description → Quantified Achievement

**Before:**
```
• Worked on various projects for clients
```

**After:**
```
• Led development of 12+ client projects, consistently delivering within budget and ahead of schedule
```

**What Changed:**
- ❌ "Worked on" → ✅ "Led development of"
- Added specific number (12+ projects)
- Added outcome (within budget, ahead of schedule)

---

### Example 3: Missing Impact → Results-Oriented

**Before:**
```
• Helped with bug fixes and maintenance
```

**After:**
```
• Resolved 150+ critical bugs and reduced system downtime by 40% through proactive maintenance
```

**What Changed:**
- ❌ "Helped with" → ✅ "Resolved"
- Quantified work (150+ bugs)
- Added measurable impact (40% reduction in downtime)

---

### Example 4: Passive Voice → Active Achievement

**Before:**
```
• Participated in team meetings
```

**After:**
```
• Collaborated with cross-functional teams of 8+ members to align on technical roadmap and sprint priorities
```

**What Changed:**
- ❌ "Participated in" → ✅ "Collaborated with"
- Added context (cross-functional, 8+ members)
- Added purpose (technical roadmap, sprint priorities)

---

### Example 5: Role Description → Summary with Impact

**Before:**
```
OBJECTIVE
Looking for a software developer position where I can use my skills.
```

**After:**
```
PROFESSIONAL SUMMARY
Results-driven Software Engineer with 5+ years of experience building scalable web applications. 
Proven track record of delivering high-quality solutions using Python, JavaScript, and cloud 
technologies. Successfully led projects that improved system performance by 40% and reduced 
operational costs by $200K annually.
```

**What Changed:**
- ❌ Generic objective → ✅ Specific professional summary
- Added experience level (5+ years)
- Included key technologies
- Highlighted quantified achievements
- Shows impact and value

---

## Key Takeaways

When optimizing your CV:

1. **Use Strong Action Verbs**
   - ✅ Led, Developed, Implemented, Achieved, Managed
   - ❌ Responsible for, Worked on, Helped with

2. **Quantify Everything**
   - Add numbers: 5+ projects, 150 bugs, 10K users
   - Add percentages: 40% improvement, 25% reduction
   - Add dollar amounts: $200K savings, $2M in revenue

3. **Show Impact**
   - Don't just list tasks
   - Explain the result of your work
   - Focus on business value

4. **Be Specific**
   - ❌ "Various projects" → ✅ "12+ client projects"
   - ❌ "Team meetings" → ✅ "Cross-functional teams of 8+ members"
   - ❌ "Maintenance" → ✅ "Reduced downtime by 40%"

5. **Tailor to Job Description**
   - Mirror keywords from the posting
   - Highlight relevant skills
   - Match the tone and style

## Test Different Scenarios

### Scenario 1: Entry Level (0-2 years)
- Focus on: Education, internships, projects, coursework
- Emphasize: Technical skills, eagerness to learn, academic achievements
- Length: 1 page

### Scenario 2: Mid-Level (3-7 years)
- Focus on: Professional experience, key achievements, skills
- Emphasize: Results, leadership potential, technical expertise
- Length: 1-2 pages

### Scenario 3: Senior Level (8+ years)
- Focus on: Leadership, strategic impact, major projects
- Emphasize: Team management, business results, industry expertise
- Length: 2 pages

### Scenario 4: Career Change
- Focus on: Transferable skills, relevant projects, new skills learned
- Emphasize: Adaptability, quick learning, relevant achievements
- Reorganize sections to highlight relevant experience first

## Need Help?

Run the agent with tips:
```bash
python3 ../agent.py --tips ats        # ATS optimization tips
python3 ../agent.py --tips keywords   # Keyword tips
python3 ../agent.py --tips content    # Content writing tips
python3 ../agent.py --tips formatting # Formatting tips
python3 ../agent.py --tips general    # General best practices
```
