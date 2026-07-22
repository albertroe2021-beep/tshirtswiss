#!/usr/bin/env python3
"""
TShirtSwiss Elementor Site Builder
Orchestrates the complete setup workflow
"""

import subprocess
import sys
import time
import os

def run_cmd(cmd, desc="", timeout=120):
    """Run a command and return output"""
    print(f"\n{'='*60}")
    if desc:
        print(f"▶ {desc}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd="/workspaces/tshirtswiss/wordpress-project"
        )
        
        if result.stdout:
            # Print first and last 30 lines to avoid huge output
            lines = result.stdout.strip().split('\n')
            if len(lines) > 60:
                print('\n'.join(lines[:30]))
                print(f"\n... ({len(lines)-60} lines omitted) ...\n")
                print('\n'.join(lines[-30:]))
            else:
                print(result.stdout)
        
        if result.returncode != 0:
            print(f"\n❌ Error (exit code {result.returncode})")
            if result.stderr:
                print("STDERR:", result.stderr[:500])
            return False
        
        print(f"✅ Success")
        return True
        
    except subprocess.TimeoutExpired:
        print(f"❌ Timeout after {timeout}s")
        return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    print("\n")
    print("╔" + "═"*58 + "╗")
    print("║" + " "*58 + "║")
    print("║  TShirtSwiss - Elementor Website Kit Builder".ljust(59) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "═"*58 + "╝")
    
    os.chdir("/workspaces/tshirtswiss/wordpress-project")
    
    steps = [
        (
            "docker compose down --remove-orphans 2>&1",
            "Cleaning up existing Docker environment"
        ),
        (
            "sleep 2 && docker compose up -d 2>&1 | tail -20",
            "Starting Docker containers",
        ),
        (
            "sleep 10 && docker compose run --rm wpcli wp --version --allow-root",
            "Verifying WP-CLI",
        ),
        (
            "docker compose run --rm wpcli wp core version --allow-root",
            "Checking WordPress version",
        ),
        (
            "docker compose run --rm wpcli wp plugin is-active elementor --allow-root || echo 'Elementor not active'",
            "Checking Elementor status",
        ),
    ]
    
    for cmd, desc in steps:
        if not run_cmd(cmd, desc, timeout=120):
            print(f"\n⚠️  Failed at: {desc}")
            print("Continuing anyway...")
            continue
        time.sleep(2)
    
    print("\n" + "="*60)
    print("Phase 1 Complete: Docker environment ready")
    print("="*60)

if __name__ == "__main__":
    main()
