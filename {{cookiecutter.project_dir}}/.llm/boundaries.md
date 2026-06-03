## Always
- Run just test before committing
- Explicit CRS on every spatial operation
- Type-annotate every public function argument and return value
- Keep CLAUDE.md and AGENTS.md under 200 lines
- TDD: failing test first, then implement, then refactor
- SOLID: one responsibility per function and class
- Update knowledge_base/ AND relevant docs/ when architecture or APIs change
- One package = one workflow — rename ExampleWorkflow, update import in main.py
- Conventional Commits on every commit message
- No LLM co-author footers in any commit

## Ask first
- Adding a new dependency
- Changing public API or function signatures
- Modifying CI/CD workflows
- Switching CRS in existing logic
- Adding GDAL as a direct dependency

## Never
- Commit secrets or credentials
- Push directly to main
- Skip type hints on public functions or return values
- Reproject without specifying target CRS explicitly
- Write comments — simplify the code instead
- Break the abstract Workflow interface contract
- Add "Co-authored-by: Claude", "Co-authored-by: Copilot", or any
  LLM attribution to commit messages, file headers, or docstrings
