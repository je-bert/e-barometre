
INSERT INTO survey (
  [survey_id],
  [name],
  [description],
  [color],
  [cover_picture_url],
  [order],
  [status]
) VALUES (
  "B",
  "Base",
  "Description du questionnaire de base",
  "#E2725A",
  "/assets/img/undraw_through_the_park_retouched.png",
  1,
  'active'
),
(
  "H",
  "Historique",
  "Description du questionnaire historique",
  "#E2725A",
  "/assets/img/undraw_through_the_park_retouched.png",
  2,
  'active'
),
(
  "PCRA",
  "Parent répondant (PCR) - partie 1",
  "Description du questionnaire du parent répondant (PCR) - partie 1",
  "#E2725A",
  "/assets/img/undraw_through_the_park_retouched.png",
  3,
  'active'
),
(
  "PFA",
  "Parent favorisé (PFA)",
  "Description du questionnaire du parent favorisé (PFA)",
  "#2D6266",
  "/assets/img/undraw_through_the_park_retouched.png",
  4,
  'active'
),
(
  "E",
  "Enfant",
  "Description du questionnaire de l'enfant",
  "#D39C22",
  "/assets/img/undraw_through_the_park_retouched.png",
  5,
  'active'
),
(



  "PCRB",

  "Parent répondant (PCR) - partie 2",
  "Description du questionnaire du parent répondant (PCR) - partie 2",
  "#E2725A",
  "/assets/img/undraw_through_the_park_retouched.png",
  6,
  'active'
),
(
  "NC",

  "Nouveau·elle conjoint·e (NC)",
  "Description du questionnaire nouveau·elle conjoint·e (NC)",
  "#759693",
  "/assets/img/undraw_through_the_park_retouched.png",
  7,
  'active'
),
(
  "F",
  "Questionnaire de fin",
  "Description du questionnaire de fin",
  "#2D6266",
  "/assets/img/undraw_through_the_park_retouched.png",
  8,
  'active'
);

INSERT INTO question (
  [question_id],
  [survey_id],
  [intro],
  [title],
  [type],
  [label_id],
  [info_bubble_text],
  [condition],
  [intensity],
  [order]
) 

VALUES

 (
  "B00",
  "B",
  NULL,
  "Identification: Qui êtes-vous ?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  0
),
(
  "B01",
  "B",
 NULL,
  "Répondez-vous à ce questionnaire en votre nom ou au nom d'un autre parent ?",
  "select-single",
  NULL,
  "explication modus operandi du questionnaire / application : objectif de l'application : il est possible de répondre à ce questionnaire au nom d'un autre parent (ex.: pour comprendre ce que vit un·e ami·e ou un proche parent. La dynamique familiale à l'étude est celle d'un enfant (un à la fois) et de ses parents.",
  NULL,
  0,
  1
),
(
  "S01",
  "F",
  NULL,
  "À quel groupe d'âge appartenez-vous?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  2
),

(
  "B02",
  "B",
  NULL,
  "Souhaitez-vous faire une analyse au présent ou de manière rétrospective",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  3
),
(
  "B03",
  "B",
  NULL,
  "Quelle a été la durée de vie commune avec l'autre parent (coparent)?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  3
),
(
  "B04",
  "B",
  NULL,
  "Depuis combien de temps êtes vous séparé.e de l'autre parent (coparent)?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  4
),
(
  "B05",
  "B",
  NULL,
  "Combien d'enfants compte la fratrie ?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  5
),
(
  "B07",
  "B",
  NULL,
  "Quelle est votre situation familiale actuelle?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  6
),
(
  "B08",
  "B",
  NULL,
  "Quelle est la situation familiale actuelle de l'autre parent ?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  6
),
(
  "B11",
  "B",
  NULL,
  "Dans quelle mesure l'entente de garde et/ou les droits d'accès sont-ils respectés?",
  "labeled-ladder",
  "E1B",
  "info de base ???  Référence : Roland Broca et Olga Odinetz, Séparations conflictuelles et aliénation parentale : Enfants en danger. Édition Chronique sociale, France, 2016",
  NULL,
  3,
  7
),
(
  "B11a",
  "B",
  NULL,
  "Un jugement concernant la garde des enfants a-t-il été rendu par le tribunal ?",
  "binary",
  NULL,
  NULL,
  "B11>=3",
  0,
  8
),
(
  "B11a1",
  "B",
  NULL,
  "Est-ce que l'autre parent (coparent) respecte les ordonnances ou les jugements de la Cour ?",
  "labeled-ladder",
  "E1B",
  NULL,
 "B11a>=1", 
  2,
  9
),
(
  "B11b",
  "B",
  NULL,
  "Respectez-vous, de votre côté, les ordonnances et entente de garde ?",
  "labeled-ladder",
  "E1B",
  NULL,
  "B11>=3",
  2,
  10
),
(
  "B11c",
  "B",
  NULL,
  "Avez-vous encore un lien et/ou des contacts avec votre enfant ?",
  "select-single",
  NULL,
  "notion rupture de lien \r\nvs \r\nrupture de contact \r\n\r\n\r\nrejet actif vs rejet passif",
  "B11>=3",
  0,
  11
),
(
  "B11c1",
  "B",
  NULL,
  "Quels types de difficultés relationnelles rencontrez-vous ?",
  "select-multiple",
  NULL,
  NULL,
  "B11c>=1", 
  0,
  12
),
(
  "B11c2",
  "B",
  NULL,
  "Est-ce récent ?",
  "select-single",
  NULL,
  NULL,
  "B11c>=1", 
  0,
  13
),
(
  "B11c3",
  "B",
  NULL,
  "Est-ce qu'il y a d'autres enfants en rupture de contact ?",
  "binary",
  NULL,
  "notion rupture de lien \r\nvs \r\nrupture de contact \r\n\r\n\r\nrejet actif vs rejet passif",
  "B11c>=1", 
  0,
  14
),

