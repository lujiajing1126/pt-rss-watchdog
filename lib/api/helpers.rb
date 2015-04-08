module API
  module Helpers
    include API::Code::Http_Base
    # Checks the occurrences of required attributes, each attribute must be present in the params hash
    # or a Bad Request error is invoked.
    #
    # Parameters:
    #   keys (required) - A hash consisting of keys that must be present
    def required_attributes!(keys)
      keys.each do |key|
        bad_request!(key) unless params[key].present?
      end
    end

    # Error Helpers
    # error helpers

    def forbidden!
      render_api_error!('403 Forbidden', HTTP_FORBIDDEN)
    end

    def bad_request!(attribute)
      message = ["400 (Bad request)"]
      message << "\"" + attribute.to_s + "\" not given"
      render_api_error!(message.join(' '), HTTP_BAD_REQUEST)
    end

    def not_found!(resource = nil)
      message = ["404"]
      message << resource if resource
      message << "Not Found"
      render_api_error!(message.join(' '), HTTP_NOT_FOUND)
    end

    def unauthorized!
      render_api_error!('401 Unauthorized', HTTP_UNAUTHORIZED)
    end

    def not_allowed!
      render_api_error!('Method Not Allowed', HTTP_METHOD_NOT_FOUND)
    end

    def render_custom_code!(code)
      render_api_result!(I18n.t("api.message.code.custom#{code.to_s}"), code);
    end

    def render_custom_content!(hash)
      error!(hash,HTTP_OK)
    end

    def render_api_error!(message, status)
      error!({:code => status, :message => message}, status)
    end

    def render_api_result!(message, code)
      error!({:message => message, :code => code},HTTP_OK)
    end

    def render_success!
      render_api_result!(I18n.t('api.message.success'), HTTP_OK)
    end

    def render_no_content!
      render_api_result!('', HTTP_NO_CONTENT)
    end
  end
end