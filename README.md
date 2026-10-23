# Doniyor’s writing

A practical voice reference for agents helping me write in English, Uzbek, and Russian. It favours clear, natural wording and actual context over fixed templates.

**[Download the complete PDF](doniyors-writing-skill.pdf)** · **[Read the skill](SKILL.md)** · **[Read the examples](references/examples.md)**

Version 2.0, 23 October 2026. The PDF includes the skill, examples, and public context. The Markdown files are the source of truth.

## Use it

For a chat agent, attach the PDF and give it the actual task, recipient, questions, and any word limit. Include your own draft when you have one. For example:

> Use this guide as a voice reference, not a template. Help me answer the questions below. Preserve my meaning, fix awkward wording, and do not add a biography or unsupported claims.

For an agent that supports directory-based skills, copy this folder into its documented skill location, including `SKILL.md` and `references/`. The exact installation path depends on the agent; this repository does not assume a particular product. Other agents can simply read those files as context.

The current request takes priority over this guide. The examples are not reusable facts about availability, pay, or experience duration. A translated document does not imply proficiency in speaking that language.

## What changed in version 2

The earlier guide required particular openings, closing lines, paragraph structures, personal insights, and disclosure of circumstances. It also made broad assumptions about which projects belonged in which jobs.

This edition replaces those formulas with contextual guidance. It distinguishes original writing, approved assistant drafts, and illustrative suggestions. It keeps a few clear preferences, such as no em dashes, accurate team credit, and natural translations. The new screening reply is included with sensitive details redacted.

The old PDF is deliberately not committed. It contained personal details that do not belong in a public style guide.

## Update it

1. Identify a real mismatch: save what the agent wrote, what you preferred, and why. Use a short example, not an entire private conversation.
2. Edit `SKILL.md` only if the lesson applies beyond that one message. Avoid converting one correction into a universal ban or required phrase.
3. Add useful evidence to `references/examples.md`. Label it as **Doniyor’s original writing**, **assistant draft explicitly approved by Doniyor**, or **illustrative suggestion**. Give the date and context. Approval should be explicit, not inferred from silence.
4. Update `references/public-context.md` only for useful public facts. Keep changing personal details out of the guide. Link to the current source instead of maintaining a second CV here.
5. Check the public diff. Remove phone numbers, personal email addresses, exact pay, grades or scores, schedules, private employer conversations, credentials, and identifying details about other people. Public examples may use explicit bracketed redactions. Do not commit the unredacted original first: deleting it later leaves it in Git history.
6. Update the version/date in the guide and README, and describe the reason in `CHANGELOG.md`.
7. Regenerate the PDF, inspect it, and commit the Markdown and PDF together. Do not edit the PDF directly.

## Build the PDF

Requires Python 3 and the packages in `requirements.txt`:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/build_pdf.py
```

The build uses DejaVu Sans for English, Uzbek, and Russian text. On Debian/Ubuntu, install `fonts-dejavu-core` if needed. On another system, set `WRITING_FONT_DIR` to a directory containing `DejaVuSans.ttf` and `DejaVuSans-Bold.ttf`.

The PDF is generated locally. The build script does not send source text to an external service.

## Check a revision

Try it on a short scheduling reply, an answer to several screening questions, a CV summary, and a project explanation. Include a translation example if you changed the language guidance. Ask:

- Did the agent answer the task without adding the same biography every time?
- Did it preserve useful phrasing rather than replace the author’s voice?
- Did it invent a motivation, turn a recommendation into a result, or reuse stale details?
- Does it know when one sentence is enough and when an explanation is necessary?

These are editorial checks, not a required output template. A public guide improves consistency, but Doniyor’s feedback on the actual draft remains the best evidence.

## Public boundaries

This repository intentionally omits the original private PDF, salary figures, exam scores, detailed academic records, exact availability, private contact details, and unredacted correspondence. Public project links are included for factual checking. Do not use this guide to impersonate Doniyor or to send messages without his authorization.
