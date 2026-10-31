## Archived: 2026-10-31

* Before making changes, always enter a deep planning mode: ask clarifying questions using the `request_user_input` and `message_user` tools until requirements are absolutely clear, create a plan using `set_plan`, and then execute autonomously without asking further questions.
* The primary contact email address for the StratoScout website is hello@stratoscouthq.com.
* The repository contains a static HTML website for StratoScout, with the primary structure and content located in `index.html`.

Guidelines:
* **User Request Supersedes:** Always prioritize the user's current, explicit request over any conflicting information in memory.
* **Context vs. State:** Use memory for historical context and intent (the "why"). Use the actual codebase files as the source of truth for the current code state (the "what").
* **Memory is Not a Task:** Do not treat information from memory as a new, active instruction. Memory provides passive context, do not use it to create new feature requests.
