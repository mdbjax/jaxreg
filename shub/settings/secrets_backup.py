# This file, dummy_secrets, provides an example of how to configure
# sregistry with your authentication secrets. Copy it to secrets.py and
# configure the settings you need.

# Secret Key
# You must uncomment, and set SECRET_KEY to a secure random value
# e.g. https://djskgen.herokuapp.com/

#SECRET_KEY = '62$o*1j@5al9jsh@#c5y05=2!t!=sd=e0qy*0(j_=rc(hj8jg9'


# =============================================================================
# Social Authentication
# Set keys and secrets for social authentication methods that you have
# enabled in config.py.
# See https://singularityhub.github.io/sregistry/install.html for full details
# =============================================================================

# Twitter OAuth2
# Only required if ENABLE_TWITTER_AUTH=TRUE in config.py
# SOCIAL_AUTH_TWITTER_KEY = ''
# SOCIAL_AUTH_TWITTER_SECRET = ''

# -----------------------------------------------------------------------------
# Google OAuth2
# Only required if ENABLE_GOOGLE_AUTH=TRUE in config.py

# GOOGLE_CLIENT_FILE='/code/.grilledcheese.json'

# http://psa.matiasaguirre.net/docs/backends/google.html?highlight=google
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'xxxxxxxxxxxxxxxxxx.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'xxxxxxxxxxxxxxxxx'

# The scope is not needed, unless you want to develop something new.
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://www.googleapis.com/auth/drive']
# SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
#    'access_type': 'offline',
#    'approval_prompt': 'auto'
# }
# -----------------------------------------------------------------------------
# GitHub OAuth
# Only required if ENABLE_GITHUB_AUTH=TRUE in config.py
# http://psa.matiasaguirre.net/docs/backends/github.html?highlight=github

# SOCIAL_AUTH_GITHUB_KEY = ''
# SOCIAL_AUTH_GITHUB_SECRET = ''

# You shouldn't actually need this if we aren't using repos
# SOCIAL_AUTH_GITHUB_SCOPE = ["repo","user"]

# -----------------------------------------------------------------------------
# GitLab OAuth2

# SOCIAL_AUTH_GITLAB_SCOPE = ['api', 'read_user']
# SOCIAL_AUTH_GITLAB_KEY = ''
# SOCIAL_AUTH_GITLAB_SECRET = ''

# =============================================================================
# Google Cloud Build + Storage
# Configure a custom builder and storage endpoint
# =============================================================================

# GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"
# SREGISTRY_GOOGLE_PROJECT="myproject-ftw"

# SREGISTRY_GOOGLE_BUILD_CACHE="true"
# After build, do not delete intermediate dependencies in cloudbuild bucket (keep them as cache for rebuild if needed).
# Defaults to being unset, meaning that files are cleaned up. If you define this as anything, the build files will be cached.

# SREGISTRY_GOOGLE_BUILD_LIMIT=100
# To prevent denial of service attacks on Google Cloud Storage, you should set a reasonable limit for the number of active, concurrent builds.
# This number should be based on your expected number of users, repositories, and recipes per repository.

# SREGISTRY_GOOGLE_BUILD_SINGULARITY_VERSION="v3.2.1-slim"
# if you want to specify a version of Singularity. The version must coincide with a container tag hosted under singularityware/singularity. The version will default to 3.2.0-slim If you want to use a different version, update this variable.

# SREGISTRY_GOOGLE_STORAGE_BUCKET="taco-singularity-registry"
# is the name for the bucket you want to create. The example here is using the unique identifier appended with “sregistry-"
# If you don't define it, it will default to a string that includes the hostname.
# Additionally, a temporary bucket is created with the same name ending in _cloudbuild. This bucket is for build time dependencies, and is cleaned up after the fact. If you are having trouble getting a bucket it is likely because the name is taken,
# and we recommend creating both <name> and <name>_cloudbuild in the console and then setting the name here.

# SREGISTRY_GOOGLE_BUILD_TIMEOUT_SECONDS=None
# The number of seconds for the build to timeout. If set to None, will be 10 minutes. If
# unset, will default to 3 hours. This time should be less than the SREGISTRY_GOOGLE_BUILD_EXPIRE_SECONDS

# SREGISTRY_GOOGLE_BUILD_EXPIRE_SECONDS=28800
# The number of seconds for the build to expire, meaning it's response is no longer accepted by the server. This must be defined.
# The default 28800 indicates 8 hours (in seconds)

