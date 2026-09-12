export interface NavItem {
  label: string;
  href: string;
}

export interface SocialLink {
  platform: string;
  href: string;
  handle: string;
}

export interface StatItem {
  value: string;
  label: string;
  detail?: string;
}

export interface PartnerOrg {
  name: string;
  role: string;
  tagline: string;
}

export interface SiteConfig {
  siteUrl: string;
  siteName: string;
  title: string;
  tagline: string;
  headline: string;
  shortBio: string;
  fullBio: string[];
  navLinks: NavItem[];
  socials: SocialLink[];
  stats: StatItem[];
  partners: PartnerOrg[];
  contactEmail: string;
  location: string;
}

export const siteConfig: SiteConfig = {
  siteUrl: 'https://vindhyaumapathy.com',
  siteName: 'Vindhya Umapathy',
  title: 'Vindhya Umapathy — Design Strategist, Educator, Facilitator',
  tagline: 'Design Strategist, Educator, Facilitator',
  headline: "I help organisations make sense of complexity and create what's next.",
  shortBio: "With over a decade of human-centred design practice, I help leadership teams, educational institutions, and mission-driven organisations navigate ambiguity, unlock creative confidence, and design interventions that genuinely serve people.",
  fullBio: [
    "I believe complexity isn't something to avoid or oversimplify with buzzwords—it is the raw material from which meaningful solutions emerge.",
    "For over 10 years, my work has spanned the spectrum from grassroots classrooms to higher education leadership and corporate innovation suites. As Design Thinking Lead at CMR University, I spearheaded university-wide human-centred curriculum design impacting thousands of emerging thinkers.",
    "Earlier, as a Teach For India fellow, I worked directly inside resource-constrained learning environments, learning firsthand that empathy is not a step on a canvas—it is a rigorous, humbling discipline.",
    "Today, I facilitate strategy sprints, design thinking workshops, and organizational inquiries for teams determined to build thoughtful, resilient futures."
  ],
  navLinks: [
    { label: 'Home', href: '/' },
    { label: 'Services', href: '/services' },
    { label: 'Work', href: '/work' },
    { label: 'About', href: '/about' },
    { label: 'Contact', href: '/contact' }
    /* NOTE: Hidden route /thinking is purposefully omitted per client spec. 
       Add `{ label: 'Thinking', href: '/thinking' }` here once client confirms readiness. */
  ],
  socials: [
    { platform: 'LinkedIn', href: 'https://www.linkedin.com/in/vindhyaumapathy', handle: 'vindhyaumapathy' },
    { platform: 'Substack', href: 'https://vindhyaumapathy.substack.com', handle: 'vindhyaumapathy' },
    { platform: 'Email', href: 'mailto:hello@vindhyaumapathy.com', handle: 'hello@vindhyaumapathy.com' }
  ],
  stats: [
    { value: '10+', label: 'Years of Practice', detail: 'Designing for people, organisations, and systems' },
    { value: '8,000+*', label: 'Students & Learners', detail: '[Placeholder count — confirm with Vindhya]' },
    { value: '600+*', label: 'Professionals & Leaders', detail: '[Placeholder count — confirm with Vindhya]' }
  ],
  partners: [
    { name: 'CMR University', role: 'Design Thinking Lead', tagline: 'Curriculum & Institutional Transformation' },
    { name: 'Teach For India', role: 'Fellow & Educator', tagline: 'Grassroots Equity & Systems Inquiry' }
  ],
  contactEmail: 'hello@vindhyaumapathy.com',
  location: 'Bengaluru, India · Available Globally'
};
