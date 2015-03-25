module API
  module V1
    class Torrents < Grape::API
      version 'v1'
      format :json

      resources :torrents do
        desc 'TEST'
        get "" do
          {:Hello => "World"}
        end
      end
    end
  end
end