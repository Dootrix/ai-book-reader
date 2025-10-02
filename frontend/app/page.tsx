import React from "react";
import Link from "next/link";

export default function HomePage() {
  return (
    <main className="container">
      <section className="hero">
        <h1>AI Book Reader</h1>
        <p>
          Jump-starting the project scaffold. Connect this frontend to the backend API to
          explore books, take notes and manage bookmarks.
        </p>
        <div className="cta-grid">
          <Link className="card" href="/docs">
            <h2>Documentation</h2>
            <p>Read about the project structure and how to run it locally.</p>
          </Link>
          <a className="card" href="https://nextjs.org/docs" rel="noreferrer" target="_blank">
            <h2>Learn Next.js</h2>
            <p>Explore official Next.js resources to extend this scaffold.</p>
          </a>
        </div>
      </section>
    </main>
  );
}
