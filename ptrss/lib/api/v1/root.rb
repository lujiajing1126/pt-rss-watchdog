module API
  module V1
    class Root < Grape::API
      prefix    'api'
      format    :json

      mount API::V1::Torrents
    end
  end
end