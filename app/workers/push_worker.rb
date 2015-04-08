class PushWorker
  include Sidekiq::Worker
  def perform(torrent_id)
    torrent = Torrent.where(:id => torrent_id).first
    unless torrent.blank?
      puts torrent.title
      PushService.new.send torrent.title
      puts 'Send Push'
    end
  end
end