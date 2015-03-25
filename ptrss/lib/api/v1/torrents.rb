module API
  module V1
    class Torrents < Grape::API
      version 'v1'
      format :json
      include API::Code::Http_Base

      resources :torrents do

        desc 'RPC上传种子信息'
        params do
          requires :title,type: String,desc: 'title for the torrent'
          requires :description,type: String,desc: 'description for the torrent'
          requires :link,type: String,desc: 'link'
          requires :guid,type: String,desc: 'guid'
          requires :enclosure,type: String,desc: 'attachment also'
          requires :pub_date,type: Integer,desc: 'publish datetime'
        end
        post '' do
          torrent = Torrent.where(:title => params[:title]).first
          if torrent.blank?
            #binding.pry
            torrent_params = ActionController::Parameters.new(params).permit(:title,:description,:link,:guid,:enclosure,:pub_date)
            torrent = Torrent.new(torrent_params)
          end
          if torrent.save
            render_no_content!
          else
            render_api_error! 'error',HTTP_INTERNAL_SERVER_ERROR
          end
        end
      end
    end
  end
end