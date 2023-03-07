from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSubsection(db.Model):
    analysis_subsection_id: str
    analysis_section_id: str
    title: str
    description: str
    order: int 
    display_condition: str
    schema_type: str

    analysis_subsection_id = db.Column(db.String(20), primary_key = True)
    analysis_section_id = db.Column(db.String(20), db.ForeignKey( "analysis_section.analysis_section_id"))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    order = db.Column(db.Integer)
    display_condition = db.Column(db.String(50), nullable = True)
    schema_type = db.Column(db.String(20))