import os
import re
import yaml

REL_MAP = "maps/relationships.yaml"
OUTPUT_DIR = "final_posts/"

def extract_sections(file_path, include_sections):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    extracted = []
    for section in include_sections:
        pattern = rf"## \[project:{section}\](.*?)(?=\n## \[project:|\Z)"
        match = re.search(pattern, content, re.S)
        if match:
            extracted.append(match.group(0).strip())
    return "\n\n".join(extracted)

def build_blog():
    with open(REL_MAP, "r") as f:
        config = yaml.safe_load(f)

    for key, cfg in config.items():
        title = cfg["title"]
        series = cfg.get("series", "")
        tags = cfg.get("tags", [])
        cover = cfg.get("cover", "")
        project_file = cfg["project_file"]
        sections = cfg["project_sections"]["include"]

        content = extract_sections(project_file, sections)

        frontmatter = [
            "---",
            f'title: "{title}"',
            f"series: {series}",
            f"tags: {tags}",
            f'cover: "{cover}"',
            "---\n"
        ]

        final_output = "\n".join(frontmatter) + content

        os.makedirs(OUTPUT_DIR, exist_ok=True)
        out_file = f"{OUTPUT_DIR}/{key}.md"

        with open(out_file, "w") as out:
            out.write(final_output)

        print(f"Generated {out_file}")

if __name__ == "__main__":
    build_blog()
