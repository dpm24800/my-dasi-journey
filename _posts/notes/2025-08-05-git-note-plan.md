---
layout: post
title:  "Git – note plan"
author: Dipak Pulami Magar
date:   2025-08-05 10:12:45 +0545
categories: note-plans
status: draft
---

## 🧩 1. Introduction to Version Control {System} (VCS)
* What is Version Control?
* Why it's essential: 
  * Why (developers) use version control?
  * (e.g., tracking changes, collaboration, reverting mistakes)
* Types of version control systems: 
  * local, centralized, distributed. 
  * Centralized (e.g., SVN) vs. Distributed (e.g., Git).
  * Centralized vs. Distributed Version Control.
  * Difference between local vs. remote version control
- Benefits of using Git/Why Git
  - Distributed nature, speed, and flexibility.
  - Open-source and widely adopted.
  * Benefits of Git over SVN or CVS
  * Differences between Git and other VCS like SVN or Mercurial.
  * Other alternatives: GitLab, Bitbucket, etc.

- **Git vs. GitHub**
  - Difference between Git and GitHub (Git is the tool, GitHub is a hosting service).

  - Git: A version control system for local repositories.
  - GitHub: A platform for hosting Git repositories, collaboration, and additional features like pull requests and issues.

## 🧠 2. Git Basics
- **What is Git?** ⚙️
  - History and purpose of Git: Created by Linus Torvalds, key features like speed, data integrity, and distributed workflow.
  - How Git works (snapshots, commits, branches)
* Key Git features: speed, distributed, data integrity
* How Git works internally (Snapshots, not differences)

* Git architecture overview:
  * Working Directory
  * Staging Area (Index)
  * Local Repository
  * Remote Repository

- Git's three states: 
  - Working directory, 
  - staging area (index), and 
  - repository (commit history).

- **Core Concepts**
  - Repository (Repo): The project folder containing all files and their history.
  - Working Directory: The current state of files on your local machine.
  - Staging Area (Index): A buffer for changes to be committed.
  - Commit: A snapshot of changes in the repository.
  - HEAD: Pointer to the current commit or branch.
  
* Repository (Repo): what it is and how it works
* Commits and snapshots
* Branches and merging concepts
* HEAD pointer and master/main branch
* SHA hash (commit identifiers)
* Commit history

## ⚙️ Git Setup/Installation & Configuration
- Downloading and installing Git on various OS: (Windows/Mac/Linux)
- **Git configuration basics/Basic Configuration**: Setting up username, email, and default editor.
- Verifying installation/Checking version: `git --version`.
- Basic Git Configuration: `git config` commands for global and local settings.
  - Git global vs local config: 
    - `git config --global`, 
    - `git config --local`
  - `.gitconfig` file
  - Setting up username and email
    - `git config --global user.name "user_name"`
    * `git config --global user.email "user_email"`
    * `git config --list`
  - Configuring default editor and other settings.
- Getting Help: `git help <command>` or `git <command> --help`

---
- SSH key setup for GitHub
- Setting up SSH keys for secure authentication.
---

- Integrating Git with IDEs like VS Code, IntelliJ, or Eclipse.

*   **The Three States of a File:**
    *   Modified (Working Directory)
    *   Staged (Staging Area/Index)
    *   Committed (Repository)
  
## 📁 Git File Management
- Working Directory, Staging Area, Repository
- Tracking file changes

## 🧾 Essential/Basic Git Commands (and Workflow)
### 1 Initialization
  - Initializing a new repository: `git init`.
  - `git clone <url>`: Copy an existing repository.
  - Cloning repositories: `git clone` (from local or remote).
### 2 Staging changes/Adding files
  - Adding files to staging area/Stage changes: 
    - `git add <file>`: 
    - `git add .`: for all, or (patterns).
### 3. Committing changes:
  - `git commit -m "commit_message"`: Committing changes with messages.
  - amending commits with `--amend`
### Viewing commit history
  - Viewing commit history: 
    - `git log`: 
    - `git log --oneline`:  
    - `git log --graph`: 
    - `git log --author`: 
  - Checking status: 
    - `git status`: Check the status of your working directory (short and long formats).

---
| Branching | `git branch`, `git checkout`, `git switch`, `git merge`, `git rebase` |

| Remote Repos | `git remote`, `git push`, `git pull`, `git fetch` |
---

* **Undoing Changes**:  
  * `git reset`, `git revert`, `git stash`, `git clean`
  * `git restore --staged <file>` or `git reset HEAD <file>`: Unstage a file.
  * `git restore <file>` or `git checkout -- <file>`: Discard changes in working directory.

