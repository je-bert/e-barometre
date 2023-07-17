import { Component, OnInit } from '@angular/core';
import { BehaviorSubject, combineLatest } from 'rxjs';
import { map, tap } from 'rxjs/operators';
@Component({
  selector: 'app-resources',
  templateUrl: './resources.component.html',
  styleUrls: ['./resources.component.scss'],
})
export class ResourcesComponent implements OnInit {
  public categories: string[] = [];

  public tags: string[] = [];

  public resources: {
    title: string;
    img?: string;
    description?: string;
    url: string;
    category: string;
    tags: string[];
  }[] = [
    {
      title: 'Qu’est-ce que la coparentalité',
      url: 'https://www.maisoncalm.org/la-coparentalite.sphp',
      category: 'Coparentalité',
      tags: [],
    },
    {
      title: 'Être parents, un travail d’équipe (dossier Naître et Grandir)',
      url: 'https://naitreetgrandir.com/fr/dossier/etre-parents-travail-equipe/',
      category: 'Coparentalité',
      tags: ['conflit de loyauté', 'séparation', 'cohérence parentale'],
    },
    {
      title: 'Charte de la coparentalité - p.14 du livre électronique Porte 33',
      url: 'https://justiceprobono.ca/wp-content/uploads/sites/2/2019/05/porte33-complet-04-mai.pdf',
      category: 'Coparentalité',
      tags: ['conflit de loyauté', 'séparation', 'cohérence parentale'],
    },
    {
      title:
        'S’orienter dans la séparation familiale - Livre électronique Porte 33',
      url: 'https://justiceprobono.ca/wp-content/uploads/sites/2/2019/05/porte33-complet-04-mai.pdf',
      category: 'Coparentalité',
      tags: ['conflit de loyauté', 'séparation', 'cohérence parentale'],
    },
    {
      title: 'Modèle explicatif des conflits sévères de séparation',
      url: 'https://www.csdepj.gouv.qc.ca/fileadmin/Fichiers_clients/Documents_deposes_a_la_Commission/P-041_Modele_Conflits_Severes_Separation_CIUSSS_Capitale_Nationale.pdf',
      category: 'Coparentalité',
      tags: ['conflit de loyauté', 'séparation', 'coparentalité'],
    },
    {
      title: 'La loi expliquée en un seul endroit - éducaloi',
      url: 'https://educaloi.qc.ca/',
      category: 'Droit',
      tags: ['Canada', 'Québec', 'médiation', 'séparation'],
    },
    {
      title:
        "L'importance de l'opinion de l'enfant au sujet de sa garde - éducaloi",
      url: 'https://educaloi.qc.ca/capsules/limportance-de-lopinion-de-lenfant-au-sujet-de-sa-garde/',
      category: 'Droit',
      tags: [],
    },
    {
      title: 'Tribunal de la famille - wikipedia',
      url: 'Tribunal de la famille - wikipedia',
      category: 'Droit',
      tags: [],
    },
    {
      title:
        'S’orienter dans la séparation familiale - Livre électronique Porte 33',
      url: 'https://justiceprobono.ca/wp-content/uploads/sites/2/2019/05/porte33-complet-04-mai.pdf',
      category: 'Droit',
      tags: [
        'Canada',
        'Québec',
        'médiation',
        'séparation',
        'droit de l’enfant',
        'droit des grands-parents',
        'médiation',
        'Tribunal de la famille',
        'Tribunal de la jeunesse',
        'Canada',
        'Québec',
        'Europe',
        'États-Unis',
      ],
    },
    {
      title: "Comprendre l'aliénation parentale",
      url: 'https://alienationparentale.ca/fr/comprendre/',
      category: 'Psychologie',
      tags: ['aliénation parentale'],
    },
    {
      title: 'Éviter le conflit de loyauté',
      url: 'https://naitreetgrandir.com/fr/etape/3-5-ans/vie-famille/fiche.aspx?doc=eviter-conflits-loyaute',
      category: 'Psychologie',
      tags: ['conflit de loyauté', 'aliénation parentale'],
    },
    {
      title: 'Comprendre le conflit de loyauté',
      url: 'https://www.maisoncalm.org/quest-ce-que-le-conflit-de-loyaute.sphp',
      category: 'Psychologie',
      tags: ['conflit de loyauté', 'aliénation parentale'],
    },
    {
      title: "L'enfant piégé par le conflit de loyauté",
      url: 'https://www.cairn.info/revue-le-journal-des-psychologues-2014-9-page-47.htm',
      category: 'Psychologie',
      tags: ['conflit de loyauté', 'aliénation parentale'],
    },
    {
      title:
        'Les séparations conflictuelles : du conflit parental au conflit de loyauté',
      url: 'https://www.cairn.info/revue-enfances-et-psy-2012-3-page-57.htm',
      category: 'Psychologie',
      tags: [
        'conflit de loyauté',
        'aliénation parentale',

        'conflit sévère de séparation (CSS)',

        'communication non violente (CNV)',
        'études cliniques',
        'parentification',
      ],
    },
    {
      title:
        'La parentification au sein des séparations parentales conflictuelles',
      url: 'https://www.cairn.info/revue-dialogue-2021-1-page-177.htm',
      category: 'Psychologie',
      tags: [
        'parentification',
        'conflit de loyauté',
        'aliénation parentale',
        'conflit sévère de séparation (CSS)',
        'communication non violente (CNV)',
        'études cliniques',
      ],
    },
    {
      title: "Thérapeutique de la parentification : une vue d'ensemble",
      url: 'https://www.cairn.info/revue-therapie-familiale-2005-3-page-285.htm',
      category: 'Psychologie',
      tags: [],
    },
    {
      title: 'La loi expliquée en un seul endroit - éducaloi',
      url: 'https://educaloi.qc.ca/',
      category: 'Références',
      tags: [],
    },
    {
      title: 'Carrefour aliénation parentale',
      url: 'https://alienationparentale.ca/fr/',
      category: 'Références',
      img: 'https://alienationparentale.ca/assets/theme/img/logo-header.png',
      tags: [],
    },
    {
      title: 'Ordre des psychologues du Québec',
      url: 'https://www.ordrepsy.qc.ca/trouver-de-aide',
      category: 'Références psychosociales',
      tags: ['Québec', 'Canada'],
    },
    {
      title: 'éducaloi -- La loi expliquée en un seul endroit',
      url: 'https://educaloi.qc.ca/',
      category: 'Références juridiques',
      tags: ['Québec', 'Canada'],
    },
    {
      title: 'Baromètre de la santé psychologique',
      url: 'https://www.cisss-at.gouv.qc.ca/partage/ECLAIREURS/2022-032_BAROMETRE-SANTE-PSY.pdf',
      category: 'Santé',
      tags: [],
    },
    {
      title:
        'Les parents se séparent : mieux vivre la crise et aider son enfant (2e édition)',
      url: 'https://www.editions-chu-sainte-justine.org/livres/parents-separent-les-339.html',
      category: 'Livre',
      description:
        'Richard Cloutier, Lorraine Filion, Harry Timmermans, 2018, Éditions du CHU Sainte-Justine.',
      tags: [],
    },
    {
      title:
        'Être parents après la séparation : construire une coparentalité sereine pour préserver l’enfant',
      url: 'https://www.renaud-bray.com/Livres_Produit.aspx?id=1243178&def=%c3%8atre+parents+apr%c3%a8s+la+s%c3%a9paration+%3a+construire+une+coparentalit%c3%a9+sereine+pour+pr%c3%a9server+l%27enfant%2cBIOLLEY%2c+JACQUES%2c9782012305489',
      category: 'Livre',
      description:
        'Jacques Biolley et Stéphanie Rubini, 2021, Éditions Hachette.',
      tags: [],
    },
    {
      title:
        'Séparations conflictuelles et aliénation parentale – Enfants en danger',
      url: 'https://www.leslibraires.ca/livres/separations-conflictuelles-et-alienation-parentale-william-bernet-9782367171654.html',
      category: 'Ouvrages de référence',
      description: 'Dr Roland Broca, Olga Odinetz',
      img: 'https://www.leslibraires.ca/_next/image?url=https%3A%2F%2Fimages.leslibraires.ca%2Fbooks%2F9782367171654%2Ffront%2F9782367171654_large.jpg&w=750&q=100',
      tags: [],
    },
    {
      title:
        'La parole de l’enfant – La vérité sort-elle toujours de la bouche des enfants?',
      url: 'https://www.leslibraires.ca/livres/la-parole-de-l-enfant-jacques-toubon-9782100747078.html',
      category: 'Ouvrages de référence',
      description: 'Jacques Toubon',
      img: 'https://www.leslibraires.ca/_next/image?url=https%3A%2F%2Fimages.leslibraires.ca%2Fbooks%2F9782100747078%2Ffront%2F9782100747078_large.jpg&w=828&q=100',
      tags: [],
    },
    {
      title:
        'Conflits de loyauté – Accompagner les enfants pris au piège des loyautés familiales',
      url: 'https://www.leslibraires.ca/livres/conflits-de-loyaute-accompagner-les-enfants-9782100808793.html',
      category: 'Ouvrages de référence',
      description: 'Sous la direction de Roland Coutanceau et Jocelyne Dahan',
      tags: [],
      img: 'https://www.leslibraires.ca/_next/image?url=https%3A%2F%2Fimages.leslibraires.ca%2Fbooks%2F9782100809127%2Ffront%2F9782100809127_large.jpg&w=750&q=100',
    },
    {
      title: 'La famille recomposée – Des escales, mais quel voyage !',
      url: 'https://www.editions-chu-sainte-justine.org/livres/famille-recomposee-269.html',
      category: 'Ouvrages de référence',
      description: 'Claudine Parent, Marie-Christine Saint-Jacques',
      tags: [],
    },
    {
      title:
        'Les parents se séparent – Mieux vivre la crise et aider son enfant',
      url: 'https://www.editions-chu-sainte-justine.org/livres/parents-separent-les-339.html',
      category: 'Ouvrages de référence',
      description: 'Richard Cloutier, Lorraine Filion, Harry Timmermans',
      tags: [],
      img: 'https://cdn.editions-chu-sainte-justine.org/system/books/covers/000/000/339/large/Les_parents_se%CC%81parent.png',
    },
    {
      title:
        'Co-parenting with a Toxic Ex – What to Do When Your Ex-Spouse Tries to Turn the Kids Against You',
      url: 'https://www.leslibraires.ca/livres/la-coparentalite-avec-votre-ex-toxique-amy-j-l-baker-9782897921316.html',
      category: 'Ouvrages de référence',
      description: 'Amy J.L. Baker, Paul R. Fine',
      tags: [],
      img: 'https://www.leslibraires.ca/_next/image?url=https%3A%2F%2Fimages.leslibraires.ca%2Fbooks%2F9782897921316%2Ffront%2F9782897921316_large.jpg&w=640&q=100',
    },
    {
      title: 'Surviving Parental Alienation – a journey of hope and healing',
      url: 'https://www.chapters.indigo.ca/en-ca/books/surviving-parental-alienation-a-journey/9781442226784-item.html',
      category: 'Ouvrages de référence',
      description: 'Amy J.L. Baker, Paul R. Fine',
      tags: [],
    },
    {
      title: 'Parental Alienation Science and Law',
      url: 'https://www.amazon.ca/Parental-Alienation-Demosthenes-Ph-D-Lorandos/dp/0398093245',
      category: 'Ouvrages de référence',
      description: 'Demosthenes Lorandos, William Bernet',
      tags: [],
      img: 'https://m.media-amazon.com/images/I/51hIJ+pSOPL._SX352_BO1,204,203,200_.jpg',
    },
    {
      title: 'Ce que j’avais de plus précieux',
      url: 'https://www.leslibraires.ca/livres/ce-que-j-avais-de-plus-sonia-mascolo-9782897753207.html',
      category: 'Ouvrages de référence',
      description: 'Sonia Mascolo',
      tags: [],
      img: 'https://www.leslibraires.ca/_next/image?url=https%3A%2F%2Fimages.leslibraires.ca%2Fbooks%2F9782897753207%2Ffront%2F9782897753207_large.jpg&w=2048&q=100',
    },
  ];

  public categoryFilter$ = new BehaviorSubject<string>('');
  public tagFilter$ = new BehaviorSubject<string>('');

  public filteredResources$ = combineLatest([
    this.categoryFilter$,
    this.tagFilter$,
  ]).pipe(
    map(([category, tag]) => {
      return this.resources.filter((resource) => {
        if (category && resource.category !== category) {
          return false;
        }

        if (tag && !resource.tags.includes(tag)) {
          return false;
        }

        return true;
      });
    })
  );

  public resetFilters() {
    this.categoryFilter$.next('');
    this.tagFilter$.next('');
  }

  public openResource(url: string) {
    window.open(url, '_blank');
  }

  constructor() {
    this.resources.forEach((resource) => {
      if (!this.categories.includes(resource.category)) {
        this.categories.push(resource.category);
      }

      resource.tags.forEach((tag) => {
        if (!this.tags.includes(tag)) {
          this.tags.push(tag);
        }
      });
    });
  }

  ngOnInit(): void {}
}
