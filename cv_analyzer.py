#!/usr/bin/env python3
"""
CV Analyzer - Core module for analyzing and optimizing CVs
Part of the work-serch AI agent system
"""

import re
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class CVAnalysisResult:
    """Results from CV analysis"""
    overall_score: int  # 0-100
    ats_compatibility_score: int  # 0-100
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]
    keyword_analysis: Dict[str, int]
    formatting_issues: List[str]


class CVAnalyzer:
    """Analyzes CVs for ATS compatibility and quality"""
    
    # Standard ATS-friendly section headers
    STANDARD_SECTIONS = [
        'work experience', 'professional experience', 'employment history',
        'education', 'skills', 'technical skills', 'certifications',
        'summary', 'professional summary', 'objective', 'profile',
        'achievements', 'accomplishments', 'projects', 'publications'
    ]
    
    # Strong action verbs for CVs
    ACTION_VERBS = [
        'achieved', 'implemented', 'developed', 'managed', 'led', 'created',
        'improved', 'increased', 'decreased', 'optimized', 'delivered',
        'designed', 'built', 'established', 'launched', 'spearheaded',
        'orchestrated', 'transformed', 'streamlined', 'negotiated', 'directed'
    ]
    
    # Common ATS-unfriendly formatting elements
    ATS_PROBLEMATIC_PATTERNS = [
        (r'\|', 'pipe characters'),
        (r'[\u2022\u2023\u25E6\u2043\u2219]', 'special bullet points'),
        (r'[^\x00-\x7F]', 'non-ASCII characters'),
    ]
    
    def __init__(self):
        self.analysis_cache = {}
    
    def analyze_cv(self, cv_text: str, job_description: str = "") -> CVAnalysisResult:
        """
        Perform comprehensive CV analysis
        
        Args:
            cv_text: The CV content as plain text
            job_description: Optional job description for keyword matching
            
        Returns:
            CVAnalysisResult with detailed analysis
        """
        cv_lower = cv_text.lower()
        
        # Analyze various aspects
        section_score = self._analyze_sections(cv_lower)
        keyword_score, keywords = self._analyze_keywords(cv_text, job_description)
        formatting_issues = self._check_formatting(cv_text)
        action_verb_score = self._analyze_action_verbs(cv_lower)
        quantification_score = self._analyze_quantification(cv_text)
        
        # Calculate scores
        ats_score = self._calculate_ats_score(
            section_score, formatting_issues, keyword_score
        )
        overall_score = self._calculate_overall_score(
            ats_score, action_verb_score, quantification_score
        )
        
        # Identify strengths and weaknesses
        strengths = self._identify_strengths(cv_text, cv_lower)
        weaknesses = self._identify_weaknesses(cv_text, cv_lower, formatting_issues)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            weaknesses, formatting_issues, keyword_score, action_verb_score
        )
        
        return CVAnalysisResult(
            overall_score=overall_score,
            ats_compatibility_score=ats_score,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendations=recommendations,
            keyword_analysis=keywords,
            formatting_issues=formatting_issues
        )
    
    def _analyze_sections(self, cv_lower: str) -> int:
        """Check for standard CV sections"""
        found_sections = sum(
            1 for section in self.STANDARD_SECTIONS 
            if section in cv_lower
        )
        # Score based on having at least the essential sections
        return min(100, (found_sections / 5) * 100)
    
    def _analyze_keywords(self, cv_text: str, job_description: str) -> Tuple[int, Dict[str, int]]:
        """Analyze keyword presence and frequency"""
        keywords = {}
        
        if job_description:
            # Extract potential keywords from job description
            jd_words = re.findall(r'\b[a-zA-Z]{3,}\b', job_description.lower())
            jd_word_freq = {}
            for word in jd_words:
                jd_word_freq[word] = jd_word_freq.get(word, 0) + 1
            
            # Check which keywords appear in CV
            cv_lower = cv_text.lower()
            for word, freq in jd_word_freq.items():
                if freq > 2 and word in cv_lower:  # Only check important words
                    keywords[word] = cv_lower.count(word)
            
            # Score based on keyword coverage
            important_keywords = [w for w, f in jd_word_freq.items() if f > 2]
            if important_keywords:
                coverage = len(keywords) / len(important_keywords)
                score = int(coverage * 100)
            else:
                score = 50  # No job description provided
        else:
            score = 50  # No job description to compare against
        
        return score, keywords
    
    def _check_formatting(self, cv_text: str) -> List[str]:
        """Check for ATS-problematic formatting"""
        issues = []
        
        for pattern, description in self.ATS_PROBLEMATIC_PATTERNS:
            if re.search(pattern, cv_text):
                issues.append(f"Contains {description} which may confuse ATS systems")
        
        # Check for tables (simplified detection)
        if cv_text.count('\t') > 10:
            issues.append("Possible table formatting detected - may not parse well in ATS")
        
        # Check for very short lines (possible columns)
        lines = cv_text.split('\n')
        short_lines = sum(1 for line in lines if 0 < len(line.strip()) < 20)
        if short_lines > len(lines) * 0.3:
            issues.append("Many short lines detected - possible column formatting issues")
        
        return issues
    
    def _analyze_action_verbs(self, cv_lower: str) -> int:
        """Analyze use of strong action verbs"""
        action_verb_count = sum(
            cv_lower.count(verb) for verb in self.ACTION_VERBS
        )
        # Score based on reasonable action verb density
        words = cv_lower.split()
        if len(words) > 0:
            density = action_verb_count / len(words)
            score = min(100, int(density * 1000))  # Scale appropriately
        else:
            score = 0
        return score
    
    def _analyze_quantification(self, cv_text: str) -> int:
        """Check for quantified achievements (numbers, percentages, etc.)"""
        # Look for numbers and percentages
        numbers = re.findall(r'\b\d+[%\w]*\b', cv_text)
        
        # Score based on presence of quantification
        if len(numbers) > 10:
            return 100
        elif len(numbers) > 5:
            return 75
        elif len(numbers) > 2:
            return 50
        else:
            return 25
    
    def _calculate_ats_score(self, section_score: int, formatting_issues: List[str], 
                            keyword_score: int) -> int:
        """Calculate overall ATS compatibility score"""
        # Weight the components
        score = (section_score * 0.4 + keyword_score * 0.4)
        
        # Deduct for formatting issues
        deduction = min(30, len(formatting_issues) * 10)
        score = max(0, score - deduction)
        
        return int(score)
    
    def _calculate_overall_score(self, ats_score: int, action_verb_score: int,
                                quantification_score: int) -> int:
        """Calculate overall CV quality score"""
        return int(
            ats_score * 0.5 +
            action_verb_score * 0.25 +
            quantification_score * 0.25
        )
    
    def _identify_strengths(self, cv_text: str, cv_lower: str) -> List[str]:
        """Identify CV strengths"""
        strengths = []
        
        # Check for quantified achievements
        if len(re.findall(r'\b\d+%', cv_text)) > 3:
            strengths.append("Good use of quantified achievements with percentages")
        
        # Check for action verbs
        action_verb_count = sum(cv_lower.count(verb) for verb in self.ACTION_VERBS)
        if action_verb_count > 10:
            strengths.append("Strong use of action verbs to describe responsibilities")
        
        # Check for standard sections
        essential_sections = ['experience', 'education', 'skills']
        if all(section in cv_lower for section in essential_sections):
            strengths.append("Contains all essential CV sections")
        
        # Check for reasonable length
        word_count = len(cv_text.split())
        if 300 < word_count < 800:
            strengths.append("Appropriate length - concise yet comprehensive")
        
        return strengths if strengths else ["CV structure is present"]
    
    def _identify_weaknesses(self, cv_text: str, cv_lower: str, 
                           formatting_issues: List[str]) -> List[str]:
        """Identify CV weaknesses"""
        weaknesses = []
        
        # Check for missing sections
        if 'experience' not in cv_lower and 'employment' not in cv_lower:
            weaknesses.append("Missing work experience section")
        
        if 'education' not in cv_lower:
            weaknesses.append("Missing education section")
        
        if 'skills' not in cv_lower:
            weaknesses.append("Missing skills section")
        
        # Check for weak language
        weak_phrases = ['responsible for', 'duties included', 'worked on']
        weak_count = sum(cv_lower.count(phrase) for phrase in weak_phrases)
        if weak_count > 3:
            weaknesses.append("Overuse of weak phrases - use stronger action verbs")
        
        # Check for length issues
        word_count = len(cv_text.split())
        if word_count < 200:
            weaknesses.append("CV is too short - add more detail about achievements")
        elif word_count > 1000:
            weaknesses.append("CV is too long - focus on most relevant information")
        
        # Add formatting issues
        if formatting_issues:
            weaknesses.append(f"ATS formatting concerns: {len(formatting_issues)} issues detected")
        
        return weaknesses if weaknesses else ["Minor improvements could be made"]
    
    def _generate_recommendations(self, weaknesses: List[str], 
                                 formatting_issues: List[str],
                                 keyword_score: int,
                                 action_verb_score: int) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # Address formatting issues first (critical for ATS)
        if formatting_issues:
            recommendations.append(
                "CRITICAL: Fix ATS formatting issues - use simple formatting, "
                "standard fonts, and avoid tables/columns"
            )
        
        # Address missing sections
        if any('missing' in w.lower() for w in weaknesses):
            recommendations.append(
                "Add all essential sections: Professional Summary, Work Experience, "
                "Education, Skills, and relevant certifications"
            )
        
        # Keyword optimization
        if keyword_score < 60:
            recommendations.append(
                "Optimize keywords: Review the job description and naturally incorporate "
                "relevant terms and skills throughout your CV"
            )
        
        # Action verbs
        if action_verb_score < 50:
            recommendations.append(
                "Strengthen impact: Replace weak phrases with strong action verbs "
                "(e.g., 'managed', 'developed', 'achieved', 'implemented')"
            )
        
        # Quantification
        if not any('quantified' in s.lower() for s in weaknesses):
            recommendations.append(
                "Add quantifiable achievements: Include specific numbers, percentages, "
                "and metrics to demonstrate impact (e.g., 'Increased sales by 25%')"
            )
        
        # General best practice
        recommendations.append(
            "Tailor your CV: Customize it for each application to match the specific "
            "job requirements and company culture"
        )
        
        return recommendations


