"""Flask application for local resume preview in multiple languages."""

import gettext

from flask import Flask, g, has_request_context, render_template, request

app = Flask(__name__)
SUPPORTED_LANGUAGES = ("en", "ru", "pl", "ua")
RECOMMENDATION_DOC_URL = "https://docs.google.com/document/d/1nQCbBcRU-Sl2cMDqeSlR3eC1Yp5Rs1tqb-rRPPOdK8k/edit?pli=1&tab=t.0"
LANGUAGE_LABELS = {
    "en": "EN",
    "ru": "RU",
    "pl": "PL",
    "ua": "UA",
}


@app.route("/")
def index():
    """Render the main resume template."""
    return render_template("cv_profail.html")


@app.context_processor
def inject_translations():
    """Inject translations and language metadata into every template."""
    data = {}
    if has_request_context():
        # Accept the language from query params, form data, or JSON payload.
        data = request.get_json(silent=True) or request.form.to_dict() or {}
        data.update(request.values or {})

    lang = getattr(g, "language", None) or data.get("language") or data.get("lang") or "en"
    lang = lang.split("_")[0].lower()
    # Treat "uk" as the same language pack as our internal "ua" folder.
    if lang == "uk":
        lang = "ua"
    if lang not in SUPPORTED_LANGUAGES:
        lang = "en"
    g.language = lang

    translations = gettext.translation(
        "messages",
        localedir="translations",
        languages=[lang],
        fallback=True,
    )
    return {
        "_": translations.gettext,
        "current_language": lang,
        "supported_languages": SUPPORTED_LANGUAGES,
        "language_labels": LANGUAGE_LABELS,
        "recommendation_doc_url": RECOMMENDATION_DOC_URL,
    }


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        use_reloader=False,
        port=5800,
    )
