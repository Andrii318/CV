"""Compile .po translation files into .mo files used by Flask gettext."""

from pathlib import Path

import polib

BASE_DIR = Path(__file__).resolve().parent
LOCALES_DIR = BASE_DIR / "translations"
LANGUAGES = ("en", "ru", "pl", "ua")


def compile_translations() -> None:
    """Compile all available translation files."""
    for lang in LANGUAGES:
        po_path = LOCALES_DIR / lang / "LC_MESSAGES" / "messages.po"
        mo_path = LOCALES_DIR / lang / "LC_MESSAGES" / "messages.mo"
        po = polib.pofile(po_path)
        po.save_as_mofile(mo_path)
        print(f"Compiled: {po_path} -> {mo_path}")

    print("Translation files compiled successfully.")


if __name__ == "__main__":
    compile_translations()
