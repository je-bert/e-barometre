from database import db
from dataclasses import dataclass
from sqlalchemy import select, func
from models import AnalysisSubsection

@dataclass
class AnalysisSection(db.Model):
    analysis_section_id: str
    title: str
    order: int 
    is_active: bool

    analysis_section_id = db.Column(db.String(20), primary_key = True)
    title = db.Column(db.String(255))
    order = db.Column(db.Integer)
    subsections = db.relationship('AnalysisSubsection', backref='analysis_section', lazy='dynamic')
    is_active = db.Column(db.Boolean, default = True)