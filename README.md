# Dot Files

## Test Deploy
```sh
sudo uv run deploy.py --dry-run --force
```

## Deploy
```sh
sudo uv run deploy.py --force
```

## Install packages
```sh
shelly backup --import --name lugia --directory ~/dots/
```

## Backup 
```sh
shelly backup --export --name lugia --directory ~/dots
```
