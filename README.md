# skills

My custom skills, one folder each, on the [Agent Skills](https://agentskills.io) standard.

| Skill | What it does |
| --- | --- |
| [`no-ai-slop`](no-ai-slop) | Write prose that reads like a person wrote it, not a language model. |
| [`doniyors-writing`](doniyors-writing) | Draft or edit text in Doniyor's voice in English, Uzbek, or Russian. |

## Install

**Any agent**, through the [skills](https://skills.sh) CLI:

```bash
npx skills add doniyor117/skills                        # pick from the list
npx skills add doniyor117/skills --skill no-ai-slop     # one skill
```

**Claude Code**, as plugins:

```
/plugin marketplace add doniyor117/skills
/plugin install no-ai-slop@doniyor-skills
/plugin install doniyors-writing@doniyor-skills
```

**By hand**: clone the repo and copy or symlink a skill folder into `~/.claude/skills/`.

## Adding a skill

Create a folder named exactly like the skill's `name`, with a `SKILL.md` inside, and add an entry to `.claude-plugin/marketplace.json`. Each skill's own `AGENTS.md` has its maintenance rules.

The standalone repos `no-ai-slop` and `writing-skill` are superseded by this one.
