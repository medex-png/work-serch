#!/usr/bin/env python3
"""
CV Optimizer - Module for rewriting and optimizing CV content
Part of the work-serch AI agent system
"""

import re
from typing import Dict, List, Tuple


class CVOptimizer:
    """Optimizes CV content for ATS and human reviewers"""
    
    # Mapping of weak phrases to stronger alternatives
    PHRASE_IMPROVEMENTS = {
        'responsible for': 'managed|led|oversaw|directed',
        'worked on': 'developed|implemented|created|built',
        'helped with': 'contributed to|supported|facilitated',
        'duties included': 'key achievements included|delivered',
        'involved in': 'participated in|collaborated on|executed',
        'was part of': 'contributed to|served on|member of',
        'did': 'performed|executed|completed|accomplished',
        'made': 'created|developed|produced|generated',
        'got': 'achieved|obtained|secured|acquired',
    }
    
    # Industry-specific keywords and skills
    INDUSTRY_KEYWORDS = {
        'software': [
            'agile', 'scrum', 'ci/cd', 'devops', 'microservices',
            'cloud', 'aws', 'azure', 'docker', 'kubernetes',
            'git', 'rest api', 'database', 'testing', 'debugging'
        ],
        'marketing': [
            'seo', 'sem', 'content marketing', 'social media',
            'analytics', 'campaign management', 'brand strategy',
            'roi', 'lead generation', 'market research'
        ],
        'finance': [
            'financial analysis', 'forecasting', 'budgeting',
            'risk management', 'compliance', 'reporting',
            'excel', 'financial modeling', 'accounting', 'audit'
        ],
        'healthcare': [
            'patient care', 'hipaa', 'ehr', 'clinical',
            'healthcare administration', 'medical records',
            'regulatory compliance', 'quality assurance'
        ],
        'sales': [
            'revenue growth', 'client acquisition', 'pipeline management',
            'crm', 'negotiation', 'account management', 'quota',
            'b2b', 'b2c', 'cold calling', 'relationship building'
        ]
    }
    
    def __init__(self):
        self.optimization_history = []
    
    def optimize_cv_text(self, cv_text: str, target_role: str = "",
                        industry: str = "") -> str:
        """
        Optimize CV text for better impact and ATS compatibility
        
        Args:
            cv_text: Original CV text
            target_role: Target job role/title
            industry: Target industry (software, marketing, finance, etc.)
            
        Returns:
            Optimized CV text
        """
        optimized = cv_text
        
        # Apply various optimization techniques
        optimized = self._improve_weak_phrases(optimized)
        optimized = self._standardize_sections(optimized)
        optimized = self._clean_formatting(optimized)
        
        return optimized
    
    def _improve_weak_phrases(self, text: str) -> str:
        """Replace weak phrases with stronger alternatives"""
        improved = text
        
        for weak, strong_options in self.PHRASE_IMPROVEMENTS.items():
            # Case-insensitive replacement
            pattern = re.compile(re.escape(weak), re.IGNORECASE)
            
            if pattern.search(improved):
                # Use the first strong alternative for automated replacement
                strong = strong_options.split('|')[0]
                improved = pattern.sub(strong.capitalize() 
                                      if weak[0].isupper() else strong, 
                                      improved)
        
        return improved
    
    def _standardize_sections(self, text: str) -> str:
        """Standardize section headers for ATS compatibility"""
        # Common variations to standard names
        # Order matters - more specific patterns first
        section_mappings = [
            (r'\bemployment\s+history\b', 'WORK EXPERIENCE'),
            (r'\bjob\s+history\b', 'WORK EXPERIENCE'),
            (r'\bprofessional\s+experience\b', 'WORK EXPERIENCE'),
            (r'\beducational\s+background\b', 'EDUCATION'),
            (r'\bacademic\s+background\b', 'EDUCATION'),
            (r'\bcore\s+competencies\b', 'SKILLS'),
            (r'\btechnical\s+skills\b', 'TECHNICAL SKILLS'),
            (r'\bprofessional\s+summary\b', 'SUMMARY'),
            (r'\bcareer\s+summary\b', 'SUMMARY'),
            (r'\babout\s+me\b', 'SUMMARY'),
        ]
        
        standardized = text
        for pattern, standard in section_mappings:
            standardized = re.sub(pattern, standard, standardized, 
                                flags=re.IGNORECASE)
        
        return standardized
    
    def _clean_formatting(self, text: str) -> str:
        """Clean problematic formatting for ATS"""
        cleaned = text
        
        # Replace fancy bullets with simple dashes or asterisks
        cleaned = re.sub(r'[•●■▪▸►]', '-', cleaned)
        
        # Replace em dashes with regular hyphens
        cleaned = re.sub(r'—', '-', cleaned)
        
        # Replace fancy quotes with straight quotes
        cleaned = re.sub(r'["""]', '"', cleaned)
        cleaned = re.sub(r"['']", "'", cleaned)
        
        # Remove multiple consecutive spaces
        cleaned = re.sub(r' +', ' ', cleaned)
        
        # Normalize line breaks
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
        
        return cleaned
    
    def suggest_keywords(self, industry: str, role: str = "") -> List[str]:
        """
        Suggest relevant keywords for a given industry and role
        
        Args:
            industry: Target industry
            role: Specific role (optional)
            
        Returns:
            List of recommended keywords
        """
        keywords = []
        
        # Get industry-specific keywords
        industry_lower = industry.lower()
        for ind, kw_list in self.INDUSTRY_KEYWORDS.items():
            if ind in industry_lower:
                keywords.extend(kw_list)
                break
        
        # Add role-specific keywords if provided
        if role:
            role_lower = role.lower()
            if 'senior' in role_lower or 'lead' in role_lower:
                keywords.extend(['leadership', 'mentoring', 'team management'])
            if 'manager' in role_lower:
                keywords.extend(['project management', 'stakeholder management', 
                               'strategic planning'])
            if 'engineer' in role_lower or 'developer' in role_lower:
                keywords.extend(['problem solving', 'technical design', 
                               'code review'])
        
        return list(set(keywords))  # Remove duplicates
    
    def enhance_achievements(self, achievement_text: str) -> str:
        """
        Enhance achievement descriptions with stronger impact
        
        Args:
            achievement_text: Original achievement description
            
        Returns:
            Enhanced achievement text
        """
        enhanced = achievement_text.strip()
        
        # Check if it starts with a weak phrase
        for weak, strong_options in self.PHRASE_IMPROVEMENTS.items():
            if enhanced.lower().startswith(weak):
                strong = strong_options.split('|')[0]
                enhanced = strong.capitalize() + enhanced[len(weak):]
                break
        
        # Ensure it starts with an action verb (capitalize first letter)
        if enhanced and not enhanced[0].isupper():
            enhanced = enhanced[0].upper() + enhanced[1:]
        
        return enhanced
    
    def generate_professional_summary(self, years_experience: int,
                                     role: str, 
                                     key_skills: List[str],
                                     achievements: List[str] = None) -> str:
        """
        Generate a professional summary section
        
        Args:
            years_experience: Years of professional experience
            role: Job role/title
            key_skills: List of key skills
            achievements: Optional list of key achievements
            
        Returns:
            Professional summary text
        """
        # Determine experience level descriptor
        if years_experience < 2:
            exp_desc = "motivated"
        elif years_experience < 5:
            exp_desc = "experienced"
        elif years_experience < 10:
            exp_desc = "seasoned"
        else:
            exp_desc = "highly accomplished"
        
        # Build summary
        summary_parts = [
            f"{exp_desc.capitalize()} {role} with {years_experience}+ years of experience"
        ]
        
        # Add skills
        if key_skills:
            skills_text = ", ".join(key_skills[:4])
            summary_parts.append(f"specializing in {skills_text}")
        
        # Add achievements if provided
        if achievements:
            summary_parts.append(
                f"Proven track record of {achievements[0].lower()}"
            )
        
        summary = " ".join(summary_parts) + "."
        
        return summary
    
    def format_achievement_with_metrics(self, action: str, result: str, 
                                       metric: str = "") -> str:
        """
        Format an achievement using the Action-Result-Metric framework
        
        Args:
            action: What you did
            result: What happened as a result
            metric: Quantifiable metric (optional)
            
        Returns:
            Formatted achievement bullet point
        """
        if metric:
            return f"{action}, resulting in {result} ({metric})"
        else:
            return f"{action}, resulting in {result}"
    
    def optimize_for_job_description(self, cv_text: str, 
                                     job_description: str) -> Tuple[str, List[str]]:
        """
        Optimize CV to match a specific job description
        
        Args:
            cv_text: Original CV text
            job_description: Target job description
            
        Returns:
            Tuple of (optimized CV text, list of suggestions)
        """
        suggestions = []
        optimized = cv_text
        
        # Extract important keywords from job description
        jd_words = re.findall(r'\b[A-Za-z]{3,}\b', job_description)
        word_freq = {}
        for word in jd_words:
            word_lower = word.lower()
            if word_lower not in ['the', 'and', 'for', 'with', 'that', 'this']:
                word_freq[word_lower] = word_freq.get(word_lower, 0) + 1
        
        # Find important keywords (appear 3+ times)
        important_keywords = [
            word for word, freq in word_freq.items() 
            if freq >= 3
        ]
        
        # Check which keywords are missing from CV
        cv_lower = cv_text.lower()
        missing_keywords = [
            kw for kw in important_keywords 
            if kw not in cv_lower
        ]
        
        if missing_keywords:
            suggestions.append(
                f"Consider incorporating these keywords from the job description: "
                f"{', '.join(missing_keywords[:10])}"
            )
        
        # Apply general optimizations
        optimized = self.optimize_cv_text(optimized)
        
        return optimized, suggestions