(
  "B11c4",
  "B",
  NULL,
  "Un traumatisme vécu par vous, le co-parent ou l'enfant pourrait-il expliquer la rupture de contact ou de lien avec votre enfant ?",
  "select-single",
  NULL,
  "Un traumatisme vécu par l'enfant ou par le coparant pourrait expliquer la rupture de contact ou de lien avec votre enfant... Comprendre les raisons qui pourraient pousser l'enfant à s'allier à l'autre parent ou à prendre ses distances … quelques exemples et cas de figures :",
  "B11c>=1", 
  0,
  16
),
(
  "H01",
  "H",
  NULL,
  "Durant la vie commune avec l'autre parent, quel était le degré de complicité entre vous et votre enfant ?",
  "numeric-ladder",
  NULL,
  NULL,
  NULL,
  0,
  0
),
(
  "H02",
  "H",
  NULL,
  "Durant la vie commune avec l'autre parent, dans quelle mesure diriez-vous que votre enfant se confiait naturellement à vous pour ses questionnements, peines et chagrins ou pour partager de bonnes nouvelles ?",
  "numeric-ladder",
  NULL,
  NULL,
  NULL,
  0,
  1
),
(
  "H03",
  "H",
  NULL,
  "Dans quelle mesure diriez-vous que votre enfant idéalisait l’autre parent avant la séparation (éclatement de la famille) ?",
  "numeric-ladder",
  NULL,
  NULL,
  NULL,
  0,
  2
),
(
  "H04",
  "H",
  NULL,
  "Comment qualifieriez-vous la complicité entre votre enfant et l'autre parent avant la séparation (éclatement de votre famille) ?",
  "numeric-ladder",
  NULL,
  NULL,
  NULL,
  0,
  3
),
(
  "H04a",
  "H",
  NULL,
  "Durant la vie commune, dans quelle mesure diriez-vous que la relation entre votre enfant et l'autre parent était fusionnelle ?",
  "numeric-ladder",
  NULL,
  "définir relation fusionnelle : une relation fusionnelle peut être volontaire ou involontaire. Alliance entre un parent et son enfant ….  une relation fusionnelle peut survenir entre mère-enfant et père-enfant // Si la séparation est récente, prévoir un temps d'adaptation, être indulgent, faire valoir sa valeur de coparent, mais éviter les déclencheurs. Privilégier la médiation pour établir des accès.  // L’enfant n’est pas un confident\r\nIl ne faut pas dépasser les limites invisibles de ce qu’un enfant doit savoir ou non. Mais les parents ont tendance à oublier qu’un enfant ne peut pas tout entendre, car il est, même s’il apparaît mature ou assez grand, bien plus fragile qu’un adulte. C’est pourquoi il doit être tenu à l’écart des soucis, de certains secrets ou confidences qui pourraient le fragiliser.  réf.: https://www.aufeminin.com/enfant/parent-enfant-attention-a-la-fusion-s643495.html //. https://www.santemagazine.fr/psycho-sexo/psycho/psycho-enfant/parent-solo-ne-soyez-pas-trop-fusionnel-172034\r\nréf. : Jocelyne Dahan, médiatrice familiale \r\n\r\n(i) Il arrive que l'identité sociale du parent passe par la parentalité...",
  "H04>=5",
  0,
  4
),
(
  "H05",
  "H",
  NULL,
  "Durant la vie commune, arrivait-il que l'autre parent vous critique ou vous dénigre devant votre enfant ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  5
),
(
  "H05a",
  "H",
  NULL,
  "Durant la vie commune, arrivait-il que l'autre parent hausse le ton ou vous insulte (injure) pour imposer son point de vue ou sa volonté ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "H05>=2",
  2,
  6
),
(
  "H06",
  "H",
  NULL,
  "Dans quelle mesure êtes-vous d'accord avec l'énoncé suivant : durant la vie commune l'autre parent percevait votre rôle parental aussi important que le sien.",
  "labeled-ladder",
  "E3B",
  "notion de valeur parentale",
  NULL,
  0,
  7
),
(
  "H06a",
  "H",
  NULL,
  "Durant la vie commune, arrivait-il que l'autre parent présente à votre entourage une vision négative de vos compétences parentales?",
  "labeled-ladder",
  "E1A",
  NULL,
  "H06>=4",
  0,
  7
),
(
  "PCR02",
  "PCRA",
  NULL,
  "Dans quelle mesure devez-vous faire  des compromis pour assurer une bonne entente de garde?",
  "labeled-ladder",
  "E1A",
  NULL,
  "B11<=2",
  0,
  1
),
(
  "PCR03",
  "PCRA",
  NULL,
  "Dans quelle mesure vous arrive-t-il d'éviter ou d'ignorer l’autre parent lorsque vous le croisez à l'école, lors de changement de garde ou lors d'événements sportifs ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  1,
  1
),
(
  "PCR04",
  "PCRA",

  NULL,
  "Dans quelle mesure questionnez-vous votre enfant à son retour de garde afin de connaître la routine (repas, dodo, etc.) et les activités qu'il a fait alors qu'il était chez l'autre parent ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  2
),
(
  "PCR06",
  "PCRA",

  NULL,
  "Dans quelle mesure devez-vous faire un retour sur les interventions (nutrition, hygiène, logistique, etc.) de l'autre parent (par courriel ou texto) au retour des enfants après un séjour de garde ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  3
),
(
  "PCR06a",
  "PCRA",

  NULL,
  "Quels sont les sujets de discorde entre vous et l'autre parent ?",
  "select-multiple",
  NULL,
  NULL,
  "PCR06>=2",
  1,
  4
),
(
  "PCR07",
  "PCRA",

  NULL,
  "Vous arrive-t-il de faire des reproches à l'autre parent devant votre enfant ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  5
),
(
  "PCR08",
  "PCRA",

  NULL,
  "À quelle fréquence appelez-vous votre enfant lorsqu’il est chez l‘autre parent ?",
  "labeled-ladder",
  "E5A",
  NULL,
  NULL,
  1,
  6
),
(
  "PCR09",
  "PCRA",

  NULL,
  "Dans quelle mesure laissez-vous à votre enfant le droit de choisir la fréquence des visites et le temps qu'il passe chez l'autre parent ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  7
),
(
  "PCR00",
  "PCRA",
  "Dans quelle mesure êtes-vous d'accord ou non avec cet énoncé ?",
  "Vous êtes à l'aise en présence de l'autre parent (coparent).",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  0,
  1
),
(
  "PCR00a",
  "PCRA",
  NULL,
  "Dans quelle mesure sentez-vous que vous devez marcher sur des œufs lorsqu'en présence de l'autre parent afin d'éviter les conflits ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "H06>=4",
  0,
  1
),
(
  "PCR00b",
  "PCRA",
  NULL,
  "Dans quelle mesure l'autre parent hausse la voix ou utilise des jurons pour imposer sa vision des choses?",
  "labeled-ladder",
  "E1A",
  NULL,
  "H06>=4",
  0,
  1
),
(
  "PCR01",
  "PCRA",

  NULL,
  "Dans quelle mesure considérez-vous l'autre parent (coparent) comme étant votre égal·e sur le plan parental ?",
  "labeled-ladder",
  "E3B",
  NULL,
  NULL,
  1,
  7
),
(
  "PCR10",
  "PCRA",
  NULL,
  "De manière générale, au-delà des conflits qui pourraient vous opposer à l'autre parent, dans quelle mesure diriez-vous que les exigences de la coparentalité nuit à votre qualité de vie ?",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  1,
  8
),
(
  "PCR11",
  "PCRA",
  NULL,
  "Dans quelle mesure acceptez-vous que les jouets de votre enfant se promène d’une maison à l’autre ?",
  "labeled-ladder",
  "E3B",
  NULL,
  NULL,
  2,
  9
),
(
  "PCR12",
  "PCRA",
  NULL,
  "Dans quelle mesure vous arrive-t-il de prendre des décisions sans consulter l'autre parent ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  10
),
(
  "PCR12a",
  "PCRA",
  NULL,
  "Quel type de décisions avez-vous pris sans consulter l'autre parent ou sans attendre son approbation ?",
  "select-multiple",
  NULL,
  "notion autorité parentale ?",
  "PCR12>=4",
  2,
  11
),
(
  "PCR13",
  "PCRA",
  NULL,
  "Dans quelle mesure diriez-vous que la mauvaise entente entre vous et l'autre parent vous contraint à demander à votre enfant de faire les messages et demandes entourant la logistique familiale ?",
  "labeled-ladder",
  "E4B",
  NULL,
  NULL,
  2,
  12
),
(
  "PCR14",
  "PCRA",
  NULL,
  "Dans quelle mesure être vous d'accord ou non avec cet énoncé : Vous êtes d'avis qu'un enfant de 12 ans est assez mature pour choisir où et avec qui il veut vivre.",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  13
),
(
  "PCR15",
  "PCRA",
  NULL,
  "Dans quelle mesure diriez-vous qu'il est important que votre enfant soit au courant des enjeux de la séparation et du conflit qui vous oppose à l'autre parent ?",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  14
),
(
  "PCR15a",
  "PCRA",
  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation : vous avez mis votre enfant au courant des enjeux juridiques (pension alimentaire, modalité de garde, etc.) qui vous oppose à l’autre parent.",
  "binary",
  NULL,
  NULL,
  "PCR15>=2",
  0,
  15
),
(
  "PCR16",
  "PCRA",
  NULL,
  "Au-delà des conflits, dans quelle mesure acceptez-vous et êtes-vous serein avec la séparation (séparation de couple ou familiale) ?",
  "labeled-ladder",
  "E3B",
  NULL,
  NULL,
  1,
  16
),
(
  "PCR16a",
  "PCRA",
  NULL,
  "Dans quelle mesure diriez-vous que vous confiez à votre enfant votre peine concernant la séparation ?",
  "labeled-ladder",
  "E1B",
  NULL,
  "PCR16>=3",
  2,
  17
),
(
  "PCR17",
  "PCRA",
  NULL,
  "Au retour d’un séjour chez l’autre parent, votre enfant est agressif envers vous et vous accable de reproches. Comment réagissez-vous ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "B07!=0",
  0,
  18
),
(
  "PCR18",
  "PCRA",
  NULL,
  "Si votre enfant vous accuse de mentir, de voler l'argent de l'autre parent, etc. Comment réagissez-vous ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "B07!=0",
  0,
  19
),
(
  "PFA00",
  "PFA",
  NULL,
  "Dans quelle mesure l'autre parent (coparent) doit faire  des compromis pour assurer une bonne entente de garde?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  0,
  0
),
(
  "PFA01",
  "PFA",
  NULL,
  "Comment qualifieriez-vous la relation et le degré de complicité (ou alliance) entre votre enfant et l'autre parent, aujourd'hui ?",
  "numeric-ladder",
  "",
  NULL,
  NULL,
  0,
  0
),
(
  "PFA02",
  "PFA",
  NULL,
  "Selon vous, dans quelle mesure l'autre parent entretien (aujourd'hui) une relation fusionnelle avec votre enfant ?",
  "numeric-ladder",
  "",
  NULL,
  NULL,
  0,
  1
),
(
  "PFA02a",
  "PFA",
  NULL,
  "Diriez-vous que la relation fusionnelle entre votre enfant et l'autre parent est consciente (intentionnelle) ou inconsciente ?",
  "labeled-ladder",
  "",
  NULL,
  "PFA02>=5",
  0,
  2
),
(
  "PFA03",
  "PFA",
  NULL,
  "Selon vous, dans quelle mesure l’autre parent demande à votre enfant de garder des secrets et de vous cacher des choses ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  3
),
(
  "PFA04",
  "PFA",
  NULL,
  "Quelle est la probabilité de l'énoncé suivant ? L’autre parent laisse entendre à votre enfant que vous avez abandonné la famille.",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  1,
  4
),
(
  "PFA04a",
  "PFA",
  NULL,
  "Quelle est la probabilité de l'énoncé suivant ? L’autre parent laisse entendre à votre enfant que vous ne l’aimez pas vraiment.",
  "labeled-ladder",
  "E4A",
  NULL,
  "PFA04>=5",
  2,
  5
),
(
  "PFA05",
  "PFA",
  NULL,
  "Quelle est la probabilité de l'énoncé suivant ? L’autre parent laisse entendre à votre enfant que vous souffrez d’une maladie mentale ou que vous êtes instable psychologiquement.",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  1,
  6
),
(
  "PFA05a",
  "PFA",
  
  NULL,
  "Quelle est la probabilité de l'énoncé ? L'autre parent laisse entendre à votre enfant qu’il ou elle n’est pas en sécurité avec vous.",
  "labeled-ladder",
  "E4A",
  NULL,
  "PFA05>=3",
  2,
  7
),
(
  "PFA06",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent modifie certains faits (historiques) concernant votre passé à la faveur de l'autre parent ou à votre défaveur ?",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  2,
  8
),
(
  "PFA06a",
  "PFA",
  NULL,
  "Dans quelle mesure l'autre parent déforme les souvenirs de votre enfant (ex.: souvenirs heureux de la petite enfance vus aujourd'hui négativement) ?",
  "labeled-ladder",
  "E4A",
  NULL,
  "PFA06>=3",
  3,
  9
),
(
  "PFA07",
  "PFA",
  NULL,
  "Quelle est la probabilité de l'énoncé suivant :  l’autre parent culpabilise votre enfant de sa relation ou de son amour pour vous ?",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  1,
  10
),
(
  "PFA07a",
  "PFA",
  NULL,
  "Arrive-t-il que l’autre parent boude votre enfant ou se fâche lorsqu'il est temps de rentrer chez vous (à votre tour de garde)?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA07>=3",
  2,
  11
),
(
  "PFA07a1",
  "PFA",
  NULL,
  "Arrive-t-il à l’autre parent de se fâcher contre votre enfant lorsqu'il ou elle exprime de l'affection pour vous ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA07a>=3",
  3,
  12
),
(
  "PFA09",
  "PFA",
  NULL,
  "Arrive-t-il que l'autre parent vous accable de reproches par courriel ou texto au retour des enfants (après un séjour chez vous) ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  1,
  13
),
(
  "PFA09a",
  "PFA",
  NULL,
  "Dans quelle mesure l'autre parent fait ou a déjà fait des menaces (claires ou voilées) de vous enlever les enfants ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA09>=3",
  2,
  14
),
(
  "PFA10",
  "PFA",
  NULL,
  "Dans quelle mesure l’autre parent vous ignore lorsqu’il ou elle vous croise à l’école, lors des changements de garde ou lors d'événements sportifs?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  1,
  15
),
(
  "PFA11",
  "PFA",
  NULL,
  "L'autre parent est d'avis que votre enfant est assez mature pour choisir où et avec qui il veut vivre ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "B11>=3",
  2,
  16
),
(
  "PFA11a",
  "PFA",
  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? L'autre parent vous demande de respecter les désirs et choix de votre enfant.",
  "labeled-ladder",
  "E3A",
  NULL,
  "PFA11>=3",
  3,
  17
),
(
  "PFA12",
  "PFA",
  NULL,
  "Selon vous, dans quelle mesure l'autre parent questionne votre enfant à son retour de garde sur les activités qu'il a fait alors qu'il était chez vous?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  1,
  18
),
(
  "PFA13",
  "PFA",
  NULL,
  "Arrive-t-il que l’autre parent vous dénigre en la présence de votre enfant ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  0,
  19
),
(
  "PFA13a",
  "PFA",
  NULL,
  "Dans quelle mesure l'autre parent vous renvoie une image négative de vous-même en tant que parent, ridiculise vos décisions ou vous insulte ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA09a==0&&PFA13>=3",
  3,
  20
),
(
  "PFA13b",
  "PFA",
  NULL,
  "Dans quelle mesure l'autre parent fait ou a déjà fait des menaces (claires ou voilées) de vous enlever les enfants ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA09a==0&&PFA13>=3",
  3,
  21
),
(
  "PFA13c",
  "PFA",
  NULL,
  "Dans quelle mesure l'autre parent présente aux autres une vision négative de vos comportements ou de votre santé mentale (compétences parentales).",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA13>=3",
  2,
  22
),
(
  "PFA14",
  "PFA",
  NULL,
  "Arrive-t-il que l’autre parent dénigre ouvertement votre nouvelle famille devant votre enfant ?  (i.e: dénigrement du nouveau ou nouvelle conjoint·e et/ou enfant(s) né(s) d’une nouvelle union)",
  "labeled-ladder",
  "E1A",
  NULL,
  "B07!=0",
  1,
  23
),
(
  "PFA15",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent laisse entendre que la 'vraie' famille de votre enfant est avec l’autre parent, le nouveau ou nouvelle conjoint·e et/ou la nouvelle fratrie ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "B08!=0",
  2,
  24
),
(
  "PFA15a",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent demande à ce que votre enfant appelle le nouveau ou nouvelle conjoint·e maman ou papa ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "B08!=0&&PFA15>=3",
  3,
  25
),
(
  "PFA16",
  "PFA",
  NULL,
  "Évaluez la fréquence de l'énoncé : l'autre parent vous impose des changements d’horaires sans vous consulter au préalable et sans votre autorisation.",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  26
),
(
  "PFA16a",
  "PFA",
  NULL,
  "Évaluez l'intensité et la fréquence de l'énoncé : l'autre parent ramène votre enfant à la maison à l'heure qui lui convient (sans respecter l'entente initiale).",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA16>=2",
  2,
  27
),
(
  "PFA16b",
  "PFA",
  NULL,
  "Évaluez la fréquence de l'énoncé : l’autre parent organise et propose des activités à votre enfant sur votre temps de garde.",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA16>=2",
  2,
  28
),
(
  "PFA16b1",
  "PFA",
  NULL,
  "Arrive-t-il que l’autre parent propose des activités amusantes, voire irrésistibles à votre enfant alors que c’est votre week-end ou votre semaine avec votre enfant ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "TODO", -- TODO
  3,
  29
),
(
  "PFA17",
  "PFA",
  NULL,
  "Évaluez la fréquence de l'énoncé : l’autre parent se présente à la sortie des classes, au service de garde ou à la garderie sur votre temps de garde.",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  1,
  30
),
(
  "PFA18",
  "PFA",
  NULL,
  "Évaluez la fréquence et l'intensité de l'énoncé : l’autre parent impose sa présence en appelant (ou en textant) régulièrement votre enfant durant votre temps de garde.",
  "labeled-ladder",
  "E5A",
  NULL,
  NULL,
  1,
  31
),
(
  "PFA19",
  "PFA",
  NULL,
  "Dans quelle mesure l'autre parent vous communique les informations médicales, scolaires ou liées aux activités sociales ou sportives de votre enfant ?",
  "labeled-ladder",
  "E1B",
  NULL,
  NULL,
  2,
  32
),
(
  "PFA19a",
  "PFA",

  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent interdit aux personnes gravitant autour de votre enfant (professeurs, éducateurs, medecins, entraîneurs, etc.) de vous communiquer de l'information à son sujet ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "PFA19>=3",
  3,
  33
),
(
  "PFA20",
  "PFA",
  NULL,
  "Comment évalueriez-vous la facilité à communiquer avec votre enfant lorsqu’il est chez l’autre parent?",
  "labeled-ladder",
  "E3B",
  NULL,
  NULL,
  1,
  34
),
(
  "PFA20a",
  "PFA",

  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent contrôle, écoute ou écourte vos conversations téléphoniques avec votre enfant (lorsque chez l’autre parent) ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA20>=3",
  2,
  35
),
(
  "PFA20b",
  "PFA",
  NULL,
  "Arrive-t-il que l'autre parent vous harcèle (tél. courriel, etc.) ou se présente à votre lieu de travail ou votre domicile sans s'annoncer ou sans invitation?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA20>=3",
  3,
  36
),
(
  "PFA20c",
  "PFA",
  NULL,
  "Arrive-t-il que l'autre parent vous accable de questions ou de reproches (harcèle) par téléphone ou par courriel?",
  "labeled-ladder",
  "E1A",
  NULL,
  "H06>=4",
  3,
  37
),
(
  "PFA21",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent vous considère comme étant son égal·e sur le plan parental ?",
  "labeled-ladder",
  "E3B",
  NULL,
  NULL,
  1,
  37
),
(
  "PFA21a",
  "PFA",
  NULL,

  "Dans quelle mesure cet énoncé s'applique-t-il selon vous? L'autre parent sent qu’il est en compétition avec vous pour l’amour de votre enfant ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "TODO", -- TODO
  2,
  38
),
(
  "PFA22",
  "PFA",
  NULL,
  "Dans quelle mesure cet énoncé s'applique-t-il selon vous? L'autre parent estime que les exigences de la coparentalité (logistique horaire, transport, compromis vacances, etc.) nuit à sa qualité de vie.",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  1,
  39
),
(
  "PFA23",
  "PFA",
  NULL,

  "Dans quelle mesure diriez-vous que l'identité et la valeur sociale de l'autre parent passe par sa paternité ou sa maternité?",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  1,
  40
),
(
  "PFA24",
  "PFA",
  NULL,
  "Quelle est la probabilité de l'énoncé : depuis la séparation, l’autre parent cherche à vous blesser ou à se venger parce que vous avez brisé ou abandonné la famille ?",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  2,
  41
),
(
  "PFA25",
  "PFA",
  NULL,
  "Dans quelle mesure l'autre parent vous appelle par votre prénom devant votre enfant (versus maman ou papa) ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  1,
  42
),
(
  "PFA25a",
  "PFA",
  NULL,
  "Cette façon de s'adresser à vous devant l'enfant (prénom versus maman ou papa), est-elle habituelle ou est-ce nouveau depuis la séparation ?",
  "select-single",
  NULL,
  NULL,
  "PFA25>=3",
  2,
  43
),
(
  "PFA26",
  "PFA",
  NULL,
  "Dans quelle mesure cet énoncé s'applique-t-il selon vous? L’autre parent considère que son nouveau ou nouvelle conjoint·e est un meilleur parent que vous.",
  "labeled-ladder",
  "E4A",
  NULL,
  "B08!=0",
  2,
  44
),
(
  "PFA27",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l’autre parent cherche à limiter les contacts entre votre enfant et votre famille élargie (cousin.es, oncles, tantes, grands-parents, etc.)",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  45
),
(
  "PFA28",
  "PFA",
  NULL,
  "Dans quelle mesure cet énoncé s'aplique à votre situation ? L’autre parent permet à votre enfant d'apporter des objets (jouets ou objets symboliques) ou cadeaux reçus provenant de chez vous :",
  "labeled-ladder",
  "E1B",
  NULL,
  NULL,
  2,
  46
),
(
  "PFA28a",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l’autre parent jette les cadeaux (anniveraire, Noël) ou proscrit les photographies de vous dans sa demeure ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA28>=3",
  3,
  47
),
(
  "PFA29",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent se dit impuissant et non responsable de la décision de votre enfant de ne plus respecter l'entente de garde ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "B11>=3",
  3,
  48
),
(
  "PFA29b",
  "PFA",
  NULL,
  "Avez-vous été déchu·e (totalement ou en partie) de votre autorité parentale ?",
  "binary",
  NULL,
  NULL,
  "PFA29>=3",
  1,
  49
),
(
  "PFA29a",
  "PFA",
  NULL,
  "Quelles décisions ont été prises sans votre consentement ou connaissance de votre part ?",
  "select-multiple",
  NULL,
  NULL,
  "PFA29>=3",
  0,
  50
),
(
  "PFA30",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l’autre parent force votre enfant à choisir entre ses deux parents ?",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  3,
  51
),
(
  "PFA30a",
  "PFA",
  NULL,
  "Dans quelle mesure diriez-vous que l’autre parent cherche à vous exclure de la vie de votre enfant?",
  "labeled-ladder",
  "E4A",
  NULL,
  "PFA30>=3",
  3,
  52
),
(
  "PFA30a1",
  "PFA",

  NULL,
  "Dans quelle mesure l'autre parent fait ou a déjà fait des menaces (claires ou voilées) de vous enlever les enfants ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "PFA09a==0&&PFA13b==0&&PFA30a>=3",
  3,
  53
),
(
  "PFA30a2",
  "PFA",

  NULL,
  "Quels sont les comportements ou attitudes qui vous laissent croire que l'autre parent cherche à vous exclure de la vie de votre enfant?",
  "select-multiple",
  NULL,
  NULL,
  "PFA30a>=3",
  0,
  54
),
(
  "PFA31",
  "PFA",

  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent accepte ou vit bien avec la séparation (séparation de couple ou familiale) ?",
  "labeled-ladder",
  "E3B",
  NULL,
  NULL,
  1,
  55
),
(
  "PFA31a",
  "PFA",

  NULL,
  "Dans quelle mesure diriez-vous que l’autre parent confie à votre enfant sa peine concernant la séparation ?",
  "labeled-ladder",
  "E1B",
  NULL,
  "PFA31>=3",
  2,
  56
),
(
  "PFA31a1",
  "PFA",

  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent se confie à votre enfant sur des sujets qui vous sont personnels ou concernent votre passé (intime) ?",
  "labeled-ladder",
  "E1B",
  NULL,
  "PFA31a>=3",
  2,
  57
),
(
  "PFA32",
  "PFA",

  NULL,
  "Dans quelle mesure cet énoncé s'applique-t-il à votre situation ? L'autre parent fait lire vos échanges et communications (textos, messenger, courriels) à votre enfant.",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  58
),
(
  "PFA33",
  "PFA",

  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent encourage ou entretient un discours dénigrant ou haineux à l’égard de votre nouveau ou nouvelle conjoint·e",
  "labeled-ladder",
  "E3A",
  NULL,
  "B07!=0",
  2,
  59
),
(
  "PFA34",
  "PFA",

  NULL,
  "L’autre parent refuse de vous parler et demande à votre enfant de faire les messages et autres demandes entourant la logistique familiale",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  60
),
(
  "PFA35",
  "PFA",

  NULL,
  "Dans quelle mesure l’autre parent laisse à votre enfant le droit de choisir de respecter ou non l'entente de garde et votre temps (tour) de garde ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "B11>=3",
  3,
  61
),
(
  "PFA37",
  "PFA",

  NULL,
  "Dans quelle mesure diriez-vous que l'autre parent demande à votre enfant de choisir avec quel parent il veut vivre ?",
  "labeled-ladder",
  "E3A",
  NULL,

  "B11>=3", 
  NULL,
  62
),
(
  "PFA38",
  "PFA",

  NULL,
  "Selon vous, quels sont les enjeux les plus importants pour l'autre parent au niveau de la garde des enfants?",
  "select-multiple",
  NULL,
  NULL,

  "B11>=3", -- TODO
  NULL,
  63
),
(
  "E01",
  "E",
  NULL,

  "Comment qualifieriez-vous votre relation (harmonie) et votre degré de complicité avec votre enfant aujourd’hui ?",
  "numeric-ladder",
  NULL,
  NULL,
  NULL,
  0,
  0
),
(
  "E02",
  "E",

  NULL,
  "Dans quelle mesure diriez-vous que votre enfant idéalise (aujourd'hui) l’autre parent ?",
  "numeric-ladder",
  NULL,
  NULL,
  NULL,
  0,
  1
),
(
  "E02a",
  "E",
  
  NULL,
  "Dans quelle mesure diriez-vous que la relation entre votre enfant et l'autre parent est fusionnelle ?",
  "numeric-ladder",
  NULL,
  "définir relation fusionnelle + Mise en garde d'une relation fusionelle non intentionnelle … patience et bienveillance de mise \r\n(ex.: Frédéric J + Nancy N) + recommandation médiation",
  "E02>=5",
  0,
  2
),
(
  "E03",
  "E",
  
  NULL,
  "Dans quelle mesure cet énoncé s'applique-t-il à votre situation ? Votre enfant garde des secrets et vous cache de l'information concernant sa relation avec l'autre parent.",
  "labeled-ladder",
  "E3A",
  "",
  NULL,
  1,
  3
),
(
  "E03a",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique-t-il à votre situation ? Votre enfant a reçu l’ordre de ne pas vous raconter ce qui se passe chez l’autre parent.",
  "labeled-ladder",
  "E3A",
  NULL,
  "E03>=3",
  2,
  4
),
(
  "E04",
  "E",

  NULL,
  "Dans quelle mesure êtes-vous d'accord avec l'énoncé suivant ? Votre enfant défend systématiquement l'autre parent, quoi que vous fassiez, quoi que vous disiez.",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  5
),
(
  "E04a",
  "E",

  NULL,

  "Dans quelle mesure êtes-vous d'accord avec l'énoncé suivant? Aux yeux de votre enfant, tout ce que fait l'autre parent est bien, voire parfait, et tout ce que vous faites est mauvais ou sujet à critiques ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "E04>=3",
  3,
  6
),
(
  "E05",
  "E",

  NULL,
  "Dans quelle mesure diriez-vous que votre enfant s’exprime avec des expressions ou des paroles empruntées à l’autre parent ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  7
),
(
  "E05a",
  "E",
NULL,

  "Dans quels contextes ou à quelles occasions cela se produit-il ?",
  "select-multiple",
  NULL,
  NULL,
  "E05>=3",
  2,
  8
),
(
  "E05a1",
  "E",

  NULL,
  "À quelle fréquence cela se produit-il au retour d'un séjour (garde) de l'autre parent?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E05a==0",
  0,
  9
),
(
  "E05a2",
  "E",

  NULL,
  "À quelle fréquence cela se produit-il lorsque l'enfant est en présence de l'autre parent?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E05a==1",
  0, -- TODO
  10
),
(
  "E05a3",
  "E",

  NULL,
  "À quelle fréquence cela se produit-il lorsque mon enfant cherche à me convaincre de passer plus de temps chez l'autre parent?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E05a==2",
  0, -- TODO
  11
),
(
  "E05a4",
  "E",

  NULL,
  "À quelle fréquence cela se produit-il lorsque mon enfant me fait des reproches?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E05a==3",
  0, -- TODO
  12
),
(
  "E06",
  "E",

  NULL,
  "Dans quelle mesure diriez-vous que votre enfant vous accuse ou vous reproche d'avoir abandonné la famille ?",
  "labeled-ladder",
  "E1A",
  "Note : Je crois qu'on peut se permettre de faire un peu d'éducation, ici. \r\n\r\nIl est important de sécuriser et rassurer un enfant qui en vient à croire que son parent a abandonné la famille ou qu'il ou elle a été abandonné par conséquent. Si cette réflexion vous semble être induite par l'autre parent, référez-vous à la méthode ADR afin de vous assurer de ne pas aggraver le conflit ou l'instrumentalisation possible de l'enfant.",
  NULL,
  1,
  13
),
(
  "E06a",
  "E",

  NULL,
  "Évaluez la fréquence ou l'intensité de l'énoncé : votre enfant croit que vous souffrez d’une maladie mentale ou que vous êtes instable psychologiquement ?",
  "labeled-ladder",
  "E4A",
  "Idem ? Texte adapté pour la maladie mentale / instabilité psychologique ?",
  "E06>=3",
  3,
  14
),
(
  "E06a1",
  "E",

  NULL,
  "Évaluez la fréquence ou l'intensité de l'énoncé : votre enfant vous reproche ou vous accuse d'être dangereux.se ou de présenter un danger pour sa sécurité.",
  "labeled-ladder",
  "E4A",
  "Idem ? Texte adapté pour la dangerosité ?",
  "E06a>=3",
  3,
  15
),
(
  "E07",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique-t-il à votre situation : votre enfant se sent coupable de passer du temps avec vous car cela indispose, contrarie ou fait de la peine à l'autre parent ?",
  "labeled-ladder",
  "E3A",
  "Notion de conflit de loyauté et de parentification. \r\n\r\nIl est important de rassurer un enfant et l'amner à retrouver sa 'position' d'enfant et non de 'parent de son parent'. \r\n\r\nhttps://www.psychologies.com/Famille/Relations-familiales/Parents/Articles-et-Dossiers/Parentification-de-l-enfant-ces-parents-qui-inversent-les-roles",
  NULL,
  1,
  16
),

