# DaniLoquium

DaniLoquium is a Pelican-powered static blog.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Build

```bash
pelican content -s publishconf.py -o output
```

The generated site will be written to `output/`.

## Deployment

Every push to `main` runs `.github/workflows/deploy.yml`, which:

1. Builds the Pelican site.
2. Publishes the built site to GitHub Pages.
3. Syncs the same generated files to an FTP server.

Configure these repository secrets before relying on the FTP deployment:

- `FTP_SERVER`
- `FTP_USERNAME`
- `FTP_PASSWORD`

Optionally configure these repository variables:

- `FTP_SERVER_DIR`, for example `/public_html/`
- `FTP_PROTOCOL`, usually `ftp` or `ftps`
- `FTP_PORT`, for non-default ports

In GitHub, set Pages to deploy from GitHub Actions.

