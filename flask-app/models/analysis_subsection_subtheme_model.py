from database import db
from dataclasses import dataclass

@dataclass
class AnalysisSubsectionSubtheme(db.Model):
  analysis_subsection_subtheme_id: str
  analysis_subsection_theme_id: str
  question_id: str
  yellow_flag: str
  red_flag: str
  min_for_yellow_flag: int
  min_for_red_flag: int
  analysis_subsection_subtheme_id = db.Column(db.String(20), primary_key = True)
  analysis_subsection_theme_id = db.Column(db.String(20), db.ForeignKey( "analysis_subsection_theme.analysis_subsection_theme_id"))
  question_id = db.Column(db.String(20), db.ForeignKey( "question.question_id"))
  yellow_flag = db.Column(db.String(255))
  red_flag = db.Column(db.String(255))
  min_for_yellow_flag = db.Column(db.Integer)
  min_for_red_flag = db.Column(db.Integer)
