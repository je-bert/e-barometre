from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSubsectionTheme(db.Model):
  analysis_subsection_theme_id: str
  analysis_subsection_id: str
  name: str
  analysis_subsection_theme_id = db.Column(db.String(20), primary_key = True)
  analysis_subsection_id = db.Column(db.String(20), db.ForeignKey( "analysis_subsection.analysis_subsection_id"))
  name = db.Column(db.String(255))