(
  "E9",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique-t-il à votre situation ? Votre enfant vous tient responsable de la peine (détresse) de son autre parent.",
  "labeled-ladder",
  "E6",
  NULL,
  NULL,
  1,
  18
),
(
  "E10",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique-t-il à votre situation ? Votre enfant cherche à vous convaincre des qualités de l’autre parent.",
  "labeled-ladder",
  "E1A",
  "Principe de base ? \r\nUn enfant qui cherche à convaincre son parent des qualités de son autre parent est un enfant qui demande indirectement que vous lui donniez le droit d'aimer son parent malgré ses imperfections.  \r\n\r\nnous vous invitons à vous référer à la méthode ADR \r\n\r\n",
  NULL,
  2,
  19
),
(
  "E11",
  "E",

  NULL,
  "Dans quelle mesure votre enfant vous ignore lorsqu’il ou elle est en compagnie de l'autre parent et qu'il vous croise à l’école, lors d'événements sportifs, etc. ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  20
),
(
  "E12",
  "E",

  NULL,
  "Arrive-t-il que votre enfant dénigre vos compétences parentales devant l’autre parent ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  21
),
(
  "E13",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? Votre enfant dénigre ouvertement votre nouvelle famille (nouveau conjoint + enfant(s) né(s) d’une nouvelle union).",
  "labeled-ladder",
  "E1A",
  NULL,
  "B07!=0",
  2,
  22
),
(
  "E14",
  "E",

  NULL,
  "Dans quelle mesure votre enfant laisse-t-il ou elle entendre que sa 'vraie' famille est avec l’autre parent ?",
  "labeled-ladder",
  "E3A",
  "Si cette idée vient de l'autre parent, il faut faire attention au CL \r\nOuvrir un dialogue, discussion franche avec l'enfant / mobilisation / impliquer l'enfant dans la recherche de solutions",
  "B08!=0",
  2,
  23
),
(
  "E14a",
  "E",

  NULL,
  
  "Dans quelle mesure diriez-vous que pour votre enfant, la nouvelle famille de l'autre parent (famille recomposée ou non) a plus de valeur que la vôtre ?",
  "labeled-ladder",
  "E3A",
  NULL,
  "E14>=3",
  3,
  24
),
(
  "E15",
  "E",

  NULL,
  "Évaluez l'intensité et la fréquence de l'énoncé : il arrive à votre enfant d'être agressif envers vous à son retour d'un séjour chez l'autre parent.",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  2,
  25
),
(
  "E15a",
  "E",

  NULL,
  "Évaluez la fréquence et/ou l'intensité de l'énoncé : votre enfant vous accuse de voler de l’argent à son autre parent ou d'être responsable de son apauvrissement ?",
  "labeled-ladder",
  "E4A",
  "Méthode ADR",
  "E15>=3",
  1,
  26
),
(
  "E16",
  "E",

  NULL,
  "Dans quelle mesure votre enfant demande à changer les horaires de garde et de visite à la faveur de l'autre parent?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  27
),
(
  "E16a",
  "E",

  NULL,
  "Dans quelle mesure votre enfant impose des changements d’horaires et de visite à la faveur de l'autre parent sans vous consulter au préalable et sans votre autorisation ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E16>=3",
  3,
  28
),
(
  "E16b",
  "E",

  NULL,
  "Arrive-t-il à votre enfant de changer d’idée concernant une activité prévue à l’horaire avec vous? D’abord enthousiaste, il trouve (subitement / dernières minutes) des excuses pour ne pas participer à l’activité ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E16>=3",
  2,
  29
),
(
  "E16c",
  "E",

  NULL,
  "Évaluez l'intensité et/ou la fréquence de l'énoncé : votre enfant subit une pression pour passer plus de temps chez l'autre parent?",
  "labeled-ladder",
  "E4A",
  NULL,
  "E16>=3",
  2,
  30
),
(
  "E18",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? Votre enfant ne répond pas à vos messages (texto, messenger, instagram, etc.) lorsqu’il est chez l’autre parent.",
  "labeled-ladder",
  "E1A",
  "Apprendre à lire les signes : différences entre un enfant pressé d'aller jouer et un enfant qui est bête et se comporte différemment et de manière presque arrogante (pour le bénéfice d l'autre parent qui écroute). \r\n\r\nATTN : pression sur l'enfant / ne pas prendre ombrage du fait que l'enfant est bête au téléphone.",
  NULL,
  2,
  31
),
(
  "E20",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? Votre enfant considère le nouveau conjoint ou à la nouvelle conjointe comme son père ou sa mère.",
  "labeled-ladder",
  "E1A",
  "??? \r\nImportant pour un enfant que les frontières soient claires et que la valeur symbolique soit respectée",
  "B08!=0",
  2,
  32
),
(
  "E21",
  "E",

  NULL,
  "Êtes-vous d'accord ou pas d'accord avec l'énoncé suivant : les jouets et les vêtements de votre enfant se promène d’une maison à l’autre simplement.",
  "labeled-ladder",
  "E3B",
  "???\r\nOn veut pas faire la morale … mais devrait-on informer sur le stress que cela impose à l'enfant, ce refus de la preésence de l'autre parent ?",
  NULL,
  1,
  33
),
(
  "E21a",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? L'autre parent refuse que votre enfant apporte des objets qui proviennent de votre demeure ou de votre milieu.",
  "labeled-ladder",
  "E1A",
  NULL,
  "E21>=3",
  2,
  34
),
(
  "E22",
  "E",

  NULL,
  "Dans quelle mesure êtes-vous d'accord avec l'énoncé suivant ? Votre enfant connait des informations personnelles ou intimes de vous dont vous n'avez jamais discuté avec lui.",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  35
),
(
  "E22a",
  "E",

  NULL,
  "Les souvenirs de votre enfant commencent à être déformés (ex.: souvenirs heureux de la petite enfance vus aujourd'hui négativement).",
  "labeled-ladder",
  "E3A",
  NULL,
  "E22>=3",
  3,
  36
),
(
  "E17",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? Votre enfant tient le rôle de messager et a la responsabilité de vous communiquer les informations concernant la logistique familiale (ex. : horaires école et activités sportives, gestion lunch, vêtements, etc.).",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  1,
  37
),
(
  "E23",
  "E",

  NULL,
  "Dans quelle mesure êtes-vous d'accord avec l'énoncé suivant ? Votre enfant se sent responsable du bonheur de l’autre parent et/ou sent le besoin de le protéger.",
  "labeled-ladder",
  "E3A",
  "parentification /",
  NULL,
  1,
  38
),
(
  "E24",
  "E",

  NULL,
  "Dans quelle mesure êtes-vous d'accord avec l'énoncé suivant : votre enfant a été informé du contexte juridique, financier et autres associé au conflit vous opposant à l'autre parent par l'autre parent",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  39
),
(
  "E25",
  "E",

  NULL,
  "Dans quelle mesure diriez-vous que votre enfant sent le besoin de protéger l’autre parent ou de défendre ses intérêts ?",
  "labeled-ladder",
  "E4A",
  "idem q-E23",
  NULL,
  2,
  40
),
(
  "E26",
  "E",

  NULL,
  "Dans quelle mesure diriez-vous que le comportement et/ou l'attitude de votre enfant change en présence de l’autre parent ?",
  "labeled-ladder",
  "E4A",
  "point d'info visible sur fréquence =+3",
  NULL,
  2,
  41
),
(
  "E27",
  "E",

  NULL,
  "Dans quelle mesure notez-vous un changement au niveau du comportement de votre enfant à son retour de garde ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  42
),
(
  "E27a",
  "E",

  NULL,
  "De manière générale, au retour d'un séjour chez l'autre parent, votre enfant vous paraît :",
  "select-multiple",
  NULL,
  NULL,
  "E27>=3",
  0,
  43
),
(
  "E27b",
  "E",

  NULL,
  "Évaluez la fréquence et l'intensité de l'énoncé : au retour d’un séjour chez l’autre parent, votre enfant vous questionne sur vos décisions présentes ou passsées ou vous accable de reproches ?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E27>=3",
  2,
  44
),
(
  "E28",
  "E",

  NULL,
  "Dans quelle mesure votre enfant s'isole (ex.: chambre) ou se cache (ex.: toilettes) pour appeler son autre parents afin qu'on n'entende pas ses conversations ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  45
),
(
  "E29",
  "E",

  NULL,
  "Dans quelle mesure diriez-vous que votre enfant a changé ou adapté ses champs d’intérêts pour partager de plus en plus les intérêts de l’autre parent ?",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  2,
  46
),
(
  "E29a",
  "E",

  NULL,
  "Évaluez la fréquence et l'intensité de l'énoncé : votre enfant rejette de plus en plus vos valeurs et vos champs d’intérêts.",
  "labeled-ladder",
  "E4A",
  NULL,
  "E29>=3",
  3,
  47
),
(
  "E30",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique votre situation? Votre enfant réclame le droit de choisir les moments où il vous rend visite et la durée des visites chez vous.",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  48
),
(
  "E31",
  "E",

  NULL,
  "Évaluez la fréquence et l'intensité de l'énoncé : votre enfant calque les désirs et les paroles de l’autre parent.",
  "labeled-ladder",
  "E4A",
  NULL,
  "E05>=3",
  3,
  49
),
(
  "E32",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? Votre enfant vous accuse de mentir, de voler, etc.",
  "labeled-ladder",
  "E4A",
  NULL,
  "E04>=3",
  2,
  50
),
(
  "E33",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? Votre enfant vous reproche de ne pas le respecter (choix, besoins, désirs, rythme, etc.)",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  3,
  51
),
(
  "E33a",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? Votre enfant a déjà demandé à changer les termes de la garde afin de passer plus de temps chez l’autre parent",
  "labeled-ladder",
  "E1A",
  NULL,
  "E33>=3",
  2,
  52
),
(
  "E33b",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation ? Votre enfant vous a déjà annoncé qu’à 12 ou 14 ans, il ou elle pourrait choisir les modalités de garde et vivre là où bon lui semble",
  "labeled-ladder",
  "E1A",
  NULL,
  "E33>=3",
  3,
  53
),
(
  "E34",
  "E",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation? Votre enfant vous a bloqué des réseaux sociaux (cell/texto, messenger, instagram).",
  "labeled-ladder",
  "E1A",
  "mobilisation / notion de rejet actif ou rejet passif",
  "B11c>=1",
  3,
  54
),
(
  "E35",
  "E",

  NULL,
  "Dans quelle mesure diriez-vous que votre enfant refuse les contacts avec votre famille élargie (grands-parents, cousin.es, etc.)",
  "labeled-ladder",
  "E1A",
  NULL,
  "B11c>=1",
  1,
  55
),
(
  "E35a",
  "E",

  NULL,
  "Comment était la relation avec la famille élargie avant la séparation?",
  "labeled-ladder",
  "E2A",
  NULL,
  "E35>=3",
  1,
  56
),
(
  "E36",
  "E",

  NULL,
  "Votre enfant présente-il / elle des troubles psychosomatiques en ce moment?",
  "binary",
  NULL,
  NULL,
  NULL,
  0,
  57
),
(
  "E36a",
  "E",

  NULL,
  "Quelles sont les manifestations ou troubles psychosomatiques présents chez votre enfant?",
  "select-multiple",
  NULL,
  "Infos de base pour expliquer que les CSS, CL et les dynamiques d’AP amène des manifestations et symptômes psychosomatiques : À surveiller / Invitation à consulter un professionnel de la santé (TS / Psychologue)",
  NULL,
  0,
  58
),
(
  "E36a1",
  "E",

  NULL,
  "À quelle fréquence observez-vous des manifestations d'automutilation?",
  "labeled-ladder",
  "E1A",
  NULL,
 NULL,
  0,
  59
),
(
  "E36a2",
  "E",

  NULL,
  "À quelle fréquence observez-vous des manifestations d'anxiété?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36a==1",
  NULL, -- TODO
  60
),
(
  "E36a3",
  "E",

  NULL,
  "À quelle fréquence observez-vous des manifestations de dépression?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36a==2",
  NULL, -- TODO
  61
),
(
  "E36a4",
  "E",

  NULL,
  "À quelle fréquence observez-vous des manifestations d'idéation suicidaire?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36a==3",
  NULL, -- TODO
  62
),
(
  "E36a5",
  "E",

  NULL,
  "À quelle fréquence observez-vous des manifestations d'insomnie?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36a==4",
  NULL, -- TODO
  63
),
(
  "E36a6",
  "E",

  NULL,
  "À quelle fréquence observez-vous des manifestations d'isolement et de difficulté à socialiser",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36a==5",
  NULL, -- TODO
  64
),
(
  "E36a7",
  "E",

  NULL,
  "À quelle fréquence observez-vous un trouble de l'opposition?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36a==6",
  NULL, -- TODO
  65
),
(
  "E36a8",
  "E",

  NULL,
  "À quelle fréquence observez-vous un trouble alimentaire?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36a==7",
  NULL, -- TODO
  66
),
(
  "E36b",
  "E",

  NULL,
  "Lesquelles de ces manifestations étaient déjà apparentes avant la séparation?",
  "select-multiple",
  NULL,
  "Info / éducation : normal pour l'enfant de revenir chargé si l'enfant est exposé à un conflit",
  NULL, -- TODO
  0,
  67
),
(
  "E36b1",
  "E",

  NULL,
  "À quelle fréquence observiez-vous déjà des manifestations d'automutilation?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36b==0",
  NULL, -- TODO
  68
),
(
  "E36b2",
  "E",

  NULL,
  "À quelle fréquence observiez-vous déjà des manifestations d'anxiété?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36b==1",
  NULL, -- TODO
  69
),
(
  "E36b3",
  "E",

  NULL,
  "À quelle fréquence observiez-vous déjà des manifestations de dépression?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36b==2",
  NULL, -- TODO
  70
),
(
  "E36b4",
  "E",

  NULL,
  "À quelle fréquence observiez-vous déjà des manifestations d'idéation suicidaire?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36b==3",
  NULL, -- TODO
  71
),
(
  "E36b5",
  "E",

  NULL,
  "À quelle fréquence observiez-vous déjà des manifestations d'insomnie?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36b==4",
  NULL, -- TODO
  72
),
(
  "E36b6",
  "E",

  NULL,
  "À quelle fréquence observiez-vous déjà des manifestations d'isolement et de difficulté à socialiser?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36b==5",
  NULL, -- TODO
  73
),
(
  "E36b7",
  "E",

  NULL,
  "À quelle fréquence observiez-vous déjà un trouble de l'opposition?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36b==6",
  NULL, -- TODO
  74
),
(
  "E36b8",
  "E",

  NULL,
  "À quelle fréquence observiez-vous déjà un trouble alimentaire?",
  "labeled-ladder",
  "E1A",
  NULL,
  "E36b==7",
  NULL, -- TODO
  75
),
(
  "PCR19",


  "PCRB",


  NULL,

  "Au retour d’un séjour chez l’autre parent, votre enfant est agressif envers vous et vous accable de reproches. Comment réagissez-vous ?",
  "select-single",
  NULL,
  "Info / éducation : normal pour l'enfant de revenir chargé si l'enfant est exposé à un conflit",
  NULL,
  NULL, -- TODO
  0
),
(
  "PCR20",

  "PCRB",


  NULL,


  "Si votre enfant vous accuse de mentir, de voler l'argent de l'autre parent, etc. Comment réagissez-vous ?",
  "select-single",
  NULL,
  "Info / éducation ADR ici ?    \r\nRéférence : Méthode ADR du CAP : se référer à la méthode ADR",
  NULL,
  NULL, -- TODO
  1
),
(
  "NC01",
  "NC",

  NULL,
  "Dans quelle mesure êtes-vous d'acord avec l'énoncé suivant ? Le nouveau ou nouvelle conjoint·e joue un rôle de confident·e auprès de votre enfant ?",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  1,
  0
),
(
  "NC01a",
  "NC",

  NULL,
  "Dans quelle mesure cette relation de confident.e vous apparaît être malsaine?",
  "labeled-ladder",
  "E4A",
  "Une forte et belle complicité entre votre enfant et le nouveau ou nouvelle conjoint·e peut-être très positive si elle n'interfère pas avec votre relation avec votre enfant. Si la complicité entre votre enfant et le nouveau ou nouvelle conjoint·e existe et se déploie au détriment de votre relation avec votre enfant, faites-vous aider par un.e professionnel·le (TS / psychologue), une autorité morale neutre qui permettra aux deux relations de co-exister.",
  "NC01>=3",
  2,
  1
),
(
  "NC02",
  "NC",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation? Le nouveau ou nouvelle conjoint·e laisse entendre à votre enfant qu’il ou elle n’est pas en sécurité avec vous.",
  "labeled-ladder",
  "E4A",
  "exposer ce que ça veut dire / impact sur l'enfant / importance de sécuriser l'enfant \r\nimportantce d'intervenir ou non \r\nquelques conseils de base \r\n\r\nimportant de faire la différence entre une réelle perception de danger chez l'enfant et un message indirect de l'autre parent que l'enfant reprend à son compte. Important de différencier également l'emprise chez un enfant entre recracher les paroles de l'autre parent et l'enfant reprend à son compte le message (rejet actif) Sentiment d'insécurité induit par l'autre parent ? Un accompagnement ou un support psychologique serait",
  NULL,
  2,
  2
),
(
  "NC03",
  "NC",

  NULL,
  "Dans quelle mesure le nouveau ou nouvelle conjoint·e vous ignore lorsqu’il vous croise à l’école, lors des changements de garde ou lors d'événements sportifs?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  1,
  3
),
(
  "NC04",
  "NC",

  NULL,
  "Dans quelle mesure arrive-t-il que le nouveau ou nouvelle conjoint·e vous critique ou dénigre vos compétences parentales devant votre enfant ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  3,
  4
),
(
  "NC05",
  "NC",

  NULL,
  "Dans quelle mesure le nouveau ou nouvelle conjoint·e dénigre vos compétences parentales par texto, courriel ou autres?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  3,
  5
),
(
  "NC06",
  "NC",

  NULL,
  "Évaluez l'intensité de l'énoncé : le nouveau ou nouvelle conjoint·e dénigre ouvertement votre nouvelle famille devant votre enfant (nouveau conjoint + enfants nés ou non d’une nouvelle union)",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  3,
  6
),
(
  "NC07",
  "NC",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation? Il arrive que le nouveau ou nouvelle conjoint·e apporte des changements à l’horaire de garde (se substituant à l'autorité de l'autre parent) sans vous consulter au préalable, et sans votre autorisation.",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  7
),
(
  "NC08",
  "NC",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation? Le nouveau ou nouvelle conjoint·e organise des activités sur votre temps de garde?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  8
),
(
  "NC09",
  "NC",

  NULL,
  "Lorsque vous appelez votre enfant chez l'autre parent, arrive-t-il que le nouveau ou nouvelle conjoint·e interfère, écoute ou écourte vos conversations téléphoniques avec votre enfant ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  9
),
(
  "NC10",
  "NC",

  NULL,
  "Lorsque vous appelez votre enfant chez l'autre parent, arrive-t-il que le nouveau ou nouvelle conjoint·e interfère, écoute ou écourte vos conversations téléphoniques avec votre enfant ?",
  "labeled-ladder",
  "E1A",
  NULL,
  NULL,
  2,
  10
),
(
  "NC11",
  "NC",

  NULL,
  "Dans quelle mesure le nouveau ou nouvelle conjoint·e est responsable de la logistique familiale : communication scolaire, rendez-vous médicaux, etc.?",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  2,
  11
),
(
  "NC12",
  "NC",

  NULL,
  "Évaluez la fréquence et l'intensité de l'énoncé : le nouveau ou nouvelle conjoint·e impose sa présence en appelant (ou en textant) régulièrement votre enfant durant votre temps de garde.",
  "labeled-ladder",
  "E5A",
  NULL,
  NULL,
  NULL,
  12
),
(
  "NC13",
  "NC",

  NULL,
  "Dans quelle mesure le nouveau ou nouvelle conjoint·e interdit aux personnes gravitant autour de l’enfant (professeurs, éducateurs, medecins, entraîneurs, etc.) de vous communiquer de l'information au sujet de votre enfant?",
  "labeled-ladder",
  "E4A",
  NULL,
  NULL,
  3,
  13
),
(
  "NC14",
  "NC",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation? Le nouveau ou nouvelle conjoint·e demande à votre enfant de l'appeler maman ou papa ?",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  14
),
(
  "NC15",
  "NC",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation? Votre relation avec votre enfant est fragilisée depuis l'arrivée du nouveau ou nouvelle conjoint·e?",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  15
),
(
  "NC16",
  "NC",

  NULL,
  "Dans quelle mesure cet énoncé s'applique à votre situation? Le nouveau ou nouvelle conjoint·e vous demande de respecter les désirs et choix de votre enfant.",
  "labeled-ladder",
  "E3A",
  NULL,
  NULL,
  2,
  16
),
(
  "S02",
  "F",
  NULL,


  "Êtes-vous en processus juridique actuellement ?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  0
),
(
  "B10",
  "F",

  NULL,
  "Quelles sont les modalités de garde des enfants aujourd'hui ?",
  "select-multiple",
  NULL,
  NULL,
  NULL,
  0,
  1
),
(
  "S03a",
  "F",

  NULL,
  "Si vous avez répondu garde partagée (ou garde dite alternée), dans quelle proportion avez-vous la garde ?",
  "select-single",
  NULL,
  NULL,
  NULL,
  0,
  2
),
(
  "S04",
  "F",

  NULL,
  "Durant l’enfance et avant 14 ans, est-ce que vous et/ou votre ex-conjoint·e avez vécu l’une des situations familiales suivantes ? Cochez les réponses qui s'appliquent dans chaque colonne.",
  "select-multiple",
  NULL,
  NULL,
  NULL,
  NULL, -- TODO
  3
);

