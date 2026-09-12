export interface WorkshopFormat {
  id: string;
  duration: string;
  badge: string;
  title: string;
  targetAudience: string;
  description: string;
  focusAreas: string[];
}

export interface ServiceOffering {
  id: string;
  title: string;
  summary: string;
  description: string;
  deliverables: string[];
  bestFor: string;
}

export const workshopFormats: WorkshopFormat[] = [
  {
    id: 'half-day-sprint',
    duration: 'Half-Day Format',
    badge: '3.5 – 4 Hours',
    title: 'Mindset Shift & Problem Reframing',
    targetAudience: 'Product teams, multidisciplinary squads, or departmental leaders needing rapid alignment.',
    description: '[TODO: replace with Vindhya\'s copy — half-day intensive immersion to deconstruct habitual assumptions and reframe team challenges around user needs.]',
    focusAreas: [
      'Problem reframing & empathy inquiry',
      'Deconstructing organizational blindspots',
      'Rapid collaborative convergence'
    ]
  },
  {
    id: 'one-day-intensive',
    duration: '1-Day Intensive',
    badge: 'Full Day (7 – 8 Hours)',
    title: 'Design Thinking & Rapid Prototyping Sprint',
    targetAudience: 'Teams launching new initiatives, refining service flows, or building collaborative momentum.',
    description: '[TODO: replace with Vindhya\'s copy — end-to-end hands-on design thinking cycle from qualitative empathy to rough prototyping with peer testing.]',
    focusAreas: [
      'End-to-end human-centred design cycle',
      'Low-fidelity rapid prototyping techniques',
      'User-tested concept frameworks & roadmap'
    ]
  },
  {
    id: 'one-week-immersion',
    duration: '1-Week Immersion',
    badge: 'Multi-Day Collaborative Cycle',
    title: 'Strategic Design & Systems Transformation',
    targetAudience: 'Leadership councils, faculty groups, or business units undertaking systemic product or cultural change.',
    description: '[TODO: replace with Vindhya\'s copy — multi-stage engagement combining qualitative field research, stakeholder co-creation, and implementation blueprints.]',
    focusAreas: [
      'Field research & qualitative inquiry synthesis',
      'Cross-functional alignment on complex systems',
      'Actionable pilot roadmap with clear ownership'
    ]
  }
];

export const mainServices: ServiceOffering[] = [
  {
    id: 'creative-confidence',
    title: 'Designing Conditions for People to Think Differently',
    summary: 'Building durable creative confidence across individuals, teams, and academic faculties.',
    description: '[TODO: replace with Vindhya\'s copy — partnering with leadership to build environments where non-linear thinking, questioning assumptions, and constructive dissent are safe and generative.]',
    deliverables: [
      'Creative confidence workshops & toolkits',
      'Collaborative readiness assessment',
      'Facilitation masterclasses for educators and leaders'
    ],
    bestFor: 'Organizations experiencing analytical paralysis or teams transitioning into cross-disciplinary problem solving.'
  },
  {
    id: 'research-inquiry',
    title: 'Qualitative Research & Systems Problem Framing',
    summary: 'Unearthing latent human motivations and mapping systemic interdependencies before solutions are built.',
    description: '[TODO: replace with Vindhya\'s copy — generative qualitative field research (contextual interviews, participatory observation, stakeholder journey mapping) to uncover authentic needs.]',
    deliverables: [
      'Generative stakeholder interviews & field observations',
      'Stakeholder journey mapping & systemic tension matrices',
      'Strategic "How Might We" framing synthesis'
    ],
    bestFor: 'Teams exploring zero-to-one problem spaces, product pivots, or social impact initiatives.'
  },
  {
    id: 'org-consulting',
    title: 'Organizational Design & Educational Advisory',
    summary: 'Integrating human-centred practices into institutional curricula, governance, and operating cadences.',
    description: '[TODO: replace with Vindhya\'s copy — co-creating sustainable internal studio models, curriculum architectures, and community learning spaces based on senior academic and consulting leadership.]',
    deliverables: [
      'Curriculum architecture & experiential pedagogy design',
      'Internal innovation studio blueprints',
      'Strategic advisory for academic and enterprise leadership'
    ],
    bestFor: 'Universities updating degree curricula, school networks, and enterprise innovation divisions.'
  }
];
