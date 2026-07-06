# Fantasy Sports Waiver Agent

## Pattern

League roster intake, waiver candidate analysis, injury/news signal merge, matchup scoring, claim recommendation, and responsible-use note.

## Flow

Waiver Review Schedule -> Fetch League Roster -> Fetch Player News -> Fetch Matchups -> Waiver Agent -> Confidence Gate -> Watchlist or Claim Recommendation -> Audit -> Summary.

## Useful For

Fantasy football, fantasy basketball, dynasty leagues, casual sports fans, newsletter tools, and anyone who wants structured waiver research without doom-scrolling player blurbs.

## Setup Notes

Reconnect OpenAI, Slack, Google Sheets, and sports-data credentials. Replace league, player news, matchup, and scoring endpoints with your own providers.

## Validation Focus

The workflow labels recommendations as research, includes confidence and injury caveats, and avoids making betting or gambling claims.
