<h3 align="center">Leetcode description Fetcher</h3>

---
## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## About <a name = "about"></a>
This project was made to fetch problem descriptions from [LeetCode](https://leetcode.com/) and save them into a `README.md` file for use in other repositories, such as **LeetCode Solutions**. By using this script, you can easily get details like the title, description, difficulty, likes/dislikes and have them organized in a Markdown file.

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine.
1. Go to [Prerequisites](#prerequisites) and install required software.
2. Download project files - [ZIP](https://github.com/NNydek/leet-desc-fetcher/archive/refs/heads/main.zip) or `gh repo clone NNydek/leet-desc-fetcher`
3. Go to [Usage](#usage) 

## Prerequisites <a name = "prerequisites"></a>
Before running this script, make sure you have installed:

- **Python 3.x** (preferably Python 3.12+). You can download Python from [here](https://www.python.org/downloads/).

### Dependencies
The script requires the following Python libraries:
- `requests`

To install the dependencies, run the following command in your terminal:
```bash
pip install requests
```

## Usage <a name="usage"></a>
1. Navigate to the project directory (remember to include proper file path):
```bash
cd leetcode-problem-fetcher
```
2. By default, the script will fetch the description for the [rising temperature](https://leetcode.com/problems/rising-temperature/description/) problem.
In a file `main.py` change value of variable `problem_slug` to a problem you wish to fetch a description from.
Slug can be found in a LeetCode URL of the problem, e.g. `https://leetcode.com/problems/rising-temperature/description/` and the slug is `rising-temperature`

4. Run the Python script to fetch problem details and save them to README.md:
```bash
python main.py
```
4. Once the script runs successfully, the details of the LeetCode problem will be saved in a `README.md` file within `generated_readme` directory.


## Built Using <a name = "built_using"></a>
- [Visual Studio Code](https://code.visualstudio.com/) - Development Environment
- [Python 3.12.0](https://www.python.org/downloads/) - Programming Language

## Authors <a name = "authors"></a>
- [@NNydek](https://github.com/nnydek) - Initial work

## Acknowledgements <a name = "acknowledgement"></a>
- [The-Documentation-Compendium](https://github.com/kylelobo/The-Documentation-Compendium) - kylelobo
