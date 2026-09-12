export interface WorkCaseStudy {
  id: string;
  title: string;
  shortTitle: string;
  category: string;
  period: string;
  summary: string;
  challenge: string;
  approach: string;
  scale: string;
  outcome: string;
  tags: string[];
}

export const workCaseStudies: WorkCaseStudy[] = [
  {
    id: 'cmr-university',
    title: 'CMR University',
    shortTitle: 'CMR University',
    category: 'Higher Education · Institutional Transformation',
    period: 'Lead Role · Multi-Year Program',
    summary: '[Draft placeholder — pending Vindhya\'s review] Institutionalizing design thinking across multidisciplinary undergraduate and postgraduate faculties, reshaping how thousands of young thinkers approach complex real-world challenges.',
    challenge: '[Draft placeholder — pending Vindhya\'s review] Higher education frequently silos disciplines into theoretical rote learning, leaving students underprepared for collaborative ambiguity, real stakeholder empathy, and systemic problem-solving in fast-evolving industries.',
    approach: '[Draft placeholder — pending Vindhya\'s review] Designed, piloted, and scaled an experiential Human-Centred Design curriculum architecture across engineering, architecture, commerce, and humanities. Established faculty co-teaching masterclasses, created open design studios, and instituted project sprints where student teams partnered with municipal authorities, hospitals, and local social enterprises to solve live civic problems.',
    scale: '[Placeholder metric — confirm with Vindhya] 8,000+ students mentored through studio courses; 120+ faculty educators trained in facilitator mindsets; 450+ field-tested social innovation prototypes developed across campuses.',
    outcome: '[Draft placeholder — pending Vindhya\'s review] Permanently anchored design thinking into the university’s core graduating curriculum, fostered an enduring campus-wide culture of experimental inquiry, and established student-led innovation labs recognized nationally.',
    tags: ['Curriculum Design', 'Faculty Enablement', 'Design Thinking', 'Institutional Change']
  },
  {
    id: 'teach-for-india',
    title: 'Teach For India',
    shortTitle: 'Teach For India',
    category: 'Grassroots Systems · Educational Equity',
    period: 'Fellowship & Community Action',
    summary: '[Draft placeholder — pending Vindhya\'s review] Translating human-centred listening into classrooms in under-resourced public communities, co-creating learner-centred environments with students, parents, and school ecosystems.',
    challenge: '[Draft placeholder — pending Vindhya\'s review] Pervasive educational inequity and rigid standardized metrics created disengagement, persistent learning gaps, and disempowerment for first-generation school-going children and their communities.',
    approach: '[Draft placeholder — pending Vindhya\'s review] Anchored pedagogical design in participatory ethnography—spending hours listening to families in their homes to uncover contextual barriers to learning. Developed holistic classroom practices combining emotional wellbeing, storytelling, visual sensemaking, and student agency councils where children co-designed class norms and community action projects.',
    scale: '[Placeholder metric — confirm with Vindhya] 2-year intensive frontline fellowship; 100+ students directly taught; mobilization of family and community stakeholders in parent-led school governance.',
    outcome: '[Draft placeholder — pending Vindhya\'s review] Accelerated grade-level literacy and critical thinking scores, achieved sustained student attendance, and deepened an unshakeable belief that genuine human empathy must precede any strategic framework.',
    tags: ['Community Ethnography', 'Learner Agency', 'Social Impact', 'Systems Thinking']
  },
  {
    id: 'corporate-workshops',
    title: 'Corporate & Leadership Workshops',
    shortTitle: 'Corporate Workshops',
    category: 'Strategy Sprints · Creative Confidence',
    period: 'Consulting & Executive Facilitation',
    summary: '[Draft placeholder — pending Vindhya\'s review] Guiding cross-functional product, design, and executive teams from analytical gridlock to shared strategic clarity through bespoke facilitation and psychological safety.',
    challenge: '[Draft placeholder — pending Vindhya\'s review] Organizations dealing with product pivots, shifting market conditions, or stalled strategic initiatives frequently find their cross-functional teams paralyzed by conflicting departmental priorities, fear of failure, and over-indexing on endless analysis.',
    approach: '[Draft placeholder — pending Vindhya\'s review] Architected structured, low-ego collaborative environments using custom problem-reframing canvases, divergent thinking exercises, and rapid low-fidelity prototyping cycles. Emphasized psychological safety and constructive friction to align product, engineering, and commercial stakeholders on shared user-centric North Stars.',
    scale: '[Placeholder metric — confirm with Vindhya] 600+ product leaders, directors, and design practitioners facilitated across diverse industries including technology, financial services, healthcare, and education.',
    outcome: '[Draft placeholder — pending Vindhya\'s review] Compressed strategic discovery cycles from months to focused sprints; delivered validated, prioritized concept roadmaps backed by unified stakeholder ownership.',
    tags: ['Executive Facilitation', 'Problem Reframing', 'Creative Confidence', 'Cross-Functional Alignment']
  }
];
