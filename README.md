# Contributing for beginners, with Streamlit

Welcome to **Contributing for beginners**! This repository is designed for beginners to learn Git, GitHub, and contribute to a project that uses a simple **Streamlit** app.

## Project structure

```
contributing-for-beginners/
├── .github/
│   └── workflows/
│       └── deploy.yml               # GitHub Actions workflow for deployment
├── assets/
│   └── images/                      # Optional: Any images for the project
├── docs/
│   └── how_to_contribute.md         # Guide for contributing
├── src/
│   └── app.py                       # Streamlit Python file for contributors page
├── contributions.json               # File to store contributions (Manually updated by contributors)
├── pyproject.toml                   # Python dependencies and configurations
├── README.md                        # Main README to introduce the repo
└── CONTRIBUTING.md                  # Instructions on contributing
```

## Steps to Contribute

1. **Clone** the repository:
   ```bash
   git clone https://github.com/your-username/contributing-for-beginners.git
   cd contributing-for-beginners
   ````

2. **Create** a branch:
   ```bash
   git checkout -b my-branch-name
   ````

3. **Update** `contributions.json` and save your changes:
   - Add your `full_name` and `github_username` to the `contributions.json` file. **IMPORTANT: DO NOT add a timestamp manually**
   - Add your changes to git tracking : `git add contributions.json`
   - Save your changes by creating a new commit on your branch : `git commit -m 'add myself'`

4. **Push** your branch to the remote repository:
   ```bash
   git push origin my-branch-name
   ````

5. **Create** a Pull Request (PR) on the GitHub UI:
    - Submit a PR with a description of your changes in the repo

6. **Wait** for review:
   - Wait for repository maintainers to review your changes and approve them.
   - Once approved, your changes are merged (i.e incorporated into the main repo) and your name will now appear on the Streamlit app.

