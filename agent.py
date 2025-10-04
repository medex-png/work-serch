#!/usr/bin/env python3
"""
Main CV Optimization Agent Interface
Combines analysis and optimization capabilities for comprehensive CV improvement
"""

from cv_analyzer import CVAnalyzer, CVAnalysisResult
from cv_optimizer import CVOptimizer
from typing import Dict, List, Optional
import argparse


class CVAgent:
    """
    Main CV Optimization AI Agent
    
    Expert in HR, recruitment strategy, CV writing, ATS optimization,
    and industry-specific hiring practices.
    """
    
    def __init__(self):
        self.analyzer = CVAnalyzer()
        self.optimizer = CVOptimizer()
        self.session_history = []
    
    def analyze_and_optimize(self, cv_text: str, 
                            job_description: str = "",
                            target_role: str = "",
                            industry: str = "") -> Dict:
        """
        Complete analysis and optimization workflow
        
        Args:
            cv_text: The CV content to analyze
            job_description: Optional target job description
            target_role: Optional target role/title
            industry: Optional target industry
            
        Returns:
            Dictionary with analysis results and optimization suggestions
        """
        print("🔍 Analyzing your CV...")
        
        # Step 1: Analyze the current CV
        analysis = self.analyzer.analyze_cv(cv_text, job_description)
        
        # Step 2: Optimize the CV content
        print("✨ Optimizing your CV...")
        optimized_cv = self.optimizer.optimize_cv_text(cv_text, target_role, industry)
        
        # Step 3: Get keyword suggestions if industry provided
        suggested_keywords = []
        if industry:
            suggested_keywords = self.optimizer.suggest_keywords(industry, target_role)
        
        # Step 4: Job-specific optimization if JD provided
        jd_suggestions = []
        if job_description:
            optimized_cv, jd_suggestions = self.optimizer.optimize_for_job_description(
                optimized_cv, job_description
            )
        
        # Compile results
        results = {
            'analysis': analysis,
            'optimized_cv': optimized_cv,
            'suggested_keywords': suggested_keywords,
            'job_specific_suggestions': jd_suggestions,
            'original_cv': cv_text
        }
        
        # Store in session history
        self.session_history.append(results)
        
        return results
    
    def print_report(self, results: Dict):
        """
        Print a comprehensive report of analysis and recommendations
        
        Args:
            results: Results dictionary from analyze_and_optimize
        """
        analysis: CVAnalysisResult = results['analysis']
        
        print("\n" + "=" * 70)
        print("CV OPTIMIZATION REPORT")
        print("=" * 70)
        
        # Scores
        print(f"\n📊 SCORES:")
        print(f"   Overall Quality Score:    {analysis.overall_score}/100")
        print(f"   ATS Compatibility Score:  {analysis.ats_compatibility_score}/100")
        
        # Interpretation
        if analysis.overall_score >= 80:
            print("   ✅ Excellent! Your CV is in great shape.")
        elif analysis.overall_score >= 60:
            print("   ⚠️  Good, but there's room for improvement.")
        else:
            print("   ❌ Needs significant improvements to be competitive.")
        
        # Strengths
        print(f"\n💪 STRENGTHS ({len(analysis.strengths)}):")
        for strength in analysis.strengths:
            print(f"   ✓ {strength}")
        
        # Weaknesses
        print(f"\n⚠️  WEAKNESSES ({len(analysis.weaknesses)}):")
        for weakness in analysis.weaknesses:
            print(f"   ✗ {weakness}")
        
        # Formatting Issues
        if analysis.formatting_issues:
            print(f"\n🔧 ATS FORMATTING ISSUES ({len(analysis.formatting_issues)}):")
            for issue in analysis.formatting_issues:
                print(f"   ⚠️  {issue}")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS ({len(analysis.recommendations)}):")
        for i, rec in enumerate(analysis.recommendations, 1):
            print(f"   {i}. {rec}")
        
        # Keyword Analysis
        if analysis.keyword_analysis:
            print(f"\n🔑 KEYWORD MATCHES ({len(analysis.keyword_analysis)}):")
            sorted_keywords = sorted(
                analysis.keyword_analysis.items(), 
                key=lambda x: x[1], 
                reverse=True
            )
            for keyword, count in sorted_keywords[:10]:
                print(f"   • {keyword}: {count} occurrences")
        
        # Suggested Keywords
        if results['suggested_keywords']:
            print(f"\n📌 SUGGESTED KEYWORDS TO CONSIDER:")
            keywords_str = ", ".join(results['suggested_keywords'][:15])
            print(f"   {keywords_str}")
        
        # Job-Specific Suggestions
        if results['job_specific_suggestions']:
            print(f"\n🎯 JOB-SPECIFIC SUGGESTIONS:")
            for suggestion in results['job_specific_suggestions']:
                print(f"   • {suggestion}")
        
        print("\n" + "=" * 70)
        print("📝 NEXT STEPS:")
        print("   1. Address critical ATS formatting issues first")
        print("   2. Incorporate recommended keywords naturally")
        print("   3. Strengthen weak phrases with action verbs")
        print("   4. Add quantifiable metrics to achievements")
        print("   5. Tailor your CV for each specific job application")
        print("=" * 70 + "\n")
    
    def get_improvement_tips(self, category: str = "general") -> List[str]:
        """
        Get specific improvement tips by category
        
        Args:
            category: Type of tips (general, ats, keywords, formatting, content)
            
        Returns:
            List of tips
        """
        tips = {
            'general': [
                "Keep your CV to 1-2 pages for most roles",
                "Use a clean, professional font (Arial, Calibri, or Times New Roman)",
                "Maintain consistent formatting throughout",
                "Proofread carefully - typos are deal-breakers",
                "Update your CV for each application"
            ],
            'ats': [
                "Use standard section headers (Work Experience, Education, Skills)",
                "Avoid headers, footers, and text boxes",
                "Don't use tables or columns for layout",
                "Save as .docx or .pdf (check job posting requirements)",
                "Use standard bullet points, not special characters",
                "Spell out acronyms at least once"
            ],
            'keywords': [
                "Mirror language from the job description",
                "Include both acronyms and full terms (e.g., 'AI' and 'Artificial Intelligence')",
                "Place keywords in context, not just in a list",
                "Include technical skills, soft skills, and certifications",
                "Use industry-standard terminology"
            ],
            'formatting': [
                "Use consistent date formats (e.g., 'Jan 2020 - Dec 2022')",
                "Left-align all text for ATS readability",
                "Use simple bullet points (-, •, or *)",
                "Maintain adequate white space",
                "Avoid fancy fonts, colors, or graphics"
            ],
            'content': [
                "Start bullets with strong action verbs",
                "Quantify achievements with numbers and percentages",
                "Focus on results, not just responsibilities",
                "Use the STAR method (Situation, Task, Action, Result)",
                "Tailor content to the target role",
                "Remove outdated or irrelevant experience"
            ]
        }
        
        return tips.get(category.lower(), tips['general'])