**4. Understanding Git's History**
*   `git log`: View the commit history.
    *   Useful options: `--oneline`, `--graph`, `--all`, `-p`
*   `git show <commit-hash>`: Show what happened in a specific commit.

*   What is a Commit Hash (SHA-1)?
*   The structure of a commit: Hash, Author, Date, Message, and a snapshot of the entire project.

- **Ignoring Files**
- - Ignoring files: Creating and using `.gitignore` files.
  - Understanding `.gitignore`
  - Creating and using `.gitignore` to exclude files (e.g., temporary files, build artifacts, sensitive data).
  - Syntax for `.gitignore` (e.g., `*.log`, `node_modules/`).
  - `.gitignore` and `.gitattributes`



Basic Git Workflow


## 🌳 Branching & Merging: The "Killer Feature"
* **Understanding branches**: 
  * What is a branch?: A lightweight, movable pointer to a commit.
  * Why branch?/ why it’s used 
  * Default branch (e.g., `main` or `master`).
  * Master/main branch defaults
  * Use cases: Feature development, bug fixes, experimentation.
- **Core Branching Commands**
  * Listing branches: `git branch` or `git branch --list`.
  * Creating branches: `git branch <branch_name>` and `git checkout -b`.
  - Switching branches: 
    - `git checkout <branch_name>` or 
    - `git switch <branch_name>`: Newer, clearer command to switch
  - Creating and switching in one command: `git checkout -b <branch_name>` or `git switch -c <branch-name>`
  - Deleting a branch:
    - Local branch deletion: `git branch -d <branch_name>`
    - Remote branch deletion:
    - you cannot delete the branch while remaining in there, you have to switch to another branch
- **Merging**:
  - Merging branches/performing a merge: `git merge <branch_name>` 
  - Types of merging: 
    - Fast-Forward Merge
    - Three-Way Merges.
    - Fast-forward vs recursive merge
    * Fast-forward vs. non-fast-forward merges
- **Nerge Conflicts**: 
  - What causes them?
  - Handling/resolving merge conflicts: 
    - Identifying, resolving, and committing conflicts.
    - - Identifying conflicts in files.
    - Resolving conflicts manually and marking as resolved (`git add`).
    - Completing the merge (`git commit`).
  - Merge conflicts and resolution
  * Merge conflicts (how to detect and resolve)
  * How to identify them (`git status` will show "unmerged paths").
  *   How to resolve them: Edit the file, remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), then `git add` the resolved file.
  *   `git mergetool`: Use a visual tool to resolve.
* **Rebasing**
    - Rebase vs merge: Difference between merging and rebasing.
    - Rebasing: `git rebase` vs. merge, interactive rebasing for history cleanup.
    - Rebasing a branch: `git rebase <branch-name>`.
    - Interactive rebasing: `git rebase -i` (e.g., for squashing commits).
    - Risks of rebasing (e.g., rewriting history).
- Cherry-picking commits: `git cherry-pick`.

## 🧾 8. Undoing Changes/Things: (Proceed with Caution)
* **Unstaging a file:** 
  * `git restore --staged <file>`
* Undo last commit (`git reset HEAD~1`)
* Revert vs. Reset:  `git revert <commit>` (safe undo)
* **Discarding local changes:** `git restore <file>`
* **Amending the last commit:** `git commit --amend` (Useful for fixing a typo in the commit message or adding a forgotten file).
* **Reverting a commit:** `git revert <commit-hash>`: Creates a *new commit* that undoes the changes of a previous commit. **(Safe for shared history)**.
* **Resetting a branch:** `git reset`
    *   `--soft`: Moves HEAD, keeps changes staged.
    *   `--mixed` (default): Moves HEAD, unstages changes, but keeps them in working directory.
    *   `--hard`: **DANGER**: Moves HEAD and discards all changes. **(Destructive)**.

**4. Rebasing (An Alternative to Merging)**
*   **What is it?** Re-applying commits on top of another base tip.
*   `git rebase <base-branch>` (e.g., `git rebase main` while on a feature branch).
*   **Interactive Rebase:** `git rebase -i <base-commit>`
    *   Use for: Squashing commits, rewording messages, reordering, dropping commits.
    *   **Golden Rule:** Don't rebase commits that have been pushed to a public repository.

making a local repo, making remote repo as counter part, adding remote, pushing changes (pulling and fetching)
making remote repo, cloning remote repo, making changes, pushing changes and  (pulling and fetching)

---

### 4. Remote Repositories and GitHub/ Working with Remote Repositories
- **Introduction to Remote Repositories**
  - What is a remote repository? A hosted version of your Git repo, e.g., on GitHub.
  - Benefits of remote repositories: collaboration, backup, accessibility