def main():
    """Example usage of CV Optimizer"""
    print("CV Optimizer - Part of work-serch AI Agent System")
    print("=" * 60)
    
    optimizer = CVOptimizer()
    
    # Example 1: Improve weak phrases
    print("\n1. Improving weak phrases:")
    original = "Responsible for managing team projects and worked on implementing new features"
    improved = optimizer._improve_weak_phrases(original)
    print(f"   Original: {original}")
    print(f"   Improved: {improved}")
    
    # Example 2: Suggest keywords
    print("\n2. Suggested keywords for software industry:")
    keywords = optimizer.suggest_keywords("software", "senior developer")
    print(f"   {', '.join(keywords[:10])}")
    
    # Example 3: Generate professional summary
    print("\n3. Generated professional summary:")
    summary = optimizer.generate_professional_summary(
        years_experience=5,
        role="Software Engineer",
        key_skills=["Python", "React", "AWS", "Microservices"],
        achievements=["delivering scalable applications"]
    )
    print(f"   {summary}")
    
    # Example 4: Format achievement
    print("\n4. Formatted achievement:")
    achievement = optimizer.format_achievement_with_metrics(
        action="Implemented automated testing framework",
        result="improved code quality and reduced bugs",
        metric="40% reduction in production issues"
    )
    print(f"   {achievement}")


if __name__ == "__main__":
    main()
