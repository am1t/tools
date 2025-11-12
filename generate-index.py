#!/usr/bin/env python3
"""
Generate index.html from README.md and individual tool READMEs
Extracts tool information and creates a simple landing page
"""

import os
from datetime import datetime

def parse_tool_readme(tool_path):
    """Parse a tool's README.md and extract metadata and description"""
    readme_path = os.path.join(tool_path, 'README.md')

    if not os.path.exists(readme_path):
        return None

    with open(readme_path, 'r') as f:
        content = f.read()

    tool_info = {}
    lines = content.split('\n')

    # Extract tool name (first h1)
    for line in lines:
        if line.startswith('# '):
            tool_info['name'] = line.replace('# ', '').strip()
            break

    # Extract metadata
    in_metadata = False
    for line in lines:
        if line.strip() == '## Metadata':
            in_metadata = True
            continue

        if in_metadata:
            if line.startswith('## '):
                break

            if '**Category**:' in line or '- **Category**:' in line:
                tool_info['category'] = line.split(':', 1)[1].strip()
            elif '**Created**:' in line or '- **Created**:' in line:
                tool_info['created'] = line.split(':', 1)[1].strip()
            elif '**Updated**:' in line or '- **Updated**:' in line:
                tool_info['updated'] = line.split(':', 1)[1].strip()

    # Extract description (first paragraph after ## Description)
    in_description = False
    description_lines = []
    for line in lines:
        if line.strip() == '## Description':
            in_description = True
            continue

        if in_description:
            if line.startswith('## '):
                break
            if line.strip():
                description_lines.append(line.strip())
            elif description_lines:  # Stop at first empty line after content
                break

    tool_info['description'] = ' '.join(description_lines)

    return tool_info

def find_tools():
    """Find all tool directories and extract their information"""
    tools = []

    # Exclude these directories from tool scanning
    exclude_dirs = {'.git', '.github', 'node_modules', '__pycache__', '.vscode', '.idea'}

    # Scan current directory for tool directories
    for item in sorted(os.listdir('.')):
        # Skip files, hidden dirs, and excluded dirs
        if not os.path.isdir(item) or item.startswith('.') or item in exclude_dirs:
            continue

        tool_path = item

        # Check if this directory has both index.html AND README.md (tool markers)
        has_index = os.path.exists(os.path.join(tool_path, 'index.html'))
        has_readme = os.path.exists(os.path.join(tool_path, 'README.md'))

        if not (has_index and has_readme):
            continue

        # Parse the tool's README
        tool_info = parse_tool_readme(tool_path)

        if tool_info:
            # Use folder name as slug, path is just /{slug}/
            tool_info['slug'] = item
            tool_info['path'] = f'/{item}/'
            tools.append(tool_info)

    return tools

def format_date(date_str):
    """Convert YYYY-MM-DD to DD MMM YYYY format"""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d %b %Y')
    except (ValueError, TypeError):
        return date_str

def generate_html(tools):
    """Generate the index.html content"""

    tools_html = ''
    for tool in tools:
        name = tool.get('name', 'Unnamed Tool')
        path = tool.get('path', '')
        description = tool.get('description', 'No description')
        category = tool.get('category', 'Uncategorized')

        # Truncate description to ~80 chars for compact display
        short_desc = description[:80] + '...' if len(description) > 80 else description

        tools_html += f'''
            <a href="{path}" class="tool-pill">
                <div class="tool-header">
                    <h3>{name}</h3>
                    <span class="category">{category}</span>
                </div>
                <p class="tool-desc">{short_desc}</p>
            </a>
'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tools | Amit Gawande</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #f9bf77;
            background: #030222;
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 800px;
            margin: 0 auto;
        }}

        header {{
            text-align: center;
            color: #f9bf77;
            padding: 40px 20px;
        }}

        h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}

        .subtitle {{
            font-size: 1.5em;
            opacity: 0.9;
        }}

        .tools-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
            margin-top: 30px;
        }}

        .tool-pill {{
            background: #F0ECDB;
            border-radius: 12px;
            padding: 20px;
            text-decoration: none;
            display: block;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .tool-pill:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }}

        .tool-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}

        .tool-pill h3 {{
            color: #222;
            font-size: 1.2em;
            margin: 0;
        }}

        .category {{
            background: #D64132;
            color: #F0ECDB;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.75em;
            font-weight: 500;
            white-space: nowrap;
        }}

        .tool-desc {{
            color: #666;
            font-size: 0.9em;
            margin: 0;
            line-height: 1.4;
        }}

        footer {{
            text-align: center;
            color: #f9bf77;
            padding: 40px 20px;
            opacity: 0.8;
            font-size: 0.9em;
        }}

        footer a {{
            color: #f9bf77;
            text-decoration: underline;
        }}

        @media (max-width: 768px) {{
            .tools-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}

        @media (max-width: 500px) {{
            h1 {{
                font-size: 2em;
            }}

            .tools-grid {{
                grid-template-columns: 1fr;
            }}

            .tool-pill {{
                padding: 15px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{{ pocket.tools }}</h1>
            <p class="subtitle">Simple, self-contained web tools</p>
        </header>

        <div class="tools-grid">{tools_html}
        </div>

        <footer>
            <p>Last updated on {datetime.now().strftime('%d %b %Y at %H:%M:%S')}</p>
            <p>©<a href="https://amitgawande.com">Amit Gawande</a></p>
        </footer>
    </div>
</body>
</html>
'''

    return html

def main():
    print("Scanning tools directory...")
    tools = find_tools()
    print(f"Found {len(tools)} tool(s)")

    if not tools:
        print("Warning: No tools found with README.md files")
        return

    # Sort tools by updated date (newest first)
    tools.sort(key=lambda t: t.get('updated', '1900-01-01'), reverse=True)

    print("Generating index.html...")
    html = generate_html(tools)

    with open('index.html', 'w') as f:
        f.write(html)

    print("✓ index.html generated successfully!")

if __name__ == '__main__':
    main()
