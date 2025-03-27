import os

def save_to_readme(md_content, folder_name="generated_readme", filename="README.md"):
    if not md_content:
        print("No data to save!")
        return None

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print(f"Saved problem details to {file_path}")
    print(f"File saved at: {os.path.abspath(file_path)}")
