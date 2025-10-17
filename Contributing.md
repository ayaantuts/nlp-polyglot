# Contributing to the Polyglot NLP Toolkit
First off, thank you for considering contributing! We are thrilled to have you here. This project is open to everyone, and we believe that every contribution is valuable.

This document provides guidelines to help you through the contribution process.

## Code of Conduct
This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior.

## How Can I Contribute?
There are many ways to contribute, from writing code and documentation to improving the user interface.

### Reporting Bugs
If you find a bug, please check our [issues page](https://github.com/YOUR_USERNAME/YOUR_REPONAME/issues) to see if it has already been reported. If not, please create a new issue. Be sure to include a clear title, a description of the bug, and steps to reproduce it.

### Suggesting Enhancements
Have an idea for a new feature or an improvement to an existing one? We'd love to hear it! Please open an issue to start a discussion.

### Your First Contribution
Ready to contribute code? We have a list of issues specifically for new contributors. Look for issues with the `good first issue` or `hacktoberfest` labels.
- [Good First Issues](https://github.com/ayaantuts/nlp-polyglot/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [Hacktoberfest Issues](https://github.com/ayaantuts/nlp-polyglot/issues?q=is%3Aissue+is%3Aopen+label%3Ahacktoberfest)

## Contribution Workflow
Here is the process for submitting your changes:
1.  **Find an Issue:** Find an issue that you want to work on.
2.  **Claim the Issue:** Leave a comment on the issue (e.g., "I'd like to work on this!") so we can assign it to you and avoid duplicate work.
3.  **Fork the Repository:** Click the 'Fork' button at the top right of the repository page. This creates a copy of the project in your own GitHub account.
4.  **Clone Your Fork:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPONAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPONAME.git)
    cd YOUR_REPONAME
    ```
5.  **Create a New Branch:** Create a branch for your changes. Use a descriptive name.
    ```bash
    # Examples:
    # git checkout -b feat/add-summarization-model
    # git checkout -b fix/login-button-css
    git checkout -b your-branch-name
    ```
6.  **Make Your Changes:** Write your code! Make sure to follow the project's coding style.
7.  **Commit Your Changes:** Use clear and descriptive commit messages. We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
    ```bash
    # Examples:
    # git commit -m "feat: Add text summarization endpoint"
    # git commit -m "fix: Correct alignment of header on mobile"
    # git commit -m "docs: Update setup instructions in README"
    
    git add <path/to/files>
    git commit -m "type: your commit message"
    ```
8.  **Push to Your Fork:**
    ```bash
    git push origin your-branch-name
    ```
9.  **Submit a Pull Request (PR):**
    - Go to your fork on GitHub and click the "Compare & pull request" button.
    - Fill out the PR template with a clear title and description of your changes.
    - **Link the PR to the original issue** by including `Closes #issue_number` in the description.
    - We will review your PR, provide feedback if needed, and merge it once it's ready.

Thank you again for your contribution. Let's build something amazing together!