#!/usr/bin/env bash
# Usage: ./create_problem.sh <id> "<title>" <URL>

set -e

if [[ $# -lt 3 ]]; then
  echo "Usage: $0 <id> \"<title>\" <URL>"
  exit 1
fi

id_raw=$1
title_raw="$2"
url=$3

# zero-pad ID to 4 digits
printf -v id "%04d" "$id_raw"

# slug: lower-case, replace spaces/non-alnum with hyphens
slug=$(echo "$title_raw" | tr '[:upper:]' '[:lower:]' | tr -c 'a-z0-9' '-' | tr -s '-' | sed 's/-$//')

dir="${id}-${slug}"

# copy template
cp -r .template-problem "$dir"

# fill prompt.json placeholders
jq \
  --arg id "$id_raw" \
  --arg title "$title_raw" \
  --arg url "$url" \
  '.id = ($id|tonumber) | .title = $title | .url = $url' \
  "$dir/prompt.json" > "$dir/prompt.json.tmp" && mv "$dir/prompt.json.tmp" "$dir/prompt.json"

# touch other files to give git something non-empty to track
> "$dir/solution.py"        # empty file (overwrite)
echo "<!-- auto-generated, run your LLM script later -->" > "$dir/README.md"

echo "🆕  Created folder: $dir"
tree -L 2 "$dir"
