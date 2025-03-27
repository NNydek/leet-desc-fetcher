def generate_md_content(problem_data):
    if not problem_data:
        return ""
    md_content = f"""# {problem_data['title']}

**Difficulty:** {problem_data['difficulty']}  

## Description
{problem_data['description']}

---

*This README was generated automatically using Python.*

*Source code can be found at https://github.com/NNydek/leet-desc-fetcher*
"""
    return md_content
