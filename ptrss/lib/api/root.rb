module API
  class Root < Grape::API
    prefix    'api'
    format    :json

    rescue_from :all do |exception|
      # lifted from https://github.com/rails/rails/blob/master/actionpack/lib/action_dispatch/middleware/debug_exceptions.rb#L60
      # why is this not wrapped in something reusable?
      trace = exception.backtrace

      message = "\n#{exception.class} (#{exception.message}):\n"
      message << exception.annoted_source_code.to_s if exception.respond_to?(:annoted_source_code)
      message << "  " << trace.join("\n  ")
      Rails.logger.error message
      if Rails.env.test?
        rack_response({'code' => 500,'message' => message}.to_json, 500)
      else
        rack_response({'code' => 500,'message' => '500 Internal Server Error'}.to_json, 500)
      end
    end

    error_formatter :json, API::ErrorFormatter

    mount API::V1::Root
  end
end