const features = [
  {
    title: "AI assisted summaries",
    copy:
      "Upload chapters or notes and receive concise summaries that help you revise key ideas quickly.",
  },
  {
    title: "Smart highlights",
    copy:
      "Mark quotes or passages and let the assistant surface related context, definitions, and background reading.",
  },
  {
    title: "Synchronized bookmarks",
    copy:
      "Pick up where you left off on any device with bookmarks that are mirrored through the FastAPI backend.",
  },
];

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-white via-slate-50 to-slate-100 text-slate-900">
      <main className="mx-auto flex max-w-5xl flex-col gap-20 px-6 pb-24 pt-16 sm:px-12 sm:pt-24">
        <section className="flex flex-col items-center gap-8 text-center sm:gap-10">
          <span className="rounded-full border border-slate-200 px-4 py-1 text-sm font-medium uppercase tracking-[0.2em] text-slate-500">
            Welcome to AI Book Reader
          </span>
          <div className="space-y-6">
            <h1 className="text-balance text-4xl font-semibold tracking-tight sm:text-6xl">
              Read deeper with an assistant that captures every insight
            </h1>
            <p className="text-pretty text-lg text-slate-600 sm:text-xl">
              The AI Book Reader pairs a modern Next.js front-end with a FastAPI backend so you can explore books, collect highlights,
              and keep track of the thoughts that matter most.
            </p>
          </div>
          <div className="flex flex-col gap-4 sm:flex-row">
            <a
              className="rounded-full bg-slate-900 px-6 py-3 text-sm font-semibold tracking-wide text-white shadow-lg shadow-slate-900/20 transition hover:-translate-y-0.5 hover:bg-slate-800"
              href="/api"
            >
              Explore the API docs
            </a>
            <a
              className="rounded-full border border-slate-300 px-6 py-3 text-sm font-semibold tracking-wide text-slate-700 transition hover:-translate-y-0.5 hover:border-slate-400 hover:text-slate-900"
              href="https://nextjs.org/learn"
              target="_blank"
              rel="noreferrer"
            >
              Learn how it was built
            </a>
          </div>
        </section>

        <section className="grid gap-8 md:grid-cols-3">
          {features.map((feature) => (
            <article
              key={feature.title}
              className="rounded-3xl border border-slate-200 bg-white/60 p-6 text-left shadow-sm backdrop-blur transition hover:-translate-y-1 hover:shadow-lg"
            >
              <h2 className="mb-3 text-xl font-semibold text-slate-900">
                {feature.title}
              </h2>
              <p className="text-sm leading-6 text-slate-600">{feature.copy}</p>
            </article>
          ))}
        </section>

        <section className="grid gap-10 rounded-3xl border border-slate-200 bg-white/80 p-8 shadow-sm backdrop-blur md:grid-cols-2">
          <div className="space-y-4">
            <h2 className="text-2xl font-semibold text-slate-900">Backend ready for growth</h2>
            <p className="text-sm leading-7 text-slate-600">
              The FastAPI service persists notes and bookmarks to SQLite out of the box. As the product evolves you can extend the
              data model or swap the database engine without reworking the API surface.
            </p>
          </div>
          <div className="space-y-4">
            <h3 className="text-lg font-semibold text-slate-900">Local development</h3>
            <ol className="list-decimal space-y-2 pl-5 text-sm leading-6 text-slate-600">
              <li>Install dependencies with <code className="rounded bg-slate-900/90 px-1.5 py-0.5 font-mono text-xs text-white">npm install</code> inside <code className="rounded bg-slate-900/90 px-1.5 py-0.5 font-mono text-xs text-white">frontend</code>.</li>
              <li>Spin up the UI via <code className="rounded bg-slate-900/90 px-1.5 py-0.5 font-mono text-xs text-white">npm run dev</code>.</li>
              <li>Start the API with <code className="rounded bg-slate-900/90 px-1.5 py-0.5 font-mono text-xs text-white">uvicorn app.main:app --reload</code> from <code className="rounded bg-slate-900/90 px-1.5 py-0.5 font-mono text-xs text-white">backend</code>.</li>
            </ol>
          </div>
        </section>
      </main>
    </div>
  );
}
