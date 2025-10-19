#!/usr/bin/env python3
"""
Fetch GitHub repository descriptions using gh CLI
This script can process single repos or batch process from README.md
"""

import subprocess
import json
import re
import sys
from pathlib import Path
from typing import Optional, List, Dict


def get_repo_info(repo_path: str) -> Optional[Dict]:
    """
    Fetch repository info using gh CLI

    Args:
        repo_path: Repository path in format "owner/repo"

    Returns:
        Dict with repo info or None if failed
    """
    try:
        # Use gh api to get repo info
        cmd = ["gh", "api", f"repos/{repo_path}"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        repo_data = json.loads(result.stdout)

        return {
            "name": repo_data["name"],
            "full_name": repo_data["full_name"],
            "description": repo_data.get("description", "No description available"),
            "language": repo_data.get("language", "Unknown"),
            "stars": repo_data.get("stargazers_count", 0),
            "topics": repo_data.get("topics", []),
            "homepage": repo_data.get("homepage", ""),
            "archived": repo_data.get("archived", False),
            "fork": repo_data.get("fork", False),
        }
    except subprocess.CalledProcessError as e:
        print(f"Error fetching {repo_path}: {e.stderr}", file=sys.stderr)
        return None
    except json.JSONDecodeError:
        print(f"Error parsing response for {repo_path}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error for {repo_path}: {e}", file=sys.stderr)
        return None


def extract_repos_from_readme(readme_path: str = "README.md") -> List[str]:
    """
    Extract GitHub repository URLs from README.md

    Args:
        readme_path: Path to README file

    Returns:
        List of repo paths in format "owner/repo"
    """
    repos = []

    try:
        with open(readme_path, "r") as f:
            content = f.read()

        # Pattern to match GitHub URLs
        # Matches: https://github.com/owner/repo or [text](https://github.com/owner/repo)
        pattern = r'https://github\.com/([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)'

        matches = re.findall(pattern, content)

        # Remove duplicates while preserving order
        seen = set()
        for match in matches:
            if match not in seen:
                seen.add(match)
                repos.append(match)

        return repos

    except FileNotFoundError:
        print(f"README file not found: {readme_path}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error reading README: {e}", file=sys.stderr)
        return []


def format_repo_info(repo_info: Dict, format_type: str = "markdown") -> str:
    """
    Format repository info for display

    Args:
        repo_info: Repository information dict
        format_type: Output format ("markdown", "json", or "simple")

    Returns:
        Formatted string
    """
    if format_type == "json":
        return json.dumps(repo_info, indent=2)

    elif format_type == "markdown":
        result = f"## [{repo_info['full_name']}](https://github.com/{repo_info['full_name']})\n\n"
        result += f"**Description:** {repo_info['description']}\n\n"
        result += f"- **Language:** {repo_info['language']}\n"
        result += f"- **Stars:** ⭐ {repo_info['stars']:,}\n"

        if repo_info['topics']:
            result += f"- **Topics:** {', '.join(repo_info['topics'])}\n"

        if repo_info['archived']:
            result += "- ⚠️ **Archived**\n"

        if repo_info['fork']:
            result += "- 🔱 **Fork**\n"

        return result

    else:  # simple format
        return f"{repo_info['full_name']}: {repo_info['description']}"


def main():
    """Main function to handle CLI arguments and execute"""
    import argparse

    parser = argparse.ArgumentParser(description="Fetch GitHub repository descriptions")
    parser.add_argument(
        "repos",
        nargs="*",
        help="Repository paths (e.g., owner/repo). If empty, reads from README.md"
    )
    parser.add_argument(
        "--readme",
        default="README.md",
        help="Path to README file for batch processing (default: README.md)"
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json", "simple"],
        default="markdown",
        help="Output format (default: markdown)"
    )
    parser.add_argument(
        "--output",
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--filter-archived",
        action="store_true",
        help="Exclude archived repositories"
    )
    parser.add_argument(
        "--filter-forks",
        action="store_true",
        help="Exclude forked repositories"
    )

    args = parser.parse_args()

    # Determine which repos to process
    if args.repos:
        repos_to_process = args.repos
    else:
        print("Reading repositories from README...", file=sys.stderr)
        repos_to_process = extract_repos_from_readme(args.readme)
        print(f"Found {len(repos_to_process)} repositories", file=sys.stderr)

    # Process repositories
    results = []
    for i, repo_path in enumerate(repos_to_process, 1):
        print(f"[{i}/{len(repos_to_process)}] Fetching {repo_path}...", file=sys.stderr)

        repo_info = get_repo_info(repo_path)
        if repo_info:
            # Apply filters
            if args.filter_archived and repo_info["archived"]:
                continue
            if args.filter_forks and repo_info["fork"]:
                continue

            results.append(repo_info)

    # Format and output results
    output_lines = []

    if args.format == "json":
        output_lines.append(json.dumps(results, indent=2))
    else:
        for repo_info in results:
            output_lines.append(format_repo_info(repo_info, args.format))
            if args.format == "markdown":
                output_lines.append("\n---\n")

    output_text = "\n".join(output_lines)

    # Write output
    if args.output:
        with open(args.output, "w") as f:
            f.write(output_text)
        print(f"Results written to {args.output}", file=sys.stderr)
    else:
        print(output_text)

    print(f"\nProcessed {len(results)} repositories successfully", file=sys.stderr)


if __name__ == "__main__":
    main()