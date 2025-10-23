#!/usr/bin/env python3
"""
Generate index.html from README.md
Extracts tool information and creates a simple landing page
"""

import re
from datetime import datetime

def parse_readme():
    """Parse README.md and extract tool information"""
    with open('README.md', 'r') as f:
        content = f.read()

    # Extract tools section
    tools = []
    in_tools_section = False
    current_tool = {}

    lines = content.split('\n')
    for line in lines:
        # Start of Available Tools section
        if line.strip() == '## Available Tools':
            in_tools_section = True
            continue

        # End of Available Tools section
        if in_tools_section and line.startswith('## ') and 'Available Tools' not in line:
            break

        if in_tools_section:
            # Tool name (h3 heading)
            if line.startswith('### '):
                if current_tool:
                    tools.append(current_tool)
                current_tool = {'name': line.replace('### ', '').strip()}

            # Path
            elif line.startswith('**Path**:'):
                path = line.replace('**Path**:', '').strip().strip('`')
                current_tool['path'] = path

            # Description
            elif line.startswith('**Description**:'):
                desc = line.replace('**Description**:', '').strip()
                current_tool['description'] = desc

    if current_tool:
        tools.append(current_tool)

    return tools

def generate_html(tools):
    """Generate the index.html content"""

    tools_html = ''
    for tool in tools:
        name = tool.get('name', 'Unnamed Tool')
        path = tool.get('path', '')
        description = tool.get('description', 'No description')

        tools_html += f'''
            <div class="tool-card">
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
    print("Parsing README.md...")
    tools = parse_readme()
    print(f"Found {len(tools)} tool(s)")

    print("Generating index.html...")
    html = generate_html(tools)

    with open('index.html', 'w') as f:
        f.write(html)

    print("✓ index.html generated successfully!")

if __name__ == '__main__':
    main()