INSERT INTO question (
  [question_id],
  [survey_id],
  [intro],
  [title],
  [type],
  [label_id],
  [info_bubble_text],
  [condition],
  [intensity],
  [order],
  [min_value],
  [max_value]
) VALUES (
  "B06",
  "B",

  NULL,
  "Quel âge a l'enfant qui fait l'objet de l'analyse ?",
  "integer",
  NULL,
  "Préciser notion : Il est possible de faire une analyse comparative ou rétroactive",
  NULL,
  NULL,
  5,
  0,
  100
);



-- CHOICESS


INSERT INTO choice (
  [question_id],
   [value],
   [label],
   [order]
) VALUES (
  "B00",
  "0",
  "Une mère",
  0
),
(
  "B00",
  "1",
  "Un père",
  1
),
(
  "B00",
  "2",
  "Un parent (non binaire)",
  2
),
(
  "B00",
  "3",
  "Un grand-parent",
  3
),
(
  "B00",
  "4",
  "Un·e nouveau ou nouvelle conjoint·e",
  4
),
(
  "B00",
  "custom",
  "Autre (spécifiez)",
  5
),
(
  "B02",
  "1",
  "Analyze au présent",
  1
),
(
  "B02",
  "2",
  "Analyze au passé",
  1
),
(
  "B01",
  "0",
  "En mon nom ou celui d'une autre mère",
  0
),
(
  "B01",
  "1",
  "En mon nom ou celui d'un autre père",
  1
),
(
  "B01",
  "2",
  "En mon nom ou celui d'un autre parent (non binaire)",
  2
),
(
  "S01",
  "0",
  "moins de 24 ans",
  0
),
(
  "S01",
  "1",
  "25 à 29 ans",
  1
),
(
  "S01",
  "2",
  "30 à 39 ans",
  2
),
(
  "S01",
  "3",
  "40 à 49 ans",
  3
),
(
  "S01",
  "4",
  "50 à 59 ans",
  4
),
(
  "B02",
  "5",
  "plus de 60 ans",
  5
),
(
  "B03",
  "0",
  "1 an et moins",
  0
),
(
  "B3",
  "1",
  "2 à 5 ans",
  1
),
(
  "B03",
  "2",
  "6 à 10 ans",
  2
),
(
  "B03",
  "3",
  "11 à 20 ans",
  3
),
(
  "B03",
  "4",
  "plus de 20 ans",
  4
),
(
  "B04",
  "0",
  "moins de 1 an (incl. en union ou en instance de séparation)",
  0
),
(
  "B04",
  "1",
  "1 à 2 ans",
  1
),
(
  "B04",
  "2",
  "2 à 5 ans",
  2
),
(
  "B04",
  "3",
  "5 à 10 ans",
  3
),
(
  "B04",
  "4",
  "plus de 10 ans",
  4
),
(
  "B05",
  "1",
  "1 enfant (celui qui fait l'objet de l'analyse)",
  1
),
(
  "B05",
  "2",
  "2",
  2
),
(
  "B05",
  "3",
  "3",
  3
),
(
  "B05",
  "4",
  "Plus de 4 enfants",
  4
),
(
  "B07",
  "0",
  "Célibataire",
  0
),
(
  "B07",
  "1",
  "En couple ou famille recomposée SANS enfant issu de la nouvelle union",
  1
),
(
  "B07",
  "2",
  "Famile recomposée AVEC enfant(s) issu(s) de la nouvelle union",
  2
),
(
  "B08",
  "0",
  "Célibataire",
  0
),
(
  "B08",
  "1",
  "En couple",
  1
),
(
  "B08",
  "2",
  "Famille recomposée",
  2
),
(
  "B11c",
  "0",
  "Oui",
  0
),
(
  "B11c",
  "1",
  "Oui, mais lien fragile",
  1
),
(
  "B11c",
  "2",
  "Non",
  2
),
(
  "B11c1",
  "0",
  "Lien affectif fragilisé",
  0
),
(
  "B11c1",
  "1",
  "Contact sporadique, mais accès non-respectés",
  1
),
(
  "B11c1",
  "2",
  "Communication à distance seulement (téléphone, texto, RS)",
  2
),
(
  "B11c1",
  "3",
  "Rupture de lien affectif et de contacts",
  3
),
(
  "B11c2",
  "0",
  "< 9 mois",
  0
),
(
  "B11c2",
  "1",
  "Entre 9 mois et 2 ans",
  1
),
(
  "B11c2",
  "2",
  "Entre 2 ans et 5 ans",
  2
),
(
  "B11c2",
  "3",
  "Entre 5 ans et 10 ans",
  3
),
(
  "B11c2",
  "4",
  "plus de 10 ans",
  4
),
(
  "B11c4",
  "0",
  "Épisode de dépression (pour vous ou l'autre parent)",
  0
),
(
  "B11c4",
  "1",
  "Épisode de violence (de votre part ou de l'autre parent)",
  1
),
(
  "B11c4",
  "2",
  "Infidélité (de votre part ou de l'autre parent)",
  2
),
(
  "B11c4",
  "3",
  "Événement déclencheur (ex.: déménagement, deuil,...)",
  3
),
(
  "B11c4",
  "4",
  "Arrivée d'un·e nouveau ou nouvelle conjoint·e",
  4
),
(
  "B11c4",
  "5",
  "Autre",
  5
),
(
  "B11c4",
  "6",
  "Aucun",
  6
),
(
  "PCR06a",
  "0",
  "Préparation des repas (et boîte à lunch) des enfants",
  0
),
(
  "PCR06a",
  "1",
  "Accompagnement des devoirs",
  1
),
(
  "PCR06a",
  "2",
  "Gestion des vêtements",
  2
),
(
  "PCR06a",
  "3",
  "Choix des activités sportives",
  3
),
(
  "PCR06a",
  "custom",
  "Autres (spécifiez)",
  4
),
(
  "PCR12a",
  "0",
  "Choix d'école (primaire et/ou secondaire)",
  0
),
(
  "PCR12a",
  "1",
  "Programmes sportifs",
  1
),
(
  "PCR12a",
  "2",
  "Soins médicaux ou dentaires",
  2
),
(
  "PCR12a",
  "3",
  "Déménagement dans une autre ville en raison du travail",
  3
),
(
  "PCR12a",
  "custom",
  "Autres (spécifiez)",
  4
),
(
  "PFA25a",
  "0",
  "Normal / usuel",
  0
),
(
  "PFA25a",
  "1",
  "Nouveau",
  1
),
(
  "PFA29a",
  "0",
  "Choix d'école et/ou inscription (primaire et secondaire)",
  0
),
(
  "PFA29a",
  "1",
  "Choix de club|programme sportif",
  1
),
(
  "PFA29a",
  "2",
  "Soins médicaux ou dentaires",
  2
),
(
  "PFA29a",
  "3",
  "Déménagement (forçant un changement majeur ou autres)",
  3
),
(
  "PFA29a",
  "4",
  "Achat d'une valeur significative (auto, animal,…)",
  4
),
(
  "PFA29a",
  "custom",
  "Autre (spécifiez)",
  5
),
(
  "PFA30a2",
  "0",
  "Changement d’école ou d’équipe sportive (rupture d'environnement de l'enfant, problème de transport, etc.)",
  0
),
(
  "PFA30a2",
  "1",
  "Changement de nom",
  1
),
(
  "PFA30a2",
  "2",
  "Éloignement physique (ex.: déménagement causant un changement d’école, perte d’amis, etc.)",
  2
),
(
  "PFA30a2",
  "3",
  "Manœuvre pour vous isoler de l’entourage de votre enfant  (cercle d'influence inaccessible : professeur, entraineur, parents des amis, etc.)",
  3
),
(
  "PFA30a2",
  "custom",
  "Autres (spécifiez)",
  4
),
(
  "PFA38",
  "0",
  "Pension alimentaire (enjeux financiers)",
  0
),
(
  "PFA38",
  "1",
  "Souhaite refaire sa vie / nouvelle vie et vous êtes de trop",
  1
),
(
  "PFA38",
  "2",
  "Ne veut pas faire de compromis sur le temps passé avec les enfants",
  2
),
(
  "PFA38",
  "3",
  "Ne veut pas faire de compromis sur la logistique familiale",
  3
),
(
  "PFA38",
  "4",
  "Souhaite vous blesser et se venger en vous retirant les enfants",
  4
),
(
  "PFA38",
  "5",
  "S'approprie les enfants (désir de garde exclusive)",
  5
),
(
  "E05a",
  "0",
  "Au retour d'un séjour (garde) de l'autre parent",
  0
),
(
  "E05a",
  "1",
  "Lorsque l'enfant est en présence de l'autre parent",
  1
),
(
  "E05a",
  "2",
  "Lorsque mon enfant cherche à me convaincre de passer plus de temps chez l'autre parent",
  2
),
(
  "E05a",
  "3",
  "Lorsque mon enfant me fait des reproches",
  3
),
(
  "E27a",
  "0",
  "Neutre",
  0
),
(
  "E27a",
  "1",
  "Calme",
  1
),
(
  "E27a",
  "2",
  "Enjoué.e",
  2
),
(
  "E27a",
  "3",
  "Taciturne",
  3
),
(
  "E27a",
  "4",
  "Anxieux",
  4
),
(
  "E27a",
  "5",
  "Agressif",
  5
),
(
  "E36a",
  "0",
  "Automutilation",
  0
),
(
  "E36a",
  "1",
  "Anxiété",
  1
),
(
  "E36a",
  "2",
  "Dépression",
  2
),
(
  "E36a",
  "3",
  "Idéation suicidaire",
  3
),
(
  "E36a",
  "4",
  "Insomnie",
  4
),
(
  "E36a",
  "5",
  "Isolement et difficulté à socialiser",
  5
),
(
  "E36a",
  "6",
  "Trouble de l'opposition",
  6
),
(
  "E36a",
  "7",
  "Trouble alimentaire",
  7
),
(
  "E36a",
  "8",
  "Aucune de ces réponses",
  8
),
(
  "E36a",
  "custom",
  "Autres (veuillez spécifier)",
  9
),
(
  "E36b",
  "0",
  "Automutilation",
  0
),
(
  "E36b",
  "1",
  "Anxiété",
  1
),
(
  "E36b",
  "2",
  "Dépression",
  2
),
(
  "E36b",
  "3",
  "Idéation suicidaire",
  3
),
(
  "E36b",
  "4",
  "Insomnie",
  4
),
(
  "E36b",
  "5",
  "Isolement et difficulté à socialiser",
  5
),
(
  "E36b",
  "6",
  "Trouble de l'opposition",
  6
),
(
  "E36b",
  "7",
  "Trouble alimentaire",
  7
),
(
  "E36b",
  "8",
  "Aucune de ces réponses",
  8
),
(
  "E36b",
  "custom",
  "Autres (veuillez spécifier)",
  9
),
(
  "PCR19",
  "0",
  "Je reste calme, mais je ne me laisse pas insulter par mon enfant",
  0
),
(
  "PCR19",
  "1",
  "Je l'envoie réfléchir et lui demande de revenir lorsqu'il sera calme",
  1
),
(
  "PCR19",
  "2",
  "J'impose des conséquences pour corriger le comportement inadéquat de mon enfant",
  2
),
(
  "PCR19",
  "3",
  "Je suis en colère contre l'autre parent car je sais que le reproche vient de lui et non de mon enfant. Et je le signifie à mon enfant.",
  3
),
(
  "PCR19",
  "4",
  "Aucune de ces réponses",
  4
),
(
  "PCR20",
  "0",
  "Vous tentez de le raisonner et vous vous justifiez",
  0
),
(
  "PCR20",
  "1",
  "Vous faites valoir que l'autre parent lui a menti",
  1
),
(
  "PCR20",
  "2",
  "Vous êtes blessé·e, vous êtes émotif ou émotive",
  2
),
(
  "PCR20",
  "3",
  "Aucune de ces réponses",
  3
),
(
  "S02",
  "0",
  "Non, je ne le suis pas",
  0
),
(
  "S02",
  "1",
  "Oui - Médiation",
  1
),
(
  "S02",
  "2",
  "Oui - Tribunal droit de la famille  (ex.: Cour supérieure au Québec)",
  2
),
(
  "S02",
  "3",
  "Oui - Tribunal de la jeunesse (ex.: DPJ au Québec)",
  3
),
(
  "S02",
  "4",
  "Autre",
  4
),
(
  "S03",
  "0",
  "Garde partagée (ou garde dite alternée)",
  0
),
(
  "S03",
  "1",
  "Garde exclusive pour vous",
  1
),
(
  "S03",
  "2",
  "Garde exclusive pour l'autre parent",
  2
),
(
  "S03",
  "3",
  "Aucune garde établie",
  3
),
(
  "S03",
  "4",
  "Accès supervisés pour vous",
  4
),
(
  "S03",
  "5",
  "Accès supervisés pour l'autre parent",
  5
),
(
  "S03",
  "6",
  "Autre",
  6
),
(
  "S03a",
  "0",
  "50% / 50%",
  0
),
(
  "S03a",
  "1",
  "Plus de 50% pour vous",
  1
),
(
  "S03a",
  "2",
  "Moins de 40% pour vous",
  2
),
(
  "S03a",
  "custom",
  "Autre (veuillez préciser)",
  3
),
(
  "S04",
  "0",
  "Deuil d’un parent",
  0
),
(
  "S04",
  "1",
  "Adoption",
  1
),
(
  "S04",
  "2",
  "Maltraitance en tant qu’enfant (intervention DPJ ou non)",
  2
),
(
  "S04",
  "3",
  "Troubles mentaux chez l’un ou des deux parents (dépression, bipolarité, TPL, tentative suicide,..)",
  3
),
(
  "S04",
  "4",
  "Problème de dépendances de l’un ou des deux parents (alcool, drogues,)",
  4
),
(
  "S04",
  "5",
  "Violence conjugale entre les parents",
  5
),
(
  "S04",
  "6",
  "Divorce conflictuel des parents",
  6
),
(
  "S04",
  "7",
  "Rupture de lien avec un parent à la suite d’un divorce",
  7
),
(
  "S04",
  "8",
  "Abus sexuels",
  8
),
(
  "S04",
  "custom",
  "Autres (spécifiez)",
  9
);

