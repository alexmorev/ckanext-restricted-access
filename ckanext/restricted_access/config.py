from __future__ import annotations

import ckan.plugins.toolkit as tk


CONFIG_RESTRICTED_ACTIONS = "ckan.restricted.api_actions"
CONFIG_RESTRICTED_PATHS = "ckan.restricted.ui_paths"
CONFIG_REDIRECT_ANON_TO_LOGIN = "ckan.restricted.redirect_anon_to_login"


def get_restricted_api_actions() -> list[str]:
    return tk.aslist(tk.config.get(CONFIG_RESTRICTED_ACTIONS, ""))


def get_restricted_paths() -> list[str]:
    return tk.aslist(tk.config.get(CONFIG_RESTRICTED_PATHS, ""))


def get_redirect_anon_to_login() -> bool:
    return tk.asbool(tk.config.get(CONFIG_REDIRECT_ANON_TO_LOGIN, False))
