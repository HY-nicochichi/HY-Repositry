from flask_talisman.talisman import (
    Talisman,
    DEFAULT_FEATURE_POLICY,
    DEFAULT_PERMISSIONS_POLICY,
    DEFAULT_DOCUMENT_POLICY,
    SAMEORIGIN,
    ONE_YEAR_IN_SECS,
    DEFAULT_CSP_POLICY,
    DEFAULT_REFERRER_POLICY,
    DEFAULT_SESSION_COOKIE_SAMESITE
)

class SecurityHeader(Talisman):

    def init_app(self, app):
        self._default_conf = {
            'feature_policy': DEFAULT_FEATURE_POLICY,
            'permissions_policy': DEFAULT_PERMISSIONS_POLICY,
            'document_policy': DEFAULT_DOCUMENT_POLICY,
            'force_https': True,
            'force_https_permanent': False,
            'force_file_save': False,
            'frame_options': SAMEORIGIN,
            'frame_options_allow_from': None,
            'strict_transport_security': True,
            'strict_transport_security_preload': False,
            'strict_transport_security_max_age': ONE_YEAR_IN_SECS,
            'strict_transport_security_include_subdomains': True,
            'content_security_policy': DEFAULT_CSP_POLICY,
            'content_security_policy_report_uri': None,
            'content_security_policy_report_only': False,
            'content_security_policy_nonce_in': None,
            'referrer_policy': DEFAULT_REFERRER_POLICY,
            'session_cookie_secure': True,
            'session_cookie_http_only': True,
            'session_cookie_samesite': DEFAULT_SESSION_COOKIE_SAMESITE,
            'x_content_type_options': True,
            'x_xss_protection': False
        }
        self._header_conf = app.config.get('SECURITY_HEADER', {})
        super().init_app(
            app,
            feature_policy=self.set_param('feature_policy'),
            permissions_policy=self.set_param('permissions_policy'),
            document_policy=self.set_param('document_policy'),
            force_https=self.set_param('force_https'),
            force_https_permanent=self.set_param('force_https_permanent'),
            force_file_save=self.set_param('force_file_save'),
            frame_options=self.set_param('frame_options'),
            frame_options_allow_from=self.set_param('frame_options_allow_from'),
            strict_transport_security=self.set_param('strict_transport_security'),
            strict_transport_security_preload=self.set_param('strict_transport_security_preload'),
            strict_transport_security_max_age=self.set_param('strict_transport_security_max_age'),
            strict_transport_security_include_subdomains=self.set_param('strict_transport_security_include_subdomains'),
            content_security_policy=self.set_param('content_security_policy'),
            content_security_policy_report_uri=self.set_param('content_security_policy_report_uri'),
            content_security_policy_report_only=self.set_param('content_security_policy_report_only'),
            content_security_policy_nonce_in=self.set_param('content_security_policy_nonce_in'),
            referrer_policy=self.set_param('referrer_policy'),
            session_cookie_secure=self.set_param('session_cookie_secure'),
            session_cookie_http_only=self.set_param('session_cookie_http_only'),
            session_cookie_samesite=self.set_param('session_cookie_samesite'),
            x_content_type_options=self.set_param('x_content_type_options'),
            x_xss_protection=self.set_param('x_xss_protection')
        )

    def set_param(self, param):
        if param in self._header_conf:
            return self._header_conf[param]
        else:
            return self._default_conf[param]
