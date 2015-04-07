class TorrentsController < ApplicationController
  layout "application"
  def index
    @torrents = Torrent.all
  end
end