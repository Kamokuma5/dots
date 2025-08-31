# Test Deploy
sudo python deploy.py --dry-run --force

# Deploy
sudo python deploy.py --force

# Install packages in .config
metapac -n lugia sync

# Remove packages no in .config
metapac -n lugia clean