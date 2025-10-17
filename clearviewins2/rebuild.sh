#!/bin/bash
# Automated Podman cleanup and rebuild script
podman system prune -f
podman-compose up --build