def main():
    """Command-line interface for the CV Agent"""
    parser = argparse.ArgumentParser(
        description='CV Optimization AI Agent - Analyze and optimize your CV for ATS and recruiters'
    )
    parser.add_argument(
        'cv_file',
        help='Path to your CV file (text format)'
    )
    parser.add_argument(
        '--job-description',
        help='Path to job description file (optional)',
        default=''
    )
    parser.add_argument(
        '--role',
        help='Target role/job title (optional)',
        default=''
    )
    parser.add_argument(
        '--industry',
        help='Target industry (e.g., software, marketing, finance)',
        default=''
    )
    parser.add_argument(
        '--tips',
        help='Show improvement tips for category (general, ats, keywords, formatting, content)',
        default=''
    )
    parser.add_argument(
        '--output',
        help='Save optimized CV to file',
        default=''
    )
    
    args = parser.parse_args()
    
    # Initialize agent
    agent = CVAgent()
    
    # Show tips if requested
    if args.tips:
        print(f"\n💡 IMPROVEMENT TIPS - {args.tips.upper()}")
        print("=" * 60)
        tips = agent.get_improvement_tips(args.tips)
        for i, tip in enumerate(tips, 1):
            print(f"{i}. {tip}")
        print()
        return
    
    # Read CV file
    try:
        with open(args.cv_file, 'r', encoding='utf-8') as f:
            cv_text = f.read()
    except FileNotFoundError:
        print(f"❌ Error: CV file '{args.cv_file}' not found")
        return
    except Exception as e:
        print(f"❌ Error reading CV file: {e}")
        return
    
    # Read job description if provided
    job_description = ""
    if args.job_description:
        try:
            with open(args.job_description, 'r', encoding='utf-8') as f:
                job_description = f.read()
        except Exception as e:
            print(f"⚠️  Warning: Could not read job description file: {e}")
    
    # Analyze and optimize
    print("\n🤖 CV Optimization AI Agent")
    print("Expert in HR, Recruitment, ATS Optimization, and CV Writing\n")
    
    results = agent.analyze_and_optimize(
        cv_text=cv_text,
        job_description=job_description,
        target_role=args.role,
        industry=args.industry
    )
    
    # Print report
    agent.print_report(results)
    
    # Save optimized CV if requested
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(results['optimized_cv'])
            print(f"✅ Optimized CV saved to: {args.output}\n")
        except Exception as e:
            print(f"❌ Error saving optimized CV: {e}\n")


if __name__ == "__main__":
    main()