- **Setting Up GitHub**
  - Creating a GitHub account.
  - Creating a new repository on GitHub.
---
**1. Connecting Local Git to GitHub**
*   **Authentication Methods:**
    *   **SSH Keys:** Generating (`ssh-keygen`), adding public key to GitHub account.
    *   **Personal Access Tokens (PATs):** Creating and using them.
*   **Remotes:**
    *   What is a remote? (A pointer to another repository, typically on a server like GitHub).
    *   `git remote add origin <url>`: Add a remote named "origin".
    *   `git remote -v`: View your remotes.
---
  - Connecting a local repo/Git to GitHub:
    - Adding a remote: `git remote add origin <URL>`.
    - Verifying remotes: `git remote -v`.
- **2. The "Syncing" Workflow: Pushing and Pulling**
  - Pushing changes/local changes to GitHub: 
    - (to origin, specific branches, force push with caution).
    - `git push origin <branch-name>`: Send your local commits to GitHub.
  - 
  - `git pull origin <branch-name>`: Pulling changes from GitHub; **Fetch** and **merge** changes from GitHub to your local branch.
    - `git fetch`: Download objects and refs without merging.
    - `git merge origin/main`: Merge the fetched changes (what `git pull` does in one step).
  - Fetching and pulling: `git fetch` vs. `git pull` (with rebase option).
  - Difference between `git fetch` and `git pull` (with rebase option).
  - Upstream branches
  - Tracking branches: Setting upstream with `-u`.
  - Remote management: `git remote` commands (show, rename, remove).
---
**3. The Standard Collaboration Workflow: Pull Requests (PRs) / Merge Requests (MRs)**
*   **Forking a Repository:** Creating your own copy of someone else's repo on GitHub.
*   **Cloning Your Fork:** `git clone <your-fork-url>`
*   **Adding an "Upstream" Remote:** `git remote add upstream <original-repo-url>` to stay synced with the original project.
*   **The Process:**
    1.  Create a new branch for your feature/fix.
    2.  Make commits on your branch.
    3.  Push your branch to **your fork** on GitHub: `git push origin <your-branch>`
    4.  On GitHub, create a new Pull Request from your branch to the original repo's `main` branch.
    5.  Discuss, review, and make further commits if requested.
    6.  Merge the PR on GitHub.
---
- **Cloning Repositories**
  - Cloning a repo: `git clone <URL>`.
  - Understanding the cloned repo’s structure (includes `.git` directory).
- **Authentication with GitHub**

## 🔄 7. Git Workflow and Staging
* Git’s 3-stage workflow (Working directory → Staging area → Repository)
* Tracking and untracking files
* `git rm`, `git mv`
* `git reset` (soft, mixed, hard)
* `git restore` (restore deleted or modified files)
* - Removing files: `git rm` (cached or from disk).

**3. Common Workflows**
* **Centralized Workflow:** Everyone works directly on `main`, simple for small teams.
* **Feature Branch Workflow:** All new development happens in dedicated branches, which are merged via PRs. (The most common).
* **Gitflow Workflow:** A more structured model with `main`, `develop`, `feature`, `release`, and `hotfix` branches. (Good for projects with scheduled releases).
* **Forking Workflow:** The standard for open-source contribution (as described in the GitHub section).

### 6. Intermediate & Advanced Git Concepts/Features
**2. Stashing** Stashing Changes, (apply, pop, list, drop). 
*   `git stash` or `git stash push`: Temporarily shelves your changes.
*   `git stash list`: View your stashes.
*   `git stash pop`: Re-apply the most recent stash and remove it from the stack.
*   `git stash apply`: Re-apply but keep it in the stack.
*   `git stash drop`: Remove a stash.
  
- **Stashing Changes**: (saving temporary changes)
  - Saving uncommitted changes: `git stash`.
  - Applying stashed changes: `git stash apply` or `git stash pop`.
  - Managing multiple stashes: `git stash list`, `git stash apply stash@{n}`.

**5. Tagging**
  - Tagging: `git tag` (lightweight vs. annotated, pushing tags).
  *   `git tag`: List tags.
  *   `git tag -a v1.4 -m "my version 1.4"`: Create an annotated tag (for releases).
  *   `git push origin --tags`: Push tags to remote.
  - * `git tag` (annotated and lightweight tags)
- 
* Bisect `git bisect` (debugging with binary search)
* `git bisect`: Use binary search to find the commit that introduced a bug.

