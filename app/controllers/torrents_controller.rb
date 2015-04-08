class TorrentsController < ApplicationController
  layout "application"
  def index
    @torrents = Torrent.desc(:created_at).page(params[:page]).per(10)
  end

  def show
    @torrent = Torrent.where(:id => params[:id]).first
  end
end