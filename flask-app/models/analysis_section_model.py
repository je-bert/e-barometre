from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSection(db.Model):
    analysis_section_id: str
    title: str
    description: str
    order: int 

    analysis_section_id = db.Column(db.String(20),primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    order = db.Column(db.Integer)