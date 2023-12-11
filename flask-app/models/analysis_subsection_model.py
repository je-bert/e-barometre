from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSubsection(db.Model):
    analysis_subsection_id: str
    analysis_section_id: str
    title: str
    about_barometer: str
    flag_introduction: str
    order: int 
    display_condition: str
    barometer: str

    analysis_subsection_id = db.Column(db.String(20), primary_key = True)
    analysis_section_id = db.Column(db.String(20), db.ForeignKey( "analysis_section.analysis_section_id"))
    title = db.Column(db.String(255))
    about_barometer = db.Column(db.String(255))
    flag_introduction = db.Column(db.String(255))
    order = db.Column(db.Integer)
    display_condition = db.Column(db.String(255), nullable = True)
    barometer = db.Column(db.String(255))