INSERT INTO label (
   [label_id],
   [value],
   [label],
   [order]
) VALUES (
  "E1A",
  "0",
  "Jamais",
  0
),
(
  "E1A",
  "1",
  "Rarement",
  1
),
(
  "E1A",
  "2",
  "Parfois",
  2
),
(
  "E1A",
  "4",
  "Régulièrement",
  3
),
(
  "E1A",
  "7",
  "Souvent",
  4
),
(
  "E1A",
  "10",
  "Toujours",
  5
),
(
  "E1A",
  "NULL",
  "Sans objet",
  6
),
(
  "E2A",
  "0",
  "Excellente",
  0
),
(
  "E2A",
  "1",
  "Très bonne",
  1
),
(
  "E2A",
  "2",
  "Bonne",
  2
),
(
  "E2A",
  "4",
  "Moyenne",
  3
),
(
  "E2A",
  "7",
  "Faible",
  4
),
(
  "E2A",
  "10",
  "Mauvaise",
  5
),
(
  "E2A",
  "NULL",
  "Sans objet",
  6
),
(
  "E3A",
  "0",
  "Pas du tout d’accord",
  0
),
(
  "E3A",
  "1",
  "Pas d’accord",
  1
),
(
  "E3A",
  "2",
  "Ni d’accord, ni pas d’accord",
  2
),
(
  "E3A",
  "4",
  "Partiellement d’accord",
  3
),
(
  "E3A",
  "7",
  "D’accord",
  4
),
(
  "E3A",
  "10",
  "Tout à fait d’accord",
  5
),
(
  "E3A",
  "NULL",
  "Sans objet",
  6
),
(
  "E4A",
  "0",
  "Nulle",
  0
),
(
  "E4A",
  "1",
  "Très faible",
  1
),
(
  "E4A",
  "2",
  "Faible",
  2
),
(
  "E4A",
  "4",
  "Moyenne",
  3
),
(
  "E4A",
  "7",
  "Élevé",
  4
),
(
  "E4A",
  "10",
  "Très élevé",
  5
),
(
  "E4A",
  "NULL",
  "Sans objet",
  6
),
(
  "E5A",
  "0",
  "Au besoin",
  0
),
(
  "E5A",
  "1",
  "1 x semaine",
  1
),
(
  "E5A",
  "2",
  "3 x semaine",
  2
),
(
  "E5A",
  "4",
  "+ de 5 x semaine",
  3
),
(
  "E5A",
  "7",
  "tous les jours",
  4
),
(
  "E5A",
  "10",
  "+sieurs x par jour",
  5
),
(
  "E5A",
  "NULL",
  "Sans objet",
  6
),
(
  "E6",
  "0",
  "Pas du tout",
  0
),
(
  "E6",
  "1",
  "Un peu",
  1
),
(
  "E6",
  "2",
  "Normalement",
  2
),
(
  "E6",
  "4",
  "Beaucoup",
  3
),
(
  "E6",
  "7",
  "Énormément",
  4
),
(
  "E6",
  "10",
  "Trop",
  5
),
(
  "E6",
  "NULL",
  "Sans objet",
  6
),
(
  "E1B",
  "0",
  "Toujours",
  0
),
(
  "E1B",
  "1",
  "Souvent",
  1
),
(
  "E1B",
  "2",
  "Régulièrement",
  2
),
(
  "E1B",
  "4",
  "Parfois",
  3
),
(
  "E1B",
  "7",
  "Rarement",
  4
),
(
  "E1B",
  "10",
  "Jamais",
  5
),
(
  "E1B",
  "NULL",
  "Sans objet",
  6
),
(
  "E2B",
  "0",
  "Mauvaise",
  0
),
(
  "E2B",
  "1",
  "Faible",
  1
),
(
  "E2B",
  "2",
  "Moyenne",
  2
),
(
  "E2B",
  "4",
  "Bonne",
  3
),
(
  "E2B",
  "7",
  "Très bonne",
  4
),
(
  "E2B",
  "10",
  "Excellente",
  5
),
(
  "E2B",
  "NULL",
  "Sans objet",
  6
),
(
  "E3B",
  "0",
  "Tout à fait d’accord",
  0
),
(
  "E3B",
  "1",
  "D'accord",
  1
),
(
  "E3B",
  "2",
  "Partiellement d'accord",
  2
),
(
  "E3B",
  "4",
  "Ni d'accord, ni pas d'accord",
  3
),
(
  "E3B",
  "7",
  "Pas d'accord",
  4
),
(
  "E3B",
  "10",
  "Pas du tout d'accord",
  5
),
(
  "E3B",
  "NULL",
  "Sans objet",
  6
),
(
  "E4B",
  "0",
  "Très élevé",
  0
),
(
  "E4B",
  "1",
  "Élevé",
  1
),
(
  "E4B",
  "2",
  "Moyenne",
  2
),
(
  "E4B",
  "4",
  "Faible",
  3
),
(
  "E4B",
  "7",
  "Très faible",
  4
),
(
  "E4B",
  "10",
  "Nulle",
  5
);



