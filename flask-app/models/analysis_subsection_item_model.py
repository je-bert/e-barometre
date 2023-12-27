from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSubsectionItem(db.Model):
  analysis_subsection_item_id: int
  analysis_subsection_id: int
  analysis_subsection_theme_id: int
  content: str
  min: float
  max: float
  type: str
  analysis_subsection_item_id = db.Column(db.Integer, primary_key = True)
  analysis_subsection_id = db.Column(db.Integer, db.ForeignKey( "analysis_subsection.analysis_subsection_id"))
  analysis_subsection_theme_id = db.Column(db.Integer, db.ForeignKey( "analysis_subsection_theme.analysis_subsection_theme_id"))
  content = db.Column(db.String(255))
  min = db.Column(db.Float(20))
  max = db.Column(db.Float(20))
  type = db.Column(db.String(20))