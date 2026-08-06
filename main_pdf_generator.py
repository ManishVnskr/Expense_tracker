#!/usr/bin/env python3
"""
Main PDF Generator - Orchestrates all sections
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fpdf import FPDF
from generate_pdf import ExpenseTrackerPDF, add_problem_statement, add_requirements, add_background, add_solution_architecture, add_tech_stack
from task_breakdown import add_task_breakdown


def add_conclusion(pdf):
    """Add conclusion and next steps"""
    pdf.add_page()
    pdf.chapter_title('Conclusion', 1)
    
    conclusion_text = """This implementation plan provides a comprehensive roadmap for building a production-ready, full-stack expense tracker application with advanced features including:

- Multi-user collaboration with role-based access control
- Automatic recurring transaction detection
- Advanced budget management with rollover
- Rule-based predictive analytics
- Comprehensive data visualization
- Professional export capabilities

The architecture emphasizes:
- Security: JWT authentication, role-based authorization, input validation
- Scalability: Stateless backend, efficient caching, database indexing
- Maintainability: Clean code structure, comprehensive testing, documentation
- Developer Experience: Modern tooling, hot reloading, type safety
- Production Readiness: Docker deployment, CI/CD pipelines, monitoring

The modular task breakdown allows for flexible implementation, enabling teams to prioritize features based on business requirements while maintaining a clear path to completion."""
    
    pdf.chapter_body(conclusion_text)
    
    pdf.chapter_title('Key Success Factors', 2)
    success_factors = [
        "Follow test-driven development: Write tests before implementation",
        "Maintain consistent code style: Use linters and formatters",
        "Document as you go: Don't defer documentation to the end",
        "Review security implications: Every feature should be security-reviewed",
        "Optimize performance: Profile and optimize database queries early",
        "User feedback: Test with real users during development",
        "Version control discipline: Meaningful commits, feature branches, PR reviews",
        "Monitoring and logging: Implement from day one, not as an afterthought"
    ]
    pdf.add_bullet_list(success_factors)
    
    pdf.chapter_title('Potential Extensions', 2)
    extensions = [
        "Mobile applications: React Native or Flutter apps",
        "Receipt scanning: OCR integration for automatic transaction entry",
        "Bank integration: Connect to banking APIs for automatic imports",
        "Advanced ML predictions: Implement machine learning models for better forecasts",
        "Social features: Share achievements, spending challenges with friends",
        "Investment tracking: Expand to track investments and net worth",
        "Tax reporting: Generate tax-ready reports for specific jurisdictions",
        "Multi-currency support: Handle international transactions",
        "Notifications: Email/SMS/Push notifications for budget alerts",
        "API webhooks: Allow third-party integrations"
    ]
    pdf.add_bullet_list(extensions)
    
    pdf.chapter_title('Resources and References', 2)
    
    references_text = """Technical Documentation:
- Spring Boot: https://spring.io/projects/spring-boot
- React: https://react.dev/
- TanStack Query: https://tanstack.com/query
- shadcn/ui: https://ui.shadcn.com/
- PostgreSQL: https://www.postgresql.org/docs/
- Flyway: https://flywaydb.org/documentation/
- Docker: https://docs.docker.com/

Best Practices:
- Spring Security: https://spring.io/guides/topicals/spring-security-architecture
- JWT: https://jwt.io/introduction
- REST API Design: https://restfulapi.net/
- React Patterns: https://reactpatterns.com/
- TypeScript: https://www.typescriptlang.org/docs/handbook/

Deployment Platforms:
- Vercel: https://vercel.com/docs
- Netlify: https://docs.netlify.com/
- Railway: https://docs.railway.app/
- Render: https://render.com/docs"""
    
    pdf.chapter_body(references_text)
    
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'End of Implementation Plan', 0, 1, 'C')
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 6, 'Built with dedication for a robust expense tracking solution', 0, 1, 'C')


def main():
    """Main function to generate complete PDF"""
    print("=" * 60)
    print("Expense Tracker - PDF Generation")
    print("=" * 60)
    print()
    
    print("[1/8] Initializing PDF document...")
    pdf = ExpenseTrackerPDF()
    pdf.add_page()
    
    # Title Page
    print("[2/8] Creating title page...")
    from datetime import datetime
    pdf.set_font('Arial', 'B', 24)
    pdf.ln(40)
    pdf.cell(0, 15, 'Expense Tracker Application', 0, 1, 'C')
    pdf.set_font('Arial', 'B', 18)
    pdf.cell(0, 10, 'Full-Stack Implementation Plan', 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 8, f'Generated: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}', 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font('Arial', 'I', 11)
    pdf.multi_cell(0, 6, 'A production-ready, cloud-deployable expense tracker with multi-user collaboration, role-based access control, recurring transaction detection, advanced budget management, and comprehensive analytics.', 0, 'C')
    
    # Main Content
    print("[3/8] Adding problem statement and requirements...")
    add_problem_statement(pdf)
    add_requirements(pdf)
    
    print("[4/8] Adding background research and findings...")
    add_background(pdf)
    
    print("[5/8] Adding solution architecture...")
    add_solution_architecture(pdf)
    
    print("[6/8] Adding technology stack details...")
    add_tech_stack(pdf)
    
    print("[7/8] Adding task breakdown (30 tasks)...")
    add_task_breakdown(pdf)
    
    print("[8/8] Adding conclusion and references...")
    add_conclusion(pdf)
    
    # Save PDF
    output_path = '/home/govind/Desktop/project/Expense_Tracker.pdf'
    print()
    print(f"Saving PDF to: {output_path}")
    pdf.output(output_path)
    
    # Get file size
    file_size = os.path.getsize(output_path)
    file_size_mb = file_size / (1024 * 1024)
    
    print()
    print("=" * 60)
    print("PDF Generation Complete!")
    print("=" * 60)
    print(f"File: {output_path}")
    print(f"Size: {file_size_mb:.2f} MB")
    print(f"Pages: {pdf.page_no()}")
    print()
    print("The PDF contains:")
    print("  * Problem Statement")
    print("  * Functional & Technical Requirements")
    print("  * Background Research & Best Practices")
    print("  * Solution Architecture & Database Design")
    print("  * Complete Technology Stack")
    print("  * 30 Detailed Implementation Tasks")
    print("  * Timeline & Resource Estimates")
    print("  * Conclusion & Next Steps")
    print()
    print("Ready for implementation! ")
    print("=" * 60)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error generating PDF: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