def main():
    """Example usage of CV Analyzer"""
    print("CV Analyzer - Part of work-serch AI Agent System")
    print("=" * 60)
    
    # Example CV text
    sample_cv = """
    John Doe
    Software Engineer
    
    PROFESSIONAL SUMMARY
    Experienced software engineer with 5 years in web development.
    
    WORK EXPERIENCE
    Senior Developer at Tech Corp (2020-2023)
    - Developed new features for main product
    - Worked on team projects
    - Responsible for code reviews
    
    Developer at StartUp Inc (2018-2020)
    - Built web applications
    - Maintained existing codebase
    
    EDUCATION
    BS Computer Science, University (2018)
    
    SKILLS
    Python, JavaScript, React, SQL
    """
    
    analyzer = CVAnalyzer()
    result = analyzer.analyze_cv(sample_cv)
    
    print(f"\nOverall Score: {result.overall_score}/100")
    print(f"ATS Compatibility: {result.ats_compatibility_score}/100")
    
    print("\nSTRENGTHS:")
    for strength in result.strengths:
        print(f"  ✓ {strength}")
    
    print("\nWEAKNESSES:")
    for weakness in result.weaknesses:
        print(f"  ✗ {weakness}")
    
    print("\nRECOMMENDATIONS:")
    for i, rec in enumerate(result.recommendations, 1):
        print(f"  {i}. {rec}")
    
    if result.formatting_issues:
        print("\nFORMATTING ISSUES:")
        for issue in result.formatting_issues:
            print(f"  ⚠ {issue}")


if __name__ == "__main__":
    main()