- **3. Comparing Changes**
*   `git diff`: Show unstaged changes since last commit.
*   `git diff --staged`: Show staged changes.
*   `git diff <commit-A> <commit-B>`: Compare two specific commits.
*   `git diff <branch-A>..<branch-B>`: Compare the tips of two branches.
*   Diffing changes: `git diff` (between working dir, staged, commits).

- **Undoing Changes**
- Undoing changes: `git reset` (soft, mixed, hard), `git revert`.
  - Reverting a commit: `git revert <commit-hash>`.
  - Resetting changes:
    - Soft reset: `git reset --soft <commit-hash>` (keeps changes in staging).
    - Hard reset: `git reset --hard <commit-hash>` (discards changes).
    - Mixed reset: `git reset <commit-hash>` (default, unstages changes).
  - Amending a commit: `git commit --amend`.

- **Cherry-Picking**
  - Applying specific commits to another branch: `git cherry-pick <commit-hash>`.

- **Reflog** 
- - Git reflog: Recovering lost commits.
  - (recovering lost commits)
  - `git reflog`: Your safety net. Shows a log of where your HEAD and branch references have been. Can recover lost commits.
  - Viewing the reference log: `git reflog`.
  - Recovering lost commits or branches using reflog.

- **Submodules**
- - Submodules: Adding and updating nested repositories.
  - Including another Git repo as a subdirectory: `git submodule add <URL>`.
  - Updating submodules: `git submodule update`.

- **Git Hooks**
  - Git hooks: Client-side and server-side hooks for automation.
  - Automating tasks with hooks (e.g., pre-commit, post-merge).
  - Example: Running linters or tests before committing.
  - Hooks (`.git/hooks/`): Scripts that run automatically before/after events like commit, push, etc.
* `git rebase`
* Git bisect: Binary search for bug introduction.
- Git worktrees: Managing multiple working directories.
- Git LFS (Large File Storage): Handling binary files.

### 8. 📚 Best Practices and Tips
- **Commit Best Practices**
  - Writing clear, concise commit messages (e.g., “Add user authentication feature”).
  - Keeping commits atomic (one change per commit).
  - Commit message conventions: Semantic commits, conventional commits.
- **2. Writing Good Commit Messages**
  * The **Conventional Commits** standard (e.g., `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`).
  * Best Practices: Subject line <50 chars, body explaining *what and why*, not *how*.
- **Branch Naming Conventions**
  - Examples: `feature/login-page`, `bugfix/footer-alignment`, `hotfix/security-patch`.
  - Branch naming strategies: Feature, bugfix, release branches.
- **The `.gitignore` File**
  * What is it? A file that tells Git which files/folders to ignore.
  * Common examples: `node_modules/`, `*.log`, `.env`, `dist/`, `.DS_Store`.
  * Patterns and syntax.
* Using `.gitignore` and `.gitattributes` effectively
* Keeping repos clean (squashing commits, cleaning history)
* Git aliases for faster workflow
- **Collaboration Etiquette**
  - Communicating changes in pull requests.
  - Respecting code review feedback.
- **Backup and Safety**
  - Regularly pushing to remote repositories.
  - Avoiding force pushes (`git push --force`) on shared branches.
- **Performance Optimization**
  - Using `git gc` for repository cleanup.
  - Managing large files with Git LFS (Large File Storage).

- Writing good commit messages
- Keeping branches clean
- Using tags and releases
- Semantic versioning

---
### Best Practices and Advanced Topics
- Git flow workflows: GitFlow, GitHub Flow, trunk-based development.

- Rebasing vs. merging debates: When to use each.
- Handling large repositories: Git sparse-checkout, shallow clones.
- GitHub integrations: With tools like Slack, Jira, Docker.
- Open source contribution: Finding projects, first PR guidelines.
- Troubleshooting common errors: Merge conflicts, push rejected, detached HEAD.
- Performance optimization: Git gc, prune, fsck.
- Security in Git and GitHub: Signing commits, protecting branches.
---

## ☁️ 16. Integration and Automation
* Git with VS Code / PyCharm
* GitHub Desktop
* GitHub CLI (`gh` command-line tool)
* GitHub Actions (Automate tests/deployments)


## 🧩 18. Git Internals (optional deep dive)
* Git object types: blob, tree, commit, tag
* Git references and refs
* The `.git` directory structure
* How Git stores data (content-addressable storage)


<!-- ### Resources and Learning Tips
- Official documentation: Git book, GitHub docs.
- Cheat sheets: Common commands reference.
- Tools: Git GUI clients like GitHub Desktop, Sourcetree.
- Practice exercises: Setting up a sample project, collaborating on a repo.
- Community: Stack Overflow, Reddit (r/git), GitHub forums. -->