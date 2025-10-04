# Quick Start Guide - CV Optimization AI Agent

Get your CV analyzed and optimized in under 5 minutes!

## 🚀 1-Minute Setup

No installation required! Just have Python 3.7+ installed.

```bash
# Clone the repository
git clone https://github.com/medex-png/work-serch.git
cd work-serch

# You're ready to go!
```

## 🎯 Your First Analysis (30 seconds)

Try it with our sample CV:

```bash
python3 agent.py examples/sample_cv.txt
```

You'll immediately see:
- ✅ Overall quality score
- ✅ ATS compatibility score
- ✅ Strengths and weaknesses
- ✅ Actionable recommendations

## 💪 Analyze Your Own CV (2 minutes)

### Step 1: Prepare Your CV
Save your CV as a plain text file (`.txt`). You can:
- Copy-paste your CV into a text editor
- Export from Word: File → Save As → Plain Text (.txt)
- Use any text extraction tool

### Step 2: Run the Analysis
```bash
python3 agent.py /path/to/your_cv.txt
```

### Step 3: Review Results
The agent will show you:
1. **Scores** - How good is your CV? (0-100)
2. **Strengths** - What you're doing right
3. **Weaknesses** - What needs work
4. **Recommendations** - Specific actions to take
5. **Next Steps** - Prioritized improvement plan

## 🎓 Level Up: Match a Job Description (5 minutes)

For best results, analyze against a specific job posting:

### Step 1: Save the Job Description
Copy the job posting text and save it as `job.txt`

### Step 2: Run Enhanced Analysis
```bash
python3 agent.py your_cv.txt \
  --job-description job.txt \
  --role "Your Target Role" \
  --industry "your_industry"
```

Example:
```bash
python3 agent.py my_cv.txt \
  --job-description senior_dev_job.txt \
  --role "Senior Software Engineer" \
  --industry software
```

### Step 3: Get Keywords & Optimized Version
```bash
python3 agent.py my_cv.txt \
  --job-description senior_dev_job.txt \
  --role "Senior Software Engineer" \
  --industry software \
  --output optimized_cv.txt
```

This will:
- ✅ Analyze your CV against the job requirements
- ✅ Show which keywords you're missing
- ✅ Suggest industry-specific terms
- ✅ Generate an optimized version
- ✅ Save it to `optimized_cv.txt`

## 📚 Get Expert Tips

Need help with specific aspects? Get targeted advice:

```bash
# ATS optimization tips
python3 agent.py --tips ats

# Keyword optimization
python3 agent.py --tips keywords

# Content writing tips
python3 agent.py --tips content

# Formatting guidelines
python3 agent.py --tips formatting

# General best practices
python3 agent.py --tips general
```

## 🔥 Common Use Cases

### Use Case 1: Quick CV Check
**Scenario**: "Is my CV good enough?"
```bash
python3 agent.py my_cv.txt
```
**Time**: 10 seconds
**You Get**: Instant score and recommendations

---

### Use Case 2: Job Application Prep
**Scenario**: "I found a job I want to apply for"
```bash
python3 agent.py my_cv.txt --job-description job_posting.txt
```
**Time**: 20 seconds
**You Get**: Keyword match analysis, missing terms, tailored suggestions

---

### Use Case 3: Complete CV Overhaul
**Scenario**: "I need to improve my CV significantly"
```bash
# Step 1: Get baseline analysis
python3 agent.py my_cv.txt --output optimized_v1.txt

# Step 2: Review optimized_v1.txt and make manual improvements

# Step 3: Analyze again to track progress
python3 agent.py optimized_v1.txt

# Repeat until your score is 80+
```
**Time**: 30 minutes - 2 hours (iterative)
**You Get**: Professional-grade CV with 80+ score

---

### Use Case 4: Industry Switch
**Scenario**: "I'm changing from marketing to tech"
```bash
python3 agent.py my_cv.txt \
  --role "Software Developer" \
  --industry software
```
**Time**: 30 seconds
**You Get**: Industry-specific keywords and role-relevant suggestions

---

### Use Case 5: ATS Troubleshooting
**Scenario**: "My applications aren't getting through"
```bash
# Get ATS tips
python3 agent.py --tips ats

# Analyze your CV's ATS compatibility
python3 agent.py my_cv.txt
```
**Time**: 1 minute
**You Get**: Specific ATS issues and how to fix them

