#!/usr/bin/env python3
import os
import sys
import json
from pathlib import Path
from datetime import datetime
from google import genai

# Get API key from environment variable (secure)
API_KEY = os.getenv("GEMINI_API_KEY") or "YOUR_API_KEY_HERE"
if API_KEY == "":
    print("WARNING: GEMINI_API_KEY environment variable not set!")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)


SYSTEM_PROMPT = """
You are 'Altus', an expert code editor who provides unfiltered and objective answers, 
thinking about how to improve both the code and the developer's skills.
Your task is to analyze the given code and optimize it according to the user's request.
ONLY return the code, explain it with comment lines without unnecessary explanations.
Do NOT wrap code in backticks (```), provide raw code directly so it can be written to file.
"""

def save_backup(file_path, original_code):
    """Create timestamped backup file"""
    backup_dir = Path(file_path).parent / ".altus_backups"
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"{Path(file_path).stem}_{timestamp}.bak"
    with open(backup_path, 'w', encoding='utf-8') as b:
        b.write(original_code)
    return backup_path

def smart_coder_mode():
    if len(sys.argv) < 2:
        print("📖 Usage: python Altus.py <file_name> [instruction]")
        print("💡 Example: python Altus.py test.py 'optimize this code'")
        return

    file_path = sys.argv[1]
    
    # Convert to absolute path
    file_path = os.path.abspath(file_path)
    
    # File check
    if not os.path.isfile(file_path):
        print(f"❌ Error: {file_path} not found!")
        print(f"📂 Current directory: {os.getcwd()}")
        print(f"📂 Looking for: {file_path}")
        return

    # Read current code
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_code = f.read()
    except Exception as e:
        print(f" Could not read file: {e}")
        return

    print(f"\n✨ --- [ {file_path} loaded. Altus is ready. ] ---")
    
    # Get instruction from command line or user input
    if len(sys.argv) > 2:
        instruction = " ".join(sys.argv[2:])
        print(f"Instruction: {instruction}")
    else:
        instruction = input("Tell me, what can we do to make this code better: ")

    if not instruction.strip():
        print(" Instruction is empty! Operation cancelled.")
        return

    print("\n Altus is thinking and coding...")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config={'system_instruction': SYSTEM_PROMPT},
            contents=f"CURRENT CODE:\n{original_code}\n\nINSTRUCTION: {instruction}"
        )

        # Response validation - PROPER WAY
        if not response:
            print("No response from API!")
            return

        if response.text is None:
            print("API returned empty content!")
            return

        new_code = response.text.strip()

        # Check for empty string after strip
        if not new_code:
            print("Response is empty!")
            return

        # Approval mechanism
        print("\n" + "="*50)
        print("SUGGESTED CHANGES (FIRST 500 CHARACTERS):")
        print("="*50)
        print(new_code[:500] + "..." if len(new_code) > 500 else new_code)
        print("="*50)
        
        confirm = input(f"\n Do you approve updating '{file_path}'? (y/n): ").strip().lower()

        if confirm == 'y':
            # Create timestamped backup
            backup_path = save_backup(file_path, original_code)
            #--------------------------------------------------
            # Write new code
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_code)
            print(f"\n [OK] {file_path} successfully updated.")
            print(f" Backup location: {backup_path}")
        else:
            print("\n [!] Changes rejected. Original file protected.")

    except Exception as e: 
        print(f"\n An error occurred: {e}")

if __name__ == "__main__":
    smart_coder_mode()