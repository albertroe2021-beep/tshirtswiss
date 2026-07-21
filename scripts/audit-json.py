#!/usr/bin/env python3
"""
Phase 1: Audit existing Elementor JSON files in the repository.

Scans all exported JSON files, validates them, extracts metadata,
and produces audit reports.
"""

import json
import os
from pathlib import Path
from datetime import datetime

def audit_json_file(filepath):
    """Parse and audit a single JSON file."""
    result = {
        'path': str(filepath),
        'status': 'unknown',
        'error': None,
        'data': {}
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.strip():
                result['status'] = 'empty'
                return result
            
            data = json.loads(content)
            result['data'] = data
            result['status'] = 'valid'
            
            # Extract metadata based on file type
            filename = filepath.name
            
            if filename == 'manifest.json':
                result['type'] = 'manifest'
                result['metadata'] = {
                    'version': data.get('version'),
                    'site_url': data.get('site_url'),
                    'title': data.get('title'),
                    'description': data.get('description'),
                    'pages': data.get('pages'),
                    'templates': data.get('templates'),
                    'export_date': data.get('export_date'),
                }
            
            elif filename == 'content.json':
                result['type'] = 'content'
                if isinstance(data, list):
                    result['metadata'] = {
                        'item_count': len(data),
                        'pages': len([d for d in data if d.get('type') == 'page']),
                        'posts': len([d for d in data if d.get('type') == 'post']),
                        'templates': len([d for d in data if d.get('type') == 'elementor_library']),
                        'items': [
                            {
                                'id': d.get('id'),
                                'title': d.get('title'),
                                'type': d.get('type'),
                                'slug': d.get('slug'),
                                'status': d.get('status'),
                                'has_elementor_data': bool(d.get('elementor_data')),
                            } for d in data
                        ]
                    }
            
            elif filename == 'styles.json':
                result['type'] = 'styles'
                result['metadata'] = {
                    'global_colors': len(data.get('global_colors', {})),
                    'global_fonts': len(data.get('global_fonts', {})),
                    'site_settings': bool(data.get('site_settings')),
                }
            
            elif filename == 'theme-settings.json':
                result['type'] = 'theme_settings'
                result['metadata'] = data
            
            elif filename.startswith('template-'):
                result['type'] = 'template'
                result['metadata'] = {
                    'has_elements': isinstance(data, list),
                    'element_count': len(data) if isinstance(data, list) else 0,
                    'first_element_type': data[0].get('elType') if data and isinstance(data, list) else None,
                }
            
            else:
                result['type'] = 'unknown'
                result['metadata'] = {'keys': list(data.keys())[:5]}
    
    except json.JSONDecodeError as e:
        result['status'] = 'malformed'
        result['error'] = f'JSON decode error: {str(e)}'
    except Exception as e:
        result['status'] = 'error'
        result['error'] = f'Error: {str(e)}'
    
    return result

def main():
    """Run Phase 1 audit."""
    # Scan for JSON files
    export_dir = Path('/workspaces/tshirtswiss/wordpress-project/exports')
    json_files = list(export_dir.rglob('*.json'))
    
    if not json_files:
        print('No JSON files found.')
        return
    
    print(f'Found {len(json_files)} JSON files.')
    
    # Audit each file
    audit_results = []
    for filepath in sorted(json_files):
        print(f'  Auditing {filepath.name}...')
        result = audit_json_file(filepath)
        audit_results.append(result)
    
    # Summarize results
    summary = {
        'audit_date': datetime.utcnow().isoformat() + 'Z',
        'total_files': len(audit_results),
        'valid_files': len([r for r in audit_results if r['status'] == 'valid']),
        'malformed_files': len([r for r in audit_results if r['status'] == 'malformed']),
        'error_files': len([r for r in audit_results if r['status'] == 'error']),
        'files': audit_results,
    }
    
    # Write JSON report
    json_report_path = Path('/workspaces/tshirtswiss/build/json-audit.json')
    with open(json_report_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'\nJSON audit saved to {json_report_path}')
    
    # Write Markdown report
    md_report_path = Path('/workspaces/tshirtswiss/build/json-audit.md')
    with open(md_report_path, 'w') as f:
        f.write('# Elementor JSON Files Audit\n\n')
        f.write(f'**Audit Date:** {summary["audit_date"]}\n\n')
        f.write('## Summary\n\n')
        f.write(f'- **Total files:** {summary["total_files"]}\n')
        f.write(f'- **Valid:** {summary["valid_files"]}\n')
        f.write(f'- **Malformed:** {summary["malformed_files"]}\n')
        f.write(f'- **Errors:** {summary["error_files"]}\n\n')
        
        f.write('## File Details\n\n')
        
        for result in audit_results:
            path = result['path']
            status = result['status']
            f.write(f'### {Path(path).name}\n\n')
            f.write(f'**Path:** `{path}`\n')
            f.write(f'**Status:** {status}\n')
            
            if result.get('type'):
                f.write(f'**Type:** {result["type"]}\n')
            
            if result.get('error'):
                f.write(f'**Error:** {result["error"]}\n')
            
            if result.get('metadata'):
                f.write('\n**Metadata:**\n\n')
                meta = result['metadata']
                if isinstance(meta, dict):
                    for key, value in meta.items():
                        if isinstance(value, list) and key == 'items':
                            f.write(f'- **{key}:** {len(value)} items\n')
                            for item in value[:5]:
                                if isinstance(item, dict):
                                    f.write(f'  - {item.get("title", item.get("id"))} ({item.get("type", "unknown")})\n')
                            if len(value) > 5:
                                f.write(f'  - ... and {len(value) - 5} more\n')
                        else:
                            f.write(f'- **{key}:** {value}\n')
            
            f.write('\n')
    
    print(f'Markdown audit saved to {md_report_path}\n')
    
    # Print summary
    print(summary)

if __name__ == '__main__':
    main()
