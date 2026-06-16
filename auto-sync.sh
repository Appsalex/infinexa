#!/bin/bash
echo "👀 Watching for changes..."
fswatch -o . --exclude='.git' | while read; do
  git add -A
  git commit -m "auto-sync: $(date '+%H:%M:%S')"
  git push
  echo "✅ Subido a GitHub!"
done
