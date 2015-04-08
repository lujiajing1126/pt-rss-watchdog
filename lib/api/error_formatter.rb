module API
  module ErrorFormatter
    def self.call message, backtrace, options, env
      message.to_json
    end
  end
end