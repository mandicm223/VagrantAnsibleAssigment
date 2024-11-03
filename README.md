# Kanye Quote Fetcher and Displayer

This project creates a Vagrant-based development environment that provisions an Ubuntu 22.04 VM, installs Docker, and schedules tasks using Ansible and systemd-cron. The setup automates fetching quotes from the [Kanye REST API](https://api.kanye.rest) and displays them at regular intervals using Docker containers.

## Features

- **Vagrant**: Sets up an Ubuntu 22.04 virtual machine with Docker installed.
- **Ansible**: Manages provisioning, including Docker installation, script setup, and cron job configuration.
- **systemd-cron**: Schedules and manages tasks for fetching and displaying quotes.
- **Docker**: Runs a Python script in a container that reads and displays quotes from text files.

## Requirements

- **Vagrant**: Install from [Vagrant's official site](https://www.vagrantup.com/downloads).
- **Virtualization Provider**: e.g., VirtualBox, VMware.
- **Ansible**: Used for provisioning inside the VM.

