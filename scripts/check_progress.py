import os
import nbformat
import webbrowser

def get_notebook_completion_percentage(nb_path):
    try:
        nb = nbformat.read(nb_path, as_version=4)
    except Exception:
        return 0

    code_cells = [cell for cell in nb.cells if cell.cell_type == 'code']
    if not code_cells:
        return 0

    executed = sum(1 for cell in code_cells if cell.get('execution_count') is not None)
    completion = (executed / len(code_cells)) * 100
    return completion

def color_for_progress(pct):
    if pct < 30:
        return '#e74c3c'  # red
    elif pct <= 70:
        return '#f1c40f'  # yellow
    else:
        return '#2ecc71'  # green

def generate_html_report(progress, output_path='progress_report.html'):
    rows = []
    for week, pct in progress.items():
        color = color_for_progress(pct)
        bar_width = pct
        row = f'''
        <tr>
            <td>{week}</td>
            <td style="width: 70%;">
                <div style="background-color: #ddd; width: 100%; height: 20px; border-radius: 4px;">
                    <div style="width: {bar_width}%; background-color: {color}; height: 100%; border-radius: 4px;"></div>
                </div>
            </td>
            <td>{pct:.1f}%</td>
        </tr>
        '''
        rows.append(row)

    html_content = f'''
    <html>
    <head>
        <title>Course Progress Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 30px;
            }}
            table {{
                border-collapse: collapse;
                width: 60%;
            }}
            th, td {{
                text-align: left;
                padding: 8px;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h2>Course Progress Report</h2>
        <table>
            <thead>
                <tr><th>Week</th><th>Progress</th><th>Completion %</th></tr>
            </thead>
            <tbody>
                {''.join(rows)}
            </tbody>
        </table>
    </body>
    </html>
    '''

    with open(output_path, 'w') as f:
        f.write(html_content)

    print(f"HTML progress report saved to {output_path}")
    abs_path = os.path.abspath(output_path)
    webbrowser.open(f'file://{abs_path}')
def main():
    base_dir = '../notebooks'  # relative to /scripts folder
    progress = {}

    for week_folder in sorted(os.listdir(base_dir)):
        week_path = os.path.join(base_dir, week_folder)
        if os.path.isdir(week_path):
            # Assume two notebooks per week: python and R
            notebooks = [f for f in os.listdir(week_path) if f.endswith('.ipynb')]
            if not notebooks:
                progress[week_folder] = 0
                continue

            completions = []
            for nb_file in notebooks:
                nb_path = os.path.join(week_path, nb_file)
                completion = get_notebook_completion_percentage(nb_path)
                completions.append(completion)
            # Average progress of all notebooks in the week
            avg_completion = sum(completions) / len(completions)
            progress[week_folder] = avg_completion

    generate_html_report(progress)

if __name__ == '__main__':
    main()
