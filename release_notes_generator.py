def format_release_notes(issues):
    """Generates HTML-based release notes in tabular format."""
    notes = """
    <h2>🚀 Sprint Release Notes</h2>
    <table border="1">
        <tr>
            <th>Jira ticket #</th>
            <th>Title</th>
            <th>Short description of Fix/Feature/Value Add</th>
            <th>Screenshots / Videos</th>
            <th>Content edit for review</th>
            <th>Questions, Comments, Notes</th>
        </tr>
    """

    for category, items in issues.items():
        notes += f"<tr><th colspan='6'>{category}</th></tr>"
        for issue in items:
            notes += f"""
            <tr>
                <td>{issue['Jira ticket #']}</td>
                <td>{issue['Title']}</td>
                <td>{issue['Short description of Fix/Feature/Value Add']}</td>
                <td>{issue.get('Screenshots / Videos', '')}</td>
                <td>{issue.get('Content edit for review', '')}</td>
                <td>{issue.get('Questions, Comments, Notes', '')}</td>
            </tr>
            """
    
    notes += "</table>"
    return notes