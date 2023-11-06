#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Ask ChatGPT
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Question" }

# Documentation:
# @raycast.author Stephan Fitzpatrick

~/.local/bin/ask "$1"
