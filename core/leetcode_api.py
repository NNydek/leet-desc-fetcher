import requests

def get_leetcode_problem(slug):
    url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        title
        content
        difficulty
        likes
        dislikes
      }
    }
    """
    variables = {"titleSlug": slug}
    response = requests.post(url, json={"query": query, "variables": variables})
    
    if response.status_code == 200:
        data = response.json()
        question = data["data"]["question"]
        return {
            "title": question["title"],
            "description": question["content"],
            "difficulty": question["difficulty"],
            "likes": question["likes"],
            "dislikes": question["dislikes"],
        }
    else:
        return None
