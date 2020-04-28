"""

Copyright (C) 2017-2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

# AUTHENTICATION

# Which social auths do you want to use?
ENABLE_GOOGLE_AUTH = False
ENABLE_TWITTER_AUTH = False
ENABLE_GITHUB_AUTH = False
ENABLE_GITLAB_AUTH = False
ENABLE_BITBUCKET_AUTH = False

# NOTE you will need to set autehtication methods up.
# Configuration goes into secrets.py
# see https://singularityhub.github.io/sregistry/install.html
# secrets.py.example provides a template to work from

# See below for additional authentication module, e.g. LDAP that are
# available, and configured, as plugins.

# DOMAIN NAMES
## IMPORTANT: if/when you switch to https, you need to change "DOMAIN_NAME"
# to have https, otherwise some functionality will not work (e.g., GitHub webhooks)

DOMAIN_NAME = "https://jaxreg.jax.org"
DOMAIN_NAME_HTTP = "http://jaxreg.jax.org"
DOMAIN_NAKED = DOMAIN_NAME_HTTP.replace("http://", "")

ADMINS = (("bradlma", "matt.bradley@jax.org"),("mckend", "david.mckenzie@jax.org"), ("ssander", "shane.sanders@jax.org"), ("macklj", "jason.macklin@jax.org"),("mcdiva", "aaron.mcdivitt@jax.org"))
MANAGERS = ADMINS

HELP_CONTACT_EMAIL = "rit-ci@jax.org"
HELP_INSTITUTION_SITE = ''
REGISTRY_NAME = "Jackson Laboratory Singularity Container Registry"
REGISTRY_URI = "jaxreg"
GOOGLE_ANALYTICS = None  # "UA-XXXXXXXXX"

# Permissions and Views

# Set this to be some size in MB to limit uploads.
# Uploads > 2.5GB will not use memory, but the filesystem
DATA_UPLOAD_MAX_MEMORY_SIZE = None

# Allow users to create public collections
USER_COLLECTIONS = True

# Limit users to N collections (None is unlimited)
USER_COLLECTION_LIMIT = 2

# Should registries by default be private, with no option for public?
PRIVATE_ONLY = False

# Should the default for a new registry be private or public?
DEFAULT_PRIVATE = False

# The number of collections to show on the /<domain>/collections page
COLLECTIONS_VIEW_PAGE_COUNT = 250

# The maximum number of downloads allowed per container/collection, per week
CONTAINER_WEEKLY_GET_LIMIT = 1000
COLLECTION_WEEKLY_GET_LIMIT = 1000

# Disable all pushes of containers, recipes, etc. Also for Google Cloud Build
DISABLE_BUILDING = False

# Plugins ######################################################################
# See dummy_secrets.py for more details.

SREGISTRY_GOOGLE_BUILD_LIMIT = 100
SREGISTRY_GOOGLE_BUILD_SINGULARITY_VERSION = "v3.3.0-slim"
SREGISTRY_GOOGLE_BUILD_TIMEOUT_SECONDS = None  # None defaults to 10 minutes
SREGISTRY_GOOGLE_BUILD_EXPIRE_SECONDS = 28800
CONTAINER_SIGNED_URL_EXPIRE_SECONDS = 10

# A global setting to disable all webhooks / interaction with Github
DISABLE_GITHUB = False

# A global setting to disable all building
DISABLE_BUILDING = False

# prevent responses from being received from Google Cloud Build
DISABLE_BUILD_RECEIVE = False


# DATABASE

# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "HOST": "db",
        "PORT": "5432",
    }
}


# Logging

# Do you want to save complete response metadata per each pull?
# If you disable, we still keep track of collection pull counts, but not specific versions
LOGGING_SAVE_RESPONSES = True

# Rate Limits

VIEW_RATE_LIMIT = (
    "50/1d"
)  # The rate limit for each view, django-ratelimit, "50 per day per ipaddress)
VIEW_RATE_LIMIT_BLOCK = (
    True  # Given that someone goes over, are they blocked for the period?
)

# Plugins
# Add the name of a plugin under shub.plugins here to enable it

# Available Plugins:
# - ldap_auth: Allows sregistry to authenitcate against an LDAP directory
# - google_build: a custom storage with that uses Google Cloud Build + Storage
# - pam_auth: Allow users from (docker) host to log in
# - globus: allows connection from sregistry to endpoints
# - saml_auth: authentication with SAML
# - pgp: deploy a key server alongside your registry

PLUGINS_ENABLED = [
    #    'pgp'
        'ldap_auth'
    #    'google_build'
    #    'pam_auth',
    #    'globus',
    #    'saml_auth'
]
