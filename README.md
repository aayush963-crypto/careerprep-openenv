# CareerPrep OpenEnv

CareerPrep OpenEnv is a simple benchmark environment designed for evaluating AI agents on career guidance tasks.

## Objective
This environment tests whether an AI agent can respond effectively to common student and fresher career-related questions.

## Example Tasks
- Resume improvement for internships
- Data analytics skill suggestions
- HR interview preparation
- Web development project recommendations
- LinkedIn optimization advice

## Components
- `tasks.py` → benchmark tasks
- `grader.py` → keyword-based reward scoring
- `env.py` → environment logic
- `baseline_agent.py` → simple rule-based agent
- `run_baseline.py` → evaluation script

## How it works
1. The environment provides a career-related question.
2. The agent generates a response.
3. The grader checks the response against expected keywords.
4. A reward score is assigned.

## Why this matters
CareerPrep OpenEnv demonstrates how domain-specific evaluation environments can be created for student-focused AI systems, especially in resume building, interview preparation, and job-readiness guidance.