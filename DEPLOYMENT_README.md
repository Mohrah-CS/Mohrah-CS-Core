# MOHRAH CS CORE — Permanent Deployment Package

This package is a non-destructive release candidate built from the approved course-preview chain. It contains the complete Streamlit application, all local custom diagrams for DSA, OOP, COAL, and Digital Logic Design, and the targeted Chapter 14 comparator-text correction.

## What remains unchanged

All lessons, code examples, quizzes, Smart Exam behavior, comments and ratings, Supabase references, navigation, and chapter scroll-to-top behavior remain in the application. The only Chapter 14 code change is HTML-safe rendering of the three explanatory `A<B` expressions so the browser displays the complete text.

## Files for the repository root

Use `final_app.py` as the Streamlit entry file, `requirements.txt` as the dependency list, and all four `*_preview_assets` folders in the same repository root. Keep `.streamlit/config.toml` in place.

## Required private hosting secrets

Add the following two existing values in the hosting provider's private Secrets settings. Do not place their actual values in GitHub or any tracked file.

```toml
SUPABASE_URL = "existing Supabase project URL"
SUPABASE_WRITE_SECRET = "existing Supabase server-side write key"
```

The included `.streamlit/secrets.toml.example` is only a template and contains no live secret.

## Recommended hosting route

Deploy this repository as a Streamlit application. Set the main file path to `final_app.py` and retain the private secrets above. A permanent URL is created by the hosting provider after publish.
