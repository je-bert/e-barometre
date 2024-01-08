from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSubsectionSubtheme(db.Model):
  analysis_subsection_subtheme_id: str
  analysis_subsection_theme_id: str
  question_id: str
  ranges: str
  intensity: float
  weight: float
  is_active: bool
  analysis_subsection_subtheme_id = db.Column(db.String(20), primary_key = True)
  analysis_subsection_theme_id = db.Column(db.String(20), db.ForeignKey( "analysis_subsection_theme.analysis_subsection_theme_id"))
  question_id = db.Column(db.String(20), db.ForeignKey( "question.question_id"))
  ranges = db.Column(db.String(100))
  intensity = db.Column(db.Float)
  weight = db.Column(db.Float)
  is_active = db.Column(db.Boolean, default = True)