## 🎯 Score Interpretation Guide

| Score | What It Means | Action Needed |
|-------|---------------|---------------|
| **80-100** | 🎉 Excellent! | Minor tweaks, focus on tailoring per job |
| **60-79** | 👍 Good | Address top 3-5 recommendations |
| **40-59** | ⚠️ Needs Work | Follow all recommendations, iterate |
| **0-39** | 🚨 Critical | Major overhaul needed, follow guide below |

## 🆘 Help! My Score is Low (<40)

Don't panic! Follow this step-by-step recovery plan:

### Priority 1: Fix ATS Killers (Do First!)
```bash
python3 agent.py --tips ats
```
Check your CV for:
- ❌ Tables or columns? → Convert to simple linear format
- ❌ Special bullets (•, ►)? → Replace with simple dashes (-)
- ❌ Headers/footers? → Move info to main body
- ❌ Graphics/images? → Remove them

### Priority 2: Add Essential Sections
Ensure you have:
- ✅ Professional Summary (3-4 lines at top)
- ✅ Work Experience (with dates and achievements)
- ✅ Education
- ✅ Skills (list relevant technical and soft skills)

### Priority 3: Strengthen Content
```bash
python3 agent.py --tips content
```
For each job bullet:
- Replace: "Responsible for..." → Use: "Managed", "Led", "Developed"
- Replace: "Worked on..." → Use: "Built", "Created", "Implemented"
- Add numbers: "Improved performance" → "Improved performance by 40%"

### Priority 4: Re-analyze
```bash
python3 agent.py my_improved_cv.txt
```
Target: Get to 60+ on next try

## 💡 Pro Tips

### Tip #1: Save Multiple Versions
```bash
python3 agent.py my_cv.txt --output cv_version1.txt
# Make changes
python3 agent.py cv_version1.txt --output cv_version2.txt
```

### Tip #2: Test Against Multiple Jobs
```bash
python3 agent.py my_cv.txt --job-description job1.txt > analysis1.txt
python3 agent.py my_cv.txt --job-description job2.txt > analysis2.txt
python3 agent.py my_cv.txt --job-description job3.txt > analysis3.txt
```

### Tip #3: Track Your Progress
Keep a log of your scores:
```
Version 1: 35/100 - Too many ATS issues
Version 2: 52/100 - Fixed formatting, added metrics
Version 3: 68/100 - Added keywords, strengthened verbs
Version 4: 82/100 - Ready to apply! ✅
```

### Tip #4: Industry-Specific Optimization
```bash
# Software/Tech
python3 agent.py cv.txt --industry software

# Marketing
python3 agent.py cv.txt --industry marketing

# Finance
python3 agent.py cv.txt --industry finance

# Healthcare
python3 agent.py cv.txt --industry healthcare

# Sales
python3 agent.py cv.txt --industry sales
```

## 🤔 FAQ

**Q: What format should my CV be in?**
A: Plain text (.txt). Copy-paste your CV into a text file.

**Q: Will this rewrite my CV automatically?**
A: It provides an optimized version, but YOU should review and refine it. The tool enhances, you decide.

**Q: Do I need to install anything?**
A: Just Python 3.7+. No external packages required!

**Q: Can I use this for cover letters?**
A: The tool is designed for CVs, but the keyword analysis can help with cover letters too.

**Q: How often should I update my CV?**
A: Run analysis before each job application to tailor it to that specific role.

**Q: My score is 90 but I'm not getting interviews. Why?**
A: The score measures ATS compatibility and CV quality. Also consider: job fit, experience level, application timing, networking, and cover letter quality.

## 🎉 Ready? Start Now!

```bash
# Try the example first
python3 agent.py examples/sample_cv.txt

# Then analyze your CV
python3 agent.py /path/to/your_cv.txt

# Level up with job matching
python3 agent.py your_cv.txt --job-description job.txt
```

## 📖 Want More Details?

See the [full README](README.md) for:
- Complete feature list
- Advanced usage
- Library/API usage
- Technical details

---

**Good luck with your job search! 🚀**
