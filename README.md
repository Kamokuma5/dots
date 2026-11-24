# Dot Files

## Test Deploy
```sh
sudo uv run deploy.py --dry-run --force
```

## Deploy
```sh
sudo uv run deploy.py --force

# If you update limine, run the following:
sudo btrfs filesystem label / CachyOS 
limine-mkinitcpio
```

## Install packages
```sh
shelly backup --import --name lugia --directory ~/dots/
```

## Backup 
```sh
shelly backup --export --name lugia --directory ~/dots
```