INSERT INTO user (
  [email],
  [first_name],
  [last_name],
  [password],
  [phone_number],
  [date_logged_in],
  [date_created],
  [role]
) VALUES (
  "sl@gmail.com",
  "Simon",
  "Leroux",
  -- 123456$
  "$2a$10$4FMxApBcKJBJDyg.Vis8HeFf41UlbezpI7h.N1tylZIBsdYMi1i.W", 
  "0612345678",
   "2022-08-01",
  "2022-08-01",
  "admin"
);



-- after migration





update question set ladderC = 100 where question_id = 'B11';
update question set ladderC = 100 where question_id = 'B11a';
update question set ladderC = 100 where question_id = 'B11b';
update question set ladderC = 50 where question_id = 'B11c';
update question set ladderE = 50 where question_id = 'B11c';


-- Questionnaire PCRA 




update question set ladderC = 100 where question_id = 'PCR02';
update question set ladderC = 100 where question_id = 'PCR06';
update question set ladderC = 100 where question_id = 'PCR06a';
update question set ladderC = 100 where question_id = 'PCR08';
update question set ladderC = 100 where question_id = 'PCR09';
update question set ladderC = 100 where question_id = 'PCR11';
update question set ladderC = 100 where question_id = 'PCR12';
update question set ladderC = 100 where question_id = 'PCR12a';
update question set ladderC = 100 where question_id = 'PCR13';
update question set ladderC = 100 where question_id = 'PCR14';
update question set ladderC = 100 where question_id = 'PCR15';
update question set ladderC = 100 where question_id = 'PCR15a';
update question set ladderC = 100 where question_id = 'PCR17';

