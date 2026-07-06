# Study Spaced Repetition Agent

## Pattern

Study-topic intake, quiz-history review, weak-area scoring, spaced repetition schedule generation, card creation, and progress audit.

## Flow

Study Plan Webhook -> Normalize Study Goal -> Fetch Quiz History -> Fetch Existing Cards -> Study Agent -> Mastery Gate -> Review Queue or New Cards -> Audit -> Respond.

## Useful For

Students, certification prep, language practice, interview prep, athletes learning playbooks, and anyone who wants review sessions based on weak areas instead of vibes.

## Setup Notes

Reconnect OpenAI, Google Sheets, and Slack credentials. Replace the quiz-history sheet, card bank, review channel, and audit sheet before using with real study data.

## Validation Focus

The workflow uses quiz evidence and confidence scores to decide what to review next, and it preserves weak-area reasons so future sessions can improve.
