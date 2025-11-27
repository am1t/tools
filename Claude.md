# Pocket Tools 🔧 - Claude Instructions

## Project Overview
This is a simple repository for building small, self-contained web tools. Each tool is a single HTML file with inline CSS and JavaScript - no build process, no dependencies, just open and use.

## Core Principles
- **KISS (Keep It Simple, Stupid)**: Simplicity over complexity
- **One file per tool**: Everything (HTML, CSS, JS) in a single file
- **No dependencies**: No npm, no build process, no frameworks unless absolutely necessary
- **Self-contained**: Each tool works independently
- **Easy to share**: Just copy the HTML file

## Repository Structure
```
/
├── README.md                    # Main documentation with tool list
├── index.html                   # Auto-generated landing page
├── generate-index.py            # Python generator script
├── Claude.md                    # This file - instructions for Claude Code
├── .gitignore
└── [tool-name]/                 # Each tool is a folder at root level
    ├── index.html               # Self-contained tool
    └── README.md                # Tool metadata and description
```

## Workflow for Adding New Tools

When asked to create a new tool, follow these steps:

1. **Choose a creative one-word name**:
   - Tool names should be single, creative words (e.g., "counter", "wordly", "markify", "quotify", "untrack")
   - Use kebab-case for folder names if compound (though single word is preferred)
   - The name should be memorable and reflect the tool's purpose
   - Examples: counter, wordly, markify, quotify, untrack

2. **Create tool directory**: `[tool-name]/` at the root level

3. **Create tool README**: `[tool-name]/README.md` with:
   ```markdown
   # Tool Name

   ## Metadata
   - **Category**: [Category Name]
   - **Created**: YYYY-MM-DD
   - **Updated**: YYYY-MM-DD

   ## Description
   Brief description of what the tool does.

   ## Features
   - Feature 1
   - Feature 2

   ## Usage
   How to use the tool.
   ```

4. **Create single HTML file**: `[tool-name]/index.html`
   - Complete HTML5 document
   - All CSS inline in `<style>` tags
   - All JavaScript inline in `<script>` tags
   - Clean, modern design following color palette
   - Mobile-responsive
   - Include a "← Back to Tools" link to `/` (root), centered at the bottom
   - Title format: `<title>[ToolName] - Brief Description</title>`
   - H1 should use the creative one-word name with an emoji

5. **Regenerate index.html**: Run `python generate-index.py`
   - This automatically discovers all tools with README.md files
   - No need to manually update the main README.md

6. **Commit changes**: Include tool HTML, tool README.md, and regenerated index.html

## Design Guidelines

### Visual Style
- Modern, clean design with rounded corners (8-12px border-radius)
- Use gradient backgrounds or solid colors
- Card-based layouts with subtle shadows
- Smooth transitions and hover effects
- Mobile-first responsive design

### Color Palette
- Background: #030222 (dark blue)
- Text: #f9bf77 (golden)
- Card Background: #F0ECDB (cream)
- Card Text: #222 (dark gray)
- Accent (in cards): #D64132 (red) - for buttons, links, highlights within cards
- Accent (outside cards): #f9bf77 (golden) - for header, footer, and body links

### Typography
- System font stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`
- Clear hierarchy with appropriate font sizes
- Adequate line-height (1.5-1.6) for readability

### Layout
- Max-width containers (500-800px for tools)
- Generous padding and spacing
- Centered layouts when appropriate
- Grid or flexbox for responsive layouts

## Code Standards

### HTML
- Use semantic HTML5 elements
- Include proper meta tags (charset, viewport)
- Descriptive title tags
- Clean, indented structure

### CSS
- Mobile-first media queries
- CSS variables for repeated values (optional)
- Smooth transitions for interactive elements
- Consistent spacing units (rem/em preferred)
- Box-sizing: border-box on all elements

### JavaScript
- Use modern ES6+ syntax
- Event delegation where appropriate
- Clear, descriptive variable and function names
- Comments for complex logic
- No external dependencies unless absolutely necessary

## Example Tool Template

When creating a new tool, use this basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tool Name</title>
    <style>
        /* Reset and base styles */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            /* ... */
        }
        
        /* Tool-specific styles */
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 Tool Name</h1>
        <p class="description">Brief description</p>
        
        <!-- Tool content -->
        
        <a href="../../" class="back-link">← Back to all tools</a>
    </div>
    
    <script>
        // Tool JavaScript
    </script>
</body>
</html>
```

## Common Tool Ideas
- Calculators (basic, scientific, tip, mortgage)
- Text tools (word counter, case converter, diff checker)
- Converters (units, currency, time zones)
- Generators (QR codes, lorem ipsum, passwords)
- Utilities (color picker, timer, stopwatch)
- Fun tools (random picker, dice roller, magic 8-ball)

## Testing Before Committing
- Open the HTML file in a browser
- Test on mobile viewport (use browser dev tools)
- Verify all functionality works
- Check that back link works correctly
- Ensure no console errors

## Git Workflow
```bash
# After creating a tool
git add .
git commit -m "Add [tool-name] tool"
git push origin main
```

## Tool README.md Format

Each tool must have its own `README.md` file in its directory with this structure:

```markdown
# Tool Name

## Metadata
- **Category**: [Category like "Utility", "Calculator", "Text Tool", etc.]
- **Created**: YYYY-MM-DD
- **Updated**: YYYY-MM-DD

## Description
A brief description (1-2 sentences) that will appear on the main index page.

## Features
- Feature 1
- Feature 2

## Usage
Instructions on how to use the tool.
```

The generator script automatically scans the root directory for tool folders (those with both `index.html` and `README.md`) and extracts this information.

## Notes
- The index.html is auto-generated - NEVER edit it manually
- Always regenerate index.html after adding or updating tools
- Each tool needs its own README.md with metadata (category, created, updated)
- The generator automatically discovers tools - no manual registration needed
- Tools are accessible at `/<folder-name>/` (the folder name becomes the slug)
- Use kebab-case for folder names (e.g., `word-counter`, `color-picker`)
- Keep tools simple and focused on one task
- Prioritize user experience and accessibility
- Test thoroughly before committing

## When in Doubt
- Check the counter tool for reference
- Keep it simple - KISS principle
- Ask for clarification if requirements are unclear
- Focus on making tools useful and easy to use
