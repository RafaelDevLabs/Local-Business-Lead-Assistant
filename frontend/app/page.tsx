import { LeadForm } from "@/components/LeadForm";

const services = [
  "Simple websites that make the next step obvious",
  "Lead capture connected directly to your inbox",
  "Fast follow-up with practical AI lead summaries",
  "Local visibility basics for calls, bookings, and visits",
];

const benefits = [
  "Turn visitors into real conversations",
  "Respond faster while the customer is still interested",
  "Track every inquiry without a messy spreadsheet",
];

export default function Home() {
  return (
    <main className="min-h-screen bg-cloud text-ink">
      <section
        className="relative overflow-hidden bg-cover bg-center text-white"
        style={{
          backgroundImage:
            "linear-gradient(rgba(23,33,27,0.72), rgba(23,33,27,0.62)), url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1800&q=80')",
        }}
      >
        <div className="mx-auto flex min-h-[72vh] max-w-6xl flex-col justify-center px-6 py-20">
          <p className="mb-4 text-sm font-semibold uppercase text-sun">
            More calls. More bookings. Cleaner follow-up.
          </p>
          <h1 className="max-w-3xl text-4xl font-bold leading-tight sm:text-5xl lg:text-6xl">
            Local Growth Studio
          </h1>
          <p className="mt-6 max-w-2xl text-lg leading-8 text-white/88">
            We build simple websites and lead tracking flows for local
            businesses that need more leads, booked consultations, and faster
            response times.
          </p>
          <div className="mt-8 flex flex-col gap-3 sm:flex-row">
            <a
              href="#lead-form"
              className="inline-flex min-h-12 items-center justify-center rounded-md bg-sun px-5 py-3 font-semibold text-ink transition hover:bg-white"
            >
              Book a consultation
            </a>
            <a
              href="#services"
              className="inline-flex min-h-12 items-center justify-center rounded-md border border-white/55 px-5 py-3 font-semibold text-white transition hover:bg-white hover:text-ink"
            >
              View services
            </a>
          </div>
        </div>
      </section>

      <section className="border-b border-moss/15 bg-white">
        <div className="mx-auto grid max-w-6xl gap-6 px-6 py-12 md:grid-cols-3">
          {benefits.map((benefit) => (
            <div key={benefit} className="border-l-4 border-leaf pl-4">
              <p className="text-lg font-semibold">{benefit}</p>
            </div>
          ))}
        </div>
      </section>

      <section id="services" className="mx-auto max-w-6xl px-6 py-20">
        <div className="max-w-2xl">
          <p className="text-sm font-semibold uppercase text-leaf">
            What we set up
          </p>
          <h2 className="mt-3 text-3xl font-bold sm:text-4xl">
            A practical system for capturing and acting on local demand.
          </h2>
        </div>
        <div className="mt-10 grid gap-4 md:grid-cols-2">
          {services.map((service) => (
            <article
              key={service}
              className="rounded-md border border-moss/15 bg-white p-6 shadow-sm"
            >
              <h3 className="text-xl font-semibold">{service}</h3>
              <p className="mt-3 leading-7 text-ink/70">
                Built for small teams that need clear requests, phone-ready
                context, and a reliable place to see new opportunities.
              </p>
            </article>
          ))}
        </div>
      </section>

      <section id="lead-form" className="bg-white">
        <div className="mx-auto grid max-w-6xl gap-10 px-6 py-20 lg:grid-cols-[0.8fr_1.2fr]">
          <div>
            <p className="text-sm font-semibold uppercase text-leaf">
              Start here
            </p>
            <h2 className="mt-3 text-3xl font-bold sm:text-4xl">
              Tell us what you want to grow.
            </h2>
            <p className="mt-5 leading-8 text-ink/70">
              Send a few details and we will reply with the next best step for
              your website, booking flow, or lead follow-up process.
            </p>
          </div>
          <div className="rounded-md border border-moss/15 bg-cloud p-6 shadow-sm sm:p-8">
            <LeadForm />
          </div>
        </div>
      </section>
    </main>
  );
}
