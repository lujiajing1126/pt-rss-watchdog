class Torrent
  include Mongoid::Document
  include Mongoid::Timestamps

  field :title
  field :description
  field :link
  field :guid
  field :enclosure
  field :pub_date, type: DateTime
end