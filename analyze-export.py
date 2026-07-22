#!/usr/bin/env python3
import zipfile
import json
import sys

zip_path = '/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-kit.zip'

try:
    with zipfile.ZipFile(zip_path, 'r') as zf:
        print("=== ZIP File Analysis ===\n")
        
        # List all files
        all_files = zf.namelist()
        print(f"Total files: {len(all_files)}\n")
        
        # Read manifest
        print("=== Manifest ===")
        try:
            with zf.open('manifest.json') as f:
                manifest = json.load(f)
                print(f"Elementor version: {manifest.get('version', 'unknown')}")
                pages = manifest.get('pages', {})
                print(f"Pages in manifest: {len(pages)}")
                if pages:
                    sample_ids = list(pages.keys())[:5]
                    for page_id in sample_ids:
                        page_info = pages[page_id]
                        print(f"  - {page_info.get('title', f'Page {page_id}')} (ID: {page_id})")
        except Exception as e:
            print(f"Error reading manifest: {e}")
        
        print("\n=== Content Files ===")
        content_files = [f for f in all_files if 'content/page' in f]
        print(f"Page content files: {len(content_files)}")
        if content_files:
            for cf in content_files[:5]:
                size = zf.getinfo(cf).file_size
                print(f"  {cf} ({size} bytes)")
        
        print("\n=== Sample Page Content ===")
        if content_files:
            first_page = content_files[0]
            with zf.open(first_page) as f:
                try:
                    page_data = json.load(f)
                    print(f"File: {first_page}")
                    print(f"Is array: {isinstance(page_data, list)}")
                    if isinstance(page_data, list):
                        print(f"Elements: {len(page_data)}")
                        if page_data:
                            print(f"First element keys: {list(page_data[0].keys())[:10]}")
                            first = page_data[0]
                            print(f"First element type: {first.get('elType', 'unknown')}")
                            print(f"First widget type: {first.get('widgetType', 'unknown')}")
                except json.JSONDecodeError as e:
                    print(f"Error decoding: {e}")
                    content = f.read()[:200]
                    print(f"File starts with: {content}")
        
        print("\n=== File Listing ===")
        for fname in all_files:
            size = zf.getinfo(fname).file_size
            print(f"{fname} ({size} bytes)")
            
except FileNotFoundError:
    print(f"ZIP file not found: {zip_path}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
