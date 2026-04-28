"""Build a static version of the resume for GitHub Pages."""

from pathlib import Path
import shutil

from app import SUPPORTED_LANGUAGES, app


BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
STATIC_SRC = BASE_DIR / "static"
STATIC_DST = DOCS_DIR / "static"
PAGE_MAP = {
    "en": "en.html",
    "ru": "ru.html",
    "pl": "pl.html",
    "ua": "ua.html",
}


def rewrite_html(html: str) -> str:
    """Convert Flask URLs into relative links used by static hosting."""
    html = html.replace('href="/static/styles/style.css"', 'href="static/styles/style.css"')
    html = html.replace('src="/static/images/profile.jpg"', 'src="static/images/profile.jpg"')
    for lang, filename in PAGE_MAP.items():
        html = html.replace(f'href="/?lang={lang}"', f'href="{filename}"')
    return html


def export_pages() -> None:
    """Render all language versions into the docs/ folder."""
    DOCS_DIR.mkdir(exist_ok=True)
    shutil.copytree(STATIC_SRC, STATIC_DST, dirs_exist_ok=True)

    with app.test_client() as client:
        for lang in SUPPORTED_LANGUAGES:
            response = client.get(f"/?lang={lang}")
            if response.status_code != 200:
                raise RuntimeError(f"Failed to render language '{lang}': HTTP {response.status_code}")
            html = rewrite_html(response.get_data(as_text=True))
            (DOCS_DIR / PAGE_MAP[lang]).write_text(html, encoding="utf-8")

    # Keep the English page as the default root URL for job platform links.
    (DOCS_DIR / "index.html").write_text((DOCS_DIR / "en.html").read_text(encoding="utf-8"), encoding="utf-8")
    # Disable Jekyll processing so GitHub Pages serves files exactly as-is.
    (DOCS_DIR / ".nojekyll").write_text("GitHub Pages\n", encoding="utf-8")


if __name__ == "__main__":
    export_pages()
    print(f"Static site exported to: {DOCS_DIR}")
