from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSubsectionItem(db.Model):
  analysis_subsection_item_id: int
  analysis_subsection_id: int
  analysis_subsection_theme_id: int
  content: str
  min: int
  max: int
  type: str
  analysis_subsection_item_id = db.Column(db.Integer, primary_key = True)
  analysis_subsection_id = db.Column(db.Integer, db.ForeignKey( "analysis_subsection.analysis_subsection_id"))
  analysis_subsection_theme_id = db.Column(db.Integer, db.ForeignKey( "analysis_subsection_theme.analysis_subsection_theme_id"))
  content = db.Column(db.String(255))
  min = db.Column(db.Integer)
  max = db.Column(db.Integer)
  type = db.Column(db.String(20))