update question set ladderE = 100 where question_id = 'PCR10';
update question set ladderE = 100 where question_id = 'PCR16';
update question set ladderE = 100 where question_id = 'PCR16a';
update question set ladderE = 100 where question_id = 'PCR18';

update question set ladderV = 100 where question_id = 'PCR04';
update question set ladderV = 100 where question_id = 'PCR07';


-- conditional intensity

update question set conditional_intensity='3: PCR08 >=2 && (B04 >= 3 || B02 >=3)' where question_id= 'PCR08';
update question set conditional_intensity='2: B02 >= 4; 3: B02 <=3' where question_id= 'PCR09';

update question set conditional_intensity='2: B02 >= 4; 3: B02 <=3' where question_id= 'PCR09';
update question set conditional_intensity='1: B02 >= 4; 3: B02 <=3' where question_id= 'E06';

-- parent

update question set parent='B11' where question_id ='B11a';

update question set parent='B11a' where question_id ='B11a1';

update question set parent='B11' where question_id ='B11b';

update question set parent='B11' where question_id ='B11c';

update question set parent='B11c' where question_id ='B11c1';
update question set parent='B11c' where question_id ='B11c2';
update question set parent='B11c' where question_id ='B11c3';
update question set parent='B11c' where question_id ='B11c4';

