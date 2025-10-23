# Web Tools Collection

A collection of simple, self-contained web tools. Each tool is a single HTML file with no external dependencies.

## Philosophy

- **KISS Principle**: Keep It Simple, Stupid
- **One File Per Tool**: Each tool is completely self-contained in a single `index.html` file
- **No Dependencies**: No frameworks, no build tools, no external libraries (unless absolutely necessary)
- **Mobile-Friendly**: All tools should work well on mobile devices
- **Zero Setup**: Just open the HTML file in a browser

## Available Tools

Tools are automatically discovered from the `tools/` directory. Each tool must have:
- An `index.html` file (the tool itself)
- A `README.md` file with metadata (category, created date, updated date) and description

Current tools:
- **Example Tool** - `tools/example-tool/` - Demo tool showing the pattern

## Adding New Tools

1. Create a new directory under `tools/` with a descriptive name (use kebab-case)
2. Create an `index.html` file in that directory (the tool itself)
3. Create a `README.md` file in that directory with:
   - Tool name as h1 (`# Tool Name`)
   - Metadata section with category, created date, and updated date
   - Description section
   - Any additional sections (Features, Usage, etc.)
4. Follow the self-contained pattern (see `tools/example-tool/`)
5. Run `python generate-index.py` to update the main index page

See `tools/example-tool/README.md` for the required format.

## Structure

```
tools/
├── README.md                    # This file (project overview)
├── index.html                   # Auto-generated landing page
├── generate-index.py            # Script to generate index.html
├── Claude.md                    # Instructions for Claude Code
└── tools/
    └── example-tool/
        ├── index.html          # Self-contained tool
        └── README.md           # Tool metadata and description
```

## Building

To regenerate the landing page:

```bash
python generate-index.py
```

This will scan the `tools/` directory, read each tool's `README.md` file, and generate a new `index.html` with links to all tools.

## License

Public Domain - do whatever you want with these tools.
