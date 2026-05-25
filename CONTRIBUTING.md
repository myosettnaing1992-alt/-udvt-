# Contributing to the UDVT Suite

Thank you for your interest in contributing to the Unified Dynamic Vacuum Theory (UDVT) project. This document explains how to report problems, propose changes, and submit code, documentation, or data so your contribution can be reviewed and merged smoothly.

## 1. Our values and expectations
- Be constructive and respectful.
- Aim for reproducibility and rigor.
- Cite sources for theoretical material.
- By contributing you agree to license your contributions under the MIT License.

## 2. Before you start
- Read README, monographs, CITATION.cff, and glossary.
- Check open issues; open a new issue if none exists.
- Fork and create a branch: `feat/<desc>`, `fix/<desc>`, `docs/<desc>`.

## 3. Reporting bugs and requesting features
- Open an issue with environment, steps to reproduce, expected vs actual behavior, logs, and minimal code.

## 4. Code contributions (PR workflow)
1. Branch from `main`.
2. Write tests (pytest).
3. Follow style: Python 3.10+, use `black`, `flake8`.
4. Docstrings: NumPy or Google style.
5. Type hints for public APIs.
6. Add/update docs in `docs/`.
7. Run tests locally.
8. Commit messages: imperative style.
9. Open PR with description, linked issues.
10. Respond to review comments.

## 5. Tests, CI, and reproducibility
- Unit tests for deterministic logic.
- Integration tests with fixed seeds and tolerances.
- Large datasets: do not commit; provide links.

## 6. Documentation and examples
- Keep docstrings up to date.
- Jupyter notebooks allowed for demos; keep small.

## 7. Data, figures, and external resources
- Provide provenance and license for datasets.
- Prefer scripts to regenerate figures.

## 8. Theoretical contributions and derivations
- State assumptions, definitions, and notation.
- Cite monograph sections and external literature.
- Include scripts reproducing numerical predictions.

## 9. Code of conduct
- Follow CODE_OF_CONDUCT.md.
- Contact maintainers for disputes.

## 10. Security and sensitive information
- Do not commit secrets.
- Responsible disclosure via maintainer email.

## 11. Templates
- Issue template and PR checklist included in repo.

## 12. Contact
- See CITATION.cff for maintainer contact.

Thank you for contributing.