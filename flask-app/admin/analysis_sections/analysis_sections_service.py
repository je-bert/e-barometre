from models import AnalysisSection 
from flask import render_template



def find_all():
    analysis_sections = AnalysisSection.query.all()

    return render_template('analysis-sections.html',analysis_sections = analysis_sections)