#!/usr/bin/env python3

import json
import os
from collections import defaultdict
from typing import Dict, List, Tuple

def load_json_file(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)

def get_all_problems() -> List[Tuple[str, dict, dict]]:
    problems = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and item[0].isdigit():
            prompt_path = os.path.join(item, 'prompt.json')
            submission_path = os.path.join(item, 'submission.json')
            
            if os.path.exists(prompt_path) and os.path.exists(submission_path):
                prompt = load_json_file(prompt_path)
                submission = load_json_file(submission_path)
                problems.append((item, prompt, submission))
    
    return problems

def generate_statistics(problems: List[Tuple[str, dict, dict]]) -> Dict:
    stats = {
        'total_problems': len(problems),
        'difficulty_count': defaultdict(int),
        'tag_count': defaultdict(int),
        'avg_runtime': 0,
        'avg_memory': 0,
        'avg_time_percentile': 0,
        'avg_memory_percentile': 0,
        'languages': defaultdict(int)
    }
    
    total_runtime = 0
    total_memory = 0
    total_time_percentile = 0
    total_memory_percentile = 0
    
    for _, prompt, submission in problems:
        # Count difficulties
        stats['difficulty_count'][prompt['difficulty']] += 1
        
        # Count tags
        for tag in prompt['tags']:
            stats['tag_count'][tag] += 1
        
        # Sum up metrics
        total_runtime += submission['runtime_ms']
        total_memory += submission['memory_mb']
        total_time_percentile += submission['time_percentile']
        total_memory_percentile += submission['memory_percentile']
        
        # Count languages
        stats['languages'][submission['language']] += 1
    
    # Calculate averages
    stats['avg_runtime'] = total_runtime / len(problems)
    stats['avg_memory'] = total_memory / len(problems)
    stats['avg_time_percentile'] = total_time_percentile / len(problems)
    stats['avg_memory_percentile'] = total_memory_percentile / len(problems)
    
    return stats

def generate_markdown_table(stats: Dict) -> str:
    md = "## 📊 Statistics\n\n"
    
    # Overall stats
    md += "### Overall\n\n"
    md += f"- Total Problems Solved: {stats['total_problems']}\n"
    md += f"- Average Runtime: {stats['avg_runtime']:.2f} ms\n"
    md += f"- Average Memory: {stats['avg_memory']:.2f} MB\n"
    md += f"- Average Time Percentile: {stats['avg_time_percentile']:.2f}%\n"
    md += f"- Average Memory Percentile: {stats['avg_memory_percentile']:.2f}%\n\n"
    
    # Difficulty breakdown
    md += "### Difficulty Breakdown\n\n"
    md += "| Difficulty | Count |\n"
    md += "|------------|-------|\n"
    for diff, count in sorted(stats['difficulty_count'].items()):
        md += f"| {diff} | {count} |\n"
    md += "\n"
    
    # Top tags
    md += "### Top Tags\n\n"
    md += "| Tag | Count |\n"
    md += "|-----|-------|\n"
    for tag, count in sorted(stats['tag_count'].items(), key=lambda x: x[1], reverse=True)[:10]:
        md += f"| {tag} | {count} |\n"
    md += "\n"
    
    # Languages used
    md += "### Languages Used\n\n"
    md += "| Language | Count |\n"
    md += "|----------|-------|\n"
    for lang, count in sorted(stats['languages'].items()):
        md += f"| {lang} | {count} |\n"
    
    return md

def update_readme(stats_md: str):
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Find the position to insert stats
    if "## 📊 Statistics" in content:
        # Update existing stats section
        start = content.find("## 📊 Statistics")
        end = content.find("##", start + 1)
        if end == -1:
            end = len(content)
        content = content[:start] + stats_md + content[end:]
    else:
        # Add stats section before the first ##
        first_section = content.find("##")
        if first_section == -1:
            content += "\n" + stats_md
        else:
            content = content[:first_section] + stats_md + content[first_section:]
    
    with open('README.md', 'w') as f:
        f.write(content)

def main():
    problems = get_all_problems()
    stats = generate_statistics(problems)
    stats_md = generate_markdown_table(stats)
    update_readme(stats_md)
    print("Statistics updated in README.md")

if __name__ == "__main__":
    main() 