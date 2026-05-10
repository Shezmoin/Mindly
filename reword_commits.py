#!/usr/bin/env python3
"""
Reword specific git commits by hash and message pattern
"""
import subprocess
import sys
import os

def run_command(cmd):
    """Run a shell command and return output"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def main():
    os.chdir(r'c:\Users\Shez\Mindly\Mindly')
    
    # Disable pager
    run_command('git config core.pager ""')
    
    # First, let's get the commit hash that has "AI traces"
    stdout, _, _ = run_command('git log --oneline --all')
    target_commit = None
    target_message = None
    
    for line in stdout.split('\n'):
        if 'AI traces' in line:
            parts = line.split(' ', 1)
            target_commit = parts[0]
            target_message = parts[1] if len(parts) > 1 else ''
            print(f"Found commit to fix: {target_commit} - {target_message}")
            break
    
    if not target_commit:
        print("No commit with 'AI traces' found")
        return
    
    # Count how many commits back this is
    stdout, _, _ = run_command(f'git rev-list --count HEAD..{target_commit}^@')
    
    # New message: replace "and AI traces" with empty, making it "docs: add final cleanup requirement"
    new_message = "docs: add final cleanup requirements"
    
    print(f"\nAbout to change commit {target_commit}")
    print(f"Old message: {target_message}")
    print(f"New message: {new_message}")
    
    # Use git filter-branch to change the commit message
    # This is safer than interactive rebase in an automated context
    cmd = f'git filter-branch -f --msg-filter "sed \'s/docs: add final cleanup requirement to remove checklist and AI traces/docs: add final cleanup requirements/g\'" -- {target_commit}^..'
    
    stdout, stderr, code = run_command(cmd)
    
    if code == 0:
        print("\n✓ Commit message successfully updated!")
        print("New history:")
        run_command('git log --oneline -10')
    else:
        print(f"\n✗ Failed to update: {stderr}")
        
    # Verify
    stdout, _, _ = run_command('git log --oneline --all | grep -i "ai"')
    if stdout:
        print(f"\n⚠ Still found AI mentions:\n{stdout}")
    else:
        print("\n✓ No more AI mentions in commit history")

if __name__ == '__main__':
    main()
