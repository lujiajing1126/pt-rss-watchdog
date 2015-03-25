module API
  module V1
    class Root < Grape::API
      prefix    'api'
      format    :json

      mount API::V1::Torrents

      add_swagger_documentation mount_path: '/docs/v1',api_version: 'v1',hide_documentation_path:true,  markdown: GrapeSwagger::Markdown::KramdownAdapter
    end
  end
end