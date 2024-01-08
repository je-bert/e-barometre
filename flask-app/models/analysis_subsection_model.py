from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSubsection(db.Model):
    analysis_subsection_id: str
    analysis_section_id: str
    title: str
    about_barometer: str
    order: int 
    barometer: str
    min_result: float
    min_weight: float
    is_active: bool

    analysis_subsection_id = db.Column(db.String(20), primary_key = True)
    analysis_section_id = db.Column(db.String(20), db.ForeignKey( "analysis_section.analysis_section_id"))
    title = db.Column(db.String(255))
    about_barometer = db.Column(db.String(255))
    order = db.Column(db.Integer)
    barometer = db.Column(db.String(255))
    min_result = db.Column(db.Float)
    min_weight = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default = True)