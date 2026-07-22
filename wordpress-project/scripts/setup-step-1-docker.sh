#!/bin/bash
# Step 1: Docker Setup
# Brings up fresh WordPress + MySQL containers

echo "=== Step 1: Docker Environment Setup ==="
echo ""

cd /workspaces/tshirtswiss/wordpress-project

echo "Stopping any existing containers..."
docker compose down --remove-orphans 2>/dev/null || true

echo "Starting fresh Docker environment..."
docker compose up -d

echo "Waiting for containers to be healthy..."
sleep 15

echo ""
echo "✓ Docker containers running"
docker compose ps --services
