# work-serch: CV Optimization AI Agent

A cutting-edge AI agent specialized in HR, recruitment strategy, CV/resume writing, ATS (Applicant Tracking System) optimization, and industry-specific hiring practices. This agent analyzes, rewrites, and optimizes CVs to maximize their chances of passing automated screening systems and impressing human recruiters.

## 🎯 Agent Role & Purpose

This AI agent is an expert in:

- **Human Resources (HR)** - Understanding HR best practices and recruitment processes
- **Recruitment Strategy** - Knowledge of modern recruitment workflows and hiring trends
- **CV/Resume Writing** - Expertise in crafting compelling, professional CVs
- **ATS Optimization** - Deep understanding of how ATS systems parse, rank, and filter CVs
- **Industry-Specific Hiring Practices** - Awareness of unique requirements across different industries

### Mission
To **analyze, rewrite, and optimize CVs** to maximize chances of:
1. ✅ Passing automated screening systems (ATS)
2. ✅ Impressing human recruiters and hiring managers
3. ✅ Securing interviews and job offers

## 🚀 Features

### Core Capabilities

1. **Comprehensive CV Analysis**
   - Parse and understand CV structure and content
   - Identify strengths and weaknesses
   - Assess ATS compatibility (0-100 score)
   - Evaluate formatting and readability
   - Detect common mistakes and omissions

2. **ATS Optimization**
   - Ensure proper keyword usage aligned with job descriptions
   - Optimize formatting for ATS parsing
   - Structure content in ATS-friendly sections
   - Remove elements that confuse ATS systems
   - Enhance discoverability through strategic keyword placement

3. **Content Enhancement**
   - Improve impact and clarity of achievements
   - Replace weak phrases with strong action verbs
   - Suggest quantifiable metrics for accomplishments
   - Tailor content to target roles
   - Eliminate redundant language

4. **Industry-Specific Guidance**
   - Provide sector-specific advice (software, marketing, finance, healthcare, sales)
   - Suggest relevant keywords for target industries
   - Adapt recommendations to industry norms

5. **Actionable Recommendations**
   - Prioritized improvement suggestions
   - Specific formatting fixes
   - Keyword optimization tips
   - Content enhancement strategies

## 📦 Installation

### Prerequisites
- Python 3.7 or higher

### Setup
Clone the repository and navigate to the directory:

```bash
git clone https://github.com/medex-png/work-serch.git
cd work-serch
```

No external dependencies required - uses only Python standard library!

## 💻 Usage

### Basic Analysis

Analyze a CV and get optimization recommendations:

```bash
python3 agent.py path/to/your_cv.txt
```

### Advanced Usage

**With Job Description Matching:**
```bash
python3 agent.py your_cv.txt --job-description job_posting.txt
```

**With Target Role and Industry:**
```bash
python3 agent.py your_cv.txt --role "Senior Software Engineer" --industry software
```

**Complete Analysis with All Options:**
```bash
python3 agent.py your_cv.txt \
  --job-description job_posting.txt \
  --role "Senior Software Engineer" \
  --industry software \
  --output optimized_cv.txt
```

### Get Improvement Tips

Get category-specific tips without analyzing a CV:

```bash
# General tips
python3 agent.py --tips general

# ATS optimization tips
python3 agent.py --tips ats

# Keyword optimization tips
python3 agent.py --tips keywords

# Formatting tips
python3 agent.py --tips formatting

# Content writing tips
python3 agent.py --tips content
```

### Command-Line Options

| Option | Description |
|--------|-------------|
| `cv_file` | Path to your CV file (required, text format) |
| `--job-description` | Path to job description file for keyword matching |
| `--role` | Target job role/title (e.g., "Senior Developer") |
| `--industry` | Target industry (software, marketing, finance, healthcare, sales) |
| `--tips` | Show improvement tips (general, ats, keywords, formatting, content) |
| `--output` | Save optimized CV to specified file |

## 📊 Understanding Your Results

### Scores

- **Overall Quality Score (0-100)**: Comprehensive assessment of CV quality
  - 80-100: Excellent - CV is in great shape
  - 60-79: Good - Room for improvement
  - 0-59: Needs significant improvements

- **ATS Compatibility Score (0-100)**: How well your CV will perform in ATS systems
  - Factors: Section structure, formatting, keyword presence

### Report Sections

1. **Strengths**: What your CV does well
2. **Weaknesses**: Areas that need improvement
3. **ATS Formatting Issues**: Specific problems that could prevent ATS parsing
4. **Recommendations**: Prioritized action items
5. **Keyword Matches**: Keywords found from job description
6. **Suggested Keywords**: Industry/role-specific keywords to consider

## 📁 Project Structure

```
work-serch/
├── agent.py              # Main agent interface
├── cv_analyzer.py        # CV analysis engine
├── cv_optimizer.py       # CV optimization and rewriting
├── agent_config.md       # Detailed agent configuration
├── examples/
│   ├── sample_cv.txt     # Example CV
│   └── job_description.txt  # Example job description
└── README.md            # This file
```

## 🔧 Using as a Library

You can also use the modules directly in your Python code:

```python
from agent import CVAgent

# Initialize the agent
agent = CVAgent()

# Analyze and optimize a CV
with open('cv.txt', 'r') as f:
    cv_text = f.read()

results = agent.analyze_and_optimize(
    cv_text=cv_text,
    job_description="",  # Optional
    target_role="Software Engineer",
    industry="software"
)

# Print detailed report
agent.print_report(results)

# Access specific results
print(f"Overall Score: {results['analysis'].overall_score}")
print(f"Optimized CV: {results['optimized_cv']}")
```

## 💡 Best Practices

### For Best Results:

1. **Provide Job Description**: Always include the job description for keyword matching
2. **Specify Role & Industry**: This enables targeted keyword suggestions
3. **Use Plain Text**: Extract CV as plain text for accurate analysis
4. **Address Critical Issues First**: Fix ATS formatting issues before content
5. **Iterate**: Run analysis multiple times as you improve your CV

### Common ATS Killers to Avoid:

- ❌ Tables and columns for layout
- ❌ Headers and footers
- ❌ Special characters and fancy bullets
- ❌ Images and graphics
- ❌ Text boxes
- ❌ Non-standard section headers
- ❌ Multiple columns

### What Works:

- ✅ Simple, clean formatting
- ✅ Standard fonts (Arial, Calibri, Times New Roman)
- ✅ Standard section headers (Work Experience, Education, Skills)
- ✅ Simple bullet points (-, •, or *)
- ✅ Keywords from job description
- ✅ Quantified achievements
- ✅ Strong action verbs
- ✅ Left-aligned text

## 🎓 Examples

See the `examples/` directory for:
- Sample CV with common issues
- Example job description
- Before/after optimization examples

Run the example:
```bash
python3 agent.py examples/sample_cv.txt \
  --job-description examples/job_description.txt \
  --role "Senior Software Engineer" \
  --industry software
```

## 🤝 Contributing

This is an AI agent project designed to help job seekers optimize their CVs. Contributions and improvements are welcome!

## 📄 License

This project is open source and available for use in job search and recruitment processes.

## 🔗 Related Resources

- [ATS Best Practices Guide](agent_config.md)
- [CV Writing Tips](agent_config.md#interaction-guidelines)
- [Industry Keywords](agent_config.md#core-capabilities)

## 📞 Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Made with ❤️ to help you land your dream job!**
