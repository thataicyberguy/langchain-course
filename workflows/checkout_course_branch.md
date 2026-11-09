# Check out a course branch in its own folder

## Objective
Work on a branch from the course author's repo in a separate sibling folder, so the `dev` branch in `langchain-course` is never disturbed.

## Inputs
| Name | Example |
|------|---------|
| Course repo URL | `https://github.com/emarco177/langchain-course.git` |
| Remote name | `course` |
| Course branch | `project/ReAct-search-agent` (case-sensitive) |
| New local branch | `react-search-agent` |
| Sibling folder | `../langchain-course-react` |

## Steps
Run from `/Users/ai/Documents/projects/langchain-course`.

1. Add the course repo as a second remote (`origin` is your own repo):
   ```bash
   git remote add course https://github.com/emarco177/langchain-course.git
   ```
2. Confirm the exact branch name:
   ```bash
   git ls-remote --heads course 'project/*'
   ```
3. Fetch only that branch (downloads history; merges nothing):
   ```bash
   git fetch course project/ReAct-search-agent
   ```
4. Create the worktree on a new local branch:
   ```bash
   git worktree add ../langchain-course-react -b react-search-agent course/project/ReAct-search-agent
   ```
5. Set up the new folder:
   ```bash
   cd ../langchain-course-react
   uv sync
   ```
   Copy `.env` into this folder yourself (it is gitignored and never read by Claude).

Result:
```
projects/
├── langchain-course/         # dev
└── langchain-course-react/   # react-search-agent
```

## Verify
```bash
git worktree list
git branch -vv
```

## Clean up
```bash
git worktree remove ../langchain-course-react
git branch -D react-search-agent      # optional: delete the local branch
git remote remove course              # optional
```

## Edge cases and lessons learned
- `git worktree add` takes a **local path and a branch**, not a URL. Passing a GitHub URL fails.
- The branch lives in the author's repo, not `origin`, so `git fetch origin` won't find it. Add the second remote first.
- Branch names are case-sensitive. Use the exact name `ls-remote` prints.
- `.env` and `.venv/` are untracked, so each worktree needs its own `uv sync` and `.env`.
- You can't push to the `course` remote. To keep your work on GitHub, run `git push -u origin react-search-agent`.
- A branch can be checked out in only one worktree at a time.
- Commit to `dev` only in `langchain-course`; the course branch follows its own rules.
