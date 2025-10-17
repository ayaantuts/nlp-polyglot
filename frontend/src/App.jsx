import React from 'react';
import styles from './App.module.css';

// Replace with your actual GitHub username and repository name
const GITHUB_REPO_URL = 'https://github.com/ayaantuts/nlp-polyglot';

function App() {
  return (
    <div className={styles.container}>
      <main className={styles.content}>
        <div className={styles.logo}>🚀</div>
        <h1 className={styles.title}>Polyglot NLP Toolkit</h1>
        <p className={styles.subtitle}>Our full site is launching soon.</p>
        <p className={styles.description}>
          We're building a powerful, web-based toolkit for multilingual text analysis. Get ready to explore sentiment, entities, and more with just a few clicks.
        </p>
        <div className={styles.ctaSection}>
          <p>This is an open-source project for <strong>Hacktoberfest 2025</strong>!</p>
          <a
            href={GITHUB_REPO_URL}
            className={styles.button}
            target="_blank"
            rel="noopener noreferrer"
          >
            Contribute on GitHub
          </a>
        </div>
      </main>
      <footer className={styles.footer}>
        &copy; 2025 Polyglot NLP Toolkit
      </footer>
    </div>
  );
}

export default App;