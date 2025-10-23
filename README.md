# Web Tools Collection

A collection of simple, self-contained web tools. Each tool is a single HTML file with no external dependencies.

## Philosophy

- **KISS Principle**: Keep It Simple, Stupid
- **One File Per Tool**: Each tool is completely self-contained in a single `index.html` file
- **No Dependencies**: No frameworks, no build tools, no external libraries (unless absolutely necessary)
- **Mobile-Friendly**: All tools should work well on mobile devices
- **Zero Setup**: Just open the HTML file in a browser

## Available Tools

### Example Tool
**Path**: `tools/example-tool/`
**Description**: A simple demonstration tool showing the pattern for creating new tools. Includes a basic counter and styling examples.

## Adding New Tools

1. Create a new directory under `tools/` with a descriptive name (use kebab-case)
2. Create an `index.html` file in that directory
3. Follow the self-contained pattern (see `tools/example-tool/index.html`)
4. Add your tool to this README under "Available Tools"
5. Run `python generate-index.py` to update the main index page

## Structure

```
tools/
├── README.md                    # This file
├── index.html                   # Auto-generated landing page
├── generate-index.py            # Script to generate index.html
└── tools/
    └── example-tool/
        └── index.html          # Self-contained tool
```

## Building

To regenerate the landing page:

```bash
python generate-index.py
```

This will read this README.md file and generate a new `index.html` with links to all tools.

## License

Public Domain - do whatever you want with these tools.
