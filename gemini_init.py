#!/usr/bin/env python3
"""
gemini_init.py

Create a LeetCode problem folder with AI-populated metadata using Gemini.
Takes a LeetCode problem URL and populates the template with correct metadata.

Usage:
    python gemini_init.py <leetcode_url>

Example:
    python gemini_init.py https://leetcode.com/problems/two-sum/

Requirements:
    pip install google-genai python-dotenv pydantic
"""

import json
import sys
import re
import shutil
import os
from pathlib import Path
from typing import List
from pydantic import BaseModel, Field
import google.genai as genai
from google.genai import types
from dotenv import load_dotenv


def fetch_problem_with_gemini(url: str, client, models: list) -> str:
    """Use Gemini to fetch and extract problem content from LeetCode URL."""
    
    prompt = f"""
Please visit this LeetCode problem URL and extract the complete problem information: {url}

I need you to fetch the webpage content and extract:
1. The exact problem number and title (e.g., "1. Two Sum")
2. The difficulty level (Easy/Medium/Hard) 
3. The problem description/statement
4. The topics/tags listed for this problem
5. Any example test cases

Please provide all the information you can gather from the webpage in a structured format.
"""

    # Try models to fetch content
    for model in models:
        try:
            print(f"🌐 Fetching problem content with {model}...")
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            content = response.text.strip()
            if content and len(content) > 100:  # Ensure we got meaningful content
                print(f"✅ Successfully fetched content with {model}")
                return content
        except Exception as e:
            print(f"⚠️  {model} failed to fetch content: {e}")
            if model == models[-1]:
                raise Exception(f"All models failed to fetch content. Last error: {e}")
            continue
    
    return ""


class ProblemMetadata(BaseModel):
    """Pydantic model for LeetCode problem metadata."""
    id: int = Field(description="Problem number extracted from title")
    title: str = Field(description="Problem name without the number prefix")
    difficulty: str = Field(description="Difficulty level", enum=["Easy", "Medium", "Hard"])
    tags: List[str] = Field(description="Topics/tags in lowercase with hyphens")


def analyze_with_gemini(problem_content: str, client, models: list) -> dict:
    """Use Gemini to extract metadata from problem content with model fallback."""

    prompt = f"""
Extract metadata from this LeetCode problem information:

{problem_content}

Instructions:
1. id: Extract the problem number from the title (e.g., "1. Two Sum" → 1)
2. title: Extract just the problem name without the number (e.g., "1. Two Sum" → "Two Sum")  
3. difficulty: Find the difficulty level (Easy/Medium/Hard)
4. tags: Find the topics and convert to lowercase with hyphens (e.g., "Hash Table" → "hash-table")
"""

    # Try models in order of preference with fallback
    for model in models:
        try:
            print(f"🧠 Analyzing metadata with {model}...")
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ProblemMetadata
                )
            )
            
            result = json.loads(response.text)
            print(f"✅ Successfully analyzed with {model}")
            return result
            
        except Exception as e:
            print(f"⚠️  {model} failed: {e}")
            if model == models[-1]:  # Last model in list
                raise Exception(f"All models failed. Last error: {e}")
            continue  # Try next model


def create_problem_folder(metadata: dict, problem_url: str):
    """Create problem folder using template and populate with metadata."""
    
    # Generate folder name
    problem_id = metadata.get('id', 0)
    
    # Extract slug directly from URL
    # e.g., https://leetcode.com/problems/k-closest-points-to-origin/ -> k-closest-points-to-origin
    match = re.search(r'/problems/([^/]+)', problem_url)
    if match:
        slug = match.group(1)
    else:
        # Fallback: create slug from title if URL parsing fails
        title = metadata.get('title', 'UNTITLED')
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    
    folder_name = f"{problem_id:04d}-{slug}"
    folder_path = Path("problems") / folder_name
    
    if folder_path.exists():
        print(f"⚠️  Folder {folder_name} already exists")
        return folder_path
    
    # Copy template
    template_path = Path('problems/.template-problem')
    if not template_path.exists():
        raise Exception("Template folder .template-problem not found")
    
    shutil.copytree(template_path, folder_path)
    
    # Update prompt.json with metadata
    prompt_data = {
        "id": metadata.get('id'),
        "title": metadata.get('title'),
        "url": problem_url,
        "difficulty": metadata.get('difficulty'),
        "tags": metadata.get('tags', [])
    }
    
    prompt_path = folder_path / 'prompt.json'
    prompt_path.write_text(json.dumps(prompt_data, indent=2), encoding='utf-8')
    
    return folder_path


def main():
    if len(sys.argv) != 2:
        print("Usage: python gemini_init.py <leetcode_url>")
        print("Example: python gemini_init.py https://leetcode.com/problems/two-sum/")
        sys.exit(1)
    
    problem_url = sys.argv[1]
    
    # Validate URL
    if 'leetcode.com/problems/' not in problem_url:
        print("✘ Invalid LeetCode problem URL")
        sys.exit(1)
    
    # Load environment variables and setup Gemini
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        print("✘ GOOGLE_API_KEY not found. Please add it to your .env file")
        sys.exit(1)
    
    try:
        client = genai.Client(api_key=api_key)
        
        # Model hierarchy: latest 2025 models (best to most cost-effective)
        models = [
            'gemini-2.5-pro',         # Most powerful model with adaptive thinking
            'gemini-2.5-flash',       # Stable 2.5 Flash workhorse model
            'gemini-2.5-flash-lite',  # Fast, low-cost, high-performance
            'gemini-2.0-flash-exp',   # Experimental 2.0 fallback
            'gemini-1.5-pro-002',     # Legacy enhanced reasoning
            'gemini-1.5-flash-002'    # Final stable fallback
        ]
    except Exception as e:
        print(f"✘ Gemini setup failed: {e}")
        sys.exit(1)
    
    try:
        print(f"🔍 Fetching problem from: {problem_url}")
        problem_content = fetch_problem_with_gemini(problem_url, client, models)
        
        if not problem_content:
            print("✘ Failed to fetch problem content")
            sys.exit(1)
        
        print("🤖 Analyzing problem with Gemini...")
        metadata = analyze_with_gemini(problem_content, client, models)
        
        print("📊 Extracted metadata:")
        print(json.dumps(metadata, indent=2))
        
        print("📁 Creating problem folder...")
        folder_path = create_problem_folder(metadata, problem_url)
        
        print(f"🆕 Created folder: {folder_path}")
        
        # Show folder structure
        try:
            import subprocess
            result = subprocess.run(['tree', '-L', '2', str(folder_path)], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout)
        except:
            print("Contents:")
            for item in sorted(folder_path.iterdir()):
                print(f"  {item.name}")
        
    except Exception as e:
        print(f"✘ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()