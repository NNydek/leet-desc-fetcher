from core.leetcode_api import get_leetcode_problem
from core.md_generator import generate_md_content
from core.file_handler import save_to_readme

def main():
    problem_slug = "rising-temperature"  # Change this to any problem's slug
    problem_data = get_leetcode_problem(problem_slug)
    md_content = generate_md_content(problem_data)
    save_to_readme(md_content)

if __name__ == "__main__":
    main()
