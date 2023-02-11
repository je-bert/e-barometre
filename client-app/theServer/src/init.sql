drop table if exists question_category_question;
drop table if exists question;
drop table if exists condition;
drop table if exists survey;
drop table if exists choice;
drop table if exists label;
drop table if exists answer;
drop table if exists custom_answer;
drop table if exists user;
drop table if exists question_category;


CREATE TABLE survey(
   [survey_id] TEXT PRIMARY KEY,
   [name] TEXT,
   [description] TEXT,
   [color] char(7),
   [cover_picture_url] TEXT,
   [status] TEXT,
   [order] INTEGER
);

CREATE TABLE question(
   [question_id] varchar(255)PRIMARY KEY,
   [survey_id] varchar(255),
   [intro] varchar(255),
   [title] varchar(255),
   [type] varchar(255),
   [label_id] varchar(255),
   [info_bubble_text] varchar(255),
   [condition] varchar(255),
   [intensity] INTEGER,
   [conditional_intensity] varchar (255),
   [order] INTEGER,
   [min_value] INTEGER,
   [max_value] INTEGER,
   [active] INTEGER default TRUE,
   [violence_related] INTEGER default FALSE,
   [parent] varchar(255) default null,


   FOREIGN KEY (survey_id)
      REFERENCES survey (survey_id),
   

   FOREIGN KEY (parent)
      REFERENCES survey (survey_id)
);


create table condition(
   [condition_id] INTEGER PRIMARY KEY,
   [question_id] varchar(255) not null,
   [left_operand] varchar(255) not null,
   [operator] varchar(2) not null,
   [right_operand] varchar(255) not null,



   FOREIGN key (question_id) REFERENCES 
      question (question_id),

   FOREIGN key (right_operand) REFERENCES
      question (question_id)
);



CREATE TABLE question_category(
   [category_id] varchar(255) PRIMARY KEY
);

CREATE TABLE question_category_question(
   [question_id] varchar(255),
   [category_id] varchar(255),
   FOREIGN KEY (question_id)
      REFERENCES question (question_id),
   FOREIGN KEY (category_id)
      REFERENCES question_category (category_id)
);

CREATE TABLE choice(
   [question_id] varchar(255),
   [value] varchar(255),
   [label] varchar(255),
   [order] INTEGER,
   PRIMARY KEY (question_id, value),
   FOREIGN KEY (question_id)
    REFERENCES questions (question_id)
);

CREATE TABLE label(
   [label_id] varchar(255),
   [value] varchar(255),
   [label] varchar(255),
   [order] INTEGER,
   PRIMARY KEY (label_id, value)
);

CREATE TABLE answer(
   [question_id] varchar(255) NOT NULL,
   [user_id] varchar(255) NOT NULL,
   [value] varchar(255) NOT NULL,
   [date_created] DATE,
   PRIMARY KEY (question_id, user_id)
);

CREATE TABLE custom_answer(
   [question_id] varchar(255) NOT NULL,
   [user_id] varchar(255) NOT NULL,
   [value] varchar(255) NOT NULL,
   [date_created] DATE,
   PRIMARY KEY (question_id, user_id)
);

CREATE TABLE user(
  [user_id] INTEGER PRIMARY KEY AUTOINCREMENT,
  [email] TEXT,
  [first_name] TEXT,
  [last_name] TEXT,
  [password] TEXT,
  [phone_number] TEXT,
  [date_logged_in] DATE,
  [date_created] DATE,
  [role] TEXT
);


-- migration 

alter table question add column ladderC INTEGER default null;
alter table question add column ladderE INTEGER default null;
alter table question add column ladderV INTEGER default null;


alter table question add column red_flag varchar(255) default null;
alter table question add column past_title varchar(255) default null;






