# Contributing

Thanks for helping keep this the most useful directory of startup communities on the internet.

## Add a community

The README, CSV and llms.txt are generated from `scripts/data.py`, so don't edit `README.md` directly. Open a pull request that adds one tuple to the right section of `scripts/data.py`:

```python
("Name", "https://link", "Who gets the most from it", "One or two sentences on what it is and what makes it useful."),
```

A GitHub Action rebuilds the README when your change is merged. Not comfortable with Python? Open an issue with the name, link and a sentence on why it belongs, and it'll be added for you.

A community is accepted when it:

- is active (recent posts or events in the last 3 months)
- serves startup founders or people building toward founding
- has a working public link where people can join or apply
- describes itself accurately (no invented member counts or outcomes)

## Report a dead link or a closed community

Open an issue with the community name and what changed. Closed communities move to the "Recently closed" section.

## Listings are free

Listings are never sold. If you run a community you're adding, say so in the pull request, the same way the maintainer discloses his own.
