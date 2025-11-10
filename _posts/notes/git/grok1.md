

### 5. Collaboration on GitHub
- **Forking Repositories**
  - What is forking? (Creating a personal copy of someone else’s repo.)
  - Forking vs. cloning.
  - Syncing a fork with the upstream repository.
- **Pull Requests (PRs)**
  - Purpose of pull requests (code review, collaboration).
  - Creating a pull request on GitHub.
  - Reviewing and merging pull requests.
  - Best practices: Writing clear PR descriptions, requesting reviewers.
- **Issues and Project Management**
  - Creating and managing issues (bug reports, feature requests).
  - Assigning issues, adding labels, and milestones.
  - Linking issues to pull requests (e.g., “Closes #123”).
- **Collaborative Workflows**
  - Centralized workflow: Single branch for small teams.
  - Feature branch workflow: Separate branches for features/bug fixes.
  - Gitflow: Structured branching model (main, develop, feature, release, hotfix branches).
  - Forking workflow: For open-source contributions.

### 7. GitHub Features and Tools
- **GitHub Actions**
  - Overview of CI/CD pipelines.
  - Creating workflows (e.g., `.github/workflows/ci.yml`).
  - Common use cases: Automated testing, deployment, linting.
- **GitHub Pages**
  - Hosting static websites from a GitHub repository.
  - Setting up a GitHub Pages site (e.g., using `gh-pages` branch).
- **Code Reviews**
  - Commenting on code in pull requests.
  - Suggesting changes and approving PRs.
- **GitHub CLI**
  - Installing and using `gh` (GitHub CLI).
  - Common commands: `gh repo clone`, `gh pr create`, `gh issue list`.
- **GitHub Desktop**
  - Overview of GitHub Desktop for GUI-based Git operations.
  - Use cases for beginners or non-technical users.

### 9. Troubleshooting and Common Issues/Common Git Errors and Fixes (Part of best practices)
- **Merge Conflicts**
  - Steps to resolve conflicts manually.
  - Tools for conflict resolution (e.g., VS Code, SourceTree).
- **Detached HEAD State**
  - Causes and fixes: `git checkout <branch>` or creating a new branch.
- **Authentication Errors/Issues**
  - Authentication issues (SSH vs HTTPS)
  - Fixing SSH or HTTPS authentication issues.
  - Updating credentials or tokens.
- **Recovering Lost Work**
  - Recovering deleted branches or commits
  - Using `git reflog` to recover lost commits.
  - Restoring deleted branches or files.
- **Common Error Messages**
  - Examples: “non-fast-forward”, “failed to push some refs”, “untracked files”.
  - Steps to diagnose and resolve.
- Push rejection (non-fast-forward errors) correct

### 10. Learning Resources and Tools
- **Official Documentation**
  - Git: `git-scm.com/doc`.
  - GitHub: `docs.github.com`.
- **Interactive Learning**
  - Git Branching Game: `learngitbranching.js.org`.
  - GitHub Learning Lab.
- **GUI Tools**
  - SourceTree, GitKraken, VS Code Git integration.
- **Community Resources**
  - Stack Overflow, GitHub Community Forum.
  - Open-source projects for practice.

### 11. Real-World Use Cases
- **Solo Projects**
  - Using Git for personal projects (e.g., tracking progress, experimenting safely).
- **Team Collaboration**
  - Setting up a team repository and defining workflows.
  - Example: A team building a web app with feature branches.
- **Open-Source Contributions**
  - Forking a repo, making changes, and submitting a pull request.
  - Following a project’s contribution guidelines.
- **CI/CD Integration**
  - Using GitHub Actions for automated testing and deployment.
  - Example: Deploying a static site to GitHub Pages.

### 12. Security and Permissions
- **Repository Permissions**
  - Setting up collaborators and teams on GitHub.
  - Managing access levels (read, write, admin).
- **Protecting Branches**
  - Configuring branch protection rules (e.g., requiring PRs, status checks).
- **Sensitive Data**
  - Avoiding committing sensitive information (e.g., API keys).
  - Using `git filter-branch` or BFG Repo-Cleaner to remove sensitive data from history.
- **Two-Factor Authentication (2FA)**
  - Enabling 2FA on GitHub for account security.

## 🔒 15. Git and GitHub Security
* SSH key setup (`ssh-keygen`, adding to GitHub)
* Personal access tokens (PATs)
* Repository privacy settings
* Managing collaborators and permissions

### Example Notes Structure
Here’s how you might structure concise notes for quick reference:

**Git Cheat Sheet**
- **Setup**: `git config --global user.name "Your Name"`, `git config --global user.email "email@example.com"`.
- **Basic Workflow**:
  - Initialize: `git init`.
  - Add: `git add .`.
  - Commit: `git commit -m "Initial commit"`.
  - Status: `git status`.
- **Branching**: `git branch feature-x`, `git checkout feature-x`, `git merge feature-x`.
- **Remote**: `git remote add origin <URL>`, `git push origin main`, `git pull origin main`.
- **Undoing**: `git revert <commit>`, `git reset --hard <commit>`, `git stash`.

**GitHub Workflow Example**
1. Fork repo → Clone locally (`git clone`).
2. Create branch (`git checkout -b feature-x`).
3. Commit changes (`git add .`, `git commit -m "Add feature-x"`).
4. Push to GitHub (`git push origin feature-x`).
5. Create pull request on GitHub.
6. Address review comments and merge.

## 📚 17. Real-World Git Workflows
* Feature branch workflow
* Gitflow workflow
* Forking workflow (open-source)
* Trunk-based development
* Rebase vs. Merge in team projects