update question set parent='E02' where question_id ='E02a';

update question set parent='E03' where question_id ='E03a';

update question set parent='E04' where question_id ='E04a';

update question set parent='E05' where question_id ='E05a';
update question set parent='E05a' where question_id ='E05a1';
update question set parent='E05a' where question_id ='E05a2';
update question set parent='E05a' where question_id ='E05a3';
update question set parent='E05a' where question_id ='E05a4';

update question set parent='E06' where question_id ='E06a';
update question set parent='E06a' where question_id ='E06a1';

update question set parent='E14' where question_id ='E14a';

update question set parent='E15' where question_id ='E15a';

update question set parent='E16' where question_id ='E16a';
update question set parent='E16' where question_id ='E16b';
update question set parent='E16' where question_id ='E16c';

update question set parent='E21' where question_id ='E21a';

update question set parent='E22' where question_id ='E22a';

update question set parent='E27' where question_id ='E27a';
update question set parent='E27' where question_id ='E27b';

update question set parent='E29' where question_id ='E29a';

update question set parent='E33' where question_id ='E33a';
update question set parent='E33' where question_id ='E33b';

update question set parent='E35' where question_id ='E35a';

update question set parent='E36' where question_id ='E36a';

update question set parent='E36a' where question_id ='E36a1';
update question set parent='E36a' where question_id ='E36a2';
update question set parent='E36a' where question_id ='E36a3';
update question set parent='E36a' where question_id ='E36a4';
update question set parent='E36a' where question_id ='E36a5';
update question set parent='E36a' where question_id ='E36a6';
update question set parent='E36a' where question_id ='E36a7';
update question set parent='E36a' where question_id ='E36a8';

update question set parent='E36' where question_id ='E36b';
update question set parent='E36b' where question_id ='E36b1';
update question set parent='E36b' where question_id ='E36b2';
update question set parent='E36b' where question_id ='E36b3';
update question set parent='E36b' where question_id ='E36b4';
update question set parent='E36b' where question_id ='E36b5';
update question set parent='E36b' where question_id ='E36b6';
update question set parent='E36b' where question_id ='E36b7';
update question set parent='E36b' where question_id ='E36b8';

update question set parent='H04' where question_id ='H04a';

update question set parent='H05' where question_id ='H05a';

update question set parent='H06' where question_id ='H06a';

update question set parent='NC01' where question_id ='NC01a';

update question set parent='PCR00' where question_id ='PCR00a';
update question set parent='PCR00' where question_id ='PCR00b';

update question set parent='PCR06' where question_id ='PCR06a';

update question set parent='PCR12' where question_id ='PCR12a';

update question set parent='PCR15' where question_id ='PCR15a';

update question set parent='PCR16' where question_id ='PCR16a';

update question set parent='PFA02' where question_id ='PFA02a';

update question set parent='PFA04' where question_id ='PFA04a';

update question set parent='PFA05' where question_id ='PFA05a';

update question set parent='PFA06' where question_id ='PFA06a';

update question set parent='PFA07' where question_id ='PFA07a';
update question set parent='PFA07a' where question_id ='PFA07a1';

update question set parent='PFA09' where question_id ='PFA09a';

update question set parent='PFA11' where question_id ='PFA11a';

update question set parent='PFA13' where question_id ='PFA13a';
update question set parent='PFA13' where question_id ='PFA13b';
update question set parent='PFA13' where question_id ='PFA13c';

update question set parent='PFA15' where question_id ='PFA15a';

update question set parent='PFA16' where question_id ='PFA16a';
update question set parent='PFA16' where question_id ='PFA16b';

update question set parent='PFA16b' where question_id ='PFA16b1';

update question set parent='PFA19' where question_id ='PFA19a';

update question set parent='PFA20' where question_id ='PFA20a';
update question set parent='PFA20' where question_id ='PFA20b';
update question set parent='PFA20' where question_id ='PFA20c';

update question set parent='PFA21' where question_id ='PFA21a';

update question set parent='PFA25' where question_id ='PFA25a';

update question set parent='PFA28' where question_id ='PFA28a';

update question set parent='PFA29' where question_id ='PFA29a';
update question set parent='PFA29' where question_id ='PFA29b';

update question set parent='PFA30' where question_id ='PFA30a';

update question set parent='PFA30a' where question_id ='PFA30a1';
update question set parent='PFA30a' where question_id ='PFA30a2';

update question set parent='PFA31' where question_id ='PFA31a';

update question set parent='PFA31a' where question_id ='PFA31a1';

update question set parent='S03' where question_id ='S03a';