# CONTAINER_SIGNED_URL_EXPIRE_SECONDS=10
# The number of seconds to expire a signed URL given to download a container
# from storage. This can be much smaller than 10, as we only need it to endure
# for the POST.

# -----------------------------------------------------------------------------
# Bitbucket OAuth2

# SOCIAL_AUTH_BITBUCKET_OAUTH2_KEY = '<your-consumer-key>'
# SOCIAL_AUTH_BITBUCKET_OAUTH2_SECRET = '<your-consumer-secret>'
# SOCIAL_AUTH_BITBUCKET_OAUTH2_VERIFIED_EMAILS_ONLY = True

# =============================================================================
# Plugin Authentication
# Set options for authentication plugins that you have enabled in config.py
# =============================================================================

# LDAP Authentication (ldap-auth)
# Only required if 'ldap-auth' is added to PLUGINS_ENABLED in config.py

# This example assumes you are using an OpenLDAP directory
# If using an alternative directory - e.g. Microsoft AD, 389 you
# will need to modify attribute names/mappings accordingly
# See https://django-auth-ldap.readthedocs.io/en/1.2.x/index.html

# To work with OpenLDAP and posixGroup groups we need to import some things
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType


SECRET_KEY = "62$o*1j@5al9jsh@#c5y05=2!t!=sd=e0qy*0(j_=rc(hj8jg9"


# The URI to our LDAP server (may be ldap:// or ldaps://)
AUTH_LDAP_SERVER_URI = "ldaps://ldaps.jax.org:636"

# DN and password needed to bind to LDAP to retrieve user information
# Can leave blank if anonymous binding is sufficient
AUTH_LDAP_BIND_DN = "CN=svc-ldapbind,OU=ServiceAccounts,DC=jax,DC=org"
AUTH_LDAP_BIND_PASSWORD = "Un1corn!"


# Any user account that has valid auth credentials can login
# AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=example,dc=com",
#                                   ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

# AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=example,dc=com",
#                                    ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)"
#                                    )
# AUTH_LDAP_GROUP_TYPE = PosixGroupType()

AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=jax,dc=org",
                                   ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=jax,dc=org",
                                    ldap.SCOPE_SUBTREE, "(objectClass=group)"
                                    )
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()



# Populate the Django user model from the LDAP directory.
# AUTH_LDAP_USER_ATTR_MAP = {
#    "first_name": "givenName",
#    "last_name": "sn",
#    "email": "mail"
# }

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {

    # Anyone in this group can get a token to manage images, not superuser
    #"is_staff": "cn=staff,ou=django,ou=groups,dc=example,dc=com",
    "is_staff": "CN=researchit,OU=Unix,OU=Groups,DC=jax,DC=org",

    # Anyone in this group is a superuser for the app
    #"is_superuser": "cn=superuser,ou=django,ou=groups,dc=example,dc=com"
    "is_superuser": "CN=jaxadmin,OU=Unix,OU=Groups,DC=jax,DC=org"

}

AUTH_LDAP_GLOBAL_OPTIONS = {
        ldap.OPT_X_TLS_REQUIRE_CERT: False,
        ldap.OPT_X_TLS_ALLOW: 1,
        ldap.OPT_REFERRALS: False
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'sregistry',
#        'USER': 'sregistry_rw',
#        'PASSWORD':'b3at5!!',
#        'HOST': 'ctecho02.jax.org',
#        'PORT': '5432',
#    }
#}


# AUTH_LDAP_USER_FLAGS_BY_GROUP = {

#    # Anyone in this group can get a token to manage images, not superuser
#    "is_staff": "cn=staff,ou=django,ou=groups,dc=example,dc=com",
#
#    # Anyone in this group is a superuser for the app
#    "is_superuser": "cn=superuser,ou=django,ou=groups,dc=example,dc=com"

# }

# Globus Assocation (globus)
# Only required if 'globus' is added to PLUGINS_ENABLED in config.py

# SOCIAL_AUTH_GLOBUS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# SOCIAL_AUTH_GLOBUS_USERNAME="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@clients.auth.globus.org"
# SOCIAL_AUTH_GLOBUS_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# GLOBUS_ENDPOINT_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


# SAML Authentication (saml)
# Only required if 'saml_auth' is added to PLUGINS_ENABLED in config.py

# AUTH_SAML_IDP = "stanford"
