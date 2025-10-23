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

def generate_html(tools):
    """Generate the index.html content"""

    tools_html = ''
    for tool in tools:
        name = tool.get('name', 'Unnamed Tool')
        path = tool.get('path', '')
        description = tool.get('description', 'No description')
        category = tool.get('category', 'Uncategorized')
        updated = tool.get('updated', 'Unknown')

        tools_html += f'''
            <div class="tool-card">
                <div class="tool-meta">
                    <span class="category">{category}</span>
                    <span class="updated">Updated: {updated}</span>
                </div>
                <h2>{name}</h2>
                <p>{description}</p>
                <a href="{path}" class="tool-link">Open Tool →</a>
            </div>
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
            gap: 20px;
            margin-top: 30px;
        }}

        .tool-card {{
            background: #F0ECDB;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .tool-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        }}

        .tool-meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            font-size: 0.85em;
            color: #666;
        }}

        .category {{
            background: #030222;
            color: #F0ECDB;
            padding: 4px 12px;
            border-radius: 12px;
            font-weight: 500;
            font-size: 0.9em;
        }}

        .updated {{
            color: #666;
        }}

        .tool-card h2 {{
            color: #222;
            margin-bottom: 10px;
            font-size: 1.5em;
        }}

        .tool-card p {{
            color: #222;
            margin-bottom: 20px;
        }}

        .tool-link {{
            display: inline-block;
            background: #030222;
            color: #F0ECDB;
            padding: 10px 20px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 500;
            transition: background 0.2s;
        }}

        .tool-link:hover {{
            background: #b53527;
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

        @media (max-width: 600px) {{
            h1 {{
                font-size: 2em;
            }}

            .tool-card {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>{{ tools.amitgawande }}</h1>
            <p class="subtitle">Simple, self-contained web tools</p>
        </header>

        <div class="tools-grid">{tools_html}
        </div>

        <footer>
            <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
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

    print("Generating index.html...")
    html = generate_html(tools)

    with open('index.html', 'w') as f:
        f.write(html)

    print("✓ index.html generated successfully!")

if __name__ == '__main__':
    main()
